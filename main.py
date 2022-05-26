class zipio:
    	#unzip
	def unzip(self,hkfilepath,password):
		here=tool().osgetlocation()
		target=hkfilepath.replace(".hk",".zip")
		#print(target)
		#tool().ospause()
		Alist=target.split("/")
		Alist.pop(-1)
		targetfolder=""
		for i in Alist:
			targetfolder=targetfolder+i+"/"
		clist=[]
		clist.append("chcp 65001\n")
		clist.append("7z x \""+target+"\" -o\""+targetfolder+"\" -p"+password)
		#a="7z x \""+target+"\" -o\""+here+"\" -p"+password
		#print(a)
		#clist.append("cd \""+here+"\"\n")
		clist.append("chcp 936")
		import os
		for c in clist:
			os.system(c)
	#enzip
	def enfoldzip(self,file,password):
		here=tool().osgetlocation()
		filename=file.split("\\")[-1]

		clist=[]
		command="chcp 65001\n"
		clist.append(command)
		#command="cd 7-Zip\n"
		clist.append(command)
		#7z.exe a -tzip -r myfile.zip test -p123
		command="7z a -tzip -r \""+file+".zip\" \""+file+"\" -p"+password
		clist.append(command)
		#command="cd \""+here+"\"\n"
	
		clist.append("chcp 936")
		import os
		for c in clist:
			os.system(c)
		tpath=file+".zip"
		return tpath
	def enzip(self,file,password):
		here=tool().osgetlocation()
		#7z a -tzip archive.zip -pbuildforge 0076\
		filename=file.split("\\")[-1]
		target=filename+".zip"
		clist=[]
		command="chcp 65001\n"
		clist.append(command)
		#command="cd 7-Zip\n"
		clist.append(command)
		command="7z a -tzip \""+target+"\" -p"+password+" \""+file+"\"\n"
		clist.append(command)
		#command="cd \""+here+"\"\n"
		clist.append("chcp 936")
		import os
		for c in clist:
			os.system(c)
		return target

class hashio:
	#import pyDes
	#import base64
	#get the xxhash of the file
	def b64d(self,obj):
		import base64
		return base64.b64decode(obj).decode("utf-8","ignore")
	def getfilehash(self,file,blocksize,size):
		import xxhash
		print("获取xxhash中，请耐心等待，觉得过慢请在.setting.txt关闭相应功能")
		hasher=xxhash.xxh64()
		blocksize=int(blocksize)
		size2=int(size)
		with open(file,"rb") as f:
			while True:
				size2-=65565
				process=str(round(((size-size2)/size)*100,4))+"%"+" 计算中xxhash中，剩余"+str(size2)
				print("\r"+process,end="")
				buf=f.read(blocksize)
				if not buf:
					print("\nOver")
					break
				hasher.update(buf)
		print("xxhash",hasher.hexdigest())
		return hasher.hexdigest()
	#hash my string
	def getStringhash(self,string,key,iv):
		import pyDes
		import base64
		try:
			#observe
			#dev
			#print(key,iv)
			string.encode('utf-8')
		except:
			print("Encode Failed,please make an issue.")
			tool().ospause()
			exit()
		
		des=pyDes.des(key,pyDes.ECB,iv,pad=None,padmode=pyDes.PAD_PKCS5)
		
		res=des.encrypt(string)

		return str(base64.b64encode(res).decode("utf-8"))
	
	#decode
	def decodeStringhash(self,string,key,iv):
		#dev
		#observe
		import pyDes,base64
		string=base64.b64decode(string)
		des=pyDes.des(key,pyDes.ECB,iv,pad=None,padmode=pyDes.PAD_PKCS5)
		res=des.decrypt(string)
		return res.decode('utf-8')
		
	
	def genspcode(self,desres,key,iv,xxhashcode,releaser,time):
		#may crash by string(TypeError)
		import base64
		chuck1=str(desres)
		chuck2=key+"/!"+iv
		chuck3=xxhashcode+"/!"+releaser+"/!"+time
		
		chuck2=str(base64.b64encode(chuck2.encode("utf-8")).decode('utf-8'))
		chuck3=str(base64.b64encode(chuck3.encode("utf-8")).decode('utf-8'))
		
		code="saltzip://"+chuck1+"|"+chuck2+"|"+chuck3
		return code

