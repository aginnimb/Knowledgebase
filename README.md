# Knowledgebase-Project(Neo4j implementation) 

#Creating a consolidated graph database and mapping relations between the databases using Neo4j. This includes XML file conversions - Parsing and flattening the XML file into CSV

## Installation
https://neo4j.com/download-center/#releases (install the Community version)-- 
make sure to set up the home directory so we can run through the command line

## Installation using Home Brew: (Popular package manager for macOS)
*Ensure Homebrew is installed before you think of using it
if not run this on command line: ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
For better understanding : https://docs.brew.sh/Installation

Then on command line run: Brew cask Install neo4j
*You will see something like this: 
 home:         /Users/aginni/opt/brew/Cellar/neo4j/3.5.3/libexec
  config:       /Users/aginni/opt/brew/Cellar/neo4j/3.5.3/libexec/conf
  logs:         /Users/aginni/opt/brew/var/log/neo4j
  plugins:      /Users/aginni/opt/brew/Cellar/neo4j/3.5.3/libexec/plugins
  *import:       /Users/aginni/opt/brew/Cellar/neo4j/3.5.3/libexec/import
  data:         /Users/aginni/opt/brew/var/neo4j/data
  certificates: /Users/aginni/opt/brew/Cellar/neo4j/3.5.3/libexec/certificates
  run:          /Users/aginni/opt/brew/Cellar/neo4j/3.5.3/libexec/run
Starting Neo4j.
Started neo4j (pid 72115). It is available at http://localhost:7474/. #Copy this to the browser to launch neo4j
There may be a short delay until the server is ready.
See /Users/aginni/opt/brew/var/log/neo4j/neo4j.log for current status.

## Load CSV WITH HEADERS 
*neo4j which will create the nodes with their properties while loading
* Neo4j cannot find the file unless it is in the neo4j imports directory.Make sure the data is in neo4j imports directory

*phenolsdata directory is copied to the neo4j imports
cp /Users/aginni/Documents/phenolsdata/phenols_classification.csv /Users/aginni/opt/brew/Cellar/neo4j/3.5.3/libexec/import/phenolsdata/

*/Users/aginni/opt/brew/Cellar/neo4j/3.5.3/libexec/import/phenolsdata 

*Either MERGE or CREATE functions can be used to create the nodes with all the properties 
*Syntax is important: for example if you specify line.data instead of Line.data it gives an erroer.
* Also aliases you specify will appear on the nodes, so now is the chance to give a good(consider as renaming)property labels
/*
LOAD CSV WITH HEADERS FROM 'file:///phenolsdata/phenols_classification.csv' AS Line CREATE (:phenols_classfication {class: Line.class, subclass: Line.subclass, compound_name: Line.compound_name, phenol_id: Line.phenol_id, mol_wt: Line.mol_wt, formula: Line.formula}) */

/*
LOAD CSV WITH HEADERS FROM 'file:///phenolsdata/phenol_to_chebi.csv' AS Line MERGE (:phenol_to_chebi {phenol_id: Line.phenol_id, chebi_id: Line.chebi_id}) */ 

/* LOAD CSV WITH HEADERS FROM 'file:///phenol_to_pubmed.csv' AS Line MERGE (:phenol_to_pubmed {phenol_id: Line.phenol_id, pubchem_id: Line.pubchem_id}) */

/* LOAD CSV WITH HEADERS FROM 'file:///phenolsdata/compounds.csv' AS Line CREATE(:compounds{phenol_id: Line.phenol_to_chebi, class: Line.class, subclass: Line.subclass, compound_name: Line.compound_name,mol_wt: Line.mol_wt, synonyms: Line.synonyms, formula: Line.formula, cas_number: Line.cas_number,
chebi_id: Line.chebi_id, pubchem_id: Line.pubchem_id, aglycones: Line.aglycones, created_on: Line.created_on, updated_on: Line.updated_on}) */

/* LOAD CSV WITH HEADERS FROM 'file:///phenolsdata/PhenolCompounds1.csv' AS Line CREATE(:PhenolCompounds{phenol_id: Line.id, compound_class: Line.compound_class, name:Line.name, mol_wt: Line.molecular_weight, synonyms: Line.synonyms, formula: Line.formula, cas_number: Line.cas_number,
chebi_id: Line.chebi_id, cid: Line.pubchem_compound_id, aglycones: Line.aglycones, created_at: Line.created_at, updated_at: Line.updated_at}) */

## Querying

/* EXAMPLES TO TEST THE MAPPING
Always check for the existence of the data before updating, creating relations or even deleting, as Neo4j does not throw any errors 
In the below code, we are matching two node labels ased on their properties and returning the graph 

-- MATCH (r:phenol_to_chebi{phenol_id : '421'})
-- MATCH (x:CHEBI{chebi_id:'CHEBI:62023'})
-- RETURN r, x. #r,x are aliases for phenol_to chebi and CHEBI nodes respectively


#Same as above but here we are matching and creating a relationship between the nodes based on a matching property
-- MATCH (a:Compound) MATCH(b:PhenolCompounds) WHERE a.cid = b.cid 
-- CREATE (a)-[r:SAME_AS]->(b) 
-- RETURN a,b

-- MATCH (a:PhenolCompounds) MATCH (b:CHEBI)
-- WHERE a.chebi_id = b.chebi_id
-- CREATE (a)-[r:SAME_AS]->(b) RETURN a,b

## Rename label and remove old one

#Match the node label and rename using SET function. And it is important to remove the old one as it creates redundancy with in the database

/* MATCH (s:phenols_classfication)
 SET s:Phenols_Classification
REMOVE s:phenols_classfication */
/* MATCH (phenol_to_chebi) DELETE phenol_to_chebi */ (not sure)


## Matching label and removing

/* MATCH (s:phenol_to_pubmed) #to remove any unnecessary nodes
REMOVE s:phenol_to_pubmed */

/* MATCH (s:phenol_to_chebi)
REMOVE s:phenol_to_chebi */

##DELETE relationships between nodes

*To delete the relationship between two nodes, make sure to specify the relation type else it may remove existing relationships
/* MATCH(:phenol_to_chebi)-[r:REFERENCED_IN](:phenolcompounds) DELETE r */

/* MATCH(:KEGG)-[r:SAME_AS]-(:BioSystem) DELETE r */

*Same as above,but here we are deleting the relation just between the two properties of the nodes
/* MATCH (r:phenol_to_chebi{phenol_id : '421'})-[deleteme:SAME_AS]->(x:CHEBI{chebi_id:'CHEBI:62023'})
DELETE deleteme; */
