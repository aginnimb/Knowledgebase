import csv
import xml.etree.ElementTree as ET
tree = ET.parse('saliva_metabolites.xml') #small_saliva.xml
root = tree.getroot()
ns ={'nsstring':'http://www.hmdb.ca'} #storing namespace string in a variable 
salivaheader=['Accession','name','secondary_accessions','cs_description','synonyms','chemical_formula','average_mol_wt','monisotopic_mol_wt',
'iupac_name','traditional_iupac','cas_number','drugbank_id','chebi_id','cid','phenol_id','foodb_id','knapsack_id','chemspider_id','kegg_id',
'meta_cyc_id','bigg_id','metlin_id','pdb_id','wikipedia_id']
salivadata=[]
with open("saliva_metabolites.csv",'w') as salivacsv:
	writer = csv.writer(salivacsv)
	for metabolite in root.findall('nsstring:metabolite', ns):
		accession = metabolite.find('nsstring:accession',ns)	#Extract data at level#1
		name = metabolite.find('nsstring:name',ns)  # exception condition to avoid the none type 
		try:
			v_name = name.text
		except:
			v_name = 'unknown'
		cs_description= metabolite.find('nsstring:cs_description',ns)
		try:
			v_cs_description = cs_description.text
		except:
			v_cs_description = 'unknown'
		chemical_formula= metabolite.find('nsstring:chemical_formula',ns)
		try:
			v_chemical_formula = chemical_formula.text
		except:
			v_chemical_formula = 'unknown'
		average_mol_wt= metabolite.find('nsstring:average_molecular_weight',ns)
		try:
			v_average_mol_wt = average_mol_wt.text
		except:
			v_average_mol_wt = 'unknown'
		monisotopic_mol_wt= metabolite.find('nsstring:monisotopic_molecular_weight',ns)
		try:
			v_monisotopic_mol_wt = monisotopic_mol_wt.text
		except:
			v_monisotopic_mol_wt = 'unknown'
		iupac_name= metabolite.find('nsstring:iupac_name',ns)
		try:
			v_iupac_name = iupac_name.text
		except:
			v_iupac_name = 'unknown'
		traditional_iupac= metabolite.find('nsstring:traditional_iupac',ns)
		try:
			v_traditional_iupac = traditional_iupac.text
		except:
			v_traditional_iupac = 'unknown'
		cas_number= metabolite.find('nsstring:cas_registry_number',ns)
		try:
			v_cas_number = cas_number.text
		except:
			v_cas_number = 'unknown'
		drugbank_id= metabolite.find('nsstring:drugbank_id',ns)
		try:
			v_drugbank_id = drugbank_id.text
		except:
			v_drugbank_id = 'unknown'
		chebi_id= metabolite.find('nsstring:chebi_id',ns)
		try:
			v_chebi_id = chebi_id.text
		except:
			v_chebi_id = 'unknown'
		cid= metabolite.find('nsstring:pubchem_compound_id',ns)
		try:
			v_cid = cid.text
		except:
			v_cid = 'unknown'
		phenol_id= metabolite.find('nsstring:phenol_explorer_compound_id',ns)
		try:
			v_phenol_id = phenol_id.text
		except:
			v_phenol_id = 'unknown'
		foodb_id= metabolite.find('nsstring:foodb_id',ns)
		try:
			v_foodb_id = foodb_id.text
		except:
			v_foodb_id = 'unknown'
		knapsack_id= metabolite.find('nsstring:knapsack_id',ns)
		try:
			v_knapsack_id = knapsack_id.text
		except:
			v_knapsack_id= 'unknown'
		chemspider_id=metabolite.find('nsstring:chemspider_id',ns)
		try:
			v_chemspider_id = chemspider_id.text
		except:
			v_chemspider_id= 'unknown'
		kegg_id=metabolite.find('nsstring:kegg_id',ns)
		try:
			v_kegg_id = kegg_id.text
		except:
			v_kegg_id= 'unknown'
		meta_cyc_id= metabolite.find('nsstring:meta_cyc_id',ns)
		try:
			v_meta_cyc_id = meta_cyc_id.text
		except:
			v_meta_cyc_id= 'unknown'
		bigg_id=metabolite.find('nsstring:bigg_id',ns)
		try:
			v_bigg_id = bigg_id.text
		except:
			v_bigg_id = 'unknown'
		metlin_id=metabolite.find('nsstring:metlin_id',ns)
		try:
			v_metlin_id = metlin_id.text
		except:
			v_metlin_id = 'unknown'
		pdb_id=metabolite.find('nsstring:pdb_id',ns)
		try:
			v_pdb_id = pdb_id.text
		except:
			v_pdb_id = 'unknown'
		wikipedia_id=metabolite.find('nsstring:wikipedia_id',ns)
		try:
			v_wikipedia_id = wikipedia_id.text
		except:
			v_wikipedia_id = 'unknown'
		secondary_accessions= metabolite.find('nsstring:secondary_accessions',ns)
		sa =[] #Extract data at level#2 with multiple occurences
		for sec_accession in secondary_accessions.findall('nsstring:accession',ns):
			sa.append(sec_accession.text)
			synonyms= metabolite.find('nsstring:synonyms',ns)
		sy = []
		for syns in synonyms.findall('nsstring:synonym',ns):
			sy.append(syns.text)
		salivadata.append([accession.text,v_name,sa,v_cs_description,sy,v_chemical_formula,v_average_mol_wt,v_monisotopic_mol_wt,v_iupac_name,v_traditional_iupac,v_cas_number,v_drugbank_id,v_chebi_id,v_cid,v_phenol_id,v_foodb_id,v_knapsack_id,v_chemspider_id,v_kegg_id,v_meta_cyc_id,
		v_bigg_id,v_metlin_id,v_pdb_id,v_wikipedia_id])
	writer.writerow(salivaheader)
	for row in salivadata:
		writer.writerow(row)
salivacsv.close()
