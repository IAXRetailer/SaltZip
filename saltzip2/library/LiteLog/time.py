import time
def getdate():
	return time.strftime("%Y-%m-%d", time.localtime())
def gettime():
	return time.strftime("%H:%M:%S", time.localtime())