# Competency Questions

In the following we provide some CQs for each class in our Ontology.
All the queries provided below are executable via [SPARQL endpoint](http://w3id.org/esw/sparql).


## Contents 
- [Search Track CQ](#search-track-cq)
- [Search Topic CQ](#search-topic-cq)
- [Search Workflow CQ](#search-workflow-cq)
- [Search Task CQ](#search-task-cq)
- [Search Job CQ](#search-job-cq)
- [Worker CQ](#worker-cq)


## Competency Questions

### Search Track CQ


**CQ1. For each Search Track, which is the number of Search Topics, Exploratory Search Workflows and Workers belonging to it?**


[Execute the query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=PREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0APREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0D%0ASELECT+%3Ftrack+%28COUNT+%28DISTINCT+%3Ftopic%29+AS+%3Ftopics%29+%0D%0A+%28COUNT+%28DISTINCT+%3Fwork%29+AS+%3Fworkflows%29+%0D%0A+%28COUNT+%28DISTINCT+%3Fworker%29+AS+%3Fworkers%29+%0D%0A+WHERE%7B%0D%0A++++%3Ftopic++esw%3ApartOf+%3Ftrack.%0D%0A++++%3Fwork+esw%3Aimplements+%3Ftopic%3B%0D%0A++++++++++esw%3AwroteBy+%3Fworker.%0D%0A%7D%0D%0AGROUP+BY+%3Ftrack&format=text%2Fhtml&timeout=0&signal_void=on)

```SPARQL
PREFIX esw: <http://w3id.org/esw/ontology#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT ?track (COUNT (DISTINCT ?topic) AS ?topics) 
 (COUNT (DISTINCT ?work) AS ?workflows) 
 (COUNT (DISTINCT ?worker) AS ?workers) 
 WHERE{
    ?topic  esw:partOf ?track.
    ?work esw:implements ?topic;
          esw:wroteBy ?worker.
}
GROUP BY ?track
```

| ?track |	?topics	| ?workflows| 	?workers |
|--|--|--|--|
| http://w3id.org/esw/resource/Informative2021Track	| 24 |126 | 21 |
| http://w3id.org/esw/resource/Completeness2022Track | 21 | 108 | 36 |


**CQ2. For each Search Track, how many queries are there?**


[Execute the query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=PREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0APREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0D%0ASELECT+%3Ftrack+%28COUNT+%28DISTINCT+%3Fquery%29+AS+%3Fqueries%29+%0D%0A+WHERE%7B%0D%0A++++%3Ftopic+esw%3ApartOf+%3Ftrack.%0D%0A++++%3Fwork+esw%3Aimplements+%3Ftopic%3B%0D%0A++++++++++esw%3AwroteBy+%3Fworker%3B%0D%0A++++++++++esw%3AhasPart+%3Fpart.%0D%0A++++%3Fpart+esw%3Aqueries+%3FqueriesList.%0D%0A++++%3FqueriesList+rdf%3Arest*%2Frdf%3Afirst+%3Fquery.%0D%0A%7D%0D%0AGROUP+BY+%3Ftrack&format=text%2Fhtml&timeout=0&signal_void=on)

```SPARQL
PREFIX esw: <http://w3id.org/esw/ontology#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT ?track (COUNT (DISTINCT ?query) AS ?queries) 
 WHERE{
    ?topic esw:partOf ?track.
    ?work esw:implements ?topic;
          esw:wroteBy ?worker;
          esw:hasPart ?part.
    ?part esw:queries ?queriesList.
    ?queriesList rdf:rest*/rdf:first ?query.
}
GROUP BY ?track
```

| ?track |	?queries |
|--|--|
| http://w3id.org/esw/resource/Informative2021Track	| 4861 |
| http://w3id.org/esw/resource/Completeness2022Track | 5784 |



### Search Topic CQ

All the CQs presented below refers to the Search Topic http://w3id.org/esw/resource/TOPIC5c2cbb34bd (eswr:TOPIC5c2cbb34bd)

**CQ3. Which is the Search Topic's name?**

[Execute the query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=PREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0APREFIX+eswr%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fresource%2F%3E%0D%0ASELECT+%3Fdescription%0D%0A+WHERE%7B%0D%0A++++eswr%3ATOPIC5c2cbb34bd+esw%3Adescription+%3Fdescription.%0D%0A%7D&format=text%2Fhtml&timeout=0&signal_void=on)

```SPARQL
PREFIX esw: <http://w3id.org/esw/ontology#>
PREFIX eswr: <http://w3id.org/esw/resource/>
SELECT ?description
 WHERE{
    eswr:TOPIC5c2cbb34bd esw:description ?description.
}
```
| ?description |
|---------------|
| Movie Workflow Series (Directors explorative search) |



**CQ4. Which is the Search Topic's macro topic?**

[Execute the query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=PREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0APREFIX+eswr%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fresource%2F%3E%0D%0ASELECT+%3FmacroTopic%0D%0A+WHERE%7B%0D%0A++++eswr%3ATOPIC5c2cbb34bd+esw%3AmacroTopic+%3FmacroTopic.%0D%0A%7D&format=text%2Fhtml&timeout=0&signal_void=on)

```SPARQL
PREFIX esw: <http://w3id.org/esw/ontology#>
PREFIX eswr: <http://w3id.org/esw/resource/>
SELECT ?macroTopic
 WHERE{
    eswr:TOPIC5c2cbb34bd esw:macroTopic ?macroTopic.
}
```
| ?macroTopic |
|---------------|
| Movie      |


**CQ5. What is the Exploratory Search Topic’s ground truth?**

[Execute the query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=PREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0APREFIX+eswr%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fresource%2F%3E%0D%0ASELECT++%3FgroundTruth%0D%0A+WHERE%7B%0D%0A++++eswr%3ATOPIC5c2cbb34bd+esw%3AhasGroundTruth+%3FgroundTruth.%0D%0A%7D&format=text%2Fhtml&timeout=0&signal_void=on)

```SPARQL
PREFIX esw: <http://w3id.org/esw/ontology#>
PREFIX eswr: <http://w3id.org/esw/resource/>
SELECT  ?groundTruth
 WHERE{
    eswr:TOPIC5c2cbb34bd esw:hasGroundTruth ?groundTruth.
}
```
| ?groundTruth |
|---------------|
| http://w3id.org/esw/resource/workflow5_0      |

**CQ6. Which are the Search Tasks that are part of the Topic?**

[Execute the query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=PREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0APREFIX+eswr%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fresource%2F%3E%0D%0ASELECT++%3Ftask%0D%0A+WHERE%7B%0D%0A++++%3Ftask+esw%3AbelongsTo+eswr%3ATOPIC5c2cbb34bd+.%0D%0A%7D&format=text%2Fhtml&timeout=0&signal_void=on)

```SPARQL
PREFIX esw: <http://w3id.org/esw/ontology#>
PREFIX eswr: <http://w3id.org/esw/resource/>
SELECT  ?task
 WHERE{
    ?task esw:belongsTo eswr:TOPIC5c2cbb34bd .
}
```
| ?task                                       |
|---------------------------------------------|
| http://w3id.org/esw/resource/TASK027f92f957 |
| http://w3id.org/esw/resource/TASK04bae680c2 |
| http://w3id.org/esw/resource/TASK0b0a775c88 |
| http://w3id.org/esw/resource/TASK10bf2bf780 |
| http://w3id.org/esw/resource/TASK15a6a10e8b |
| http://w3id.org/esw/resource/TASK481acd9c34 |
| http://w3id.org/esw/resource/TASK4caaa95d4e |
| http://w3id.org/esw/resource/TASKa0babb70eb |
| http://w3id.org/esw/resource/TASKc4da274eca |
| http://w3id.org/esw/resource/TASKd5203cafed |
| http://w3id.org/esw/resource/TASKfb04a99027 |



**CQ7. How many different Search Workflows implement the Search Topic?**

[Execute the query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=PREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0APREFIX+eswr%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fresource%2F%3E%0D%0ASELECT++%28COUNT%28%3Fwork%29+AS+%3FnumberOfWorkflows%29%0D%0A+WHERE%7B%0D%0A++++%3Fwork+esw%3Aimplements+eswr%3ATOPIC5c2cbb34bd+.%0D%0A%7D&format=text%2Fhtml&timeout=0&signal_void=on)

```SPARQL
PREFIX esw: <http://w3id.org/esw/ontology#>
PREFIX eswr: <http://w3id.org/esw/resource/>
SELECT  (COUNT(?work) AS ?numberOfWorkflows)
 WHERE{
    ?work esw:implements eswr:TOPIC5c2cbb34bd .
}
```
| ?numberOfWorkflows                     |
|---------------------------------------------|
|              7             |



**CQ8. How many different Search Topics are there?**

[Execute the query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=PREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0APREFIX+eswr%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fresource%2F%3E%0D%0ASELECT++%28COUNT%28DISTINCT+%3Fs%29+AS+%3FsearchTopics%29%0D%0A+WHERE%7B%0D%0A++++%3Fs+a+esw%3ASearchTopic.%0D%0A%7D&format=text%2Fhtml&timeout=0&signal_void=on)

```SPARQL
PREFIX esw: <http://w3id.org/esw/ontology#>
PREFIX eswr: <http://w3id.org/esw/resource/>
SELECT  (COUNT(DISTINCT ?s) AS ?searchTopics)
 WHERE{
    ?s a esw:SearchTopic.
}
```
| ?searchTopics               |
|---------------------------------------------|
|              45             |


### Search Workflow CQ

All the CQs presented below refers to the Search Workflow http://w3id.org/esw/resource/1181ce72bf (eswr:1181ce72bf)

**CQ9. Which is the Workflow’s topic with its description?**

[Execute the query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=PREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0APREFIX+eswr%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fresource%2F%3E%0D%0ASELECT++%3Ftopic+%3Fdescription%0D%0A+WHERE%7B%0D%0A++++eswr%3A1181ce72bf+esw%3Aimplements+%3Ftopic.%0D%0A%3Ftopic+esw%3Adescription+%3Fdescription.%0D%0A%7D&format=text%2Fhtml&timeout=0&signal_void=on)

```SPARQL
PREFIX esw: <http://w3id.org/esw/ontology#>
PREFIX eswr: <http://w3id.org/esw/resource/>
SELECT  ?topic ?description
 WHERE{
    eswr:1181ce72bf esw:implements ?topic.
    ?topic esw:description ?description.
}
```
| ?topic | ?description |
|---------------|---------------|
| http://w3id.org/esw/resource/TOPIC5c2cbb34bd      | Movie Workflow Series (Directors explorative search)|


**CQ10. Which are the Search Jobs that composed the Workflow?**


[Execute the query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=PREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0APREFIX+eswr%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fresource%2F%3E%0D%0ASELECT++%3Fjob%0D%0A+WHERE%7B%0D%0A++++eswr%3A1181ce72bf+esw%3AhasPart+%3Fjob.%0D%0A%7D&format=text%2Fhtml&timeout=0&signal_void=on)

```SPARQL
PREFIX esw: <http://w3id.org/esw/ontology#>
PREFIX eswr: <http://w3id.org/esw/resource/>
SELECT  ?job
 WHERE{
    eswr:1181ce72bf esw:hasPart ?job.
}
```


| ?job |
|---------------|
| http://w3id.org/esw/resource/JOB1W1181ce72bf |
| http://w3id.org/esw/resource/JOB2W1181ce72bf |
| http://w3id.org/esw/resource/JOB3W1181ce72bf |
| http://w3id.org/esw/resource/JOB4W1181ce72bf |
| http://w3id.org/esw/resource/JOB5W1181ce72bf |
| http://w3id.org/esw/resource/JOB6W1181ce72bf |
| http://w3id.org/esw/resource/JOB71W1181ce72bf |
| http://w3id.org/esw/resource/JOB72W1181ce72bf |
| http://w3id.org/esw/resource/JOB7W1181ce72bf |


**CQ11. Who wrote the Workflow? What is the worker's quality?**


[Execute the query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=PREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0APREFIX+eswr%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fresource%2F%3E%0D%0ASELECT++%3Fworker+%3Fquality%0D%0A+WHERE%7B%0D%0A++++eswr%3A1181ce72bf+esw%3AwroteBy+%3Fworker.%0D%0A++++%3Fworker+esw%3Aquality+%3Fquality.%0D%0A%7D&format=text%2Fhtml&timeout=0&signal_void=on)

```SPARQL
PREFIX esw: <http://w3id.org/esw/ontology#>
PREFIX eswr: <http://w3id.org/esw/resource/>
SELECT  ?worker ?quality
 WHERE{
    eswr:1181ce72bf esw:wroteBy ?worker.
    ?worker esw:quality ?quality.
}
```

| ?worker | ?quality |
|---------------|---------------|
| http://w3id.org/esw/resource/WORKER2021_19 | 0.785714|




**CQ12. How many different Exploratory Search Workflows are there?**

[Execute the query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=PREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0APREFIX+eswr%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fresource%2F%3E%0D%0ASELECT++%28COUNT%28DISTINCT+%3Fs%29+AS+%3FexploratoryWorkflows%29%0D%0A+WHERE%7B%0D%0A++++%3Fs+a+esw%3AExploratoryWorkflow.%0D%0A%7D&format=text%2Fhtml&timeout=0&signal_void=on)

```SPARQL
PREFIX esw: <http://w3id.org/esw/ontology#>
PREFIX eswr: <http://w3id.org/esw/resource/>
SELECT  (COUNT(DISTINCT ?s) AS ?exploratoryWorkflows)
 WHERE{
    ?s a esw:ExploratoryWorkflow.
}
```
| ?exploratoryWorkflows                   |
|---------------------------------------------|
|              234             |

### Search Task CQ

All the CQs presented below refers to the Search Task http://w3id.org/esw/resource/TASK027f92f957 (eswr:TASK027f92f957)

**CQ13. Which is the task's Search Topic with its description?**


[Execute the query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=PREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0APREFIX+eswr%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fresource%2F%3E%0D%0ASELECT++%3Ftopic+%3Fdescription%0D%0A+WHERE%7B%0D%0A++++eswr%3ATASK027f92f957+esw%3AbelongsTo+%3Ftopic.%0D%0A++++%3Ftopic+esw%3Adescription+%3Fdescription.%0D%0A%7D&format=text%2Fhtml&timeout=0&signal_void=on)

```SPARQL
PREFIX esw: <http://w3id.org/esw/ontology#>
PREFIX eswr: <http://w3id.org/esw/resource/>
SELECT  ?topic ?description
 WHERE{
    eswr:TASK027f92f957 esw:belongsTo ?topic.
    ?topic esw:description ?description.
}
```
| ?topic | ?description |
|---------------|---------------|
| http://w3id.org/esw/resource/TOPIC5c2cbb34bd      | Movie Workflow Series (Directors explorative search)|

**CQ14. Which is the task's requirement?**


[Execute the query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=PREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0APREFIX+eswr%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fresource%2F%3E%0D%0ASELECT++%3Fdescription%0D%0A+WHERE%7B%0D%0A++++eswr%3ATASK027f92f957+esw%3Adescription+%3Fdescription.%0D%0A%7D&format=text%2Fhtml&timeout=0&signal_void=on)

```SPARQL
PREFIX esw: <http://w3id.org/esw/ontology#>
PREFIX eswr: <http://w3id.org/esw/resource/>
SELECT  ?description
 WHERE{
    eswr:TASK027f92f957 esw:description ?description.
}
```
| ?description |
|---------------|
| Identify the BGP for films    |


**CQ15. How many different Search Tasks are there?**

[Execute the query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=PREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0APREFIX+eswr%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fresource%2F%3E%0D%0ASELECT++%28COUNT%28DISTINCT+%3Fs%29+AS+%3FsearchTasks%29%0D%0A+WHERE%7B%0D%0A++++%3Fs+a+esw%3ASearchTask.%0D%0A%7D&format=text%2Fhtml&timeout=0&signal_void=on)

```SPARQL
PREFIX esw: <http://w3id.org/esw/ontology#>
PREFIX eswr: <http://w3id.org/esw/resource/>
SELECT  (COUNT(DISTINCT ?s) AS ?searchTasks)
 WHERE{
    ?s a esw:SearchTask.
}
```
| ?searchTasks               |
|---------------------------------------------|
|              340             |



## Search Job CQ


All the CQs presented below refers to the Search Job http://w3id.org/esw/resource/JOB1W1181ce72bf (eswr:JOB1W1181ce72bf)

**CQ16. Which Search Task is the Search Job performing?**


[Execute the query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=PREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0APREFIX+eswr%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fresource%2F%3E%0D%0ASELECT++%3Ftask%0D%0A+WHERE%7B%0D%0A++++eswr%3AJOB1W1181ce72bf+esw%3Aperforms+%3Ftask.%0D%0A%7D&format=text%2Fhtml&timeout=0&signal_void=on)

```SPARQL
PREFIX esw: <http://w3id.org/esw/ontology#>
PREFIX eswr: <http://w3id.org/esw/resource/>
SELECT  ?task
 WHERE{
    eswr:JOB1W1181ce72bf esw:performs ?task.
}
```
| ?task |
|---------------|
| http://w3id.org/esw/resource/TASK027f92f957      |

**CQ17. Which is the Search Job's workflow?**


[Execute the query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=PREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0APREFIX+eswr%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fresource%2F%3E%0D%0ASELECT+%3Fworkflow%0D%0AWHERE%7B%0D%0A+%3Fworkflow+++esw%3AhasPart+eswr%3AJOB1W1181ce72bf+.%0D%0A%7D&format=text%2Fhtml&timeout=0&signal_void=on)

```SPARQL
PREFIX esw: <http://w3id.org/esw/ontology#>
PREFIX eswr: <http://w3id.org/esw/resource/>
SELECT ?workflow
WHERE{
 ?workflow esw:hasPart eswr:JOB1W1181ce72bf .
}
```
| ?workflow |
|---------------|
| http://w3id.org/esw/resource/1181ce72bf   |


**CQ18. How many queries the Search Job contains?**


[Execute the query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=PREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0APREFIX+eswr%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fresource%2F%3E%0D%0ASELECT+%28COUNT%28%3Fquery%29+AS+%3FnumberOfQueries%29%0D%0AWHERE%7B%0D%0A++++eswr%3AJOB1W1181ce72bf+esw%3Aqueries+%3Fqueries.%0D%0A++++%3Fqueries+rdf%3Arest*%2Frdf%3Afirst++%3Fquery.%0D%0A%7D&format=text%2Fhtml&timeout=0&signal_void=on)

```SPARQL
PREFIX esw: <http://w3id.org/esw/ontology#>
PREFIX eswr: <http://w3id.org/esw/resource/>
SELECT (COUNT(?query) AS ?numberOfQueries)
WHERE{
    eswr:JOB1W1181ce72bf esw:queries ?queries.
    ?queries rdf:rest*/rdf:first  ?query.
}
```
| ?numberOfQueries |
|---------------|
| 12   |




**CQ19. For each query in the Search Job, which is the text, the precision, the recall and the result set count?**


[Execute the query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=PREFIX+lsqv%3A+%3Chttp%3A%2F%2Flsq.aksw.org%2Fvocab%23%3E%0D%0APREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0APREFIX+eswr%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fresource%2F%3E%0D%0ASELECT+%3Fquery+%3Ftext+%3Frecall+%3Fprecision+%3FresultCount%0D%0AWHERE%7B%0D%0A++++eswr%3AJOB1W1181ce72bf+esw%3Aqueries+%3Fqueries.%0D%0A++++%3Fqueries+rdf%3Arest*%2Frdf%3Afirst++%3Fquery.%0D%0A++++%3Fquery+lsqv%3Atext+%3Ftext%3B%0D%0A++++++++++++esw%3Arecall+%3Frecall%3B%0D%0A++++++++++++esw%3Aprecision+%3Fprecision%3B%0D%0A++++++++++++lsqv%3AresultCount+%3FresultCount.%0D%0A%7D&format=text%2Fhtml&timeout=0&signal_void=on)

```SPARQL
PREFIX lsqv: <http://lsq.aksw.org/vocab#>
PREFIX esw: <http://w3id.org/esw/ontology#>
PREFIX eswr: <http://w3id.org/esw/resource/>
SELECT ?query ?text ?recall ?precision ?resultCount
WHERE{
    eswr:JOB1W1181ce72bf esw:queries ?queries.
    ?queries rdf:rest*/rdf:first  ?query.
    ?query lsqv:text ?text;
            esw:recall ?recall;
            esw:precision ?precision;
            lsqv:resultCount ?resultCount.
}
```
| ?query | ?text| ?recall | ?precision | ?resultCount |
|--|--|--|--|--|
| http://w3id.org/esw/resource/Q_2021_149	|SELECT * WHERE { wd:Q25089 ?p ?obj . }|0.0|0.0|333 |
| http://w3id.org/esw/resource/Q_2021_151	|SELECT ?name WHERE { wd:Q25089 ?p wd:Q5 . wdt:P166 \<[http://schema.org/name](http://schema.org/name)> ?name . }|0.0|0.0|0 |
| http://w3id.org/esw/resource/Q_2021_152	|SELECT ?name WHERE { wd:Q25089 ?p wd:Q5 . wdt:P800 \<[http://schema.org/name](http://schema.org/name)> ?name . }|0.0|0.0|0 |
| http://w3id.org/esw/resource/Q_2021_153	|SELECT ?name WHERE { wd:Q25089 ?p wd:Q5 . wdt:P106 \<[http://schema.org/name](http://schema.org/name)> ?name . }|0.0|0.0|0 |
| http://w3id.org/esw/resource/Q_2021_154	|SELECT ?obj ?name WHERE { wd:Q25089 wdt:P106 ?obj . ?obj \<[http://schema.org/name](http://schema.org/name)> ?name . }|0.0|0.0|14 |
| http://w3id.org/esw/resource/Q_2021_155	|SELECT ?person ?personName ?p ?pName WHERE { ?person ?p wd:Q2526255. ?person \<[http://schema.org/name](http://schema.org/name)> ?personName . ?p \<[http://schema.org/name](http://schema.org/name)> ?pName . } limit 30|0.0|0.0|29 |
| http://w3id.org/esw/resource/Q_2021_156 |SELECT ?obj ?name WHERE { wd:Q25089 wdt:P800 ?obj . ?obj \<[http://schema.org/name](http://schema.org/name)> ?name . }|0.0|0.0|48 |
| http://w3id.org/esw/resource/Q_2021_157	|SELECT ?pName ?objName ?name WHERE { wd:Q25089 ?p ?obj . ?obj \<[http://schema.org/name](http://schema.org/name)> ?objName . ?p \<[http://schema.org/name](http://schema.org/name)> ?pName . FILTER (?p = wdt:P800 \|\| ?p = wdt:P106) }|0.0|0.0|63 |
| http://w3id.org/esw/resource/Q_2021_158	|SELECT ?p ?pName ?obj ?objName WHERE { wd:Q25089 ?p ?obj . ?obj \<[http://schema.org/name](http://schema.org/name)> ?objName . ?p \<[http://schema.org/name](http://schema.org/name)> ?pName . }|0.0|0.0|133 |
| http://w3id.org/esw/resource/Q_2021_159	|SELECT DISTINCT ?work ?workName ?p ?pName ?obj ?objName WHERE { wd:Q25089 wdt:P800 ?work . ?work ?p ?obj . ?work \<[http://schema.org/name](http://schema.org/name)> ?workName . ?obj \<[http://schema.org/name](http://schema.org/name)> ?objName . ?p \<[http://schema.org/name](http://schema.org/name)> ?pName . }|1.0|0.000413565|2418 |
| http://w3id.org/esw/resource/Q_2021_160	|SELECT DISTINCT ?p ?pName ?obj ?objName WHERE { wd:Q17417520 ?p ?obj . ?p \<[http://schema.org/name](http://schema.org/name)> ?pName . OPTIONAL{?obj \<[http://schema.org/name](http://schema.org/name)> ?objName .} } LIMIT 15|1.0|0.0714286|14 |


**CQ20. How many different Search Jobs are there?**

[Execute the query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=PREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0APREFIX+eswr%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fresource%2F%3E%0D%0ASELECT++%28COUNT%28DISTINCT+%3Fs%29+AS+%3FsearchJobs%29%0D%0A+WHERE%7B%0D%0A++++%3Fs+a+esw%3ASearchJob.%0D%0A%7D&format=text%2Fhtml&timeout=0&signal_void=on)

```SPARQL
PREFIX esw: <http://w3id.org/esw/ontology#>
PREFIX eswr: <http://w3id.org/esw/resource/>
SELECT  (COUNT(DISTINCT ?s) AS ?searchJobs)
 WHERE{
    ?s a esw:SearchJob.
}
```
| ?searchJobs               |
|---------------------------------------------|
|              1455             |

## Worker CQ


**CQ21. How many different Worker are there?**

[Execute the query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=PREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0APREFIX+eswr%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fresource%2F%3E%0D%0ASELECT++%28COUNT%28DISTINCT+%3Fs%29+AS+%3Fworkers%29%0D%0A+WHERE%7B%0D%0A++++%3Fs+a+esw%3AWorker.%0D%0A%7D&format=text%2Fhtml&timeout=0&signal_void=on)

```SPARQL
PREFIX esw: <http://w3id.org/esw/ontology#>
PREFIX eswr: <http://w3id.org/esw/resource/>
SELECT  (COUNT(DISTINCT ?s) AS ?workers)
 WHERE{
    ?s a esw:Worker.
}
```
| ?workers               |
|---------------------------------------------|
|              57             |



**CQ22. Which is the average quality score of the workers?**

[Execute the query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=PREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0APREFIX+eswr%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fresource%2F%3E%0D%0ASELECT++%28AVG%28%3Fquality%29+AS+%3FavgQuality%29%0D%0A+WHERE%7B%0D%0A++++%3Fs+a+esw%3AWorker%3B%0D%0A+++++++++esw%3Aquality+%3Fquality.%0D%0A%7D&format=text%2Fhtml&timeout=0&signal_void=on)

```SPARQL
PREFIX esw: <http://w3id.org/esw/ontology#>
PREFIX eswr: <http://w3id.org/esw/resource/>
SELECT  (AVG(?quality) AS ?avgQuality)
 WHERE{
    ?s a esw:Worker;
         esw:quality ?quality.
}
```
| ?workers               |
|---------------------------------------------|
|              0.670426061278895            |


