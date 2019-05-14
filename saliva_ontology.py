import csv
import xml.etree.ElementTree as ET
tree = ET.parse('small_saliva.xml')
root = tree.getroot()
#print(root)
ns ={'nsstring':'http://www.hmdb.ca'}
# pathheader = ['pathway_name','smpdb_id','kegg_map_id']
# bio_props = []
# with open("saliva_pathways.csv","w") as sal:
#     writer= csv.writer(sal)
#     for metabolite in root.findall('nsstring:metabolite', ns):
#         for biological_properties in metabolite.findall('nsstring:biological_properties',ns):
#             for pathways in biological_properties.findall('nsstring:pathways',ns):
#                 for pathway in pathways.findall('nsstring:pathway',ns):
#                     pathway_name= pathway.find('nsstring:name',ns)
#                     try:
#                         v_pathway_name = pathway_name.text
#                     except:
#                         v_pathway_name = 'unknown'
#                     smpdb_id= pathway.find('nsstring:smpdb_id',ns)
#                     try:
#                         v_smpdb_id = smpdb_id.text
#                     except:
#                         v_smpdb_id = 'unknown'
#                     kegg_map_id= pathway.find('nsstring:kegg_map_id',ns)
#                     try:
#                         v_kegg_map_id = kegg_map_id.text
#                     except:
#                         v_kegg_map_id = 'unknown'
#                     bio_props.append([v_pathway_name,v_smpdb_id,v_kegg_map_id])
#     writer.writerow(pathheader)
#     for row in bio_props:
#         writer.writerow(row)
# sal.close()
dis_header = ['disease_name','omim_id','reference','pubmed_id']
dis_data = []
with open("saliva_diseases.csv","w") as dis:
    writer = csv.writer(dis)
    for metabolite in root.findall('nsstring:metabolite', ns):
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
                        dis_data.append([v_disease_name,v_omim_id,v_ref_text,v_pubmed_id])
    writer.writerow(dis_header)
    for row in dis_data:
        writer.writerow(row)
dis.close()
    # for protein_associations in metabolite.findall('nsstring:protein_associations',ns):
    #     for protein in protein_associations.findall('nsstring:protein',ns):
    #         protein_accession=protein.find('nsstring:protein_accession',ns)
    #         protein_name=protein.find('nsstring:name',ns)
    #         uniprot_id= protein.find('nsstring:uniprot_id',ns)
    #         gene_name= protein.find('nsstring:gene_name',ns)
    #         protein_type = protein.find('nsstring:protein_type',ns)
    #         #print(protein_accession.text,protein_name.text,uniprot_id.text,gene_name.text,protein_type.text)
    # for ontology in metabolite.findall('nsstring:ontology',ns):
    #     for root in ontology.findall('nsstring:root',ns):
    #         term_root = root.find('nsstring:term',ns)
    #         definition_root=root.find('nsstring:definition',ns)
    #         parent_id_root= root.find('nsstring:parent_id',ns)
    #         level_root=root.find('nsstring:level',ns)
    #         type_root= root.find('nsstring:type',ns)
    #         for descendants in root.findall('nsstring:descendants',ns):
    #             for descendant in descendants.findall('nsstring:descendant',ns):
    #                 term_desc= descendant.find('nsstring:term',ns)
    #                 term_def = descendant.find('nsstring:definition',ns)
    #                 parent_id_desc=descendant.find('nsstring:parent_id',ns)
    #                 desc_level=descendant.find('nsstring:level',ns)
    #                 type_desc= descendant.find('nsstring:type',ns)
    #                 synonyms_desc=descendant.find('nsstring:synonyms',ns)
    #                 #print(term_root.text,definition_root.text,parent_id_root.text,level_root.text,type_root.text,term_desc.text,term_def.text,parent_id_desc.text,type_desc.text,desc_level.text,synonyms_desc.text)
