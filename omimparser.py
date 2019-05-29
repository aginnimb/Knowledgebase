# import urllib.request
# print("Beginning file download with urllib...")
# url = 'https://data.omim.org/downloads/1r6-54cxR_inA4Zf_bzd0w/mimTitles.txt'
# urllib.request.urlretrieve(url, '/Users/aginni/Documents/omim/omimTitles.txt')   
															## importing files from OMIM web browser using urllib.request module
# print("Beginning file download with urllib...")
# url = 'https://data.omim.org/downloads/1r6-54cxR_inA4Zf_bzd0w/genemap2.txt'
# urllib.request.urlretrieve(url,'/Users/aginni/Documents/omim/omimgenemap2.txt')


# def omimdata(self):
# 	# header = Mim Number	Preferred Title; symbol	Alternative Title(s); symbol(s)	Included Title(s); symbols
# 	data = (self.file, delimiter = '\t',header = None)
# 	return data

# omimdata= []
def omimparser(self):
	with open(file,'r') as mim:
		data = mim.readlines()
		for elem in data:
			if elem.startswith('# Prefix'): 
				data = elem.strip('/n').split('\t')[1:]
				print(data)						
		# for row in data:
		# 	print(row)
			# if line.startswith('# Prefix'): 
			# 	header =  line.strip('/n').split('\t')[1:]
			# elif "Preferred Title; symbol" in line:
			# 	title = line.strip().split(";")[0]
			# elif "Preferred Title; symbol" in line:
			# 	symbol = line.strip().split(";")[1]
			# 	print(symbol)

				#print(header)
				
				# data = list([header,colvalues])
				# data = dict(zip(colnames,colvalues))
				# print(data)




file = ('/Users/aginni/Documents/omim/omimTitles.txt')
omim = omimparser(file)