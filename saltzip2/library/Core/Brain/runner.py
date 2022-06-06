import systemwheel
from os.path import getsize
from library.Core.Hash import tool,des
from library.Core.Hash import xxhash as Ixxhash
from library.Core.Bitlayer import BitString
from library.LiteLog import logpr
from library.LiteLog import time as Itime
def enfile(filepath):
    outpath=filepath+".sip"
    password=tool.genrds(16)
    logpr.infolog("压缩密码为"+password,__name__)
    commandList=[]
    #"7z a -tzip \""+filepath+"\" -p"+password+" \""+outpath+"\"\n"
    commandList.append("7z a -tzip \""+outpath+"\" -p"+password+" \""+filepath+"\"\n")
    systemwheel.systemrunner(commandList)
    xxhash=Ixxhash.getfilehash(outpath,655650,getsize(outpath))
    logpr.infolog("XXHASH值为"+xxhash,__name__)
    key,iv=tool.genrds(8),tool.genrds(8)
    logpr.infolog("秘文秘钥 | 向量 :"+key+" "+iv,__name__)
    enpassword=des.getStringhash(password,key,iv)
    writecon=enpassword+key+xxhash+iv#16 8 16 8
    logpr.infolog(enpassword,__name__)
    WTN=logpr.colorinput("签名：",logpr.Fore.LIGHTYELLOW_EX)
    DATE=Itime.getdate()
    hkpath=filepath+"."+str(len(WTN))+".h2k"
    writecon=writecon+WTN+DATE
    BitString.writetobin(hkpath,writecon)
    logpr.infolog(BitString.readrbtostring(hkpath,32+16+8+8+10+len(WTN)),__name__)
    return

def enfolder():
    
    return