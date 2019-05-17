import csv
import xml.etree.ElementTree as ET
tree = ET.parse('hmdb_metabolites.xml')
root = tree.getroot()
#print(root)
ns ={'nsstring':'http://www.hmdb.ca'}
header = ['accession','pathway_name','smpdb_id','kegg_map_id']
bio_props = []
with open("hmdb_pathways.csv","w") as dis:
    writer= csv.writer(sweat)
    for metabolite in root.findall('nsstring:metabolite', ns):
        accession = metabolite.find('nsstring:accession',ns)    #Extract data at level#1
        for biological_properties in metabolite.findall('nsstring:biological_properties',ns):
            for cellular_locations in biological_properties.findall('nsstring:cellular_locations'):
                location = cellular_locations.find('nsstring:cellular')
            for biospecimen_locations in biological_properties.findall('nsstring:biospecimen_locations')
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
                    bio_props.append([accession.text,v_pathway_name,v_smpdb_id,v_kegg_map_id])
    writer.writerow(header)
    for row in bio_props:
        writer.writerow(row)
dis.close()
