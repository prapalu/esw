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
[Execute the query](http://grace.dei.unipd.it/sparql/?default-graph-uri=&query=PREFIX+esw%3A+%3Chttp%3A%2F%2Fw3id.org%2Fesw%2Fontology%23%3E%0D%0A%0D%0ASELECT+%3Fw+%3Ft+%3Ffs+%3Fgt+WHERE%7B%0D%0A++++%0D%0A++++%7B%0D%0A++++++++SELECT+%3Ftopic+%3Fmacro+%28MAX%28%3Ffscore%29+AS+%3Fmax_score%29+WHERE%0D%0A++++++++%7B%0D%0A++++++++++++%7B%0D%0A++++++++++++++++select+%3Fwork+%28AVG%28%3Fscore%29+AS+%3Ffscore%29+WHERE%7B%0D%0A++++++++++++++++++++%3Fwork+a+esw%3ASearchWorkflow%3B%0D%0A++++++++++++++++++++++++++esw%3AhasPart+%3Fpart.%0D%0A++++++++++++++++++++%3Fpart+esw%3Afscore+%3Fscore.%0D%0A++++++++++++++++%7D%0D%0A++++++++++++++++GROUP+BY+%3Fwork+%0D%0A++++++++++++%7D%0D%0A++++++++++++FILTER%28%3Ffscore+%3E+0.1%29.%0D%0A++++++++++++%3Fwork+esw%3Aimplements+%3Ftopic.%0D%0A++++++++++++%3Ftopic+esw%3Adescription+%3Fmacro.%0D%0A++++++++%7D%0D%0A++++++++GROUP+BY+%3Ftopic+%3Fmacro%0D%0A%0D%0A++++++++%7D%0D%0A++++%0D%0A++++%7B%0D%0A++++++++select+%3Fw+%3Ft+%28AVG%28%3Fs%29+AS+%3Ffs%29+WHERE%7B%0D%0A++++++++++++%3Fw+a+esw%3ASearchWorkflow%3B%0D%0A++++++++++++++++esw%3AhasPart+%3Fp.%0D%0A++++++++++++++++%3Fp+esw%3Afscore+%3Fs.%0D%0A++++++++++++%3Fw+esw%3Aimplements+%3Ft.%0D%0A++++++++++++%0D%0A++++++++%7D%0D%0A++++++++GROUP+BY+%3Fw+%3Ft+%0D%0A++++%7D%0D%0A++++FILTER%28%3Ffs+%3D+%3Fmax_score%29.%0D%0A++++FILTER%28%3Ft+%3D+%3Ftopic%29.%0D%0A++++%3Ft+esw%3AhasGroundTruth+%3Fgt%3B%0D%0A++++++++esw%3Adescription+%3Fm.%0D%0A%7D&format=text%2Fhtml&timeout=0&signal_void=on)
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
