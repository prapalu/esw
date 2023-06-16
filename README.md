# Exploratory Search Workflows collection (ESW)

This repository contains the data and the scripts for the Exploratory Search Workflows collection  

## Scope

<!--This resource provides a new benchmark for exploratory search workflow. 
For this purpose we created some ``Search Topic`` with 5 to 10 ``Search Task`` each.
We assigned from 4 to 6 different workers the same ``Search Topic``, in order to collect different results and different points of view.
After that we analyzed each ``Search Workflow`` and amongst those of the same ``Search Topic`` we built a ``Ground Truth`` for the ``Search Topic``.
Using ``Ground Truths`` we evaluated the ``Search Workflows`` that all together composed our resource. 
For convenience we put all the information about topics,tasks,workflows and the evaluations in a RDF Graph which it can be queried [here](http://w3id.org/esw/sparql)-->
Exploratory search on Knowledge Graphs (KGs) arise when a user needs to understand and extract insights from an unfamiliar KG. 
In these exploratory sessions the users issue a series of queries to identify relevant portions of the KG that can answer their questions, 
with each query answer informing the formulation of the next query. 
Despite the widespread adoption of KGs, the needs of current KG exploration use cases are not well understood. 
This work presents the "Exploratory Search Workflows" (ESW) collection focusing on real-world exploration sessions of an open-domain KG, WikiData, conducted by 57 MSc Computer Engineering students in two editions of an advanced Graph Database course. 
This resource includes 234 real exploratory workflows, each containing an average of 45 SPARQL queries, along reference workflows that serve as gold standard solutions to the proposed tasks. 
The ESW collection is available as an RDF graph and accessible via a public SPARQL endpoint.
It allows for analysis of real user sessions, understanding of query evolution and complexity, and serves as the first query benchmark for KG management systems for exploratory search.


## Contents 
- [src](src): the folder with the source code to parse, to evaluate and to serialize the workflows. 
- [rdf](rdf): the folder that contains the information about the RDF Graph (ontology, turtle files and useful queries).
- [tracks](tracks): the folder that contains the exploratory workflows. 

## Definitions

### Search Topic and Search Task

A Search Topic investigates a specific portion of a Knowledge Base (e.g. Basketball Players). It is a collection of questions (also called Search Task) that guide the exploration. Usually, there are some given URIs related to the Search Topic in order to provide a starting point for the exploration.

### Exploratory Workflow

An Exploratory Workflow is an implementation of a Search Topic. Given the Search Topic, the worker has to write a sequence of queries to give an answer to the Search Tasks provided.

### Ground Truth (Gold Standard)

A Ground Truth (or Gold Standard) is a special Exploratory Workflow that in our opinion solves in the best way the Search Tasks of the Search Topic. Ground Truths are used to evaluate the performance of the Exploratory Workflows.

## Inside the resource

The Exploratory Workflows were collected during the Graph Database course taught in the University of Padua during the Master Degree in Computer Engineering in the Academic Years 2021 and 2022. For this reason we have two tracks, once per Academic Year. 
Also, the Search Topics in the 2021 track include very general tasks that can have multiple valid answers (e.g. Return some numerical comparisons between Woody Allen and Quentin Tarantino) thus it is more "Information Retrival" oriented.
On the contrary the Search Topics in the 2022 track include very specific tasks, that usually specify the format of the final answer output (e.g. Return for each country the number of appearances in the FIFA World Cup: the output format should be a list of triples (Country IRI, Country label, #appareances)).
Ground Truths are available for all the Search Topics of the 2022 track, while for the 2021 track the Ground Truths available are the ones of the Movie macro topic thus it is more completeness.


About 2021 track (more information [here](tracks/2021)):
- 6 macro topic (Geography, Politics, Movies, Books, Sports, Companies)
- 21 workers
- 24 Search Topics
- 126 Exploratory Workflows (each worker was assigned to implement an exploratory workflow for each macro topic)
- 4861 queries

About 2022 track (more information [here](tracks/2022)):
- 3 macro topic (Movies, Sports, History)
- 36 workers
- 21 Search Topics
- 108 Exploratory Workflows (each worker was assigned to implement an exploratory workflow for each macro topic)
- 5784 queries



## License

Since this work is a mixture of code and datasets, the code is distributed under the MIT License while the datasets are distributed under a [Creative Commons Attribution 4.0 International License][cc-by]. See [LICENSE-MIT](LICENSE-MIT) and [LICENSE-CC-BY](LICENSE-CC-BY) for more information.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![CC BY 4.0][cc-by-shield]][cc-by]


[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg