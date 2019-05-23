import sys
import csv
import xml.etree.cElementTree as ET

def parsedrugbank(drugbank, writer):
	# print("I am here")
	for drug in drugbank.findall('nsstring:drug',ns):
		drugbank_id = drug.find('nsstring:drugbank-id',ns)     #Extract data at level#1
		#print(drugbank_id[1].text)    
		description= drug.find('nsstring:description',ns)
		try:
		    v_description = description.text
		except:
		    v_description = 'unknown'
			#print(description)
		cas_number= drug.find('nsstring:cas-number',ns)
		try:
		    v_cas_number = cas_number.text
		except:
		    v_cas_number = 'unknown'

		for general_references in drug.findall('nsstring:general-references',ns):
			for articles in general_references.findall('nsstring:articles',ns):
				for article in articles.findall('nsstring:article',ns):
					pubmed_id = article.find('nsstring:pubmed-id',ns)
					try:
						v_pubmed_id = pubmed_id.text
					except:
						v_pubmed_id = 'unknown'

		for external_identifiers in drug.findall('nsstring:external-identifiers',ns):
			for external_identifier in external_identifiers.findall('nsstring:external-identifier',ns):
				resource = external_identifier.find('nsstring:resource',ns)
				try:
					v_resource = resource.text
				except:
					v_resource = 'unknown'
				identifier = external_identifier.find('nsstring:identifier',ns)
				try:
					v_identifier = identifier.text
				except:
					v_identifier = 'unknown'
				writer.writerow([drugbank_id.text,v_description,v_cas_number,v_pubmed_id,v_resource,v_identifier]) #write the file to get all th external identifiers

		            
ns ={'nsstring':'http://www.drugbank.ca'}

drugheader=['drugbank_id','description','cas_number','pubmed_id','resource','identifier','smpdv_id',]
   
count=0
drugcsv = open('drugstest.csv','w')
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

