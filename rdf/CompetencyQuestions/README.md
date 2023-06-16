# Competency Questions

In the following we provide some CQs for each class in our Ontology.
All the queries provided below are executable via [SPARQL endpoint](http://w3id.org/esw/sparql).


## Contents 
- [Search Topic CQ](#search-topic-cq)
- [Search Workflow CQ](#search-workflow-cq)
- [Search Task CQ](#search-task-cq)
- [Search Job CQ](#search-job-cq)


## Competency Questions

### Search Topic CQ

All the CQs presented below referring to the Search Topic http://w3id.org/esw/resource/TOPIC5c2cbb34bd (eswr:TOPIC5c2cbb34bd)

**CQ1. Which is the Search Topic's name?**

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



**2. Which is the Search Topic's macro topic?**

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


**CQ3. What is the Exploratory Search Topic’s ground truth?**

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

**CQ4. Which are the Search Tasks that are part of the Topic?**

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

### Search Workflow CQ

All the CQs presented below referring to the Search Workflow http://w3id.org/esw/resource/1181ce72bf (eswr:1181ce72bf)

**CQ5. Which is the Workflow’s topic? ?**

[Execute the query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=PREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0APREFIX+eswr%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fresource%2F%3E%0D%0ASELECT++%3Ftopic%0D%0A+WHERE%7B%0D%0A++++eswr%3A1181ce72bf+esw%3Aimplements+%3Ftopic.%0D%0A%7D&format=text%2Fhtml&timeout=0&signal_void=on)

```SPARQL
PREFIX esw: <http://w3id.org/esw/ontology#>
PREFIX eswr: <http://w3id.org/esw/resource/>
SELECT  ?topic
 WHERE{
    eswr:1181ce72bf esw:implements ?topic.
}
```
| ?topic |
|---------------|
| http://w3id.org/esw/resource/TOPIC5c2cbb34bd      |


**CQ6. Which are the Search Jobs that composed the Workflow?**


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

**CQ7. Who wrote the Workflow?**


[Execute the query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=PREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0APREFIX+eswr%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fresource%2F%3E%0D%0ASELECT++%3Fjob%0D%0A+WHERE%7B%0D%0A++++eswr%3A1181ce72bf+esw%3AhasPart+%3Fjob.%0D%0A%7D&format=text%2Fhtml&timeout=0&signal_void=on)

```SPARQL
PREFIX esw: <http://w3id.org/esw/ontology#>
PREFIX eswr: <http://w3id.org/esw/resource/>
SELECT  ?job
 WHERE{
    eswr:1181ce72bf esw:hasPart ?job.
}
```

| ?worker |
|---------------|
| http://w3id.org/esw/resource/WORKER2021_19 |