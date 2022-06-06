from xxhash import xxh64
def getfilehash(file,blocksize,size):
	#print("获取xxhash中，请耐心等待，觉得过慢请在.setting.txt关闭相应功能")
	hasher=xxh64()
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
	return hasher.hexdigest()