# Tracks

We have 2 tracks of workflows divided in the subfolders [2021](2021/) and [2022](2022/).
Each subfolder contains the following folders:
- `notebooks`: it contains the original `Search Workflows` wrote through python notebook. In this folder each worker has its own folder with the notebooks he/she wrote
- `workflows_json`: it contains the json representation of the workflows. More information about the standard we used to represent the workflow are written below. Like the `notebook` folder each worker has its own folder with his/her workflows
- `ground_truths`: it contains the ground truths for the `Search Topic`.
- `workflows_evaluated`: it contains the workflows evaluated using the ground truths.
- `querylogs`: it contains the logs of the executed queries by the workers.
- `workflows_executed`: it contains the workflows re-executed in our [SPARQL endpoint](htt://grace.dei.unipd.it/sparql) to collect the duration of the queries' execution .
- `rdf`: it contains the turtle files to populate the RDF Graph.
- `empty_notebooks`: it contains the template notebooks for each Search Topic, which you can reuse to do your own Search Workflow.

### JSON representation of the workflows

Each workflow originally wrote through python notebook has been translated in a json file, in order to manipulate it.

#### Main fields
The structure of the json workflow is the following:
- `macro_topic`: represents the macro topic of the workflow (Movie,Sport,History)
- `topic`: represents the `Search Topic` of the workflow
- `worker`: represents the id of the worker
- `goals`: is the list of `Search Task` for the `Search Topic`
- `name`: is the name of the file and the (unique) code of the `Search Workflow`
- `search_workflow`: is the collection of queries that compose the `Search Workflow`.

#### Search_workflow

Going deeper in the `search_workflow` field of the json workflow, the queries are grouped by `Search Job` in order to maintain the correct order of the queries for each task.

#### Query


The structure of the query is the following:
- `narrative`: is the comment (narrative) associated to the query. It is not always present.
- `query`: is the SPARQL query text
- `output`: is the output of the query execution. It is an array so each record of the output is an element of the array. If the output of the execution was empty then the `output` field contains an empty array, if the query was not executed or there was any problem in the execution, the `output` field is `null`
- `parseError`: if there is any error on the execution of the query, it is reported here. If there is no error, the `parseError` field is `null`.
- `keywords`: is a map of the SPARQL keywords in the query. The list of the SPARQL keywords is available [here](../src/data/keywords.txt)
- `recall`: is the recall value associated to the query according to the ground truth. 
- `precision`: is the precision value associated to the query according to the ground truth. 
- `accuracy`: is the accuracy value associated to the query according to the ground truth. 
- `fscore`: is the fscore value associated to the query according to the ground truth. 

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![CC BY 4.0][cc-by-shield]][cc-by]

The code inside this folder is distributed under the MIT License. In particular, for each track, the folder with this license are:
- notebooks
- querylogs

The other data are distributed under a [Creative Commons Attribution 4.0 International License][cc-by]. See [LICENSE-MIT](LICENSE-MIT) and [LICENSE-CC-BY](LICENSE-CC-BY) for more information.


[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg