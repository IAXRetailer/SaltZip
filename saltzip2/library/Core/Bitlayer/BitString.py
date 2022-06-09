import struct
def writetobin(binPath,string):
    slist=list(string)
    data = struct.pack(f"i",ord(slist[0]))
    with open(binPath, 'w+b') as f:
        f.write(data)
    slist.pop(0)
    for i in slist:
        data=struct.pack(f"i",ord(i))
        with open(binPath, 'a+b') as f:
            f.write(data)

def readrbtostring(filepath,lenstr):
    rbcon=open(filepath,"rb").read()
    data=str(lenstr)+"i"
    ms=struct.unpack(data,rbcon)
    res=""
    for i in ms:
        res=res+chr(i)
    return res