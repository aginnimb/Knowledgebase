mport xml.etree.ElementTree as ET
tree = ET.parse('saliva_metabolites.xml')
root = tree.getroot()
#print(root)
ns ={'nsstring':'http://www.hmdb.ca'} 

for metabolite in root.findall('nsstring:metabolite', ns):
    #Extract data at level#1
    accession = metabolite.find('nsstring:accession',ns)
    name = metabolite.find('nsstring:name',ns)
    
    #Extract data at level#2 with multiple occurences
    secondary_accessions= metabolite.find('nsstring:secondary_accessions',ns)
    sa =[]
    for sec_accession in secondary_accessions.findall('nsstring:accession',ns):
        sa.append(sec_accession.text)
    print (accession.text,name.text,sa)