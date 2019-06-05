## downloading files from web using python urllib module
# import urllib.request
# print("Beginning file download with urllib...")
# url = 'https://data.omim.org/downloads/1r6-54cxR_inA4Zf_bzd0w/mimTitles.txt'
# urllib.request.urlretrieve(url, '/Users/aginni/Documents/omim/omimTitles.txt')
															## importing files from OMIM web browser using urllib.request module
# print("Beginning file download with urllib...")
# url = 'https://data.omim.org/downloads/1r6-54cxR_inA4Zf_bzd0w/genemap2.txt'
# urllib.request.urlretrieve(url,'/Users/aginni/Documents/omim/omimgenemap2.txt')

## ETL using Python Pandas, not efficient but does the job
import pandas as pd
import numpy as np 
from itertools import chain
import re

data = pd.read_csv("/Users/aginni/Documents/omim/omimgenemap2.txt", sep = "\t",index_col = 0,skiprows = 3, skipfooter = 63,engine = 'python')
# print(data)
# print(data.columns)

data.columns = ['GenomicPositionStart','GenomicPositionEnd','CytoLocation','ComputedCytoLocation','Mim_Number','GeneSymbols','GeneName','ApprovedSymbol','EntrezGene_ID','EnsemblGene_ID','Comments','Phenotypes','MouseGeneSymbol/ID']

# return list from series of colon-separated strings
def chainer(s):
    return list(chain.from_iterable(s.str.split(';')))

data['Phenotypes'].fillna('', inplace=True)			
lens = data['Phenotypes'].str.split(';').map(len)	#calculate lengths of splits	
# # print(data['Phenotypes'])

# # create new dataframe, repeating or chaining as appropriate and with necessary columns
final = pd.DataFrame({'Mim_Number': np.repeat(data['Mim_Number'], lens),'GeneSymbols':np.repeat(data['GeneSymbols'],lens),'GeneName':np.repeat(data['GeneName'],lens),'Phenotypes': chainer(data['Phenotypes'])})
# print("Before:\n", data)
# print("After:\n", test)
# faster way to extract the column substrings than doing it individually like line[42-49
x = final['Phenotypes'].str.extract('.?([^{}[\]]*).?, (\d{6})') 
final['phenotype_id'] = x[1]
final['Phenotypes'] = x[0]
# print(final)

final.to_csv("finalomim.csv",index=False)

# final['phenotype_id'] = final['Phenotypes'].str.extract('(\d{6})')
# sub = '(\d{6})'
# final['Phenotypes']= final['Phenotypes'].str.replace(sub, '')
# final['Phenotypes']= final['Phenotypes'].str.replace('{', '')
# final['Phenotypes']= final['Phenotypes'].str.replace('}', '')
# final['Phenotypes']= final['Phenotypes'].str.replace('[', '')
# final['Phenotypes']=final['Phenotypes'].str.replace(']', '')
# final['Phenotypes']= final['Phenotypes'].str.replace('((\d))', '')


# ## extracting phenotype_ids from from 'Phenotypes' column
# data[['phenotype_id']]  = data.Phenotypes.str.extract('(\d{6})')
# # print(phenotype_id)

# #defining new columns with the split values
# data[['mouse_gene','mouse_gene_id']]= data["Mouse Gene Symbol/ID"].str.split(" ", n=1,expand = True)
# # print(data['mouse_gene_id'])

# #replacing na's with empty string
# data[['mouse_gene_id']] =data[['mouse_gene_id']].fillna('unknown')

# # data[["mouse_gene_id"]] = data[["mouse_gene_id"]].str.replace('(',"").str.replace(')',"") #it works but not on dataframe,hence following method

# test= data['mouse_gene_id'] # to string, as dataframe doesnot have str attribute
# data['mouse_gene_id']=test.str.replace("(","").str.replace(')',"")
# #print(data)

# data.to_csv("/Users/aginni/Documents/omim/omim.csv", index = False) #writing dataframe into csv

## Tried following ETL using python pandas, need corrections

# omimdata= []

# def omimparser(self):
# 	self.omimkey = ["Mim Number","Preferred Title","symbol","Alternative Title(s)","symbol(s)","Included Title(s)","symbols"]
# 	self.omimvals = {key:None for key in self.omimkey}

# 	with open(file,'r') as mim:
# 		for line in mim.readlines().split(','):
# 			print(line)
# 			for i,colnames in enumerate(self.omimkey):
# 				omimvals[omimkey] = omimkey[i]
					# if "Preferred Title; symbol" in line:
					# 	self.omimvals["Preferred_title"]= line.split(";")[0]
					# 	self.omimvals["symbol"] = line.split(";")[1]
			# elif "Alternative Title(s); symbol(s)" in line:
			# 	self.omimvals["Alternative_titles"] = line.split(";")[0]
			# 	self.omimvals["Alt_symbols"] = line.split(";")[1]
			# elif "Included Title(s); symbols" in line:
			# 	self.omimvals["Included_Titles"] = line.split(";")[0]
			# 	self.omimvals["Included_symbols"] = line.split(";")[1]
				# print(self.omimkey,self.omimvals)
				# omimdata.append([min_number + '\t' + Preferred_title + '\t' + symbol+ '\t' +Alternative_titles+ '\t' +Alt_symbols+ '\t' +Included_Titles+ '\t' +Included_symbols])
				# print(omimdata)


# file = ('/Users/aginni/Documents/omim/omimTitles.txt')
# omim = omimparser(file)

# ## Using pandas on jupyter notebook

# import pandas as pd
# import re

# data = pd.read_csv("/Users/aginni/Documents/omim/omimgenemap2.txt", sep = "\t",index_col = 0,skiprows = 3)
# # print(data)

# ## Splitting Phenotypes columns by comma, n is no of splits, expand is to keep the split values in separate columns
# ph_type = data["Phenotypes"].str.replace("},", "};")
# ph_type =ph_type.str.replace("],", "];")
# # print(ph_type)

# for i in ph_type:
# #     print(i)
# #     if i.str.find(';') != -1:
#     print(i.str)
#continue
#     else:
#         temp = i.split(',', expand = True)
#         print(temp)



# ph_type1 = ph_type.str.split(";", n=1,expand = True)

# print(ph_type1)

## extaction using regex
# data["Phenotype_no"] = data["Phenotypes"].str.extract("\W").astype(str) # works but does not not give the ids

# data["Phenotype_no"] = data["Phenotypes"].apply(lambda x: re.search([[r'\d+']], x).group()) #not working
# data.head()