class tool:
	def getfilesize(self,target):
		import os
		return os.path.getsize(target)

	def getsetting(self):
		target=tool().osgetlocation()+"\.setting.txt"
		f=open(target,"r").read().splitlines()
		tglist=[]
		for i in f:
			if list(i)[0] != "#":
				tglist.append(i)
		return tglist
	def chosefile(self,obj):
		import tkinter as tk
		from tkinter import filedialog
		root = tk.Tk()
		root.withdraw()
		if obj == "file":
			Filepath = filedialog.askopenfilename(title="Select file") #获得选择好的文件
			return Filepath
		elif obj=="folder":
			Folderpath = filedialog.askdirectory(title="Select folder") #获得选择好的文件夹
			return Folderpath
		if obj == "hk":
			root = tk.Tk()
			root.withdraw()
			Filepath = filedialog.askopenfilename(title="Select hash key", filetypes=(("Hash key", "*.hk"),)) #获得选择好的文件
			return Filepath
		if obj == "zip":
			root = tk.Tk()
			root.withdraw()
			Filepath = filedialog.askopenfilename(title="Select hash key", filetypes=(("File(zip)", "*.zip"),)) #获得选择好的文件
			return Filepath
	def ospopen(self,command):
		import os
		os.popen(command)
	def ossys(self,command):
		import os
		os.system(command)
	#cmd pause
	def ospause(self):
		import os
		os.system("pause")
	
	def osmkdir(self,name):
		import os
		os.mkdir(name)
	
	#get file location
	def osgetlocation(self):
		import os
		return os.getcwd()
	
	#make file
	def mkfile(self,path,msg):
		msg=str(msg)
		with open(path,"w") as f:
			f.write(msg)
	
	def mkfilerb(self,path,msg):
		with open(path,"r") as f:
			f.write(msg)
	
	def checkfile(self,file):
		import os
		return os.path.isfile(file)
	
	#16bitconv
	#dev
	def ivconv(self,string):
		stringlist=list(string)
		result=""
		for i in stringlist:
			i.encode('utf-8').hex()
			result=result+r"\x"+str(i)
			#print(result)
		return result
	#Generate a string[length]
	def genrds(self,length):
		import random
		import string
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
		#print(res)
		return res
	
	#generate an iv
	def geniv(self,length):
		return tool().ivconv(tool().genrds(length))
'''	
class imgio:
	import cv2
	#TODO generate a QRcode copy and parse it
	#pip install opencv-python
	def genqrc(self,msg):
		return
	#parse the image
	def parseimg(self,imgfile):
		imgobj=cv2.imread(imgfile)
		parse=cv2.QRCodeDetector()
		return parse.detectAndDecode(imgobj)[0]
'''
class modeio:
	def chose(self,mode):
		modelist=[0,1,2,3]
		try:
			int(mode)
		except:
			while type(int(mode)) != type(0):
				print("请输入正确的数字")
				mode=input("chose mode->")
		while int(mode) not in modelist:
			print("Unknown mode")
			mode=input("chose mode->")
   
		if int(mode) == 1:
			filepath=tool().chosefile("file")
			print(filepath)
			password=tool().genrds(16)
			print("password",password)
			tool().mkfile("recode.txt", password)
			target=zipio().enzip(filepath, password)
			for i in tool().getsetting():
				if "GEN_XXHASH=" in i:
					CK=i.replace("GEN_XXHASH=", "")
			if CK != "True":
				print("Pass the xxhash GEN")
				xxhash="0000000000000000"
			else:
				xxhash=hashio().getfilehash(target, 65565,tool().getfilesize(target))
			key=tool().genrds(8)
			print("key",key)
			iv=tool().genrds(8)
			print("iv",iv)
			descode=hashio().getStringhash(password, key, iv)
			releaser=input("请签名:")
			if releaser == "":
				releaser = "None"
			import datetime
			date = datetime.date.today()
			time = date.strftime("%Y-%m-%d")
			code=hashio().genspcode(descode, key, iv, xxhash, releaser, time)
			print(code)
			hkname=filepath+".hk"
			tool().mkfile(hkname, code)
   
		if int(mode) == 2:
			filepath=tool().chosefile("hk")
			key=open(filepath,"r").read()
			chucklist=key.split("|")
			#print(chucklist)
			chuck1,chuck2,chuck3=chucklist[0],chucklist[1],chucklist[2]
			chuck1=chuck1.replace("saltzip://", "")
			#print(chuck1,chuck2,chuck3)
			import base64
			#tool().ospause()
			tc2=hashio().b64d(chuck2)
			tc3=hashio().b64d(chuck3)
			#print(tc2,tc3)
			try:
				xxhash=tc3.split("/!")[0]
				releaser=tc3.split("/!")[1]
				releasetime=tc3.split("/!")[2]
			except:
				xxhash=tc3.split("/!")[0]
				releaser=tc3.split("/!")[1]
				releasetime="Chuck3 Broken"
			print("##########################################")
			print("以下为文件信息（INFORMATION）")
			print("文件识别码(xxhash64)",xxhash)
			print("发布者",releaser)
			print("发布时间",releasetime)
			print("##########################################")
			import time
			print("3秒后开始解压")
			time.sleep(3)
			#print(tc2)
			target=filepath.replace(".hk",".zip")
			key=tc2.split("/!")[0]
			iv=tc2.split("/!")[1]
			print(key,iv)
			code=hashio().decodeStringhash(chuck1, key, iv)
			file=open("code.txt","w")
			file.write(code)
			file.close()
			for i in tool().getsetting():
				if "CK_XXHASH=" in i:
					CK=i.replace("CK_XXHASH=", "")
			if CK != "True" or xxhash=="0000000000000000":
				print("Pass the xxhash check")
			elif hashio().getfilehash(target, 65565,tool().getfilesize(target)) != xxhash:
					print("xxhash值不同，文件可能损坏，是否继续运行")
					tool().ospause()
			zipio().unzip(filepath, code)
   
		if int(mode) == 0:
			filepath=tool().chosefile("folder")
			print(filepath)
			password=tool().genrds(16)
			print("password",password)
			tool().mkfile("recode.txt", password)
			target=zipio().enfoldzip(filepath, password)
			for i in tool().getsetting():
				if "GEN_XXHASH=" in i:
					CK=i.replace("GEN_XXHASH=", "")
			if CK != "True":
				print("Pass the xxhash GEN")
				xxhash="0000000000000000"
			else:
				xxhash=hashio().getfilehash(target, 65565,tool().getfilesize(target))
			key=tool().genrds(8)
			print("key",key)
			iv=tool().genrds(8)
			print("iv",iv)
			descode=hashio().getStringhash(password, key, iv)
			releaser=input("请签名:")
			if releaser == "":
				releaser = "None"
			import datetime
			date = datetime.date.today()
			time = date.strftime("%Y-%m-%d")
			code=hashio().genspcode(descode, key, iv, xxhash, releaser, time)
			print(code)
			hkname=filepath+".hk"
			tool().mkfile(hkname, code)
		if int(mode) == 3:
			print("选择目标文件")
			filepath=tool().chosefile("zip")
			code=input("输入解压码->")
			target=filepath
			for i in tool().getsetting():
				if "GEN_XXHASH=" in i:
					CK=i.replace("GEN_XXHASH=", "")
			if CK != "True":
				print("Pass the xxhash GEN")
				xxhash="0000000000000000"
			else:
				xxhash=hashio().getfilehash(target, 65565,tool().getfilesize(target))
			key=tool().genrds(8)
			print("key",key)
			iv=tool().genrds(8)
			print("iv",iv)
			descode=hashio().getStringhash(code, key, iv)
			releaser=input("请签名:")
			if releaser == "":
				releaser = "None"
			import datetime
			date = datetime.date.today()
			time = date.strftime("%Y-%m-%d")
			code=hashio().genspcode(descode, key, iv, xxhash, releaser, time)
			print(code)
			hkname=filepath.replace(".zip",".hk")
			tool().mkfile(hkname, code)
