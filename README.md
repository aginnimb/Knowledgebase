# Knowledgebase-Project(Neo4j implementation) 

#Creating a consolidated graph database and mapping relations between the databases using Neo4j. This includes some ETL steps and data manipulations and 
XML file conversions - Parsing and flattening the XML file into CSV

## Installation 
https://neo4j.com/download-center/#releases (install the Community version)
make sure to set up the home directory so we can run through the command line

## Code

/* EXAMPLES TO TEST THE MAPPING
Always check for the existence of the data before updating, creating relations or even deleting, as Neo4j does not throw any errors 
In the below code, we are matching two node labels ased on their properties and returning the graph 

MATCH (r:phenol_to_chebi{phenol_id : '421'}) #r,x are aliases for phenol_to chebi and CHEBI nodes respectively
MATCH (x:CHEBI{chebi_id:'CHEBI:62023'})
RETURN r, x


#1 Same as above but here we are matching and creating a relationship between the nodes based on a matching property
MATCH (a:Compound) MATCH(b:PhenolCompounds) WHERE a.cid = b.cid 
CREATE (a)-[r:SAME_AS]->(b) 
RETURN a,b

#2 
MATCH (a:PhenolCompounds) MATCH (b:CHEBI)
WHERE a.chebi_id = b.chebi_id
CREATE (a)-[r:SAME_AS]->(b) RETURN a,b

# Rename label and remove old one
Match the node label and rename using SET function. And it is important to remove the old one as it creates redundancy with in the database
MATCH (s:phenols_classfication)
SET s:Phenols_Classification
REMOVE s:phenols_classfication

# Matching label and removing
to remove any unnecessary nodes
MATCH (s:phenol_to_pubmed)
REMOVE s:phenol_to_pubmed

MATCH (s:phenol_to_chebi)
REMOVE s:phenol_to_chebi

# DELETE relationships between nodes
To delete the relationship between two nodes, make sure to specify the relation type else it may remove existing relationships
MATCH(:phenol_to_chebi)-[r:REFERENCED_IN](:phenolcompounds) DELETE r
MATCH(:KEGG)-[r:SAME_AS]-(:BioSystem) DELETE r

Same as above,but here we are deleting the relation just between the two properties of the nodes
MATCH (r:phenol_to_chebi{phenol_id : '421'})-[deleteme:SAME_AS]->(x:CHEBI{chebi_id:'CHEBI:62023'})
DELETE deleteme;
