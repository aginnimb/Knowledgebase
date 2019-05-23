import sys
import csv
import xml.etree.cElementTree as ET

def parsedrugbank(drugbank, writer):
	for drug in drugbank.findall('nsstring:drug',ns):
		drugbank_id = drug.find('nsstring:drugbank-id',ns)
		for pathways in drug.findall('nsstring:pathways',ns):
			for pathway in pathways.findall('nsstring:pathway',ns):
				smpdb_id = pathway.find('nsstring:smpdb-id',ns)
				try:
					v_smpdb_id = smpdb_id.text
				except:
					v_smpdb_id = 'unknown'
				pathwayname = pathway.find('nsstring:name',ns)
				try:
					v_pathwayname = pathwayname.text
				except:
					v_pathwayname = 'unknown'
				#print(v_resource,v_identifier,v_smpdb_id,v_pathwayname)

				for enzymes in pathway.findall('nsstring:enzymes',ns):
					uniprot_id = enzymes.find('nsstring:uniprot-id',ns)
					try:
						v_uniprot_id = uniprot_id.text
					except:
						v_uniprot_id = 'unknown'
					#print(v_uniprot_id)
		for targets in drug.findall('nsstring:targets',ns):
			for target in targets.findall('nsstring:target',ns):
				target_id = target.find('nsstring:id',ns)
				try:
					v_target_id = target_id.text
				except:
					v_target_id = 'unknown'
				writer.writerow([drugbank_id.text,v_smpdb_id,v_pathwayname,v_uniprot_id,v_target_id])

ns ={'nsstring':'http://www.drugbank.ca'}

drugheader=['drugbank_id','smpdb_id','pathwayname','uniprot_id','target_id']
   
count=0
drugcsv = open('drugpathways.csv','w')
writer = csv.writer(drugcsv)
writer.writerow(drugheader)

for event, elem in ET.iterparse('drugstest.xml'):
    if event == 'end':
        if elem.tag == '{http://www.drugbank.ca}drugbank':
            row = parsedrugbank(elem, writer)
            # writer.writerow(row)
            elem.clear()
            count+=1
            sys.stderr.write("\r %d" %(count))

drugcsv.close()