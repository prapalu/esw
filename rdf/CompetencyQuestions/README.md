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

1. Which is the Search Topic's name?.

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



2. Which is the Search Topic's macro topic?.

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


3. What is the Exploratory Search Topic’s ground truth? 

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

### Search Workflow CQ