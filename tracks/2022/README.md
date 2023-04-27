# 2022 Track

This folder contains the 2022 track.

## Statistics

The 2022 track is composed of:
- 3 macro topic (Movies, Sport, History)
- 36 workers
- 21 Search Topics
- 108 Search Workflows (each worker was assigned to implement a search workflow for each macro topic)
- 5786 queries

### Search Workflows

Each Search Topic was implemented from 4 to 6 workers in order to obtain different points of view. The table below shows the distribution of the Search Workflows.

You can get the statistics below querying the RDF Graph. [Execute query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=PREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0APREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0D%0APREFIX+lsqv%3A+%3Chttp%3A%2F%2Flsq.aksw.org%2Fvocab%23%3E%0D%0APREFIX+eswr%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fresource%2F%3E%0D%0A%0D%0ASELECT+%3FtLab+%28COUNT%28DISTINCT+%3Fwork%29+AS+%3Fworks%29++%28COUNT%28DISTINCT+%3Fquery%29+AS+%3FnQueries%29+where%7B%0D%0A++++%3Ftopic+esw%3ApartOf+eswr%3ACompleteness2022Track.%0D%0A%3Ftopic+esw%3AmacroTopic+%3Fmacro.%0D%0A%3Ftopic+rdfs%3Alabel+%3FtLab.%0D%0A++++%3Fwork+esw%3Aimplements+%3Ftopic%3B%0D%0A++++++++++esw%3AhasPart+%3Fjob.%0D%0A++++%3Fjob+esw%3Aqueries+%3Fqueries.%0D%0A++++%3Fqueries+rdf%3Arest*%2Frdf%3Afirst++%3Fquery.%0D%0A%7D%0D%0AGROUP+BY+%3FtLab%0D%0AORDER+BY+%3FtLab&format=text%2Fhtml&timeout=0&signal_void=on)

| Search Topic | #Workflows | # queries|
| -------------| -----------| -----------|
| **History** | **36** | **1831**|
| Literary Movements and Divine Comedy  | 5 | 265 |
| Euro  | 6 | 323 |
| World Wide Web | 5 | 158 |
| Ancient Civilization  | 6 | 539 |
| Cultural Movements  | 5 | 174 |
| Ancient Rome  | 4 | 186 |
| Literary Movements and physicists  | 5 | 186 |
| **Movies** | **36** | **1636**|
| Tv series Without a Trace  | 5 | 284 |
| Disney  | 5 | 171 |
| Film Genre and directors  | 5 | 253 |
| Production company  | 5 | 184 |
| Tv series HIMYM  | 6 | 368 |
| Sherlock Holmes  | 6 | 232 |
| Film Genre and composer  | 4 | 144 |
| **Sport** | **36** | **2319**|
| Association Football Players  | 5 | 195 |
| Olympic Games  | 4 | 186 |
| Running  | 5 | 221 |
| Tennis  | 6 | 626 |
| Basketball and NBA seasons  | 5 | 326 |
| Association Football Club  | 5 | 382 |
| Basketball and NBA finals  | 6 | 383 |

### Keywords Analysis

The table below shows the distribution of the SPARQL keywords in the track.

You can get the statistics below querying the RDF Graph. [Execute query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=PREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0APREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0D%0APREFIX+lsqv%3A+%3Chttp%3A%2F%2Flsq.aksw.org%2Fvocab%23%3E%0D%0APREFIX+eswr%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fresource%2F%3E%0D%0A%0D%0ASELECT+%3Fkeyword+%28COUNT%28*%29+AS+%3Fcount%29+where%7B%0D%0A++++%3Ftopic+esw%3ApartOf+eswr%3ACompleteness2022Track.%0D%0A++++%3Fwork+esw%3Aimplements+%3Ftopic%3B%0D%0A++++++++++esw%3AhasPart+%3Fjob.%0D%0A++++%3Fjob+esw%3Aqueries+%3Fqueries.%0D%0A++++%3Fqueries+rdf%3Arest*%2Frdf%3Afirst++%3Fquery.%0D%0A++++%3Fquery+lsqv%3AusesFeature+%3Fkeyword.%0D%0A%7D%0D%0AGROUP+BY+%3Fkeyword%0D%0AORDER+BY+DESC+%28%3Fcount%29&format=text%2Fhtml&timeout=0&signal_void=on)

| Keyword   | # queries | % queries |
| ----------| --------- | -------- | 
| SELECT 	| 5783 	    | 99.94% |
| DISTINCT 	| 5319 	    | 91.92% |
| LIMIT 	| 5234 	    | 90.45% |
| FILTER 	| 1557 	    | 26.9%  |
| COUNT 	| 881 	    | 15.22% |
| GROUPBY 	| 864 	    | 14.93% |
| ORDERBY 	| 746 	    | 12.89% |
| REGEX 	| 671 	    | 11.59% |
| OPTIONAL 	| 348 	    | 6.01% |
| HAVING 	| 250 	    | 4.32% |
| NESTEDQUERY 	| 243 	| 4.19% |
| UNION 	| 199 	| 3.43% |
| NOTEXISTS 	| 82 	| 1.41% |
| GROUP_CONCAT 	| 71 	| 1.22% |
| MAX 	    | 46 	    | 0.79% |
| MINUS 	| 42 	    | 0.72% |
| MIN 	    | 35 	    | 0.6% |
| SUM 	    | 34 	    | 0.58% |
| EXISTS 	| 22 	    | 0.38% |
| AVG 	    | 6 	    | 0.1% |
| DESCRIBE 	| 1 	    | 0.01% |
| ----------| --------- | -------- | 
| TOTAL     | 4862      | 100%  | 

For more statistics on the SPARQL keywords usage in specific Search Workflows, Search Topics, Macro Topics, you can query the [SPARQL endpoint](http://w3id.org/esw/sparql) binding the variables you want.

### Evaluation Results

| Topic   | Avg Fscore | Avg queries | Tot queries |
| ----------| --------- | -------- |  -------- | 
| Literary Movements and Divine Comedy  | 0.73 | 53 | 265 |
| Euro  | 0.7 | 54 | 323 |
| World Wide Web | 0.64 | 32 | 158 |
| Ancient Civilization  | 0.64 | 90 | 539 |
| Cultural Movements  | 0.48 | 35 | 174 |
| Ancient Rome  | 0.74 | 47 | 186 |
| Literary Movements and physicists  | 0.62 | 37 | 186 |
| Tv series Without a Trace  | 0.58 | 57 | 284 |
| Disney  | 0.6 | 34 | 171 |
| Film Genre and directors  | 0.23 | 51 | 253 |
| Production company  | 0.52 | 37 | 184 |
| Tv series HIMYM  | 0.19 | 61 | 368 |
| Sherlock Holmes  | 0.73 | 39 | 232 |
| Film Genre and composer  | 0.42 | 36 | 144 |
| Association Football Players  | 0.58 | 39 | 195 |
| Olympic Games  | 0.58 | 47 | 186 |
| Running  | 0.3 | 44 | 221 |
| Tennis  | 0.58 | 104 | 626 |
| Basketball and NBA seasons  | 0.75 | 65 | 326 |
| Association Football Club  | 0.72 | 76 | 382 |
| Basketball and NBA finals  | 0.75 | 64 | 383 |