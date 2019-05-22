import sys
import csv
import xml.etree.cElementTree as ET

# def parsedrug(drug):
# 	drugbank_id = drug.find('nsstring:drugbank-id',ns)     #Extract data at level#1
# 	#print(drugbank_id[1].text)    
# 	description= drug.find('nsstring:description',ns)
# 	try:
# 	    v_description = description.text
# 	except:
# 	    v_description = 'unknown'
# 	print(description)
# 	cas_number= drug.find('nsstring:cas-number',ns)
# 	try:
# 	    v_cas_number = cas_number.text
# 	except:
# 	    v_cas_number = 'unknown'

# 	for general_references in drug.findall('nsstring:general-references',ns):
# 		for articles in general-references.findall('nsstring:articles',ns):
# 			for article in articles.findall('nsstring:article',ns):
# 				pubmed_id = article.find('nsstring:pubmed-id',ns)
# 				try:
# 					v_pubmed_id = pubmed_id.text
# 				except:
# 					v_pubmed_id = 'unknown'
# 	return[drugbank_id[1].text,description.text,v_cas_number,v_pubmed_id] 


	# for categories in drug.findall('nsstring:categories',ns):
	# 	for category in categories.findall('nsstring:category',ns):
	#         mesh_id= category.find('nsstring:mesh-id',ns)
	#         try:
	#             v_mesh_id = mesh_id.text
	#         except:
	#             v_mesh_id = 'unknown'
	# for drug-interactions in drug.findall('nsstring:drug-interactions',ns):
	# 	for drug-interaction in drug.findall('nsstring:drug-interaction',ns):
	# 		drugbank_id= drug.find('nsstring:drugbank-id',ns)
	#         try:
	#             v_drugbank_id = drugbank_id.text
	#         except:
	#             v_drugbank_id = 'unknown'
	#         description= drug.find('nsstring:description',ns)
	#         try:
	#             v_description =  description.text
	#         except:
	#             v_description = 'unknown'

	# for external-identifiers in drug.findall('nsstring:external-identifiers',ns):
	# 	for external-identifier in drug.findall('nsstring:external-identifier',ns):
	# 		drugproduct_id = external-identifier.find('nsstring:identifier')
	            
    		# return[drugbank_id.text,description.text,v_cas_number,v_pubmed_id] 
			#return[drugbank_id.text,description.text,v_cas_number,v_pubmed_id] 

# ns ={'nsstring':'http://www.hmdb.ca'}

# drugheader=['description','cas_number','pubmed_id']
   
# count=0
# with open('drugstest.csv','w') as drugcsv:
#     writer = csv.writer(drugcsv)
#     writer.writerow(drugheader)

# for event, elem in ET.iterparse('drugstest.xml'):
#     #print(event, elem.tag)
#     if event == 'end':
#         if elem.tag == '{http://www.drugbank.ca}drug':
#             row = parsedrug(elem)
#             writer.writerow(row)
#             elem.clear()
#             count+=1
#             sys.stderr.write("\r %d" %(count))

# drugcsv.close()


for event, elem in ET.iterparse('drugstest.xml'):
    print(event, elem.tag)
    if event == 'end':
        if elem.tag == '{http://www.hmdb.ca}drug':
            print(elem)
        elem.clear()

#v_mesh_id,v_drugbank_id,drugproduct_id.text