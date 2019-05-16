import csv
import xml.etree.ElementTree as ET

tree = ET.parse('sweat_metabolites.xml')
root = tree.getroot()
#print(root)
ns ={'nsstring':'http://www.hmdb.ca'}
props_header = ['metabolite_accession','protein_accession','protein_name','uniprot_id','gene_name','protein_type','ontology_root_term','definition','parent_id','level','type','descendant_term','descend_definition','descend_parent_id','descend_level','descend_type','descend_synonyms','subdescend_term','subdescend_definition','subdescend_parent_id','subdescend_level','subdescend_type','subdescend_synonyms']
sweatdata=[]
for metabolite in root.findall('nsstring:metabolite', ns):
    accession = metabolite.find('nsstring:accession',ns)
    for ontology in metabolite.findall('nsstring:ontology',ns):
            for root in ontology.findall('nsstring:root',ns):
                term_root = root.find('nsstring:term',ns)
                try:
                    v_term_root = term_root.text
                except:
                    v_term_root = 'unknown'
                definition_root=root.find('nsstring:definition',ns)
                try:
                    v_definition_root = definition_root.text
                except:
                    v_definition_root = 'unknown'
                parent_id_root= root.find('nsstring:parent_id',ns)
                try:
                    v_parent_id_root = parent_id_root.text
                except:
                    v_parent_id_root = 'unknown'
                level_root=root.find('nsstring:level',ns)
                try:
                    v_level_root = level_root.text
                except:
                    v_level_root = 'unknown'
                type_root = root.find('nsstring:type',ns)
                try:
                    v_type_root = type_root.text
                except:
                    v_type_root = 'unknown'
                for descendants in root.findall('nsstring:descendants',ns):
                    for descendant in descendants.findall('nsstring:descendant',ns):
                        term_descend= descendant.find('nsstring:term',ns)
                        try:
                            v_term_descend = term_descend.text
                        except:
                            v_term_descend = 'unknown'
                        descend_def = descendant.find('nsstring:definition',ns)
                        try:
                            v_descend_def = descend_def.text
                        except:
                            v_descend_def = 'unknown'
                        parent_id_desc=descendant.find('nsstring:parent_id',ns)
                        try:
                            v_parent_id_desc = parent_id_desc.text
                        except:
                            v_parent_id_desc = 'unknown'
                        desc_level=descendant.find('nsstring:level',ns)
                        try:
                            v_desc_level = desc_level.text
                        except:
                            v_desc_level = 'unknown'
                        type_desc= descendant.find('nsstring:type',ns)
                        try:
                            v_type_desc = type_desc.text
                        except:
                            v_type_desc = 'unknown'
                        synonyms_desc=descendant.find('nsstring:synonyms',ns)
                        try:
                            v_synonyms_desc = synonyms_desc.text
                        except:
                            v_synonyms_desc = 'unknown'
                    for descendants in descendant.findall('nsstring:descendants',ns):
                        for descendant in descendants.findall('nsstring:descendant',ns):
                            term_desc= descendant.find('nsstring:term',ns)
                            try:
                                v_term_desc2 = term_desc.text
                            except:
                                v_term_desc2 = 'unknown'
                            term_def = descendant.find('nsstring:definition',ns)
                            try:
                                v_term_def2 = term_def.text
                            except:
                                v_term_def2 = 'unknown'
                            parent_id_desc=descendant.find('nsstring:parent_id',ns)
                            try:
                                v_parent_id_desc2 = parent_id_desc.text
                            except:
                                v_parent_id_desc2 = 'unknown'
                            desc_level=descendant.find('nsstring:level',ns)
                            try:
                                v_desc_level2 = desc_level.text
                            except:
                                v_desc_level2 = 'unknown'
                            type_desc= descendant.find('nsstring:type',ns)
                            try:
                                v_type_desc2 = type_desc.text
                            except:
                                v_type_desc2 = 'unknown'
                            synonyms_desc=descendant.find('nsstring:synonyms',ns)
                            try:
                                v_synonyms_desc2 = synonyms_desc.text
                            except:
                                v_synonyms_desc2 = 'unknown'
                            props.append([accession.text,v_protein_accession,v_protein_name,v_uniprot_id,v_gene_name,v_protein_type,v_term_root,v_definition_root,v_parent_id_root,v_level_root,v_type_root,v_term_desc,v_term_def,v_parent_id_desc,v_desc_level,v_type_desc,v_synonyms_desc,v_term_desc2,v_term_def2,v_parent_id_desc2,v_desc_level2,v_type_desc2,v_synonyms_desc2])

 with open('sweat_metabolites.csv','w') as sweatcsv:
    writer = csv.writer(sweatcsv)
    writer.writerow(sweatheader)
    for row in sweatdata:
        writer.writerow(row)
sweatcsv.close()