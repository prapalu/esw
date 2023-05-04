# RDF


## Contents 
- [ontology](ontology): it contains the ontology schema, both the image and owl file.
- [ttl_files](ttl_files): it contains the turtle files, used to populate the RDF graph.


### Useful Queries

Using the [SPARQL endpoint](http://w3id.org/esw/sparql) it is possible to queries the RDF graph.
Some useful queries are given below with both the SPARQL code and a direct link to its execution.

1. Get general statistics for the Tracks.

The query returns a list of 5-tuples (track IRI, #macroTopics, #topics, #workflows, #workers, #queries).

[Execute the query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=PREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0APREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0D%0ASELECT+%3Ftrack+%28COUNT+%28DISTINCT+%3Fmacro%29+AS+%3FmacroTopics%29+%0D%0A+%28COUNT+%28DISTINCT+%3Ftopic%29+AS+%3Ftopics%29+%0D%0A+%28COUNT+%28DISTINCT+%3Fwork%29+AS+%3Fworkflows%29+%0D%0A+%28COUNT+%28DISTINCT+%3Fworker%29+AS+%3Fworkers%29+%0D%0A+%28COUNT+%28DISTINCT+%3Fquery%29+AS+%3Fqueries%29+%0D%0A+WHERE%7B%0D%0A++++%3Ftopic+esw%3AmacroTopic+%3Fmacro%3B%0D%0A++++++++++++++++esw%3ApartOf+%3Ftrack.%0D%0A++++%3Fwork+esw%3Aimplements+%3Ftopic%3B%0D%0A++++++++++esw%3AwroteBy+%3Fworker%3B%0D%0A++++++++++esw%3AhasPart+%3Fpart.%0D%0A++++%3Fpart+esw%3Aqueries+%3FqueriesList.%0D%0A++++%3FqueriesList+rdf%3Arest*%2Frdf%3Afirst+%3Fquery.%0D%0A%7D%0D%0AGROUP+BY+%3Ftrack&format=text%2Fhtml&timeout=0&signal_void=on)

```SPARQL
PREFIX esw: <http://w3id.org/esw/ontology#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT ?track (COUNT (DISTINCT ?macro) AS ?macroTopics) 
 (COUNT (DISTINCT ?topic) AS ?topics) 
 (COUNT (DISTINCT ?work) AS ?workflows) 
 (COUNT (DISTINCT ?worker) AS ?workers) 
 (COUNT (DISTINCT ?query) AS ?queries) 
 WHERE{
    ?topic esw:macroTopic ?macro;
                esw:partOf ?track.
    ?work esw:implements ?topic;
          esw:wroteBy ?worker;
          esw:hasPart ?part.
    ?part esw:queries ?queriesList.
    ?queriesList rdf:rest*/rdf:first ?query.
}
GROUP BY ?track
```

2. Get the best workflow for topics of which there is a ground truth.

The query returns a list of 4-tuples (workflow IRI, topic IRI, score, ground truth IRI).

[Execute the query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=PREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0A%0D%0ASELECT+%3Fworkflow+%3FtopicLabel+%3FavgFscore+%3FgroundTruth+WHERE%7B%0D%0A++++%0D%0A++++%7B%0D%0A++++++++SELECT+%3Ftopic+%3Fmacro+%28MAX%28%3Ffscore%29+AS+%3Fmax_score%29+WHERE%0D%0A++++++++%7B%0D%0A++++++++++++%7B%0D%0A++++++++++++++++select+%3Fwork+%28AVG%28%3Fscore%29+AS+%3Ffscore%29+WHERE%7B%0D%0A++++++++++++++++++++%3Fwork+a+esw%3AExploratoryWorkflow%3B%0D%0A++++++++++++++++++++++++++esw%3AhasPart+%3Fpart.%0D%0A++++++++++++++++++++%3Fpart+esw%3Afscore+%3Fscore.%0D%0A++++++++++++++++%7D%0D%0A++++++++++++++++GROUP+BY+%3Fwork+%0D%0A++++++++++++%7D%0D%0A++++++++++++FILTER%28%3Ffscore+%3E+0.1%29.%0D%0A++++++++++++%3Fwork+esw%3Aimplements+%3Ftopic.%0D%0A++++++++++++%3Ftopic+esw%3Adescription+%3Fmacro.%0D%0A++++++++%7D%0D%0A++++++++GROUP+BY+%3Ftopic+%3Fmacro%0D%0A%0D%0A++++++++%7D%0D%0A++++%0D%0A++++%7B%0D%0A++++++++select+%3Fworkflow+%3Ft+%28AVG%28%3Fs%29+AS+%3FavgFscore%29+WHERE%7B%0D%0A++++++++++++%3Fworkflow+a+esw%3AExploratoryWorkflow%3B%0D%0A++++++++++++++++esw%3AhasPart+%3Fp.%0D%0A++++++++++++++++%3Fp+esw%3Afscore+%3Fs.%0D%0A++++++++++++%3Fworkflow+esw%3Aimplements+%3Ft.%0D%0A++++++++++++%0D%0A++++++++%7D%0D%0A++++++++GROUP+BY+%3Fworkflow+%3Ft+%0D%0A++++%7D%0D%0A++++FILTER%28%3FavgFscore+%3D+%3Fmax_score%29.%0D%0A++++FILTER%28%3Ft+%3D+%3Ftopic%29.%0D%0A++++%3Ft+esw%3AhasGroundTruth+%3FgroundTruth%3B%0D%0A++++++++rdfs%3Alabel+%3FtopicLabel.%0D%0A%7D&format=text%2Fhtml&timeout=0&signal_void=on)

```SPARQL
PREFIX esw: <http://w3id.org/esw/ontology#>

SELECT ?workflow ?topicLabel ?avgFscore ?groundTruth WHERE{
    
    {
        SELECT ?topic ?macro (MAX(?fscore) AS ?max_score) WHERE
        {
            {
                select ?work (AVG(?score) AS ?fscore) WHERE{
                    ?work a esw:ExploratoryWorkflow;
                          esw:hasPart ?part.
                    ?part esw:fscore ?score.
                }
                GROUP BY ?work 
            }
            FILTER(?fscore > 0.1).
            ?work esw:implements ?topic.
            ?topic esw:description ?macro.
        }
        GROUP BY ?topic ?macro

        }
    
    {
        select ?workflow ?t (AVG(?s) AS ?avgFscore) WHERE{
            ?workflow a esw:ExploratoryWorkflow;
                esw:hasPart ?p.
                ?p esw:fscore ?s.
            ?workflow esw:implements ?t.
            
        }
        GROUP BY ?workflow ?t 
    }
    FILTER(?avgFscore = ?max_score).
    FILTER(?t = ?topic).
    ?t esw:hasGroundTruth ?groundTruth;
        rdfs:label ?topicLabel.
}
```

3. Given a specific topic, return the workflows on that topic with their average fscore 
   and the total number of queries. (For the example we use the topic 
   History Workflow Series (Cultural Movements explorative search) 
   with IRI http://w3id.org/esw/resource/TOPICd1c898149d).

The query returns a list of 3-tuples (workflow IRI, score, numberOfQueries).

[Execute the query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=PREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0APREFIX+eswr%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fresource%2F%3E%0D%0A%0D%0ASELECT+DISTINCT+%3Fworkflow+%28AVG%28%3Ffscore%29+AS+%3FavgFscore%29+%28SUM%28%3FnumQueries%29+AS+%3FtotQueries%29+where%7B%0D%0A++++%3Fworkflow+esw%3Aimplements+eswr%3ATOPICd1c898149d%3B%0D%0A++++%09++esw%3AhasPart+%3Fpart.%0D%0A+++%09%3Fpart+esw%3Afscore+%3Ffscore%3B%0D%0A++++++++++esw%3AnumberOfQueries+%3FnumQueries.%0D%0A%7D%0D%0AGROUP+BY+%3Fworkflow&format=text%2Fhtml&timeout=0&signal_void=on)

```SPARQL
PREFIX esw: <http://w3id.org/esw/ontology#>
PREFIX eswr: <http://w3id.org/esw/resource/>

SELECT DISTINCT ?workflow (AVG(?fscore) AS ?avgFscore) (SUM(?numQueries) AS ?totQueries) where{
    ?workflow esw:implements eswr:TOPICd1c898149d;
    	  esw:hasPart ?part.
   	?part esw:fscore ?fscore;
          esw:numberOfQueries ?numQueries.
}
GROUP BY ?workflow
```

4. Return the tasks with more queries (top-10).

   The query returns a list 4-tuples (task IRI, task label, numberOfQueries, numberOfWorkflows).

[Execute the query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=PREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0D%0A%0D%0ASELECT+DISTINCT+%3Ftask+%3Flabel+%28SUM%28%3FnumQueries%29+AS+%3FtotQueries%29+%28COUNT%28DISTINCT+%3Fjob%29+AS+%3Fworks%29+where%7B%0D%0A++++%3Fjob+a+esw%3ASearchJob%3B%0D%0A+++++++++esw%3Aperforms+%3Ftask%3B%0D%0A+++++++++esw%3AnumberOfQueries+%3FnumQueries.%0D%0A+++++%3Ftask+rdfs%3Alabel+%3Flabel.%0D%0A%7DGROUP+BY+%3Ftask+%3Flabel%0D%0AORDER+BY+DESC%28%3FtotQueries%29%0D%0ALIMIT+10&format=text%2Fhtml&timeout=0&signal_void=on)

```SPARQL
PREFIX esw: <http://w3id.org/esw/ontology#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?task ?label (SUM(?numQueries) AS ?totQueries) (COUNT(DISTINCT ?job) AS ?works) where{
    ?job a esw:SearchJob;
         esw:performs ?task;
         esw:numberOfQueries ?numQueries.
     ?task rdfs:label ?label.
}
GROUP BY ?task ?label
ORDER BY DESC(?totQueries)
LIMIT 10
```

5. Return the top-10 workflows with more query executions.

The query returns a list of 3-tuples (workflow IRI, numberOfQueries, numberOfExecutions).

[Execute the query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=PREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0APREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0D%0APREFIX+lsqv%3A+%3Chttp%3A%2F%2Flsq.aksw.org%2Fvocab%23%3E%0D%0A%0D%0ASELECT+DISTINCT+%3Fworkflow+%28COUNT%28+DISTINCT+%3Fquery%29+AS+%3FtotQueries%29+%28COUNT%28+%3Fexecution%29+AS+%3FtotExecutions%29+where%7B%0D%0A++++%3Fworkflow+a+esw%3AExploratoryWorkflow%3B%0D%0A+++++++++esw%3AhasPart+%3Fjob.%0D%0A++++%3Fjob+esw%3Aqueries+%3Fqueries.%0D%0A++++%3Fqueries+rdf%3Arest*%2Frdf%3Afirst++%3Fquery.%0D%0A++++%3Fquery+lsqv%3AhasExec+%3Fexecution.%0D%0A%7D%0D%0AGROUP+BY+%3Fworkflow%0D%0AORDER+BY+DESC%28%3FtotExecutions%29%0D%0ALIMIT+10&format=text%2Fhtml&timeout=0&signal_void=on)

```SPARQL
PREFIX esw: <http://w3id.org/esw/ontology#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX lsqv: <http://lsq.aksw.org/vocab#>

SELECT DISTINCT ?workflow (COUNT( DISTINCT ?query) AS ?totQueries) (COUNT( ?execution) AS ?totExecutions) where{
    ?workflow a esw:ExploratoryWorkflow;
         esw:hasPart ?job.
    ?job esw:queries ?queries.
    ?queries rdf:rest*/rdf:first  ?query.
    ?query lsqv:hasExec ?execution.
}
GROUP BY ?workflow
ORDER BY DESC(?totExecutions)
LIMIT 10
```

6.  Return the keywords usage for the 2022 collection.

   The query returns a list of couples (keyword IRI, frequency).

[Execute the query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=PREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0APREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0D%0APREFIX+lsqv%3A+%3Chttp%3A%2F%2Flsq.aksw.org%2Fvocab%23%3E%0D%0APREFIX+eswr%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fresource%2F%3E%0D%0A%0D%0ASELECT+%3Fkeyword+%28COUNT%28*%29+AS+%3Ffrequency%29+where%7B%0D%0A++++%3Ftopic+esw%3ApartOf+eswr%3ACompleteness2022Track.%0D%0A++++%3Fwork+esw%3Aimplements+%3Ftopic%3B%0D%0A++++++++++esw%3AhasPart+%3Fjob.%0D%0A++++%3Fjob+esw%3Aqueries+%3Fqueries.%0D%0A++++%3Fqueries+rdf%3Arest*%2Frdf%3Afirst++%3Fquery.%0D%0A++++%3Fquery+lsqv%3AusesFeature+%3Fkeyword.%0D%0A%7D%0D%0AGROUP+BY+%3Fkeyword%0D%0AORDER+BY+DESC+%28%3Ffrequency%29&format=text%2Fhtml&timeout=0&signal_void=on)

```SPARQL
PREFIX esw: <http://w3id.org/esw/ontology#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX lsqv: <http://lsq.aksw.org/vocab#>
PREFIX eswr: <http://w3id.org/esw/resource/>

SELECT ?keyword (COUNT(*) AS ?frequency) where{
    ?topic esw:partOf eswr:Completeness2022Track.
    ?work esw:implements ?topic;
          esw:hasPart ?job.
    ?job esw:queries ?queries.
    ?queries rdf:rest*/rdf:first  ?query.
    ?query lsqv:usesFeature ?keyword.
}
GROUP BY ?keyword
ORDER BY DESC (?frequency)
```

7. Get for each topic the average fscore of the workflows, the average number of queries per workflow and the total number of queries.

   The query returns a list of 5-tuples (topic IRI, topic label, AVG(fscore), AVG(queries), #queries).

[Execute the query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=PREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0A%0D%0ASELECT+%3Ftopic+%3FtopicLabel+%28AVG%28%3Ffscore%29+AS+%3FavgFscore%29+%28ROUND%28AVG%28%3Fqs%29%29+AS+%3FavgQueries%29+%28SUM%28%3Fqs%29+AS+%3FtotQueries%29+WHERE%7B+%0D%0A++++%7B%0D%0A++++++++SELECT+%3Fworkflow+%28AVG%28%3Ffs%29+AS+%3Ffscore%29+%28SUM%28%3Fqueries%29+AS+%3Fqs%29+WHERE%7B%0D%0A++++++++++++%3Fworkflow+esw%3Aimplements+%3Ft%3B%0D%0A++++++++++++++++++esw%3AwroteBy+%3Fworker%3B%0D%0A++++++++++++++++++esw%3AhasPart+%3Fpart.%0D%0A++++++++++++%3Fpart+esw%3Afscore+%3Ffs%3B%0D%0A++++++++++++++++++esw%3AnumberOfQueries+%3Fqueries.%0D%0A++++++++%7DGROUP+BY+%3Fworkflow%0D%0A++++%7D%0D%0A++++%3Fworkflow+esw%3Aimplements+%3Ftopic.%0D%0A++++%3Ftopic+rdfs%3Alabel+%3FtopicLabel.%0D%0A%7D%0D%0AGROUP+BY+%3Ftopic+%3FtopicLabel%0D%0AHAVING+%28AVG%28%3Ffscore%29%3E+0.0%29%0D%0AORDER+BY+%3FtopicLabel&format=text%2Fhtml&timeout=0&signal_void=on)

```SPARQL 
PREFIX esw: <http://w3id.org/esw/ontology#>

SELECT ?topic ?topicLabel (AVG(?fscore) AS ?avgFscore) (ROUND(AVG(?qs)) AS ?avgQueries) (SUM(?qs) AS ?totQueries) WHERE{ 
    {
        SELECT ?workflow (AVG(?fs) AS ?fscore) (SUM(?queries) AS ?qs) WHERE{
            ?workflow esw:implements ?t;
                  esw:wroteBy ?worker;
                  esw:hasPart ?part.
            ?part esw:fscore ?fs;
                  esw:numberOfQueries ?queries.
        }GROUP BY ?workflow
    }
    ?workflow esw:implements ?topic.
    ?topic rdfs:label ?topicLabel.
}
GROUP BY ?topic ?topicLabel
HAVING (AVG(?fscore)> 0.0)
ORDER BY ?topicLabel
```

8. Workers statistics

   The query returns a list of 6-tuples (worker IRI, quality, #workflows, #jobs, AVG(fscore), #queries).

[Execute the query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=PREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0ASELECT+%3Fworker+%3Fquality+%3Fworkflows+%3Fjobs+%3FavgFScore+%3FtotQueries++WHERE%7B%0D%0A++++%7B%0D%0A++++++++SELECT+%3Fworker+%28COUNT%28DISTINCT+%3Fworkflow%29+AS+%3Fworkflows%29+%0D%0A++++++++%28COUNT%28DISTINCT+%3Fjob%29+AS+%3Fjobs%29++%28AVG%28%3Ffscore%29+AS+%3FavgFScore%29+%28SUM%28%3FnumQueries%29+AS+%3FtotQueries%29++WHERE%7B%0D%0A++++++++++++%3Fworkflow+esw%3AwroteBy+%3Fworker%3B%0D%0A++++++++++++++++++++++esw%3AhasPart+%3Fjob.%0D%0A++++++++++++%3Fjob+esw%3Afscore+%3Ffscore%3B%0D%0A+++++++++++++++++esw%3AnumberOfQueries+%3FnumQueries.%0D%0A++++++++%7D%0D%0A++++++++GROUP+BY+%3Fworker%0D%0A++++%7D%0D%0A++++%3Fworker+esw%3Aquality+%3Fquality.%0D%0A%7D%0D%0AORDER+BY+%3Fworker&format=text%2Fhtml&timeout=0&signal_void=on)


```SPARQL
PREFIX esw: <http://w3id.org/esw/ontology#>
SELECT ?worker ?quality ?workflows ?jobs ?avgFScore ?totQueries  WHERE{
    {
        SELECT ?worker (COUNT(DISTINCT ?workflow) AS ?workflows) 
        (COUNT(DISTINCT ?job) AS ?jobs)  (AVG(?fscore) AS ?avgFScore) (SUM(?numQueries) AS ?totQueries)  WHERE{
            ?workflow esw:wroteBy ?worker;
                      esw:hasPart ?job.
            ?job esw:fscore ?fscore;
                 esw:numberOfQueries ?numQueries.
        }
        GROUP BY ?worker
    }
    ?worker esw:quality ?quality.
}
ORDER BY ?worker
```

9. Queries execution statistics by tracks


```SPARQL
PREFIX esw: <http://w3id.org/esw/ontology#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX lsqv: <http://lsq.aksw.org/vocab#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?track ?avgTrackDuration ((SUM(?thisVar)/?numTrackDuration) AS ?variance) ?maxTrackDuration ?executionErrors WHERE{
    {
        SELECT ?track (AVG(?dur) AS ?avgTrackDuration) (COUNT(?dur) AS ?numTrackDuration) (MAX(?dur) AS ?maxTrackDuration) where { 
            ?topic esw:partOf ?track.
            ?work esw:hasPart ?part.
            ?work esw:implements ?topic.
            ?part esw:queries ?o .
            ?o rdf:rest*/rdf:first  ?query.
            ?query lsqv:hasExec ?exec.
            ?exec lsqv:evalDuration ?dur.
        } GROUP BY ?track
    }
    {
        SELECT ?track (COUNT(*) AS ?executionErrors) where { 
            ?topic esw:partOf ?track.
            ?work esw:hasPart ?part.
            ?work esw:implements ?topic.
            ?part esw:queries ?o .
            ?o rdf:rest*/rdf:first  ?query.
            ?query lsqv:parseError ?pErr.
        } GROUP BY ?track
    }
	?topic esw:partOf ?track.
    ?work esw:hasPart ?part.
    ?work esw:implements ?topic.
    ?part esw:queries ?o .
    ?o rdf:rest*/rdf:first  ?query.
    ?query lsqv:hasExec ?exec.
    ?exec lsqv:evalDuration ?dur.
    BIND(xsd:float(xsd:float(?dur) - xsd:float(?avgTrackDuration))*(xsd:float(?dur) - xsd:float(?avgTrackDuration)) AS ?thisVar)
}
GROUP BY ?track ?avgTrackDuration ?numTrackDuration ?executionErrors ?maxTrackDuration

```


10. Queries execution statistics by tracks and macro topic


```SPARQL
PREFIX esw: <http://w3id.org/esw/ontology#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX lsqv: <http://lsq.aksw.org/vocab#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?track ?macro ?avgTrackDuration ((SUM(?thisVar)/?numTrackDuration) AS ?variance) ?maxTrackDuration ?executionErrors WHERE{
    {
        SELECT ?track ?macro (AVG(?dur) AS ?avgTrackDuration) (COUNT(?dur) AS ?numTrackDuration) (MAX(?dur) AS ?maxTrackDuration) where { 
            ?topic esw:partOf ?track.
            ?topic esw:macroTopic ?macro.
            ?work esw:hasPart ?part.
            ?work esw:implements ?topic.
            ?part esw:queries ?o .
            ?o rdf:rest*/rdf:first  ?query.
            ?query lsqv:hasExec ?exec.
            ?exec lsqv:evalDuration ?dur.
        } GROUP BY ?track ?macro
    }
    {
        SELECT ?track ?macro (COUNT(*) AS ?executionErrors) where { 
            ?topic esw:partOf ?track.
            ?topic esw:macroTopic ?macro.
            ?work esw:hasPart ?part.
            ?work esw:implements ?topic.
            ?part esw:queries ?o .
            ?o rdf:rest*/rdf:first  ?query.
            ?query lsqv:parseError ?pErr.
        } GROUP BY ?track ?macro
    }
	?topic esw:partOf ?track.
    ?topic esw:macroTopic ?macro.
    ?work esw:hasPart ?part.
    ?work esw:implements ?topic.
    ?part esw:queries ?o .
    ?o rdf:rest*/rdf:first  ?query.
    ?query lsqv:hasExec ?exec.
    ?exec lsqv:evalDuration ?dur.
    BIND(xsd:float(xsd:float(?dur) - xsd:float(?avgTrackDuration))*(xsd:float(?dur) - xsd:float(?avgTrackDuration)) AS ?thisVar)
}
GROUP BY ?track ?macro ?avgTrackDuration ?numTrackDuration ?executionErrors ?maxTrackDuration

```


9. Queries execution statistics by tracks


```SPARQL
PREFIX esw: <http://w3id.org/esw/ontology#>
PREFIX eswr: <http://w3id.org/esw/resource/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX lsqv: <http://lsq.aksw.org/vocab#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?keyword ?avgKeywordDuration ((SUM(?thisVar)/?numKeywordDuration) AS ?variance) ?maxKeywordDuration ?executionErrors ?numKeywordDuration WHERE{
    {
        SELECT ?keyword (AVG(?dur) AS ?avgKeywordDuration) (COUNT(?dur) AS ?numKeywordDuration) (MAX(?dur) AS ?maxKeywordDuration) where { 
            ?topic esw:partOf eswr:Completeness2022Track.
            ?work esw:hasPart ?part.
            ?work esw:implements ?topic.
            ?part esw:queries ?o .
            ?o rdf:rest*/rdf:first  ?query.
            ?query lsqv:hasExec ?exec.
            ?query lsqv:usesFeature ?keyword.
            ?exec lsqv:evalDuration ?dur.
        } GROUP BY ?keyword
    }
    {
        SELECT ?keyword (COUNT(*) AS ?executionErrors) where { 
            ?topic esw:partOf eswr:Completeness2022Track.
            ?work esw:hasPart ?part.
            ?work esw:implements ?topic.
            ?part esw:queries ?o .
            ?o rdf:rest*/rdf:first  ?query.
            ?query lsqv:usesFeature ?keyword.
            ?query lsqv:parseError ?pErr.
        } GROUP BY ?keyword
    }
	?topic esw:partOf eswr:Completeness2022Track.
    ?work esw:hasPart ?part.
    ?work esw:implements ?topic.
    ?part esw:queries ?o .
    ?o rdf:rest*/rdf:first  ?query.
    ?query lsqv:hasExec ?exec.
    ?query lsqv:usesFeature ?keyword.
    ?exec lsqv:evalDuration ?dur.
    BIND(xsd:float(xsd:float(?dur) - xsd:float(?avgKeywordDuration))*(xsd:float(?dur) - xsd:float(?avgKeywordDuration)) AS ?thisVar)
}
GROUP BY ?keyword ?avgKeywordDuration ?numKeywordDuration ?executionErrors ?maxKeywordDuration

```

PREFIX eswr: <http://w3id.org/esw/resource/>
PREFIX esw: <http://w3id.org/esw/ontology#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX lsqv: <http://lsq.aksw.org/vocab#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?keyword ?avgTrackDuration ((SUM(?thisVar)/?numTrackDuration) AS ?variance) ?maxTrackDuration ?executionErrors WHERE{
    {
        SELECT ?keyword (AVG(?dur) AS ?avgTrackDuration) (COUNT(?dur) AS ?numTrackDuration) (MAX(?dur) AS ?maxTrackDuration) where { 
            ?topic esw:partOf eswr:Informative2021Track.
            ?work esw:hasPart ?part.
            ?work esw:implements ?topic.
            ?part esw:queries ?o .
            ?o rdf:rest*/rdf:first  ?query.
            ?query lsqv:hasExec ?exec.
            ?query lsqv:usesFeature ?keyword.
            ?exec lsqv:evalDuration ?dur.
        } GROUP BY ?keyword
    }
    {
        SELECT ?keyword (COUNT(?pErr) AS ?executionErrors) where { 
            ?topic esw:partOf eswr:Informative2021Track.
            ?work esw:hasPart ?part.
            ?work esw:implements ?topic.
            ?part esw:queries ?o .
            ?o rdf:rest*/rdf:first  ?query.
            ?query lsqv:usesFeature ?keyword.
            OPTIONAL{?query lsqv:parseError ?pErr.}
        } GROUP BY ?keyword
    }
	?topic esw:partOf eswr:Informative2021Track.
    ?work esw:hasPart ?part.
    ?work esw:implements ?topic.
    ?part esw:queries ?o .
    ?o rdf:rest*/rdf:first  ?query.
    ?query lsqv:hasExec ?exec.
    ?exec lsqv:evalDuration ?dur.
    ?query lsqv:usesFeature ?keyword.
    BIND(xsd:float(xsd:float(?dur) - xsd:float(?avgTrackDuration))*(xsd:float(?dur) - xsd:float(?avgTrackDuration)) AS ?thisVar)
}
GROUP BY ?keyword ?avgTrackDuration ?numTrackDuration ?executionErrors ?maxTrackDuration
ORDER BY ?keyword
