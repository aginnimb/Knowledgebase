import xml.etree.ElementTree as ET
tree = ET.parse('saliva_metabolites.xml')
root = tree.getroot()
#print(root)
ns ={'nsstring':'http://www.hmdb.ca'} 
salivaheader=['Accession','name','secondary_accessions','cs_description','synonyms','chemical_formula','average_mol_wt','monisotopic_mol_wt',
'iupac_name','traditional_iupac','cas_number','drugbank_id','chebi_id','cid','phenol_id','foodb_id','knapsack_id','chemspider_id','kegg_id',
'meta_cyc_id','bigg_id','metlin_id','pdb_id','wikipedia_id']
salivadata=[]
with open("saliva_metabolites.csv",'w') as salivacsv:
	writer = csv.writer(salivacsv)
	for metabolite in root.findall('nsstring:metabolite', ns):
		accession = metabolite.find('nsstring:accession',ns)	#Extract data at level#1
		name = metabolite.find('nsstring:name',ns)
		cs_description= metabolite.find('nsstring:cs_description',ns)
		chemical_formula= metabolite.find('nsstring:chemical_formula',ns)
		average_mol_wt= metabolite.find('nsstring:average_molecular_weight',ns)
		monisotopic_mol_wt= metabolite.find('nsstring:monisotopic_molecular_weight',ns)
		iupac_name= metabolite.find('nsstring:iupac_name',ns)
		traditional_iupac= metabolite.find('nsstring:traditional_iupac',ns)
		cas_number= metabolite.find('nsstring:cas_registry_number',ns)
		drugbank_id= metabolite.find('nsstring:drugbank_id',ns) #has none type
		chebi_id= metabolite.find('nsstring:chebi_id',ns)
		cid= metabolite.find('nsstring:pubchem_compound_id',ns)
		phenol_id= metabolite.find('nsstring:phenol_explorer_compound_id',ns) #has none type
		foodb_id= metabolite.find('nsstring:foodb_id',ns)
		knapsack_id= metabolite.find('nsstring:knapsack_id',ns) #has none type
		chemspider_id=metabolite.find('nsstring:chemspider_id',ns)
		kegg_id=metabolite.find('nsstring:kegg_id',ns)
		meta_cyc_id= metabolite.find('nsstring:meta_cyc_id',ns)
		bigg_id=metabolite.find('nsstring:bigg_id',ns) #has none type
		metlin_id=metabolite.find('nsstring:metlin_id',ns) #has none type
		pdb_id=metabolite.find('nsstring:pdb_id',ns) #has none type
		wikipedia_id=metabolite.find('nsstring:wikipedia_id',ns) #has none type
		secondary_accessions= metabolite.find('nsstring:secondary_accessions',ns)
		sa =[] #Extract data at level#2 with multiple occurences
		for sec_accession in secondary_accessions.findall('nsstring:accession',ns):
			sa.append(sec_accession.text)
			synonyms= metabolite.find('nsstring:synonyms',ns)
		sy = []
		for syns in synonyms.findall('nsstring:synonym',ns):
			sy.append(syns.text)
		salivadata.append([accession.text,name.text,sa,cs_description.text,sy,chemical_formula.text,average_mol_wt.text,
		monisotopic_mol_wt.text,iupac_name.text,traditional_iupac.text,cas_number.text,drugbank_id.text,chebi_id.text,cid.text,phenol_id.text,foodb_id.text,knapsack_id.text,chemspider_id.text,kegg_id.text,meta_cyc_id.text,
		bigg_id.text,metlin_id.text,pdb_id.text,wikipedia_id.text])
	writer.writerow(salivaheader)
	for row in salivadata:
		writer.writerow(row)
salivacsv.close()
 
