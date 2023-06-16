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

All the CQs presented below referring to the Search Topic http://w3id.org/esw/resource/TOPIC10a10a1675 (eswr:TOPIC10a10a1675)

1. Which is the Search Topic's name?.

[Execute the query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=PREFIX+xsd%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23%3E%0D%0APREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0APREFIX+eswr%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fresource%2F%3E%0D%0APREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0D%0ASELECT+%3Fdescription%0D%0A+WHERE%7B%0D%0A++++eswr%3ATOPIC10a10a1675+esw%3Adescription+%3Fdescription.%0D%0A%7D%0D%0A&format=text%2Fhtml&timeout=0&signal_void=on)

```SPARQL
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX esw: <http://w3id.org/esw/ontology#>
PREFIX eswr: <http://w3id.org/esw/resource/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT ?description
 WHERE{
    eswr:TOPIC10a10a1675 esw:description ?description.
}
```
| ?description |
|---------------|
| Book Workflow Series (Political Magazines explorative search) |


