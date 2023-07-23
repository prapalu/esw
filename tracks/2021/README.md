# 2021 Track

This folder contains the 2021 track.
Furthermore we report here some statistics for this track.

## Content

- [general statistics](#statistics)
- [exploratory workflows](#exploratory-workflows)
- [keywords analysis](#keywords-analysis)
- [evaluation results](#evaluation-results)

### Statistics

The 2021 track is composed of:
- 6 macro topic (Geography, Politics, Movies, Books, Sports, Companies)
- 21 workers
- 24 Search Topics
- 126 Exploratory Workflows (each worker was assigned to implement a exploratory workflow for each macro topic)
- 4861 queries

### Exploratory Workflows

Each Search Topic was implemented by 4 to 6 workers in order to obtain different points of view. The table below shows, for each Search Topic, the number of Exploratory Workflows, the average and total number of queries.

You can get the statistics below querying the RDF Graph. [Execute query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=PREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0APREFIX+eswr%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fresource%2F%3E%0D%0A%0D%0ASELECT+%3FtopicLabel+%28COUNT%28DISTINCT+%3Fworkflow%29+AS+%3Fworkflows%29+%28SUM%28%3FnumQueries%29%2FCOUNT%28DISTINCT+%3Fworkflow%29+AS+%3FavgQueries%29+%28SUM%28%3FnumQueries%29+AS+%3FtotQueries%29+where%7B%0D%0A++++%3Fworkflow+esw%3Aimplements+%3Ftopic%3B%0D%0A++++%09esw%3AhasPart+%3Fpart.%0D%0A+++%09%3Fpart+esw%3AnumberOfQueries+%3FnumQueries.%0D%0A++++%3Ftopic+esw%3ApartOf+eswr%3AInformative2021Track%3B%0D%0A+++++++++++rdfs%3Alabel+%3FtopicLabel.%0D%0A%7D%0D%0AGROUP+BY+%3Ftopic+%3FtopicLabel%0D%0AORDER+BY+%3FtopicLabel&format=text%2Fhtml&timeout=0&signal_void=on)

| Search Topic | #Workflows | AVG(queries)  | # queries|
| -------------| -----------| -----------| -----------|
| **Books** | **21** | **44** |**931**|
| Political Magazines 	| 4	| 36	| 144 |
| Nobel laureates 	| 6	| 45	| 274 |
| Authors comparison 	| 6	| 42	| 253 |
| Author comparison 	| 5	| 52	| 260 |
| **Companies** | **21** | **33** | **711**|
| IT Companies 	| 6	| 30	| 185 |
| Economy of EU States	| 6	| 40	| 242 |
| Trademarks across the world	| 5	| 34	| 171 |
| Business People in Germany	| 4	| 28	| 113 |
| **Geography** | **21** | **28** | **592**|
| American Architects	| 5	| 33	| 166 |
| European Cathedrals	| 4	| 16	| 65 |
| archaeological sites	| 6	| 27	| 164 |
| Place of Birth, Death, and Burial	| 6	| 32	| 197 |
| **Movies** | **21** | **46** | **986**|
| Tv series 	| 5	| 50	| 251 |
| Directors 	| 6	| 55	| 331 |
| The Batman movies 	| 4	| 48	| 193 |
| Horror Franchises 	| 6	| 35	| 211 |
| **Politics** | **21** | **36** | **759**|
| International Treaties	| 4	| 21	| 87 |
| Monarchies	| 5	| 51	| 257 |
| Politicians in E.U.	| 6	| 27	| 164 |
| Presidents of countries	| 6	| 41	| 251 |
| **Sport** | **21** | **42** | **882**|
| F1 pilots 	| 6	| 46	| 276 |
| Olympic 	| 6	| 35	| 213 |
| World Records 	| 4	| 48	| 193 |
| FIFA World Cup events 	| 5	| 40	| 200 |

### Keywords Analysis

The table below shows the distribution of the SPARQL keywords in the track.

You can get the statistics below querying the RDF Graph. [Execute query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=PREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0APREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0D%0APREFIX+lsqv%3A+%3Chttp%3A%2F%2Flsq.aksw.org%2Fvocab%23%3E%0D%0APREFIX+eswr%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fresource%2F%3E%0D%0A%0D%0ASELECT+%3Fkeyword+%28COUNT%28*%29+AS+%3Ffrequency%29+%28%28COUNT%28*%29%2Fxsd%3Afloat%28%3FtotQuery%29*100.0+AS+%3Fpercentage%29%29+where%7B%0D%0A++++%7B%0D%0A++++++++SELECT+%28+COUNT%28%3Fquery%29+AS+%3FtotQuery%29%7B%0D%0A++++++++++++%3Ftopic+esw%3ApartOf+eswr%3AInformative2021Track.%0D%0A++++++++++++%3Fwork+a+esw%3AExploratoryWorkflow%3B%0D%0A++++++++++++++++esw%3Aimplements+%3Ftopic%3B%0D%0A++++++++++++++++esw%3AhasPart+%3Fjob.%0D%0A++++++++++++%3Fjob+esw%3Aqueries+%3Fqueries.%0D%0A++++++++++++%3Fqueries+rdf%3Arest*%2Frdf%3Afirst++%3Fquery.%0D%0A++++++++%7D%0D%0A++++%7D%0D%0A++++%3Ftopic+esw%3ApartOf+eswr%3AInformative2021Track.%0D%0A++++%3Fwork++a+esw%3AExploratoryWorkflow%3B%0D%0A++++++++esw%3Aimplements+%3Ftopic%3B%0D%0A++++++++esw%3AhasPart+%3Fjob.%0D%0A++++%3Fjob+esw%3Aqueries+%3Fqueries.%0D%0A++++%3Fqueries+rdf%3Arest*%2Frdf%3Afirst++%3Fquery.%0D%0A++++%3Fquery+lsqv%3AusesFeature+%3Fkeyword.%0D%0A%7D%0D%0AGROUP+BY+%3Fkeyword+%3FtotQuery%0D%0AORDER+BY+DESC+%28%3Ffrequency%29&format=text%2Fhtml&timeout=0&signal_void=on)

| Keyword   | # queries | % queries |
| ----------| --------- | -------- | 
| SELECT	| 4841	| 99.59% |
| DISTINCT	| 3412	| 70.19% |
| LIMIT	    | 2349	| 48.32% |
| ORDER BY	| 1863	| 38.33% |
| FILTER	| 1482	| 30.49% |
| COUNT	    | 1242	| 25.55% |
| GROUP BY	| 1050	| 21.6% |
| REGEX	    | 485	| 9.98% |
| OPTIONAL	| 343	| 7.06% |
| UNION	    | 259	| 5.33% |
| GROUP_CONCAT	| 201	| 4.13% |
| NOT EXISTS	| 137	| 2.82% |
| MAX	    | 114	| 2.35% |
| MIN	    | 85	| 1.75% |
| AVG	    | 57	| 1.17% |
| HAVING	| 56	| 1.15% |
| ASK	    | 51	| 1.05% |
| EXISTS	| 41	| 0.84% |
| SUM	    | 28	| 0.58% |
| MINUS	    | 8	| 0.16% |
| AND	    | 6	| 0.12% |
| CONSTRUCT	| 1	| 0.02% |
| DESCRIBE	| 1	| 0.02% |
| ----------| --------- | -------- | 
| TOTAL     | 4861  | 100%  | 

For more statistics on the SPARQL keywords usage in specific Exploratory Workflows, Search Topics, Macro Topics, you can query the [SPARQL endpoint](http://w3id.org/esw/sparql) binding the variables you want.



### Evaluation Results

#### Average FScore for each topic

The table below shows, for each topic of the track, the average f-score obtained by the Exploratory Workflows.

For this example, the f-score of the workflow is calculated averaging the f-scores of the Search Jobs, which is in turn computes as the maximum f-score of the queries in such Search Job.

You can get these statistics querying the RDF Graph. [Execute query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=PREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0APREFIX+eswr%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fresource%2F%3E%0D%0A%0D%0ASELECT+%3FtopicLabel+%28AVG%28%3Favgfscore%29+AS+%3Favgfscore%29+where%7B%0D%0A++++%7B%0D%0A++++++++SELECT+%3Fworkflow+%3Ftopic+%28AVG%28%3Fscore%29+AS+%3Favgfscore%29+WHERE%7B%0D%0A++++++++++++%7B%0D%0A++++++++++++++++SELECT+%3Fworkflow+%3Fpart+%28MAX%28%3Fscore%29+AS+%3Fscore%29+WHERE%7B%0D%0A++++++++++++++++++++%3Fworkflow+a+esw%3AExploratoryWorkflow%3B%0D%0A++++++++++++++++++++++++esw%3AhasPart+%3Fpart.%0D%0A++++++++++++++++++++%3Fpart+esw%3Aqueries+%3Fqueries.%0D%0A++++++++++++++++++++%3Fqueries+rdf%3Arest*%2Frdf%3Afirst+%3Fquery.%0D%0A++++++++++++++++++++OPTIONAL%7B%3Fquery+esw%3Afscore+%3Fscore.%7D%0D%0A++++++++++++++++%7D%0D%0A++++++++++++++++GROUP+BY+%3Fworkflow+%3Fpart%0D%0A++++++++++++%7D%0D%0A++++++++++++%3Fworkflow+a+esw%3AExploratoryWorkflow%3B%0D%0A++++++++++++++++esw%3Aimplements+%3Ftopic.%0D%0A++++++++%7D%0D%0A++++++++GROUP+BY+%3Fworkflow+%3Ftopic%0D%0A++++%7D%0D%0A++++%3Ftopic+esw%3ApartOf+eswr%3AInformative2021Track%3B%0D%0A++++++++rdfs%3Alabel+%3FtopicLabel.%0D%0A%7D%0D%0AGROUP+BY+%3FtopicLabel%0D%0AHAVING+%28AVG%28%3Favgfscore%29%3E0.0%29&format=text%2Fhtml&timeout=0&signal_void=on)

| Search Topic          | Avg Fscore | 
| --------------------- | --------- |
| Horror Franchises 	| 0.18 |
| Directors 	        | 0.28 |
| The Batman movies 	| 0.31 |
| Tv series 	        | 0.29 |

PREFIX esw: <http://w3id.org/esw/ontology#>
PREFIX eswr: <http://w3id.org/esw/resource/>

SELECT ?macro (AVG(?avgfscore) AS ?avgfscore) where{
    {
        SELECT ?workflow ?topic (AVG(?score) AS ?avgfscore) WHERE{
            {
                SELECT ?workflow ?part (MAX(?score) AS ?score) WHERE{
                    ?workflow a esw:ExploratoryWorkflow;
                        esw:hasPart ?part.
                    ?part esw:queries ?queries.
                    ?queries rdf:rest*/rdf:first ?query.
                    OPTIONAL{?query esw:fscore ?score.}
                }
                GROUP BY ?workflow ?part
            }
            ?workflow a esw:ExploratoryWorkflow;
                esw:implements ?topic.
        }
        GROUP BY ?workflow ?topic
    }
    ?topic esw:partOf eswr:Completeness2022Track;
        esw:macroTopic ?macro.
}
GROUP BY ?macro
HAVING (AVG(?avgfscore)>0.0)
ORDER BY ?macro

#### Best Exploratory Workflow for each Search Topic

The table below shows, for each topic of the track, the best Exploratory Workflows, with its Fscore, the number of queries and the realted ground truth.

For this example, the f-score of the workflow is calculated averaging the f-scores of the Search Jobs, which is in turn computes as the maximum f-score of the queries in such Search Job.

The exploratory Workflows and the Ground Truths links to the real resource.

You can get these statistics querying the RDF Graph. [Execute query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=%0D%0APREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0APREFIX+eswr%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fresource%2F%3E%0D%0A%0D%0ASELECT+%3Fworkflow+%3FtopicLabel+%3FavgFscore+%3FnumQueries+%3FgroundTruth+WHERE%7B%0D%0A++++%0D%0A++++%7B%0D%0A++++++++SELECT+%3Ftopic+%3Fmacro+%28MAX%28%3Ffscore%29+AS+%3Fmax_score%29+WHERE%0D%0A++++++++%7B%0D%0A++++++++++++%7B%0D%0A++++++++++++++++SELECT+%3Fwork+%28AVG%28%3Fscore%29+AS+%3Ffscore%29+WHERE%7B%0D%0A++++++++++++++++++++%7B%0D%0A++++++++++++++++++++++++SELECT+%3Fwork+%3Fpart+%28MAX%28%3Fscore%29+AS+%3Fscore%29+WHERE%7B%0D%0A++++++++++++++++++++++++++++%3Fwork+a+esw%3AExploratoryWorkflow%3B%0D%0A++++++++++++++++++++++++++++++++esw%3AhasPart+%3Fpart.%0D%0A++++++++++++++++++++++++++++%3Fpart+esw%3Aqueries+%3Fqueries.%0D%0A++++++++++++++++++++++++++++%3Fqueries+rdf%3Arest*%2Frdf%3Afirst+%3Fquery.%0D%0A++++++++++++++++++++++++++++OPTIONAL%7B+%3Fquery+esw%3Afscore+%3Fscore.+%7D%0D%0A++++++++++++++++++++++++%7D%0D%0A++++++++++++++++++++++++GROUP+BY+%3Fwork+%3Fpart%0D%0A++++++++++++++++++++%7D%0D%0A++++++++++++++++++++%3Fwork+a+esw%3AExploratoryWorkflow%3B%0D%0A++++++++++++++++++++++++++esw%3AhasPart+%3Fpart.%0D%0A++++++++++++++++%7D%0D%0A++++++++++++++++GROUP+BY+%3Fwork+%0D%0A++++++++++++%7D%0D%0A++++++++++++FILTER%28%3Ffscore+%3E+0.0%29.%0D%0A++++++++++++%3Fwork+esw%3Aimplements+%3Ftopic.%0D%0A++++++++++++%3Ftopic+esw%3Adescription+%3Fmacro.%0D%0A++++++++%7D%0D%0A++++++++GROUP+BY+%3Ftopic+%3Fmacro%0D%0A%0D%0A++++++++%7D%0D%0A++++%0D%0A++++%7B%0D%0A++++++++SELECT+%3Fworkflow+%3Ft+%28AVG%28%3Fscore%29+AS+%3FavgFscore%29+%28SUM%28%3FnumQueries%29+AS+%3FnumQueries%29+WHERE%7B%0D%0A++++++++++++%7B%0D%0A++++++++++++++++SELECT+%3Fworkflow+%3Fpart+%28MAX%28%3Fscore%29+AS+%3Fscore%29+WHERE%7B%0D%0A++++++++++++++++++++%3Fworkflow+a+esw%3AExploratoryWorkflow%3B%0D%0A++++++++++++++++++++++++esw%3AhasPart+%3Fpart.%0D%0A++++++++++++++++++++%3Fpart+esw%3Aqueries+%3Fqueries.%0D%0A++++++++++++++++++++%3Fqueries+rdf%3Arest*%2Frdf%3Afirst+%3Fquery.%0D%0A++++++++++++++++++++OPTIONAL%7B%3Fquery+esw%3Afscore+%3Fscore.%7D%0D%0A++++++++++++++++%7D%0D%0A++++++++++++++++GROUP+BY+%3Fworkflow+%3Fpart%0D%0A++++++++++++%7D%0D%0A++++++++++++%3Fworkflow+a+esw%3AExploratoryWorkflow%3B%0D%0A++++++++++++++++esw%3Aimplements+%3Ft%3B%0D%0A++++++++++++++++esw%3AhasPart+%3Fpart.%0D%0A++++++++++++%3Fpart+esw%3AnumberOfQueries+%3FnumQueries.%0D%0A++++++++%7D%0D%0A++++++++GROUP+BY+%3Fworkflow+%3Ft%0D%0A++++%7D%0D%0A++++FILTER%28%3FavgFscore+%3D+%3Fmax_score%29.%0D%0A++++FILTER%28%3Ft+%3D+%3Ftopic%29.%0D%0A++++%3Ft+esw%3AhasGroundTruth+%3FgroundTruth%3B%0D%0A++++++++esw%3ApartOf+eswr%3AInformative2021Track%3B%0D%0A++++++++rdfs%3Alabel+%3FtopicLabel.%0D%0A%7D%0D%0AORDER+BY+%3FtopicLabel&format=text%2Fhtml&timeout=0&signal_void=on)

| Exploratory Workflow|Search Topic | Fscore | queries | Ground Truth |
| ---------- | ---------- | --------- | -------- |  -------- | 
| **Movies** ||||
| [8f65f028f0](http://w3id.org/esw/resource/8f65f028f0) | Tv series             | 0.49 | 37 | [workflow5_3](http://w3id.org/esw/resource/workflow5_3) |
| [daa4ae72bf](http://w3id.org/esw/resource/daa4ae72bf) | Directors             | 0.60 | 83 | [workflow5_0](http://w3id.org/esw/resource/workflow5_0) |
| [d000799b39](http://w3id.org/esw/resource/d000799b39) | The Batman movies     | 0.45 | 12 | [workflow5_1](http://w3id.org/esw/resource/workflow5_1) |
| [28dde04e63](http://w3id.org/esw/resource/28dde04e63) | Horror Franchises     | 0.44 | 53 | [workflow5_2](http://w3id.org/esw/resource/workflow5_2) |