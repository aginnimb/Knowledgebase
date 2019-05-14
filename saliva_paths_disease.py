import csv
import xml.etree.ElementTree as ET
tree = ET.parse('saliva_metabolites.xml')
root = tree.getroot()
#print(root)
ns ={'nsstring':'http://www.hmdb.ca'}
header = ['accession','pathway_name','smpdb_id','kegg_map_id','disease_name','omim_id','pubmed_id']
bio_props = []
with open("saliva_paths_diseases.csv","w") as sal:
    writer= csv.writer(sal)
    for metabolite in root.findall('nsstring:metabolite', ns):
        accession = metabolite.find('nsstring:accession',ns)    #Extract data at level#1
        for biological_properties in metabolite.findall('nsstring:biological_properties',ns):
            for pathways in biological_properties.findall('nsstring:pathways',ns):
                for pathway in pathways.findall('nsstring:pathway',ns):
                    pathway_name= pathway.find('nsstring:name',ns)
                    try:
                        v_pathway_name = pathway_name.text
                    except:
                        v_pathway_name = 'unknown'
                    smpdb_id= pathway.find('nsstring:smpdb_id',ns)
                    try:
                        v_smpdb_id = smpdb_id.text
                    except:
                        v_smpdb_id = 'unknown'
                    kegg_map_id= pathway.find('nsstring:kegg_map_id',ns)
                    try:
                        v_kegg_map_id = kegg_map_id.text
                    except:
                        v_kegg_map_id = 'unknown'
        for diseases in metabolite.findall('nsstring:diseases',ns):
            for disease in diseases.findall('nsstring:disease',ns):
                disease_name=disease.find('nsstring:name',ns)
                try:
                    v_disease_name = disease_name.text
                except:
                    v_disease_name = 'unknown'
                omim_id= disease.find('nsstring:omim',ns)
                try:
                    v_omim_id = omim_id.text
                except:
                    v_omim_id = 'unknown'
                # print(disease_name.text,omim_id.text) #has Nonetype
                for references in disease.findall('nsstring:references',ns):
                    for reference in references.findall('nsstring:reference',ns):
                        ref_text=reference.find('nsstring:reference_text',ns)
                        try:
                            v_ref_text = ref_text.text
                        except:
                            v_ref_text = 'unknown'
                        pubmed_id= reference.find('nsstring:pubmed_id',ns)
                        try:
                            v_pubmed_id = pubmed_id.text
                        except:
                            v_pubmed_id = 'unknown'
                        bio_props.append([accession.text,v_pathway_name,v_smpdb_id,v_kegg_map_id,v_disease_name,v_omim_id,v_pubmed_id])
    writer.writerow(header)
    for row in bio_props:
        writer.writerow(row)
sal.close()
