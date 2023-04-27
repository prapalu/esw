# 2021 Track

This folder contains the 2021 track.

## Statistics

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

| Keyword   | # queries | %queries |
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
| TOTAL     | 4862  | 100%  | 

For more statistics on the SPARQL keywords usage in specific Search Workflows, Search Topics, Macro Topics, you can query the [SPARQL endpoint](http://w3id.org/esw/sparql) binding the variables you want.

