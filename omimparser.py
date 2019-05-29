# import urllib.request
# print("Beginning file download with urllib...")
# url = 'https://data.omim.org/downloads/1r6-54cxR_inA4Zf_bzd0w/mimTitles.txt'
# urllib.request.urlretrieve(url, '/Users/aginni/Documents/omim/omimTitles.txt')   
															## importing files from OMIM web browser using urllib.request module
# print("Beginning file download with urllib...")
# url = 'https://data.omim.org/downloads/1r6-54cxR_inA4Zf_bzd0w/genemap2.txt'
# urllib.request.urlretrieve(url,'/Users/aginni/Documents/omim/omimgenemap2.txt')

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


omimdata= []	
		
def omimparser(self):
	self.omimkey = ["Mim Number","Preferred Title","symbol","Alternative Title(s)","symbol(s)","Included Title(s)","symbols"]
	self.omimvals = {key:None for key in self.omimkey}

	with open(file,'r') as mim:
		for line in mim.readlines().split(','):
			print(line)
			for i,colnames in enumerate(self.omimkey):
				omimvals[omimkey] = omimkey[i]
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


file = ('/Users/aginni/Documents/omim/omimTitles.txt')
omim = omimparser(file)
