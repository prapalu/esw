# Source code

This folder contains the python source code to manipulate the `Search Workflow`, evaluate them, and serialize everything in turtle files.

## Contents
- [data](data/) folder contains the file of the SPARQL keywords and other csv files needed for the RDF serialization
- [gt_modules] (gt_modules/) folder contains a python module for the creation of the ground truth json files
- [resource] (resource/) folder contains the python modules needed to manipulate the `Search Workflow`. More details [here](resource/README.md)
- the executable python files that process the original python notebooks `Search Workflows`, convert, evaluate and serialize them. It is possible to reproduce the data the are already in this repository for the two collections, following the steps:
    - [clean](#clean)
    - [convert](#convert)
    - [evaluate](#evaluate)
    - [serialize](#serialize)

#### Clean

First of all it should be performed a clean operation