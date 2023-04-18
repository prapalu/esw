# RDF


## Contents 
- `ontology`: it contains the ontology schema, both the image and owl file.
- `ttl_files`: it contains the turtle files, used to populate the RDF graph.


### Useful Queries

Using the [SPARQL endpoint](http://w3id.org/esw/sparql) it is possible to queries the RDF graph.
Some useful queries are given below. For each query there are:
- scope of the query
- direct link to the execution
- SPARQL code

1. Get the best workflow for topics of which there is a ground truth
The query returns a list of 4-tuples (workflow IRI, topic IRI, score, ground truth IRI)

```SPARQL
PREFIX esw: <http://w3id.org/esw/ontology#>

SELECT ?w ?t ?fs ?gt WHERE{
    
    {
        SELECT ?topic ?macro (MAX(?fscore) AS ?max_score) WHERE
        {
            {
                select ?work (AVG(?score) AS ?fscore) WHERE{
                    ?work a esw:SearchWorkflow;
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
        select ?w ?t (AVG(?s) AS ?fs) WHERE{
            ?w a esw:SearchWorkflow;
                esw:hasPart ?p.
                ?p esw:fscore ?s.
            ?w esw:implements ?t.
            
        }
        GROUP BY ?w ?t 
    }
    FILTER(?fs = ?max_score).
    FILTER(?t = ?topic).
    ?t esw:hasGroundTruth ?gt;
        esw:description ?m.
}
```
