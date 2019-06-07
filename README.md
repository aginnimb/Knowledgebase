# XML parsing using Python & Neo4j implementation

This repository contains python scripts to parse various file formats which includes XML, .txt etc and also Neo4j scripts to upload CSV files,creating relations between the nodes,querying using Cypher along with some update and delete scripts.

##### FYI :sunglasses: :wink:

* all the scripts are in Python 3.6.8 & 3.7 version
* used atom, sublime text, jupyter notebook for scripting
* make sure to check your environments and home directories set up before implementing any uitlities/tools
* some command line ETL is done (refer ETL.rtf file)
* DDL, DML files contains schema definitions and data manipulations for **PostgreSQL** *ignore if not required*

**flow goes from code to extra data  --> write to csv --> upload to neo4j --> relationships --> querying**

#### Code 

* all the .py files includes mostly the similar scripts,however the level of data extraction changes from file to file
* imported xml.etree.ElementTree module to parse the file 

*this is snippet of code, refer Knowledge-Project/*.py files

###### example:

```python3    
import csv
import xml.etree.ElementTree as ET
tree = ET.parse('saliva_metabolites.xml') #small_saliva.xml
root = tree.getroot()
ns ={'nsstring':'http://www.hmdb.ca'} #storing namespace string in a variable 
```
* conditions to check none type
* csv writer to store the extracted data into a csv file format

###### example:

```python3
writer.writerow(salivaheader)
	for row in salivadata:
		writer.writerow(row)
salivacsv.close()
```

## Installation
[install neo4j](https://neo4j.com/download-center/#releases) 

--suggested Community version-- 

*make sure to set up the home directory so we can run through the command line*

### Load CSV files WITH HEADERS 

* As of now neo4j accepts csv files to upload data with or without headers, all scripts in this repo are for **csv with headers**.(refer Knowledge-Project/Neo4jloads folder for more examples)

* Neo4j cannot find the path to file on your local machine unless it is in the neo4j imports directory. Make sure the data is in neo4j imports directory

*phenolsdata directory is copied to the neo4j imports*

```neo4j
cp /Users/aginni/Documents/phenolsdata/phenols_classification.csv /Users/aginni/opt/brew/Cellar/neo4j/3.5.3/libexec/import/phenolsdata/
```
* Either MERGE or CREATE functions can be used to create the nodes with all the properties

* Syntax is important: for example if you specify line.data instead of Line.data it gives an error

* Also aliases you specify will appear on the nodes, so now is the chance to give a good(consider as renaming)property labels

###### Example:

```
LOAD CSV WITH HEADERS FROM 'file:///phenolsdata/phenols_classification.csv' AS Line CREATE (:phenols_classfication {class: Line.class, subclass: Line.subclass, compound_name: Line.compound_name, phenol_id: Line.phenol_id, mol_wt: Line.mol_wt, formula: Line.formula})
```

### Querying

*EXAMPLES TO TEST THE MAPPING

* Always check for the existence of the data before updating, creating relations or even deleting, as Neo4j does not throw any errors 

* In the code below, we are matching two node labels based on their properties

###### Example:

```
MATCH (r:phenol_to_chebi{phenol_id : '421'}) MATCH (x:CHEBI{chebi_id:'CHEBI:62023'}) RETURN r, x 
# r,x are aliases for phenol_to chebi and CHEBI nodes respectively
```

* Same as above but here we are matching and creating a relationship between the nodes based on a matching property

``` 
MATCH (a:Compound) MATCH(b:PhenolCompounds) WHERE a.cid = b.cid CREATE (a)-[r:SAME_AS]->(b) RETURN a,b
```

### Rename label and remove old one

###### Example:

* Match the node label and rename using SET function and it is important to remove the old one as it creates redundancy with in the database

```
MATCH (s:phenols_classfication) SET s:Phenols_Classification REMOVE s:phenols_classfication
```

### Matching label and removing

``` 
MATCH (s:phenol_to_pubmed) REMOVE s:phenol_to_pubmed  #to remove any unnecessary nodes

MATCH (s:phenol_to_chebi) REMOVE s:phenol_to_chebi
```
### Relationships between nodes

Relation between nodes can be assigned by matching the labels and specifying the property nodes

###### Example:
```
MATCH (a:Compound) MATCH(b:HMDBMetabolites) WHERE a.cid = b.cid CREATE (a)<-[:SAMEAS]-(b) RETURN a,b
MATCH (a:CHEBI) MATCH(b:HMDBMetabolites) WHERE a.chebi_id = b.chebi_id CREATE (a)<-[:SAMEAS]-(b) RETURN a,b

MATCH (a:HMDBPathways) MATCH(b:Pathway Interaction Database) WHERE a.pathway_name = b.name return a,b limit 10 # to check
```
### DELETE relationships between nodes

* To delete the relationship between two nodes, it is important to specify the relation type else it will remove all existing relationships that matches the condition :anguished: :flushed:

###### Example:

``` MATCH(:phenol_to_chebi)-[r:REFERENCED_IN](:phenolcompounds) DELETE r  ```

* Same as above,but here we are deleting the relation just between the two properties of the nodes

``` 
MATCH (r:phenol_to_chebi{phenol_id : '421'})-[deleteme:SAME_AS]->(x:CHEBI{chebi_id:'CHEBI:62023'}) DELETE deleteme;
```



