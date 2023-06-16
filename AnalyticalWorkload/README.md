# Instructions for 2021
##  Download and clean the WikiData dump

## Preparation


** Use virtual env **

```bash

python3 -m venv wikidump
source wikidump/bin/activate

```



## Download & Parse


```bash

wget https://dumps.wikimedia.org/wikidatawiki/entities/20210922/wikidata-20210922-truthy-BETA.nt.gz

python clean-dump-gz.py wikidata-20210922-truthy-BETA.nt.gz >> parsed.log
```

**This will produce the file `./wikidata-prefiltered.nt`**


## Install Virtuoso and load the file

```bash

docker pull openlink/virtuoso-opensource-7:latest
mkdir -p virtuoso/database
cp  virtuoso.ini virtuoso/database/virtuoso.ini

mkdir -p virtuoso/settings

docker run -t -d --name virtuoso \
        -v `pwd`/virtuoso/database:/database \
        -v `pwd`/virtuoso/settings:/settings \
        --env DBA_PASSWORD=admin \
        -v `pwd`/data:/import \
        -p 1111:1111 -p 5820:8890 -i \
        openlink/virtuoso-opensource-7:latest

```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 


Distributed under the MIT License. See [LICENSE-MIT](../LICENSE-MIT) for more information. 
