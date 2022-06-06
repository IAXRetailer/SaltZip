import pyDes
import base64
def getStringhash(string,key,iv):
	des=pyDes.des(key,pyDes.ECB,iv,pad=None,padmode=pyDes.PAD_PKCS5)
	res=des.encrypt(string.encode('utf-8'))
	return str(base64.b64encode(res).decode("utf-8"))

def decodeStringhash(string,key,iv):
	import pyDes,base64
	string=base64.b64decode(string)
	des=pyDes.des(key,pyDes.ECB,iv,pad=None,padmode=pyDes.PAD_PKCS5)
	res=des.decrypt(string)
	return res.decode('utf-8')

def b64d(obj):
	return base64.b64decode(obj).decode("utf-8")

def b64e(obj):
    return base64.b64encode(obj.encode("utf-8")).decode('utf-8')