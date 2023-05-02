# 2022 Track

This folder contains the 2022 track.
Furthermore we report here some statistics for this track.

## Content

- [general statistics](#statistics)
- [search workflows](#search-workflows)
- [keywords analysis](#keywords-analysis)
- [evaluation results](#evaluation-results)
- [runtime analysis](#runtime-analysis)

### Statistics

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
| GROUP BY 	| 864 	    | 14.93% |
| ORDER BY 	| 746 	    | 12.89% |
| REGEX 	| 671 	    | 11.59% |
| OPTIONAL 	| 348 	    | 6.01% |
| HAVING 	| 250 	    | 4.32% |
| NESTED QUERY 	| 243 	| 4.19% |
| UNION 	| 199 	| 3.43% |
| NOT EXISTS 	| 82 	| 1.41% |
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

#### Average Fscore for each topic

The table below shows, for each topic of the track, the average Fscore obtained by the Search Workflows, the average queries and the total number of queries.

You can get these statistics querying the RDF Graph. [Execute query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=PREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0APREFIX+eswr%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fresource%2F%3E%0D%0A%0D%0ASELECT+%3FtopicLabel+%28AVG%28%3Ffscore%29+AS+%3FavgFscore%29+%28ROUND%28AVG%28%3Fqs%29%29+AS+%3FavgQueries%29+%28SUM%28%3Fqs%29+AS+%3FtotQueries%29+WHERE%7B+%0D%0A++++%7B%0D%0A++++++++SELECT+%3Fworkflow+%28AVG%28%3Ffs%29+AS+%3Ffscore%29+%28SUM%28%3Fqueries%29+AS+%3Fqs%29+WHERE%7B%0D%0A++++++++++++%3Fworkflow+esw%3Aimplements+%3Ft%3B%0D%0A++++++++++++++++++esw%3AwroteBy+%3Fworker%3B%0D%0A++++++++++++++++++esw%3AhasPart+%3Fpart.%0D%0A++++++++++++%3Fpart+esw%3Afscore+%3Ffs%3B%0D%0A++++++++++++++++++esw%3AnumberOfQueries+%3Fqueries.%0D%0A++++++++%7DGROUP+BY+%3Fworkflow%0D%0A++++%7D%0D%0A%3Ftopic+esw%3ApartOf+eswr%3ACompleteness2022Track.%0D%0A++++%3Fworkflow+esw%3Aimplements+%3Ftopic.%0D%0A++++%3Ftopic+esw%3Adescription+%3FtopicLabel.%0D%0A%7D%0D%0AGROUP+BY+%3FtopicLabel%0D%0AHAVING+%28AVG%28%3Ffscore%29%3E+0.0%29%0D%0AORDER+BY+ASC+%28%3FtopicLabel%29&format=text%2Fhtml&timeout=0&signal_void=on)

| Search Topic   | Avg Fscore | Avg queries | Tot queries |
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

#### Best Search Workflow for each Search Topic

The table below shows, for each topic of the track, the best Search Workflows, with its Fscore, the number of queries and the realted ground truth.

The search Workflows and the Ground Truths links to the real resource.

You can get these statistics querying the RDF Graph. [Execute query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=PREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0APREFIX+eswr%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fresource%2F%3E%0D%0A%0D%0ASELECT+%3Fworkflow+%3FtopicLabel+%3FavgFscore+%3FnumQueries+%3FgroundTruth+WHERE%7B%0D%0A++++%0D%0A++++%7B%0D%0A++++++++SELECT+%3Ftopic+%3Fmacro+%28MAX%28%3Ffscore%29+AS+%3Fmax_score%29+WHERE%0D%0A++++++++%7B%0D%0A++++++++++++%7B%0D%0A++++++++++++++++select+%3Fwork+%28AVG%28%3Fscore%29+AS+%3Ffscore%29+WHERE%7B%0D%0A++++++++++++++++++++%3Fwork+a+esw%3ASearchWorkflow%3B%0D%0A++++++++++++++++++++++++++esw%3AhasPart+%3Fpart.%0D%0A++++++++++++++++++++%3Fpart+esw%3Afscore+%3Fscore.%0D%0A++++++++++++++++%7D%0D%0A++++++++++++++++GROUP+BY+%3Fwork+%0D%0A++++++++++++%7D%0D%0A++++++++++++FILTER%28%3Ffscore+%3E+0.1%29.%0D%0A++++++++++++%3Fwork+esw%3Aimplements+%3Ftopic.%0D%0A++++++++++++%3Ftopic+esw%3Adescription+%3Fmacro.%0D%0A++++++++%7D%0D%0A++++++++GROUP+BY+%3Ftopic+%3Fmacro%0D%0A%0D%0A++++++++%7D%0D%0A++++%0D%0A++++%7B%0D%0A++++++++select+%3Fworkflow+%3Ft+%28AVG%28%3Fs%29+AS+%3FavgFscore%29+%28SUM%28%3Fnq%29+AS+%3FnumQueries%29+WHERE%7B%0D%0A++++++++++++%3Fworkflow+a+esw%3ASearchWorkflow%3B%0D%0A++++++++++++++++esw%3AhasPart+%3Fp.%0D%0A++++++++++++++++%3Fp+esw%3Afscore+%3Fs.%0D%0A++++++++++++++++%3Fp+esw%3AnumberOfQueries+%3Fnq.%0D%0A++++++++++++%3Fworkflow+esw%3Aimplements+%3Ft.%0D%0A++++++++++++%0D%0A++++++++%7D%0D%0A++++++++GROUP+BY+%3Fworkflow+%3Ft+%0D%0A++++%7D%0D%0A++++FILTER%28%3FavgFscore+%3D+%3Fmax_score%29.%0D%0A++++FILTER%28%3Ft+%3D+%3Ftopic%29.%0D%0A++++%3Ft+esw%3AhasGroundTruth+%3FgroundTruth%3B%0D%0A+++++++esw%3ApartOf+eswr%3ACompleteness2022Track%3B%0D%0A++++++++rdfs%3Alabel+%3FtopicLabel.%0D%0A%7D%0D%0AORDER+BY+%3FtopicLabel&format=text%2Fhtml&timeout=0&signal_void=on)

| Search Workflow|Search Topic | Fscore | queries | Ground Truth |
| ---------- | ---------- | --------- | -------- |  -------- | 
| [841f86edd2](http://w3id.org/esw/resource/841f86edd2) | Literary Movements and Divine Comedy  | 0.87 | 98 | [workflow1_3](http://w3id.org/esw/resource/workflow1_3) |
| [8d34e4f344](http://w3id.org/esw/resource/8d34e4f344) | Euro  | 0.9 | 157 | [workflow1_1](http://w3id.org/esw/resource/workflow1_1) |
| [cbba0a4300](http://w3id.org/esw/resource/cbba0a4300) | World Wide Web | 0.74 | 20 | [workflow1_2](http://w3id.org/esw/resource/workflow1_2) |
| [4bb8191b56](http://w3id.org/esw/resource/4bb8191b56) | Ancient Civilization  | 0.76 | 115 | [workflow1_4](http://w3id.org/esw/resource/workflow1_4) |
| [3cae106501](http://w3id.org/esw/resource/3cae106501) | Cultural Movements  | 0.75 | 54 | [workflow1_6](http://w3id.org/esw/resource/workflow1_6) |
| [d47addd645](http://w3id.org/esw/resource/d47addd645) | Ancient Rome  | 0.92 | 68 | [workflow1_5](http://w3id.org/esw/resource/workflow1_5) |
| [df6ce197ae](http://w3id.org/esw/resource/df6ce197ae) | Literary Movements and physicists  | 0.71 | 35 | [workflow1_0](http://w3id.org/esw/resource/workflow1_0) |
| [106b3c299a](http://w3id.org/esw/resource/106b3c299a) | Tv series Without a Trace  | 0.66 | 126 | [workflow2_3](http://w3id.org/esw/resource/workflow2_3) |
| [3568e26c20](http://w3id.org/esw/resource/3568e26c20) | Disney  | 0.84 | 56 | [workflow2_2](http://w3id.org/esw/resource/workflow2_2) |
| [4ddda0dbce](http://w3id.org/esw/resource/4ddda0dbce) | Film Genre and directors  | 0.28 | 31 | [workflow2_0](http://w3id.org/esw/resource/workflow2_0) |
| [54f5b7e1cb](http://w3id.org/esw/resource/54f5b7e1cb) | Production company  | 0.86 | 44 | [workflow2_6](http://w3id.org/esw/resource/workflow2_6) |
| [2621f41178](http://w3id.org/esw/resource/2621f41178) | Tv series HIMYM  | 0.29 | 54 | [workflow2_4](http://w3id.org/esw/resource/workflow2_4) |
| [06c22cdbe2](http://w3id.org/esw/resource/06c22cdbe2) | Sherlock Holmes  | 0.94 | 36 | [workflow2_1](http://w3id.org/esw/resource/workflow2_1) |
| [4b3c2739ac](http://w3id.org/esw/resource/4b3c2739ac) | Film Genre and composer  | 0.69 | 47 | [workflow2_5](http://w3id.org/esw/resource/workflow2_5) |
| [2c1bc38aaa](http://w3id.org/esw/resource/2c1bc38aaa) | Association Football Players  | 1.0 | 53 | [workflow0_6](http://w3id.org/esw/resource/workflow0_6) |
| [35c2113d62](http://w3id.org/esw/resource/35c2113d62) | Olympic Games  | 0.82 | 78 | [workflow0_5](http://w3id.org/esw/resource/workflow0_5) |
| [830baa5607](http://w3id.org/esw/resource/830baa5607) | Running  | 0.41 | 102 | [workflow0_2](http://w3id.org/esw/resource/workflow0_2) |
| [616ea09c9e](http://w3id.org/esw/resource/616ea09c9e) | Tennis  | 0.67 | 341 | [workflow0_4](http://w3id.org/esw/resource/workflow0_4) |
| [080ba229ef](http://w3id.org/esw/resource/080ba229ef) | Basketball and NBA seasons  | 0.96 | 91 | [workflow0_3](http://w3id.org/esw/resource/workflow0_3) |
| [c19f714ccc](http://w3id.org/esw/resource/c19f714ccc) | Association Football Club  | 0.93 | 49 | [workflow0_0](http://w3id.org/esw/resource/workflow0_0) |
| [95820d24bc](http://w3id.org/esw/resource/95820d24bc) | Basketball and NBA finals  | 0.99 | 43 | [workflow0_1](http://w3id.org/esw/resource/workflow0_1) |

### Runtime Analysis

#### Macro Topic Execution Analysis

The table below shows, for each macro topic the statistics for the execution time of the queries in that macro topic.

You can get these statistics querying the RDF Graph. [Execute query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=%0D%0APREFIX+eswr%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fresource%2F%3E%0D%0APREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0APREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0D%0APREFIX+lsqv%3A+%3Chttp%3A%2F%2Flsq.aksw.org%2Fvocab%23%3E%0D%0APREFIX+xsd%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23%3E%0D%0A%0D%0ASELECT+%3Fmacro+%3FavgTrackDuration+%28%28SUM%28%3FthisVar%29%2F%3FnumTrackDuration%29+AS+%3Fvariance%29+%3FmaxTrackDuration+%3FexecutionErrors+WHERE%7B%0D%0A++++%7B%0D%0A++++++++SELECT+%3Fmacro+%28AVG%28%3Fdur%29+AS+%3FavgTrackDuration%29+%28COUNT%28%3Fdur%29+AS+%3FnumTrackDuration%29+%28MAX%28%3Fdur%29+AS+%3FmaxTrackDuration%29+where+%7B+%0D%0A++++++++++++%3Ftopic+esw%3ApartOf+eswr%3ACompleteness2022Track.%0D%0A++++++++++++%3Ftopic+esw%3AmacroTopic+%3Fmacro.%0D%0A++++++++++++%3Fwork+esw%3AhasPart+%3Fpart.%0D%0A++++++++++++%3Fwork+esw%3Aimplements+%3Ftopic.%0D%0A++++++++++++%3Fpart+esw%3Aqueries+%3Fo+.%0D%0A++++++++++++%3Fo+rdf%3Arest*%2Frdf%3Afirst++%3Fquery.%0D%0A++++++++++++%3Fquery+lsqv%3AhasExec+%3Fexec.%0D%0A++++++++++++%3Fexec+lsqv%3AevalDuration+%3Fdur.%0D%0A++++++++%7D+GROUP+BY+%3Fmacro%0D%0A++++%7D%0D%0A++++%7B%0D%0A++++++++SELECT+%3Fmacro+%28COUNT%28*%29+AS+%3FexecutionErrors%29+where+%7B+%0D%0A++++++++++++%3Ftopic+esw%3ApartOf+eswr%3ACompleteness2022Track.%0D%0A++++++++++++%3Ftopic+esw%3AmacroTopic+%3Fmacro.%0D%0A++++++++++++%3Fwork+esw%3AhasPart+%3Fpart.%0D%0A++++++++++++%3Fwork+esw%3Aimplements+%3Ftopic.%0D%0A++++++++++++%3Fpart+esw%3Aqueries+%3Fo+.%0D%0A++++++++++++%3Fo+rdf%3Arest*%2Frdf%3Afirst++%3Fquery.%0D%0A++++++++++++%3Fquery+lsqv%3AparseError+%3FpErr.%0D%0A++++++++%7D+GROUP+BY+%3Fmacro%0D%0A++++%7D%0D%0A%09%3Ftopic+esw%3ApartOf+eswr%3ACompleteness2022Track.%0D%0A++++%3Ftopic+esw%3AmacroTopic+%3Fmacro.%0D%0A++++%3Fwork+esw%3AhasPart+%3Fpart.%0D%0A++++%3Fwork+esw%3Aimplements+%3Ftopic.%0D%0A++++%3Fpart+esw%3Aqueries+%3Fo+.%0D%0A++++%3Fo+rdf%3Arest*%2Frdf%3Afirst++%3Fquery.%0D%0A++++%3Fquery+lsqv%3AhasExec+%3Fexec.%0D%0A++++%3Fexec+lsqv%3AevalDuration+%3Fdur.%0D%0A++++BIND%28xsd%3Afloat%28xsd%3Afloat%28%3Fdur%29+-+xsd%3Afloat%28%3FavgTrackDuration%29%29*%28xsd%3Afloat%28%3Fdur%29+-+xsd%3Afloat%28%3FavgTrackDuration%29%29+AS+%3FthisVar%29%0D%0A%7D%0D%0AGROUP+BY+%3Fmacro+%3FavgTrackDuration+%3FnumTrackDuration+%3FexecutionErrors+%3FmaxTrackDuration%0D%0A&format=text%2Fhtml&timeout=0&signal_void=on)

| Keyword | Mean | Variance | Max Time | Execution Errors |
| ---------- | ---------- | --------- | -------- |  -------- | 
| Movie 	| 0.6 	| 12.71 	| 53.54 	| 4 |
| Sport 	| 2.38 	| 297.63 	| 292.23 	| 10 |
| Politics 	| 1.49 	| 105.31 	| 181.77 	| 24 |
| Book 	    | 3.75 	| 587.38 	| 282.55 	| 14 |
| GEO 	    | 1.01 	| 68.05 	| 184.59 	| 1 |
| Companies | 1.72 	| 94.3 	    | 151.06 	| 7 |
| Total     | 1.88  | 208.32    | 292.23    | 60 |



#### Keywords Execution Analysis

The table below shows, for each keyword the statistics for the execution time of the queries containing such keyword.

You can get these statistics querying the RDF Graph. [Execute query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=PREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0APREFIX+eswr%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fresource%2F%3E%0D%0APREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0D%0APREFIX+lsqv%3A+%3Chttp%3A%2F%2Flsq.aksw.org%2Fvocab%23%3E%0D%0APREFIX+xsd%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23%3E%0D%0A%0D%0ASELECT+%3Fkeyword+%3FavgKeywordDuration+%28%28SUM%28%3FthisVar%29%2F%3FnumKeywordDuration%29+AS+%3Fvariance%29+%3FmaxKeywordDuration+%3FparseErrors+%28%3FnumKeywordDuration+AS+%3FnumQueries+%29+WHERE%7B%0D%0A++++%7B%0D%0A++++++++SELECT+%3Fkeyword+%28AVG%28%3Fdur%29+AS+%3FavgKeywordDuration%29+%28COUNT%28%3Fdur%29+AS+%3FnumKeywordDuration%29+%28MAX%28%3Fdur%29+AS+%3FmaxKeywordDuration%29+where+%7B+%0D%0A++++++++++++%3Ftopic+esw%3ApartOf+eswr%3ACompleteness2022Track.%0D%0A++++++++++++%3Fwork+esw%3AhasPart+%3Fpart.%0D%0A++++++++++++%3Fwork+esw%3Aimplements+%3Ftopic.%0D%0A++++++++++++%3Fpart+esw%3Aqueries+%3Fo+.%0D%0A++++++++++++%3Fo+rdf%3Arest*%2Frdf%3Afirst++%3Fquery.%0D%0A++++++++++++%3Fquery+lsqv%3AhasExec+%3Fexec.%0D%0A++++++++++++%3Fquery+lsqv%3AusesFeature+%3Fkeyword.%0D%0A++++++++++++%3Fexec+lsqv%3AevalDuration+%3Fdur.%0D%0A++++++++%7D+GROUP+BY+%3Fkeyword%0D%0A++++%7D%0D%0A++++%7B%0D%0A++++++++SELECT+%3Fkeyword+%28COUNT%28*%29+AS+%3FparseErrors%29+where+%7B+%0D%0A++++++++++++%3Ftopic+esw%3ApartOf+eswr%3ACompleteness2022Track.%0D%0A++++++++++++%3Fwork+esw%3AhasPart+%3Fpart.%0D%0A++++++++++++%3Fwork+esw%3Aimplements+%3Ftopic.%0D%0A++++++++++++%3Fpart+esw%3Aqueries+%3Fo+.%0D%0A++++++++++++%3Fo+rdf%3Arest*%2Frdf%3Afirst++%3Fquery.%0D%0A++++++++++++%3Fquery+lsqv%3AusesFeature+%3Fkeyword.%0D%0A++++++++++++%3Fquery+lsqv%3AparseError+%3FpErr.%0D%0A++++++++%7D+GROUP+BY+%3Fkeyword%0D%0A++++%7D%0D%0A%09%3Ftopic+esw%3ApartOf+eswr%3ACompleteness2022Track.%0D%0A++++%3Fwork+esw%3AhasPart+%3Fpart.%0D%0A++++%3Fwork+esw%3Aimplements+%3Ftopic.%0D%0A++++%3Fpart+esw%3Aqueries+%3Fo+.%0D%0A++++%3Fo+rdf%3Arest*%2Frdf%3Afirst++%3Fquery.%0D%0A++++%3Fquery+lsqv%3AhasExec+%3Fexec.%0D%0A++++%3Fquery+lsqv%3AusesFeature+%3Fkeyword.%0D%0A++++%3Fexec+lsqv%3AevalDuration+%3Fdur.%0D%0A++++BIND%28xsd%3Afloat%28xsd%3Afloat%28%3Fdur%29+-+xsd%3Afloat%28%3FavgKeywordDuration%29%29*%28xsd%3Afloat%28%3Fdur%29+-+xsd%3Afloat%28%3FavgKeywordDuration%29%29+AS+%3FthisVar%29%0D%0A%7D%0D%0AGROUP+BY+%3Fkeyword+%3FavgKeywordDuration+%3FnumKeywordDuration+%3FparseErrors+%3FmaxKeywordDuration%0D%0AORDER+BY+%3Fkeyword&format=text%2Fhtml&timeout=0&signal_void=on)


| Keyword | Mean | Variance | Max Time | Execution Errors | # queries|
| ---------- | ---------- | --------- | -------- |  -------- | -------- | 
| COUNT 	| 1.44 	| 204.95 	| 232.51 	| 20 	| 861 |
| DISTINCT 	| 0.83 	| 79.55 	| 232.51 	| 35 	| 5284 |
| EXISTS 	| 1.34 	| 14.28 	| 13.0 	| 1 	| 21 |
| FILTER 	| 2.02 	| 196.5 	| 170.07 	| 24 	| 1533 |
| GROUP BY 	| 1.26 	| 146.25 	| 170.07 	| 20 	| 844 |
| HAVING 	| 1.24 	| 129.25 	| 170.02 	| 7 	| 243 |
| LIMIT 	| 0.81 	| 78.55 	| 232.51 	| 41 	| 5193 |
| MAX 	| 17.98 	| 2461.39 	| 170.07 	| 3 	| 43 |
| MIN 	| 0.61 	| 2.82 	| 6.0 	| 1 	| 34 |
| NESTED QUERY 	| 3.95 	| 508.72 	| 170.07 	| 9 	| 234 |
| NOTEXISTS 	| 0.31 	| 6.03 	| 22.26 	| 1 	| 81 |
| OPTIONAL 	| 0.05 	| 0.24 	| 8.89 	| 2 	| 346 |
| ORDER BY 	| 1.31 	| 163.05 	| 170.07 	| 6 	| 740 |
| REGEX 	| 4.02 	| 426.27 	| 170.07 	| 8 	| 663 |
| SELECT 	| 0.79 	| 75.8 	| 232.51 	| 41 	| 5742 |
| SUM 	| 2.7 	| 191.57 	| 75.93 	| 5 	| 29 |
| UNION 	| 1.74 	| 94.53 	| 92.93 	| 2 	| 197 |