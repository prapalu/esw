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

| Keyword   | # queries | %queries |
| ----------| --------- | -------- | 
| SELECT 	| 5783 	    | 118.94% |
| DISTINCT 	| 5319 	    | 109.39% |
| LIMIT 	| 5234 	    | 107.65% |
| FILTER 	| 1557 	    | 32.02% |
| COUNT 	| 881 	    | 18.12% |
| GROUPBY 	| 864 	    | 17.77% |
| ORDERBY 	| 746 	    | 15.34% |
| REGEX 	| 671 	    | 13.8% |
| OPTIONAL 	| 348 	    | 7.15% |
| HAVING 	| 250 	    | 5.14% |
| NESTEDQUERY 	| 243 	| 4.99% |
| UNION 	| 199 	    | 4.09% |
| NOTEXISTS 	| 82 	| 1.68% |
| GROUP_CONCAT 	| 71 	| 1.46% |
| MAX 	    | 46 	    | 0.94% |
| MINUS 	| 42 	    | 0.86% |
| MIN   	| 35 	    | 0.71% |
| SUM 	    | 34 	    | 0.69% |
| EXISTS 	| 22 	    | 0.45% |
| AVG 	    | 6 	    | 0.12% |
| DESCRIBE 	| 1 	    | 0.02% |
| ----------| --------- | -------- | 
| TOTAL     | 4862      | 100%  | 

For more statistics on the SPARQL keywords usage in specific Search Workflows, Search Topics, Macro Topics, you can query the [SPARQL endpoint](http://w3id.org/esw/sparql) binding the variables you want.