if __name__ == '__main__':
	#object
	#zipio=zipio()
	#tool=tool()
	modeio=modeio()
	
	#main
	#print("welcom to saltzip control platform!")
	title='''

      ___           ___           ___                     ___                                
     /  /\         /  /\         /  /\      ___          /__/\           ___         ___     
    /  /::\       /  /::\       /  /:/     /__/\         \  \:\         /__/\       /  /\    
   /__/:/\:\     /  /:/\:\     /  /:/      \  \:\         \  \:\        \__\:\     /  /::\   
  _\_ \:\ \:\   /  /::\ \:\   /  /:/        \__\:\         \  \:\       /  /::\   /  /:/\:\  
 /__/\ \:\ \:\ /__/:/\:\_\:\ /__/:/         /  /::\   ______\__\:\   __/  /:/\/  /  /::\ \:\ 
 \  \:\ \:\_\/ \__\/  \:\/:/ \  \:\        /  /:/\:\ \  \::::::::/  /__/\/:/    /__/:/\:\_\:/
  \  \:\_\:\        \__\::/   \  \:\      /  /:/__\/  \  \:\~~~~~   \  \::/     \__\/  \:\/:/
   \  \:\/:/        /  /:/     \  \:\    /__/:/        \  \:\        \  \:\          \  \::/ 
    \  \::/        /__/:/       \  \:\   \__\/          \  \:\        \__\/           \__\/  
     \__\/         \__\/         \__\/                   \__\/                               

[0]Mode 0 压缩文件夹加密生成秘钥
[1]Mode 1 压缩文件并加密生成秘钥
[2]Mode 2 输入秘钥并解密解压文件
[3]Mode 3 根据解压码生成秘钥分发
 
	'''
	print(title)
	import sys
	argvs=sys.argv
	if len(argvs) == 1:
		mode=input("chose mode now->")
	else:
		mode=argvs[1]
	modeio.chose(mode)