import random
import string
def genrds(length):
	resultlist=[]
	sample=[]
	for i in string.ascii_uppercase:
		sample.append(i)
	for i in string.digits:
		sample.append(i)
	while len(resultlist) < length:
		resultlist.append(random.choice(sample))
	for i in resultlist:
		try:
			res=res+i 
		except:
			res=i 
	return res