# Exploratory Search Workflow (ESW)

This repository contains the data and the scripts for the Exploratory Search Workflow project  

## Scope

This resource provides a new benchmark for exploratory search workflow. 
For this purpose we created some ``Search Topic`` with 5 to 10 ``Search Task`` each.
We assigned from 4 to 6 different workers the same ``Search Topic``, in order to collect different results and different points of view.
After that we analyzed each ``Search Workflow`` and amongst those of the same ``Search Topic`` we built a ``Ground Truth`` for the ``Search Topic``.
Using ``Ground Truths`` we evaluated the ``Search Workflows`` that all together composed our resource. 
For convenience we put all the information about topics,tasks,workflows and the evaluations in a RDF Graph which it can be queried [here](http://w3id.org/esw/sparql)


## Contents 
- `src`: the folder with the source code to parse, to evaluate and to serialize the workflows. More details [here](src/README.md)
- `rdf`: the folder that contains the information about the RDF Graph (ontology, turtle files, useful queries)
- `collections`: the folder that contains the main data of this project. More details [here](collections/README.md)

## Definitions

### Search Topic and Search Task

A Search Topic investigates a specific portion of a Knowledge Base (e.g. Basketball Players). It is a collection of questions (also called Search Task) that guide the exploration. Usually, there are some given URIs related to the Search Topic in order to provide a starting point for the exploration.

### Search Workflow

A Search Workflow is an implementation of a Search Topic. Given the Search Topic, the worker has to write a sequence of queries to give an answer to the Search Tasks provided.

### Ground Truth

A Ground Truth is a special Search Workflow that in our opinion solves in the best way the Search Tasks of the Search Topic. Ground Truth is used to evaluate the performance of the Search Workflows.

## Inside the resource

The Search Workflows were collected during the Graph Database course taught in the University of Padua during the Master Degree in Computer Engineering in the Academic Years 2021 and 2022. For this reason we have two collections, once per Academic Year. 
Also, the Search Topics in the 2021 collection include very general tasks that can have multiple valid answers (e.g. Return some numerical comparisons between Woody Allen and Quentin Tarantino) thus it is more "Information Retrival" oriented.
On the contrary the Search Topics in the 2022 collection include very specific tasks, that usually specify the format of the final answer output (e.g. Return for each country the number of appearances in the FIFA World Cup: the output format should be a list of triples (Country IRI, Country label, #appareances)).
Ground Truths are available for all the Search Topics of the 2022 collection, while for the 2021 collection the Ground Truths available are the ones of the Movie macro topic thus it is more completeness.


About 2021 collection (more information [here](collections/2021)):
- 6 macro topic (Geography, Politics, Movies, Book, Sport, Companies)
- 21 workers
- 24 Search Topics
- 126 Search Workflows (each worker was assigned to implement a search workflow for each macro topic)
- 5803 queries

About 2022 collection (more information [here](collections/2021)):
- 3 macro topic (Movies, Sport, History)
- 41 workers
- 21 Search Topics
- 123 Search Workflows (each worker was assigned to implement a search workflow for each macro topic)
- 4862 queries






| Search Topic    | #Search Workflows  |
| -----------   | ----------- |