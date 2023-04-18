# Exploratory Search Workflow (ESW)

This repository contains the data and the scripts for the Exploratory Search Workflow project  

## Scope

The main goal of the project is to create a new benchamrk for exploratory search workflow. 
For this purpose we created some ``Search Topic`` with 5 to 10 ``Search Task`` each.
We assigned from 4 to 6 different workers the same ``Search Topic``, in order to collect different results and different points of view.
After that we analyzed each ``Search Workflow`` and amongst those of the same ``Search Topic`` we built a ``Ground Truth`` for the ``Search Topic``.
Using ``Ground Truths`` we evaluated the ``Search Workflows`` that all together composed our resource. 
For convenience we put all the information about topics,tasks,workflows and the evaluations in a RDF Graph which it can be queried [here](http://w3id.org/esw/sparql)


## Contents 
- `src`: the folder with the source code to handle the workflows. More details [here](src/README.md)
- `rdf`: the folder that contains the information about the RDF Graph (ontology, turtle files, useful queries)
- `workflows`: the folder that contains the main data of this project. More details on how this folder is structured [here](workflows/README.md)
