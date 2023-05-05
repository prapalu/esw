# Source code

This folder contains the python source code to manipulate the `Exploratory Workflows`, evaluate them, and serialize everything in turtle files.

## Contents
- [data](data/) folder contains the file of the SPARQL keywords and other csv files needed for the RDF serialization
- [gt_modules](gt_modules/) folder contains a python module for the creation of the ground truth json files
- [resource](resource/) folder contains the python modules needed to manipulate the `Exploratory Workflow`. More details [here](resource/README.md)
- the executable python files that process the original python notebooks `Exploratory Workflows`, convert, evaluate and serialize them. It is possible to reproduce the data the are already in this repository for the two tracks, following the steps:
    - [clean](#clean)
    - [convert](#convert)
    - [evaluate](#evaluate)
    - [serialize](#serialize)

You can also see the [shortcut](#shortcut) to run all these 4 steps with a single command
## Scripts

Before to execute any python script move yourself in the `src` folder. To do this:

```bash
cd src
```

**IMPORTANT**: every python script need a command line argument in order to be execute that is the configuration file. There are two configuration files, one per track, that you can use:
- `config2021.properties` is the configuration for the *2021* track, in the `tracks/2021` folder
- `config2022.properties` is the configuration for the *2022* track, in the `tracks/2022` folder

If a configuration file is not specified, you will receive an error.
The example of clean/conversion/evaluation/serialization show below works for the **2022** track. 

#### Clean

First of all it should be performed a clean operation, that remove the folders `workflows_json`, `workflows_evaluated` and `rdf`. To do this:

```bash
python clean.py config2022.properties
```

#### Convert 

After cleaning up the old folders, the first step to do is to convert the python notebook in the `tracks/2022/notebooks` folder, in JSON files. To do this:

```bash
python converter.py config2022.properties
```

During the conversion, execution logs are also associated.
This script creates the `tracks/2022/workflows_json` folder and it populates it with the JSON file.

#### Evaluate

Once the folder with the JSON files is created, then you can evaluate the `Exploratory Workflows`. To do this:

```bash
python evaluator.py config2022.properties
```

This script creates the `tracks/2022/workflows_evaluated` folder and it populates it with the JSON file of the `Exploratory Workflows` evaluated using the ground truths.

#### Serialize

The last step consists in the serialization of the evaluated `Exploratory Workflows` in turtle files. To do this:

```bash
python export_ttl.py config2022.properties
```

This script creates the `rdf` folder with two turtle files, `2022topics.ttl` that contains all the serialization of the `Search Topics`, `Search Tasks`, `Workers` and the `2022workflows.ttl` that contains the serialization of the `Exploratory Workflows`.

#### Shortcut

To run the entire process with a single command you can use the `main.py` script, that performs all these four operations (clean,convert,evaluate,serialize) for the configuration file specified as command line argument. To do this:

```bash
python main.py config2022.properties
```

If you want to run the main script for both the tracks `2021` and `2022`, you can do one of the following:

```bash
python main.py config2021.properties
python main.py config2022.properties
```

or simply

```bash
python main.py
```

The entire process should take 2-3 minutes  
