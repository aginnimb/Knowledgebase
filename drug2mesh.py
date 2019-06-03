import sys
import csv
import xml.etree.cElementTree as ET

def parsedrugbank(drugbank, writer):
	for drug in drugbank.findall('nsstring:drug',ns):
		drugbank_id = drug.find('nsstring:drugbank-id',ns)
		for categories in drug.findall('nsstring:categories',ns):
			for category in categories.findall('nsstring:category',ns):
				categoryname = category.find('nsstring:category',ns)
				mesh_id= category.find('nsstring:mesh-id',ns)
				try:
					v_mesh_id = mesh_id.text
				except:
					v_mesh_id = 'unknown'
				#print(drugbank_id.text,categoryname,v_mesh_id)
				writer.writerow([drugbank_id.text,categoryname.text,v_mesh_id])

ns ={'nsstring':'http://www.drugbank.ca'}

drugheader=['drugbank_id','categoryname.text','mesh_id']
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
