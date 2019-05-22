import sys
import csv
import xml.etree.cElementTree as ET

def cleantext(t, defaultValue=None):
    try:
        return bytes(t.text, "utf-8").decode('unicode_escape')
    except:
        return defaultValue

def parseMetabolite(metabolite):
    accession = metabolite.find('nsstring:accession',ns)    #Extract data at level#1
    name = cleantext(metabolite.find('nsstring:name',ns), 'unknown')
    cs_description= cleantext(metabolite.find('nsstring:cs_description',ns),'unknown')
    
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
    iupac_name= metabolite.find('nsstring:iupac_name',ns)
    try:
        v_iupac_name = iupac_name.text
    except:
        v_iupac_name = 'unknown'
    cas_number= metabolite.find('nsstring:cas_registry_number',ns)
    try:
        v_cas_number = cas_number.text
    except:
        v_cas_number = 'unknown'
    for taxonomy in metabolite.findall('nsstring:taxonomy',ns):
        kingdom = taxonomy.find('nsstring:kingdom',ns)
        try:
            v_kingdom = kingdom.text
        except:
            v_kingdom = 'unknown'
        super_class= taxonomy.find('nsstring:super_class',ns)
        try:
            v_super_class = super_class.text
        except:
            v_super_class = 'unknown'
        taxa_class = taxonomy.find('nsstring:class',ns)
        try:
            v_taxa_class = taxa_class.text
        except:
            v_taxa_class = 'unknown'

        drugbank_id= metabolite.find('nsstring:drugbank_id',ns)
        try:
            v_drugbank_id = drugbank_id.text
        except:
            v_drugbank_id = 'unknown'
        chebi_id= metabolite.find('nsstring:chebi_id',ns)
        try:
            v_chebi_id = 'CHEBI:' + chebi_id.text
        except:
            v_chebi_id = 'unknown'
        cid= metabolite.find('nsstring:pubchem_compound_id',ns)
        try:
            v_cid =  cid.text
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
    return [accession.text,name,cs_description,v_chemical_formula,v_average_mol_wt,v_iupac_name,v_cas_number,v_kingdom,v_super_class,v_taxa_class,v_drugbank_id,v_chebi_id,v_cid,v_phenol_id,v_foodb_id,v_knapsack_id,v_chemspider_id,v_kegg_id,v_meta_cyc_id,v_bigg_id,v_metlin_id,v_pdb_id,v_wikipedia_id]

ns ={'nsstring':'http://www.hmdb.ca'}

hmdbheader=['Accession','name','cs_description','chemical_formula','average_mol_wt','iupac_name','cas_number','kingdom','super_class','taxa_class','drugbank_id','chebi_id','cid','phenol_id','foodb_id','knapsack_id','chemspider_id','kegg_id',
'meta_cyc_id','bigg_id','metlin_id','pdb_id','wikipedia_id']
   
count=0
with open('hmdb_metabolites.csv','w') as hmdbcsv:
    writer = csv.writer(hmdbcsv)
    writer.writerow(hmdbheader)

    for event, elem in ET.iterparse('hmdb_metabolites.xml'):
        #print(event, elem.tag)
        if event == 'end':
            if elem.tag == '{http://www.hmdb.ca}metabolite':
                row = parseMetabolite(elem)
                writer.writerow(row)
                elem.clear()
                count+=1
                sys.stderr.write("\r %d" %(count))

hmdbcsv.close()


## tree = ET.parse('hmdb_metabolites.xml')
## root = tree.getroot()
## sweatdata=[]
## #print(root)
## for metabolite in root.findall('nsstring:metabolite', ns):
##     row = parseMetabolite(metabolite)
##     sweatdata.append(row)
# print(sweatdata)

