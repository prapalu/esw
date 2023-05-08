
import gzip
import argparse
from functools import partial


parser = argparse.ArgumentParser(description='Clean wikidata dump')
parser.add_argument('filename', type=str,
                   help='relative path to filename to parse')
args = parser.parse_args()


STRING_PATTERN = '"@'
ENGLISH_PATTERN = '"@en '
OTHER_ENGLISH_PATTERN = '"@en-'
SKIP_LIST = ['^^<http://www.opengis.net']


big_properties = set()
big_properties.add('<http://www.w3.org/2000/01/rdf-schema#label>')
big_properties.add('<http://www.w3.org/2004/02/skos/core#altLabel>')
big_properties.add('<http://www.w3.org/2004/02/skos/core#prefLabel>')
big_properties.add('<http://schema.org/description>')

if 'truthy' in args.filename:
  TARGET_FILE = './wikidata-truthy-prefiltered.nt'
else:
  TARGET_FILE = './wikidata-all-prefiltered.nt'


f2 = open(TARGET_FILE, 'w', encoding='utf-8')

read_count=0
write_count=0

with gzip.open(args.filename,'rt') as source_file:
    print("Start...")
    # Decompress data from file
    for line in source_file:
       read_count+=1
       if not(line):
           break
       else:
           if line.split()[1] in big_properties: # filter big properties
               continue

           if any(skipword in line for skipword in SKIP_LIST):
               continue

           if STRING_PATTERN not in line:      # not big property and not a string: we write it
               f2.write(line)
               write_count+=1
           elif ENGLISH_PATTERN in line and OTHER_ENGLISH_PATTERN not in line:   # it is a string so we only write if it's in english
               f2.write(line)
               write_count+=1
f2.close()
print("Parsed {} Kepts {}".format(read_count, write_count))


