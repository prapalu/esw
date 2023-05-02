# 2021 Track

This folder contains the 2021 track.
Furthermore we report here some statistics for this track.

## Content

- [general statistics](#statistics)
- [search workflows](#search-workflows)
- [keywords analysis](#keywords-analysis)
- [evaluation results](#evaluation-results)
- [runtime analysis](#runtime-analysis)

### Statistics

The 2021 track is composed of:
- 6 macro topic (Geography, Politics, Movies, Book, Sport, Companies)
- 21 workers
- 24 Search Topics
- 126 Search Workflows (each worker was assigned to implement a search workflow for each macro topic)
- 4862 queries

### Search Workflows

Each Search Topic was implemented from 4 to 6 workers in order to obtain different points of view. The table below shows the distribution of the Search Workflows.

You can get the statistics below querying the RDF Graph. [Execute query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=PREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0APREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0D%0APREFIX+lsqv%3A+%3Chttp%3A%2F%2Flsq.aksw.org%2Fvocab%23%3E%0D%0APREFIX+eswr%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fresource%2F%3E%0D%0A%0D%0ASELECT+%3FtLab+%28COUNT%28DISTINCT+%3Fwork%29+AS+%3Fworks%29++%28COUNT%28DISTINCT+%3Fquery%29+AS+%3FnQueries%29+where%7B%0D%0A++++%3Ftopic+esw%3ApartOf+eswr%3AInformative2021Track.%0D%0A%3Ftopic+esw%3AmacroTopic+%3Fmacro.%0D%0A%3Ftopic+rdfs%3Alabel+%3FtLab.%0D%0A++++%3Fwork+esw%3Aimplements+%3Ftopic%3B%0D%0A++++++++++esw%3AhasPart+%3Fjob.%0D%0A++++%3Fjob+esw%3Aqueries+%3Fqueries.%0D%0A++++%3Fqueries+rdf%3Arest*%2Frdf%3Afirst++%3Fquery.%0D%0A%7D%0D%0AGROUP+BY+%3FtLab%0D%0AORDER+BY+%3FtLab&format=text%2Fhtml&timeout=0&signal_void=on)

| Search Topic | #Workflows | # queries|
| -------------| -----------| -----------|
| **Book** | **21** | **931**|
|Political Magazines     | 4         |  144 |
|Nobel laureates         | 6         |  274 |
|Authors comparison     | 6         |  253 |
|Author comparison         | 5         |  260 |
| **Companies** | **21** | **712**|
|IT Companies        |    6         |  186 |
|Economy of EU States       |    6         |  242 |
|Trademarks across the world        |    5        |  171 |
|Business People in Germany        |    4         |  113 |
| **Geography** | **21** | **592**|
|American Architects        |    5         |  186 |
|European Cathedrals       |    4         |  242 |
|archaeological sites        |    6        |  171 |
|Place of Birth, Death, and Burial        |    6        |  113 |
| **Movies** | **21** | **986**|
|Tv Series        |    5         |  251 |
|Directors       |    6         |  331 |
|The Batman movies        |    4        |  193 |
|Horror Franchises        |    6        |  211 |
| **Politics** | **21** | **759**|
|International Treaties        |    4         |  87 |
|Monarchies       |    5         |  257 |
|Politicians in E.U.        |    6        |  164 |
|Presidents of countries       |    6        |  251 |
| **Sport** | **21** | **882**|
|F1 pilots        |    6         |  276 |
|Olympic       |    6         |  213 |
|World Records        |    4        |  193 |
|FIFA World Cup events       |    5        |  200 |


### Keywords Analysis

The table below shows the distribution of the SPARQL keywords in the track.

You can get the statistics below querying the RDF Graph. [Execute query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=PREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0APREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0D%0APREFIX+lsqv%3A+%3Chttp%3A%2F%2Flsq.aksw.org%2Fvocab%23%3E%0D%0APREFIX+eswr%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fresource%2F%3E%0D%0A%0D%0ASELECT+%3Fkeyword+%28COUNT%28*%29+AS+%3Fcount%29+where%7B%0D%0A++++%3Ftopic+esw%3ApartOf+eswr%3AInformative2021Track.%0D%0A++++%3Fwork+esw%3Aimplements+%3Ftopic%3B%0D%0A++++++++++esw%3AhasPart+%3Fjob.%0D%0A++++%3Fjob+esw%3Aqueries+%3Fqueries.%0D%0A++++%3Fqueries+rdf%3Arest*%2Frdf%3Afirst++%3Fquery.%0D%0A++++%3Fquery+lsqv%3AusesFeature+%3Fkeyword.%0D%0A%7D%0D%0AGROUP+BY+%3Fkeyword%0D%0AORDER+BY+DESC+%28%3Fcount%29&format=text%2Fhtml&timeout=0&signal_void=on)

| Keyword   | # queries | % queries |
| ----------| --------- | -------- | 
| SELECT 	| 4841 	    | 99.56% |
| DISTINCT 	| 3412      | 70.17% |
| LIMIT 	| 2349 	    | 48.31% |
| ORDER BY 	| 1863 	    | 38.31% |
| FILTER 	| 1482  	| 30.48% |
| COUNT 	| 1242  	| 25.54% |
| GROUP BY 	| 1050  	| 21.59% |
| REGEX 	| 485 	    | 9.97% |
| NESTED QUERY 	| 416 	| 8.55% |
| OPTIONAL 	| 343 	| 7.05% |
| UNION 	| 259 	| 5.32% |
| GROUP_CONCAT 	| 201 	| 4.13% |
| NOT EXISTS 	| 137 	| 2.81% |
| MAX 	    | 114 	| 2.34% |
| MIN 	    | 85 	| 1.74% |
| AVG 	    | 57 	| 1.17% |
| HAVING 	| 56 	| 1.15% |
| ASK 	    | 51 	| 1.04% |
| EXISTS 	| 41 	| 0.84% |
| SUM 	    | 28 	| 0.57% |
| MINUS 	| 8 	| 0.16% |
| AND 	    | 6 	| 0.12% |
| DESCRIBE 	| 1 	| 0.02% |
| CONSTRUCT | 1 	| 0.02% |
| ----------| --------- | -------- | 
| TOTAL     | 4862  | 100%  | 

For more statistics on the SPARQL keywords usage in specific Search Workflows, Search Topics, Macro Topics, you can query the [SPARQL endpoint](http://w3id.org/esw/sparql) binding the variables you want.



### Evaluation Results

#### Average Fscore for each topic

The table below shows, for each topic of the track, the average Fscore obtained by the Search Workflows, the average queries and the total number of queries.

You can get these statistics querying the RDF Graph. [Execute query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=PREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0APREFIX+eswr%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fresource%2F%3E%0D%0A%0D%0ASELECT+%3FtopicLabel+%28AVG%28%3Ffscore%29+AS+%3FavgFscore%29+%28ROUND%28AVG%28%3Fqs%29%29+AS+%3FavgQueries%29+%28SUM%28%3Fqs%29+AS+%3FtotQueries%29+WHERE%7B+%0D%0A++++%7B%0D%0A++++++++SELECT+%3Fworkflow+%28AVG%28%3Ffs%29+AS+%3Ffscore%29+%28SUM%28%3Fqueries%29+AS+%3Fqs%29+WHERE%7B%0D%0A++++++++++++%3Fworkflow+esw%3Aimplements+%3Ft%3B%0D%0A++++++++++++++++++esw%3AwroteBy+%3Fworker%3B%0D%0A++++++++++++++++++esw%3AhasPart+%3Fpart.%0D%0A++++++++++++%3Fpart+esw%3Afscore+%3Ffs%3B%0D%0A++++++++++++++++++esw%3AnumberOfQueries+%3Fqueries.%0D%0A++++++++%7DGROUP+BY+%3Fworkflow%0D%0A++++%7D%0D%0A%3Ftopic+esw%3ApartOf+eswr%3AInformative2021Track.%0D%0A++++%3Fworkflow+esw%3Aimplements+%3Ftopic.%0D%0A++++%3Ftopic+esw%3Adescription+%3FtopicLabel.%0D%0A%7D%0D%0AGROUP+BY+%3FtopicLabel%0D%0AHAVING+%28AVG%28%3Ffscore%29%3E+0.0%29%0D%0AORDER+BY+ASC+%28%3FtopicLabel%29&format=text%2Fhtml&timeout=0&signal_void=on)

| Search Topic   | Avg Fscore | Avg queries | Tot queries |
| ----------| --------- | -------- |  -------- | 
| Tv series  | 0.13 | 50 | 251 |
| Directors  | 0.17 | 55 | 331 |
| The Batman movies  | 0.23 | 48 | 193 |
| Horror Franchises  | 0.13 | 35 | 211 |

#### Best Search Workflow for each Search Topic

The table below shows, for each topic of the track, the best Search Workflows, with its Fscore, the number of queries and the realted ground truth.

The search Workflows and the Ground Truths links to the real resource.

You can get these statistics querying the RDF Graph. [Execute query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=%0D%0APREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0APREFIX+eswr%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fresource%2F%3E%0D%0A%0D%0ASELECT+%3Fworkflow+%3FtopicLabel+%3FavgFscore+%3FnumQueries+%3FgroundTruth+WHERE%7B%0D%0A++++%0D%0A++++%7B%0D%0A++++++++SELECT+%3Ftopic+%3Fmacro+%28MAX%28%3Ffscore%29+AS+%3Fmax_score%29+WHERE%0D%0A++++++++%7B%0D%0A++++++++++++%7B%0D%0A++++++++++++++++select+%3Fwork+%28AVG%28%3Fscore%29+AS+%3Ffscore%29+WHERE%7B%0D%0A++++++++++++++++++++%3Fwork+a+esw%3ASearchWorkflow%3B%0D%0A++++++++++++++++++++++++++esw%3AhasPart+%3Fpart.%0D%0A++++++++++++++++++++%3Fpart+esw%3Afscore+%3Fscore.%0D%0A++++++++++++++++%7D%0D%0A++++++++++++++++GROUP+BY+%3Fwork+%0D%0A++++++++++++%7D%0D%0A++++++++++++FILTER%28%3Ffscore+%3E+0.1%29.%0D%0A++++++++++++%3Fwork+esw%3Aimplements+%3Ftopic.%0D%0A++++++++++++%3Ftopic+esw%3Adescription+%3Fmacro.%0D%0A++++++++%7D%0D%0A++++++++GROUP+BY+%3Ftopic+%3Fmacro%0D%0A%0D%0A++++++++%7D%0D%0A++++%0D%0A++++%7B%0D%0A++++++++select+%3Fworkflow+%3Ft+%28AVG%28%3Fs%29+AS+%3FavgFscore%29+%28SUM%28%3Fnq%29+AS+%3FnumQueries%29+WHERE%7B%0D%0A++++++++++++%3Fworkflow+a+esw%3ASearchWorkflow%3B%0D%0A++++++++++++++++esw%3AhasPart+%3Fp.%0D%0A++++++++++++++++%3Fp+esw%3Afscore+%3Fs.%0D%0A++++++++++++++++%3Fp+esw%3AnumberOfQueries+%3Fnq.%0D%0A++++++++++++%3Fworkflow+esw%3Aimplements+%3Ft.%0D%0A++++++++++++%0D%0A++++++++%7D%0D%0A++++++++GROUP+BY+%3Fworkflow+%3Ft+%0D%0A++++%7D%0D%0A++++FILTER%28%3FavgFscore+%3D+%3Fmax_score%29.%0D%0A++++FILTER%28%3Ft+%3D+%3Ftopic%29.%0D%0A++++%3Ft+esw%3AhasGroundTruth+%3FgroundTruth%3B%0D%0A+++++++esw%3ApartOf+eswr%3AInformative2021Track%3B%0D%0A++++++++rdfs%3Alabel+%3FtopicLabel.%0D%0A%7D%0D%0AORDER+BY+%3FtopicLabel&format=text%2Fhtml&timeout=0&signal_void=on)

| Search Workflow|Search Topic | Fscore | queries | Ground Truth |
| ---------- | ---------- | --------- | -------- |  -------- | 
| [8f65f028f0](http://w3id.org/esw/resource/8f65f028f0) | Tv series  | 0.39 | 37 | [workflow5_3](http://w3id.org/esw/resource/workflow5_3) |
| [daa4ae72bf](http://w3id.org/esw/resource/daa4ae72bf) | Directors  | 0.29 | 83 | [workflow5_0](http://w3id.org/esw/resource/workflow5_0) |
| [d000799b39](http://w3id.org/esw/resource/d000799b39) | The Batman movies  | 0.34 | 12 | [workflow5_1](http://w3id.org/esw/resource/workflow5_1) |
| [28dde04e63](http://w3id.org/esw/resource/28dde04e63) | Horror Franchises  | 0.38 | 53 | [workflow5_2](http://w3id.org/esw/resource/workflow5_2) |


### Runtime Analysis

#### Macro Topic Execution Analysis

The table below shows, for each macro topic the statistics for the execution time of the queries in that macro topic.

You can get these statistics querying the RDF Graph. [Execute query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=%0D%0APREFIX+eswr%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fresource%2F%3E%0D%0APREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0APREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0D%0APREFIX+lsqv%3A+%3Chttp%3A%2F%2Flsq.aksw.org%2Fvocab%23%3E%0D%0APREFIX+xsd%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23%3E%0D%0A%0D%0ASELECT+%3Fmacro+%3FavgTrackDuration+%28%28SUM%28%3FthisVar%29%2F%3FnumTrackDuration%29+AS+%3Fvariance%29+%3FmaxTrackDuration+%3FexecutionErrors+WHERE%7B%0D%0A++++%7B%0D%0A++++++++SELECT+%3Fmacro+%28AVG%28%3Fdur%29+AS+%3FavgTrackDuration%29+%28COUNT%28%3Fdur%29+AS+%3FnumTrackDuration%29+%28MAX%28%3Fdur%29+AS+%3FmaxTrackDuration%29+where+%7B+%0D%0A++++++++++++%3Ftopic+esw%3ApartOf+eswr%3AInformative2021Track.%0D%0A++++++++++++%3Ftopic+esw%3AmacroTopic+%3Fmacro.%0D%0A++++++++++++%3Fwork+esw%3AhasPart+%3Fpart.%0D%0A++++++++++++%3Fwork+esw%3Aimplements+%3Ftopic.%0D%0A++++++++++++%3Fpart+esw%3Aqueries+%3Fo+.%0D%0A++++++++++++%3Fo+rdf%3Arest*%2Frdf%3Afirst++%3Fquery.%0D%0A++++++++++++%3Fquery+lsqv%3AhasExec+%3Fexec.%0D%0A++++++++++++%3Fexec+lsqv%3AevalDuration+%3Fdur.%0D%0A++++++++%7D+GROUP+BY+%3Fmacro%0D%0A++++%7D%0D%0A++++%7B%0D%0A++++++++SELECT+%3Fmacro+%28COUNT%28*%29+AS+%3FexecutionErrors%29+where+%7B+%0D%0A++++++++++++%3Ftopic+esw%3ApartOf+eswr%3AInformative2021Track.%0D%0A++++++++++++%3Ftopic+esw%3AmacroTopic+%3Fmacro.%0D%0A++++++++++++%3Fwork+esw%3AhasPart+%3Fpart.%0D%0A++++++++++++%3Fwork+esw%3Aimplements+%3Ftopic.%0D%0A++++++++++++%3Fpart+esw%3Aqueries+%3Fo+.%0D%0A++++++++++++%3Fo+rdf%3Arest*%2Frdf%3Afirst++%3Fquery.%0D%0A++++++++++++%3Fquery+lsqv%3AparseError+%3FpErr.%0D%0A++++++++%7D+GROUP+BY+%3Fmacro%0D%0A++++%7D%0D%0A%09%3Ftopic+esw%3ApartOf+eswr%3AInformative2021Track.%0D%0A++++%3Ftopic+esw%3AmacroTopic+%3Fmacro.%0D%0A++++%3Fwork+esw%3AhasPart+%3Fpart.%0D%0A++++%3Fwork+esw%3Aimplements+%3Ftopic.%0D%0A++++%3Fpart+esw%3Aqueries+%3Fo+.%0D%0A++++%3Fo+rdf%3Arest*%2Frdf%3Afirst++%3Fquery.%0D%0A++++%3Fquery+lsqv%3AhasExec+%3Fexec.%0D%0A++++%3Fexec+lsqv%3AevalDuration+%3Fdur.%0D%0A++++BIND%28xsd%3Afloat%28xsd%3Afloat%28%3Fdur%29+-+xsd%3Afloat%28%3FavgTrackDuration%29%29*%28xsd%3Afloat%28%3Fdur%29+-+xsd%3Afloat%28%3FavgTrackDuration%29%29+AS+%3FthisVar%29%0D%0A%7D%0D%0AGROUP+BY+%3Fmacro+%3FavgTrackDuration+%3FnumTrackDuration+%3FexecutionErrors+%3FmaxTrackDuration%0D%0A&format=text%2Fhtml&timeout=0&signal_void=on)


| Keyword | Mean | Variance | Max Time | Execution Errors |
| ---------- | ---------- | --------- | -------- |  -------- | 
| History 	| 0.62 	| 42.37 	| 137.0 	| 8 |
| Sport 	| 0.86 	| 121.09 	| 232.51 	| 17 |
| Movie 	| 0.87 	| 48.94 	| 152.18 	| 18 |
| Total     | 0.79  | 75.79     | 232.52    | 43 |


#### Keywords Execution Statistics
The table below shows, for each keyword the statistics for the execution time of the queries containing such keyword.

You can get these statistics querying the RDF Graph. [Execute query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=PREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0APREFIX+eswr%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fresource%2F%3E%0D%0APREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0D%0APREFIX+lsqv%3A+%3Chttp%3A%2F%2Flsq.aksw.org%2Fvocab%23%3E%0D%0APREFIX+xsd%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23%3E%0D%0A%0D%0ASELECT+%3Fkeyword+%3FavgKeywordDuration+%28%28SUM%28%3FthisVar%29%2F%3FnumKeywordDuration%29+AS+%3Fvariance%29+%3FmaxKeywordDuration+%3FparseErrors+%28%3FnumKeywordDuration+AS+%3FnumQueries+%29+WHERE%7B%0D%0A++++%7B%0D%0A++++++++SELECT+%3Fkeyword+%28AVG%28%3Fdur%29+AS+%3FavgKeywordDuration%29+%28COUNT%28%3Fdur%29+AS+%3FnumKeywordDuration%29+%28MAX%28%3Fdur%29+AS+%3FmaxKeywordDuration%29+where+%7B+%0D%0A++++++++++++%3Ftopic+esw%3ApartOf+eswr%3AInformative2021Track.%0D%0A++++++++++++%3Fwork+esw%3AhasPart+%3Fpart.%0D%0A++++++++++++%3Fwork+esw%3Aimplements+%3Ftopic.%0D%0A++++++++++++%3Fpart+esw%3Aqueries+%3Fo+.%0D%0A++++++++++++%3Fo+rdf%3Arest*%2Frdf%3Afirst++%3Fquery.%0D%0A++++++++++++%3Fquery+lsqv%3AhasExec+%3Fexec.%0D%0A++++++++++++%3Fquery+lsqv%3AusesFeature+%3Fkeyword.%0D%0A++++++++++++%3Fexec+lsqv%3AevalDuration+%3Fdur.%0D%0A++++++++%7D+GROUP+BY+%3Fkeyword%0D%0A++++%7D%0D%0A++++%7B%0D%0A++++++++SELECT+%3Fkeyword+%28COUNT%28*%29+AS+%3FparseErrors%29+where+%7B+%0D%0A++++++++++++%3Ftopic+esw%3ApartOf+eswr%3AInformative2021Track.%0D%0A++++++++++++%3Fwork+esw%3AhasPart+%3Fpart.%0D%0A++++++++++++%3Fwork+esw%3Aimplements+%3Ftopic.%0D%0A++++++++++++%3Fpart+esw%3Aqueries+%3Fo+.%0D%0A++++++++++++%3Fo+rdf%3Arest*%2Frdf%3Afirst++%3Fquery.%0D%0A++++++++++++%3Fquery+lsqv%3AusesFeature+%3Fkeyword.%0D%0A++++++++++++%3Fquery+lsqv%3AparseError+%3FpErr.%0D%0A++++++++%7D+GROUP+BY+%3Fkeyword%0D%0A++++%7D%0D%0A%09%3Ftopic+esw%3ApartOf+eswr%3AInformative2021Track.%0D%0A++++%3Fwork+esw%3AhasPart+%3Fpart.%0D%0A++++%3Fwork+esw%3Aimplements+%3Ftopic.%0D%0A++++%3Fpart+esw%3Aqueries+%3Fo+.%0D%0A++++%3Fo+rdf%3Arest*%2Frdf%3Afirst++%3Fquery.%0D%0A++++%3Fquery+lsqv%3AhasExec+%3Fexec.%0D%0A++++%3Fquery+lsqv%3AusesFeature+%3Fkeyword.%0D%0A++++%3Fexec+lsqv%3AevalDuration+%3Fdur.%0D%0A++++BIND%28xsd%3Afloat%28xsd%3Afloat%28%3Fdur%29+-+xsd%3Afloat%28%3FavgKeywordDuration%29%29*%28xsd%3Afloat%28%3Fdur%29+-+xsd%3Afloat%28%3FavgKeywordDuration%29%29+AS+%3FthisVar%29%0D%0A%7D%0D%0AGROUP+BY+%3Fkeyword+%3FavgKeywordDuration+%3FnumKeywordDuration+%3FparseErrors+%3FmaxKeywordDuration%0D%0AORDER+BY+%3Fkeyword&format=text%2Fhtml&timeout=0&signal_void=on)


| Keyword | Mean | Variance | Max Time | Execution Errors | # queries|
| ---------- | ---------- | --------- | -------- |  -------- | -------- | 
| AVG 	| 0.54 	| 2.35 	| 8.22 	| 1 	| 56 |
| COUNT 	| 1.91 	| 141.05 	| 190.66 	| 12 	| 1230 |
| DISTINCT 	| 2.0 	| 196.03 	| 250.3 	| 42 	| 3370 |
| EXISTS 	| 5.06 	| 216.02 	| 73.77 	| 3 	| 38 |
| FILTER 	| 4.73 	| 576.52 	| 292.23 	| 32 	| 1450 |
| GROUP BY 	| 3.49 	| 440.0 	| 250.3 	| 16 	| 1034 |
| GROUP_CONCAT 	| 7.15 	| 1344.86 	| 250.3 	| 2 	| 199 |
| HAVING 	| 0.17 	| 0.16 	| 2.28 	| 2 	| 54 |
| LIMIT 	| 1.89 	| 203.07 	| 292.23 	| 26 	| 2323 |
| MAX 	| 6.74 	| 588.44 	| 190.66 	| 4 	| 110 |
| MIN 	| 4.87 	| 486.59 	| 181.77 	| 3 	| 82 |
| NESTED QUERY 	| 4.42 	| 361.49 	| 190.66 	| 15 	| 401 |
| NOT EXISTS 	| 6.75 	| 498.89 	| 119.19 	| 10 	| 127 |
| OPTIONAL 	| 7.05 	| 935.94 	| 250.3 	| 4 	| 339 |
| ORDER BY 	| 2.73 	| 301.28 	| 250.3 	| 23 	| 1840 |
| REGEX 	| 6.57 	| 974.82 	| 282.55 	| 4 	| 481 |
| SELECT 	| 1.85 	| 204.77 	| 292.23 	| 59 	| 4782 |
| UNION 	| 2.1 	| 75.07 	| 90.12 	| 4 	| 255 |