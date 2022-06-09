from os import path
from os import rename,remove
def rbr(filepath,block_size):
    f=open(filepath,"rb")
    key=f.read(block_size)
    other=f.read(path.getsize(filepath)-block_size)
    return key,other

def rbw(filepath,con):
    with open(filepath,"wb") as f:
        f.write(con)
        
def splitHK(hkblocksize):
    return

def contectHK(hkpath,sippath):
    asize=path.getsize(hkpath)
    hk=open(hkpath,"rb")
    con=hk.read()
    hk.close()
    with open(sippath,"ab") as f:
        f.write(con)
    remove(hkpath)
    sipxpath=sippath.replace("sip",str(asize)+".sipx")
    rename(sippath,sipxpath)
def reverseHK(sippath,hkpath):
    asize=path.getsize(sippath)
    sip=open(sippath,"rb")
    con=sip.read()
    sip.close()
    with open(hkpath,"ab") as f:
        f.write(con)
    remove(sippath)
    sipxpath=sippath.replace("sip",str(asize)+".sipx")
    rename(hkpath,sipxpath)

contectHK("F:\\rpcpost\\test\\新建文件夹\\新建文件夹\\1\\1.2.h2k","F:\\rpcpost\\test\\新建文件夹\\新建文件夹\\1\\1.sip")