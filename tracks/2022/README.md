# 2022 Track

This folder contains the 2022 track.
Furthermore we report here some statistics for this track.

## Content

- [general statistics](#statistics)
- [exploratory workflows](#exploratory-workflows)
- [keywords analysis](#keywords-analysis)
- [evaluation results](#evaluation-results)

### Statistics

The 2022 track is composed of:
- 3 macro topic (Movies, Sports, History)
- 36 workers
- 21 Search Topics
- 108 Exploratory Workflows (each worker was assigned to implement a exploratory workflow for each macro topic)
- 5784 queries

### Exploratory Workflows

Each Search Topic was implemented by 4 to 6 workers in order to obtain different points of view. The table below shows the distribution of the Exploratory Workflows.

You can get the statistics below querying the RDF Graph. [Execute query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=PREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0APREFIX+eswr%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fresource%2F%3E%0D%0A%0D%0ASELECT+%3FtopicLabel+%28COUNT%28DISTINCT+%3Fworkflow%29+AS+%3Fworkflows%29+%28SUM%28%3FnumQueries%29%2FCOUNT%28DISTINCT+%3Fworkflow%29+AS+%3FavgQueries%29+%28SUM%28%3FnumQueries%29+AS+%3FtotQueries%29+where%7B%0D%0A++++%3Fworkflow+esw%3Aimplements+%3Ftopic%3B%0D%0A++++%09esw%3AhasPart+%3Fpart.%0D%0A+++%09%3Fpart+esw%3AnumberOfQueries+%3FnumQueries.%0D%0A++++%3Ftopic+esw%3ApartOf+eswr%3ACompleteness2022Track%3B%0D%0A+++++++++++rdfs%3Alabel+%3FtopicLabel.%0D%0A%7D%0D%0AGROUP+BY+%3Ftopic+%3FtopicLabel%0D%0AORDER+BY+%3FtopicLabel&format=text%2Fhtml&timeout=0&signal_void=on)

| Search Topic | #Workflows | AVG(queries) | # queries|
| -------------| -----------| -----------|-----------|
| **History**                           | **36** | **50**| **1830**|
| Literary Movements and Divine Comedy 	| 5	| 53	| 265 |
| Euro 	                                | 6	| 53	| 323 |
| World Wide Web	                    | 5	| 31	| 158 |
| Ancient Civilization 	                | 6	| 89	| 539 |
| Cultural Movements 	                | 5	| 34	| 174 |
| Ancient Rome 	                        | 4	| 46	| 185 |
| Literary Movements and physicists 	| 5	| 37	| 186 |
| **Movies**                    | **36** | **45**| **1636**|
| Tv series Without a Trace 	| 5	| 56	| 284 |
| Disney 	                    | 5	| 34	| 171 |
| Film Genre and directors 	    | 5	| 50	| 253 |
| Production company 	        | 5	| 36	| 184 |
| Tv series HIMYM 	            | 6	| 61	| 368 |
| Sherlock Holmes 	            | 6	| 38	| 232 |
| Film Genre and composer 	    | 4	| 36	| 144 |
| **Sport**                     | **36** | **64**| **2318**|
| Association Football Players 	| 5	| 39	| 195 |
| Olympic Games 	            | 4	| 46	| 186 |
| Running 	                    | 5	| 44	| 221 |
| Tennis 	                    | 6	| 104	| 626 |
| Basketball and NBA seasons 	| 5	| 65	| 326 |
| Association Football Club 	| 5	| 76	| 382 |
| Basketball and NBA finals 	| 6	| 63	| 382 |

### Keywords Analysis

The table below shows the distribution of the SPARQL keywords in the track.

You can get the statistics below querying the RDF Graph. [Execute query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=PREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0APREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0D%0APREFIX+lsqv%3A+%3Chttp%3A%2F%2Flsq.aksw.org%2Fvocab%23%3E%0D%0APREFIX+eswr%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fresource%2F%3E%0D%0A%0D%0ASELECT+%3Fkeyword+%28COUNT%28*%29+AS+%3Ffrequency%29+%28%28COUNT%28*%29%2Fxsd%3Afloat%28%3FtotQuery%29*100.0+AS+%3Fpercentage%29%29+where%7B%0D%0A++++%7B%0D%0A++++++++SELECT+%28+COUNT%28%3Fquery%29+AS+%3FtotQuery%29%7B%0D%0A++++++++++++%3Ftopic+esw%3ApartOf+eswr%3ACompleteness2022Track.%0D%0A++++++++++++%3Fwork+esw%3Aimplements+%3Ftopic%3B%0D%0A++++++++++++++++esw%3AhasPart+%3Fjob.%0D%0A++++++++++++%3Fjob+esw%3Aqueries+%3Fqueries.%0D%0A++++++++++++%3Fqueries+rdf%3Arest*%2Frdf%3Afirst++%3Fquery.%0D%0A++++++++%7D%0D%0A++++%7D%0D%0A++++%3Ftopic+esw%3ApartOf+eswr%3ACompleteness2022Track.%0D%0A++++%3Fwork+esw%3Aimplements+%3Ftopic%3B%0D%0A++++++++++esw%3AhasPart+%3Fjob.%0D%0A++++%3Fjob+esw%3Aqueries+%3Fqueries.%0D%0A++++%3Fqueries+rdf%3Arest*%2Frdf%3Afirst++%3Fquery.%0D%0A++++%3Fquery+lsqv%3AusesFeature+%3Fkeyword.%0D%0A%7D%0D%0AGROUP+BY+%3Fkeyword+%3FtotQuery%0D%0AORDER+BY+DESC+%28%3Ffrequency%29&format=text%2Fhtml&timeout=0&signal_void=on)

| Keyword   | # queries | % queries |
| ----------| --------- | -------- | 
| SELECT	| 5783	| 99.98% |
| DISTINCT	| 5319	| 91.96% |
| LIMIT	    | 5234	| 90.49% |
| FILTER	| 1557	| 26.92% |
| COUNT	    | 881	| 15.23% |
| GROUP BY	| 864	| 14.94% |
| ORDER BY	| 746	| 12.9% |
| REGEX	    | 671	| 11.6% |
| OPTIONAL	| 348	| 6.02% |
| HAVING	| 250	| 4.32% |
| UNION	    | 199	| 3.44% |
| NOT EXISTS	| 82	| 1.42% |
| GROUP_CONCAT	| 71	| 1.23% |
| MAX	    | 46	| 0.8% |
| MINUS	    | 42	| 0.73% |
| MIN	    | 35	| 0.61% |
| SUM	    | 34	| 0.59% |
| EXISTS	| 22	| 0.38% |
| AVG	    | 6	| 0.1% |
| DESCRIBE	| 1	| 0.02% |
| ----------| --------- | -------- | 
| TOTAL     | 5784      | 100%  | 

For more statistics on the SPARQL keywords usage in specific Exploratory Workflows, Search Topics, Macro Topics, you can query the [SPARQL endpoint](http://w3id.org/esw/sparql) binding the variables you want.

### Evaluation Results

#### Average Fscore for each topic

The table below shows, for each topic of the track, the average Fscore obtained by the Exploratory Workflows.

For this example, the f-score of the workflow is calculated averaging the f-scores of the Search Jobs, which is in turn computes as the maximum f-score of the queries in such Search Job.

You can get these statistics querying the RDF Graph. [Execute query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=%0D%0APREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0APREFIX+eswr%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fresource%2F%3E%0D%0A%0D%0ASELECT+%3FtopicLabel+%28AVG%28%3Favgfscore%29+AS+%3Favgfscore%29+where%7B%0D%0A++++%7B%0D%0A++++++++SELECT+%3Fworkflow+%3Ftopic+%28AVG%28%3Fscore%29+AS+%3Favgfscore%29+WHERE%7B%0D%0A++++++++++++%7B%0D%0A++++++++++++++++SELECT+%3Fworkflow+%3Fpart+%28MAX%28%3Fscore%29+AS+%3Fscore%29+WHERE%7B%0D%0A++++++++++++++++++++%3Fworkflow+a+esw%3AExploratoryWorkflow%3B%0D%0A++++++++++++++++++++++++esw%3AhasPart+%3Fpart.%0D%0A++++++++++++++++++++%3Fpart+esw%3Aqueries+%3Fqueries.%0D%0A++++++++++++++++++++%3Fqueries+rdf%3Arest*%2Frdf%3Afirst+%3Fquery.%0D%0A++++++++++++++++++++OPTIONAL%7B%3Fquery+esw%3Afscore+%3Fscore.%7D%0D%0A++++++++++++++++%7D%0D%0A++++++++++++++++GROUP+BY+%3Fworkflow+%3Fpart%0D%0A++++++++++++%7D%0D%0A++++++++++++%3Fworkflow+a+esw%3AExploratoryWorkflow%3B%0D%0A++++++++++++++++esw%3Aimplements+%3Ftopic.%0D%0A++++++++%7D%0D%0A++++++++GROUP+BY+%3Fworkflow+%3Ftopic%0D%0A++++%7D%0D%0A++++%3Ftopic+esw%3ApartOf+eswr%3ACompleteness2022Track%3B%0D%0A++++++++rdfs%3Alabel+%3FtopicLabel.%0D%0A%7D%0D%0AGROUP+BY+%3FtopicLabel%0D%0AHAVING+%28AVG%28%3Favgfscore%29%3E0.0%29%0D%0AORDER+BY+%3FtopicLabel&format=text%2Fhtml&timeout=0&signal_void=on)

| Search Topic   | Avg Fscore | 
| ----------| --------- |
| **History**                           | **0.56** |
| Literary Movements and Divine Comedy 	| 0.74 |
| Euro 	                                | 0.70 |
| World Wide Web	                    | 0.75 |
| Ancient Civilization 	                | 0.73 |
| Cultural Movements 	                | 0.48 |
| Ancient Rome 	                        | 0.75 |
| Literary Movements and physicists 	| 0.72 |
| **Movies**                            | **0.63** |
| Tv series Without a Trace 	        | 0.61 |
| Disney 	                            | 0.61 |
| Film Genre and directors          	| 0.62 |
| Production company 	                | 0.52 |
| Tv series HIMYM 	                    | 0.35 |
| Sherlock Holmes 	                    | 0.74 |
| Film Genre and composer 	            | 0.49 |
| **Sports**                            | **0.70** |
| Association Football Players 	        | 0.59 |
| Olympic Games 	                    | 0.59 |
| Running 	                            | 0.43 |
| Tennis 	                            | 0.59 |
| Basketball and NBA seasons 	        | 0.75 |
| Association Football Club 	        | 0.73 |
| Basketball and NBA finals 	        | 0.75 |

#### Best Exploratory Workflow for each Search Topic

The table below shows, for each topic of the track, the best Exploratory Workflows, with its Fscore, the number of queries and the realted ground truth.

For this example, the f-score of the workflow is calculated averaging the f-scores of the Search Jobs, which is in turn computes as the maximum f-score of the queries in such Search Job.

The exploratory Workflows and the Ground Truths links to the real resource.


You can get these statistics querying the RDF Graph. [Execute query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=PREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0APREFIX+eswr%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fresource%2F%3E%0D%0A%0D%0ASELECT+%3Fworkflow+%3FtopicLabel+%3FavgFscore+%3FnumQueries+%3FgroundTruth+WHERE%7B%0D%0A++++%0D%0A++++%7B%0D%0A++++++++SELECT+%3Ftopic+%3Fmacro+%28MAX%28%3Ffscore%29+AS+%3Fmax_score%29+WHERE%0D%0A++++++++%7B%0D%0A++++++++++++%7B%0D%0A++++++++++++++++SELECT+%3Fwork+%28AVG%28%3Fscore%29+AS+%3Ffscore%29+WHERE%7B%0D%0A++++++++++++++++++++%7B%0D%0A++++++++++++++++++++++++SELECT+%3Fwork+%3Fpart+%28MAX%28%3Fscore%29+AS+%3Fscore%29+WHERE%7B%0D%0A++++++++++++++++++++++++++++%3Fwork+a+esw%3AExploratoryWorkflow%3B%0D%0A++++++++++++++++++++++++++++++++esw%3AhasPart+%3Fpart.%0D%0A++++++++++++++++++++++++++++%3Fpart+esw%3Aqueries+%3Fqueries.%0D%0A++++++++++++++++++++++++++++%3Fqueries+rdf%3Arest*%2Frdf%3Afirst+%3Fquery.%0D%0A++++++++++++++++++++++++++++OPTIONAL%7B+%3Fquery+esw%3Afscore+%3Fscore.+%7D%0D%0A++++++++++++++++++++++++%7D%0D%0A++++++++++++++++++++++++GROUP+BY+%3Fwork+%3Fpart%0D%0A++++++++++++++++++++%7D%0D%0A++++++++++++++++++++%3Fwork+a+esw%3AExploratoryWorkflow%3B%0D%0A++++++++++++++++++++++++++esw%3AhasPart+%3Fpart.%0D%0A++++++++++++++++%7D%0D%0A++++++++++++++++GROUP+BY+%3Fwork+%0D%0A++++++++++++%7D%0D%0A++++++++++++FILTER%28%3Ffscore+%3E+0.0%29.%0D%0A++++++++++++%3Fwork+esw%3Aimplements+%3Ftopic.%0D%0A++++++++++++%3Ftopic+esw%3Adescription+%3Fmacro.%0D%0A++++++++%7D%0D%0A++++++++GROUP+BY+%3Ftopic+%3Fmacro%0D%0A%0D%0A++++++++%7D%0D%0A++++%0D%0A++++%7B%0D%0A++++++++SELECT+%3Fworkflow+%3Ft+%28AVG%28%3Fscore%29+AS+%3FavgFscore%29+%28SUM%28%3FnumQueries%29+AS+%3FnumQueries%29+WHERE%7B%0D%0A++++++++++++%7B%0D%0A++++++++++++++++SELECT+%3Fworkflow+%3Fpart+%28MAX%28%3Fscore%29+AS+%3Fscore%29+WHERE%7B%0D%0A++++++++++++++++++++%3Fworkflow+a+esw%3AExploratoryWorkflow%3B%0D%0A++++++++++++++++++++++++esw%3AhasPart+%3Fpart.%0D%0A++++++++++++++++++++%3Fpart+esw%3Aqueries+%3Fqueries.%0D%0A++++++++++++++++++++%3Fqueries+rdf%3Arest*%2Frdf%3Afirst+%3Fquery.%0D%0A++++++++++++++++++++OPTIONAL%7B%3Fquery+esw%3Afscore+%3Fscore.%7D%0D%0A++++++++++++++++%7D%0D%0A++++++++++++++++GROUP+BY+%3Fworkflow+%3Fpart%0D%0A++++++++++++%7D%0D%0A++++++++++++%3Fworkflow+a+esw%3AExploratoryWorkflow%3B%0D%0A++++++++++++++++esw%3Aimplements+%3Ft%3B%0D%0A++++++++++++++++esw%3AhasPart+%3Fpart.%0D%0A++++++++++++%3Fpart+esw%3AnumberOfQueries+%3FnumQueries.%0D%0A++++++++%7D%0D%0A++++++++GROUP+BY+%3Fworkflow+%3Ft%0D%0A++++%7D%0D%0A++++FILTER%28%3FavgFscore+%3D+%3Fmax_score%29.%0D%0A++++FILTER%28%3Ft+%3D+%3Ftopic%29.%0D%0A++++%3Ft+esw%3AhasGroundTruth+%3FgroundTruth%3B%0D%0A++++++++esw%3ApartOf+eswr%3ACompleteness2022Track%3B%0D%0A++++++++rdfs%3Alabel+%3FtopicLabel.%0D%0A%7D%0D%0AORDER+BY+%3FtopicLabel&format=text%2Fhtml&timeout=0&signal_void=on)

| Exploratory Workflow|Search Topic | Fscore | queries | Ground Truth |
| ---------- | ---------- | --------- | -------- |  -------- | 
| **History** ||||
| [841f86edd2](http://w3id.org/esw/resource/841f86edd2) | Literary Movements and Divine Comedy  | 0.87 | 98 | [workflow1_3](http://w3id.org/esw/resource/workflow1_3) |
| [8d34e4f344](http://w3id.org/esw/resource/8d34e4f344) | Euro                                  | 0.90 | 157 | [workflow1_1](http://w3id.org/esw/resource/workflow1_1) |
| [cbba0a4300](http://w3id.org/esw/resource/cbba0a4300) | World Wide Web                        | 0.87 | 20 | [workflow1_2](http://w3id.org/esw/resource/workflow1_2) |
| [4bb8191b56](http://w3id.org/esw/resource/4bb8191b56) | Ancient Civilization                  | 0.87 | 115 | [workflow1_4](http://w3id.org/esw/resource/workflow1_4) |
| [3cae106501](http://w3id.org/esw/resource/3cae106501) | Cultural Movements                    | 0.75 | 54 | [workflow1_6](http://w3id.org/esw/resource/workflow1_6) |
| [d47addd645](http://w3id.org/esw/resource/d47addd645) | Ancient Rome                          | 0.92 | 67 | [workflow1_5](http://w3id.org/esw/resource/workflow1_5) |
| [df6ce197ae](http://w3id.org/esw/resource/df6ce197ae) | Literary Movements and physicists     | 0.82 | 35 | [workflow1_0](http://w3id.org/esw/resource/workflow1_0) |
| **Movies** ||||
| [106b3c299a](http://w3id.org/esw/resource/106b3c299a) | Tv series Without a Trace     | 0.68 | 126 | [workflow2_3](http://w3id.org/esw/resource/workflow2_3) |
| [3568e26c20](http://w3id.org/esw/resource/3568e26c20) | Disney                        | 0.84 | 56 | [workflow2_2](http://w3id.org/esw/resource/workflow2_2) |
| [8f7f46850d](http://w3id.org/esw/resource/8f7f46850d) | Film Genre and directors      | 0.74 | 31 | [workflow2_0](http://w3id.org/esw/resource/workflow2_0) |
| [54f5b7e1cb](http://w3id.org/esw/resource/54f5b7e1cb) | Production company            | 0.86 | 44 | [workflow2_6](http://w3id.org/esw/resource/workflow2_6) |
| [2621f41178](http://w3id.org/esw/resource/2621f41178) | Tv series HIMYM               | 0.44 | 54 | [workflow2_4](http://w3id.org/esw/resource/workflow2_4) |
| [06c22cdbe2](http://w3id.org/esw/resource/06c22cdbe2) | Sherlock Holmes               | 0.94 | 36 | [workflow2_1](http://w3id.org/esw/resource/workflow2_1) |
| [4b3c2739ac](http://w3id.org/esw/resource/4b3c2739ac) | Film Genre and composer       | 0.82 | 47 | [workflow2_5](http://w3id.org/esw/resource/workflow2_5) |
| **Sports** ||||
| [2c1bc38aaa](http://w3id.org/esw/resource/2c1bc38aaa) | Association Football Players  | 1.00 | 53 | [workflow0_6](http://w3id.org/esw/resource/workflow0_6) |
| [35c2113d62](http://w3id.org/esw/resource/35c2113d62) | Olympic Games                 | 0.82 | 78 | [workflow0_5](http://w3id.org/esw/resource/workflow0_5) |
| [830baa5607](http://w3id.org/esw/resource/830baa5607) | Running                       | 0.58 | 102 | [workflow0_2](http://w3id.org/esw/resource/workflow0_2) |
| [616ea09c9e](http://w3id.org/esw/resource/616ea09c9e) | Tennis                        | 0.67 | 341 | [workflow0_4](http://w3id.org/esw/resource/workflow0_4) |
| [080ba229ef](http://w3id.org/esw/resource/080ba229ef) | Basketball and NBA seasons    | 0.96 | 91 | [workflow0_3](http://w3id.org/esw/resource/workflow0_3) |
| [c19f714ccc](http://w3id.org/esw/resource/c19f714ccc) | Association Football Club     | 0.93 | 49 | [workflow0_0](http://w3id.org/esw/resource/workflow0_0) |
| [95820d24bc](http://w3id.org/esw/resource/95820d24bc) | Basketball and NBA finals     | 0.99 | 43 | [workflow0_1](http://w3id.org/esw/resource/workflow0_1) |

