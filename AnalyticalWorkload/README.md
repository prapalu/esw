# Study of Exploratory Analytical Workloads on Knowledge Graphs


## Notebooks to analize experimental results

### Conda

#### install conda


```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3.7
sudo apt install python3-pip
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 1
python --version
wget https://repo.anaconda.com/miniconda/Miniconda3-py37_4.10.3-Linux-x86_64.sh
ls -alhg
bash Miniconda3-py37_4.10.3-Linux-x86_64.sh 
conda config --set auto_activate_base false
rm Miniconda3-py37_4.10.3-Linux-x86_64.sh 
conda install -c conda-forge jupyterlab
conda install -c conda-forge sparqlwrapper
```


#### How to run:

```bash
cd notebook
jupyter-lab --ip 0.0.0.0 --port 8888
```


### Using Docker 

#### Download image

```bash
docker pull jupyter/datascience-notebook
```

#### Start image

```bash
docker run  --name endpoint_nb --rm -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes -v "$PWD/notebook":/home/jovyan jupyter/datascience-notebook
```


## Download and clean the WikiData dump

**THIS WILL TAKE 250GB of DISK SPACE**

### Preparation

** Use virtual env **

```bash

python3 -m venv .pyenv
source .pyenv/bin/activate

```
### Download & Parse


**Truthy**

```bash

# was: wget https://dumps.wikimedia.org/wikidatawiki/entities/20210922/wikidata-20210922-truthy-BETA.nt.gz
wget https://archive.org/download/wikibase-wikidatawiki-20210922/wikidata-20210922-truthy-BETA.nt.gz


python scripts/clean-dump-gz.py wikidata-20210922-truthy-BETA.nt.gz >> parsed.log
```

**This will produce the file `./wikidata-truthy-prefiltered.nt`**


**All**

Alternatively substitute with this link

```
https://dumps.wikimedia.org/wikidatawiki/entities/20210920/wikidata-20210920-all-BETA.nt.gz
```


## Install Virtuoso and load WikiData


**Preparation**

```bash

docker pull openlink/virtuoso-opensource-7:latest
mkdir -p virtuoso/database
mkdir -p virtuoso/settings
cp  files/virtuoso.ini virtuoso/database/virtuoso.ini
```

```
mkdir ./data
mv ./wikidata-prefiltered.nt ./data
```


**Start container**

```bash
docker run -t -d --name vos-wiki \
        -v `pwd`/virtuoso/database:/database \
        -v `pwd`/virtuoso/settings:/settings \
        --env DBA_PASSWORD=admin \
        -v `pwd`/data:/import \
        -p 1111:1111 -p 5820:8890 -i \
        openlink/virtuoso-opensource-7:latest

```


**Prepare and Run the loading command**


```bash
docker exec -it vos-wiki /bin/bash

echo "delete from DB.DBA.load_list;" > /settings/load.isql

echo "ld_dir ('/import', '"wikidata-prefiltered.nt"', 'http://www.wikidata.org/');" >> /settings/load.isql

echo "rdf_loader_run ();" >> /settings/load.isql
echo "checkpoint;" >> /settings/load.isql

isql exec="LOAD /settings/load.isql"
exit
```

**Additionally the following query can be used to add a direct "name" to each property**


```
INSERT
{
    GRAPH <http://www.wikidata.org/> {
        ?p  <http://schema.org/name> ?name
    }
}

WHERE { 

GRAPH <http://www.wikidata.org/> {
 ?pt <http://wikiba.se/ontology#directClaim> ?p  .
 ?pt <http://schema.org/name> ?name .
}

} 


```

probably the `rdfs:label` is more appropriate

`<http://www.w3.org/2000/01/rdf-schema#label>`


## Install GraphDB and load WikiData



```bash
docker pull ontotext/graphdb:9.9.1-ee
mkdir -p graphdb/conf/
cp <path-to-license> graphdb/conf/graphdb.license   
cp files/graphdb.repository-config.ttl files/graphdb.properties graphdb/conf/


docker run -it --name graphdb-wdata \
        -v ${PWD}/graphdb:/opt/graphdb/home  \
        -v ${PWD}/data:/data \
        -p 7200:7200  \
        --entrypoint "/bin/sh" \
        ontotext/graphdb:9.9.1-ee

ln -s /opt/graphdb/home/conf/graphdb.properties /opt/graphdb/dist/conf/graphdb.properties

preload -f -c /opt/graphdb/home/conf/graphdb.repository-config.ttl /data/wikidata*.nt

docker run -t -d --name graphdb-wdata \
        -v ${PWD}/graphdb:/opt/graphdb/home  \
        -v ${PWD}/data:/data \
        -p 7200:7200  \
        ontotext/graphdb:9.9.1-ee \
        -Dgraphdb.home=/opt/graphdb/home \
        -Dgraphdb.global.page.cache=true -Xmx164g -Xms12g

docker exec -it graphdb-wdata /bin/bash

```
