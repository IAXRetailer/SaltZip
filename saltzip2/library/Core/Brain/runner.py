from os.path import getsize,exists,dirname
from library.Core.Hash import tool,des
from library.Core.Hash import xxhash as Ixxhash
from library.Core.Bitlayer import BitString
from library.LiteLog import logpr
from library.LiteLog import time as Itime
from library.Core.Brain import bridge
from prcon import *
import systemwheel

def enfile(filepath):
    outpath=filepath+".sip"
    password=tool.genrds(16)
    logpr.infolog("压缩密码为"+password,__name__)
    commandList=[]
    #"7z a -tzip \""+filepath+"\" -p"+password+" \""+outpath+"\"\n"
    commandList.append("7z a -tzip \""+outpath+"\" -p"+password+" \""+filepath+"\"\n")
    systemwheel.systemrunner(commandList)
    if setting["GENxxhash"] == "True":
        xxhash=Ixxhash.getfilehash(outpath,65565,getsize(outpath))
        logpr.infolog("XXHASH值为"+xxhash,__name__)
    else:
        xxhash="0000000000000000"
        logpr.infolog("已跳过xxhash生成",__name__)
    key,iv=tool.genrds(8),tool.genrds(8)
    logpr.infolog("秘文秘钥 | 向量 :"+key+" "+iv,__name__)
    enpassword=des.getStringhash(password,key,iv)
    writecon=enpassword+key+xxhash+iv#16 8 16 8
    logpr.infolog(enpassword,__name__)
    WTN=logpr.colorinput("签名：",logpr.Fore.LIGHTYELLOW_EX)
    if WTN == "":
        WTN="NONE"
    DATE=Itime.getdate()
    hkpath=filepath+"."+str(len(WTN))+".h2k"
    writecon=writecon+WTN+DATE
    BitString.writetobin(hkpath,writecon)
    #logpr.infolog(BitString.readrbtostring(hkpath,32+16+8+8+10+len(WTN)),__name__)

def enfolder(filepath):
    #"7z a -tzip -r \""+file+".zip\" \""+file+"\" -p"+password
    outpath=filepath+".sip"
    password=tool.genrds(16)
    logpr.infolog("压缩密码为"+password,__name__)
    commandList=[]
    #"7z a -tzip \""+filepath+"\" -p"+password+" \""+outpath+"\"\n"
    commandList.append("7z a -tzip -r \""+outpath+"\" -p"+password+" \""+filepath+"\"\n")
    systemwheel.systemrunner(commandList)
    if setting["GENxxhash"] == "True":
        xxhash=Ixxhash.getfilehash(outpath,65565,getsize(outpath))
        logpr.infolog("XXHASH值为"+xxhash,__name__)
    else:
        xxhash="0000000000000000"
        logpr.infolog("已跳过xxhash生成",__name__)
    key,iv=tool.genrds(8),tool.genrds(8)
    logpr.infolog("秘文秘钥 | 向量 :"+key+" "+iv,__name__)
    enpassword=des.getStringhash(password,key,iv)
    writecon=enpassword+key+xxhash+iv#32 8 16 8
    logpr.infolog(enpassword,__name__)
    WTN=logpr.colorinput("签名：",logpr.Fore.LIGHTYELLOW_EX)
    if WTN == "":
        WTN="NONE"
    DATE=Itime.getdate()
    hkpath=filepath+"."+str(len(WTN))+".h2k"
    writecon=writecon+WTN+DATE
    BitString.writetobin(hkpath,writecon)


def unsip(filepath,mode):
    #"7z x \""+target+"\" -o\""+here+"\" -p"+password
    if mode == "hk":
        c2cres=False
        while c2cres == False:
            logpr.colorprint(m1c1,logpr.Fore.LIGHTGREEN_EX)
            chose=logpr.colorinput("选择(输入数字)",logpr.Fore.LIGHTGREEN_EX)
            if chose == "0":
                return
            c2cres=bridge.c2c(chose,[0,1,2])
        if c2cres == 1:
            pres="sip"
        else:
            pres="zip"
        unfilepath=filepath.replace("hk",pres)
        if not exists(unfilepath):
            logpr.warnlog(unfilepath+" 不存在，是否回车继续",__name__)
            input()
        logpr.infolog("Pick up "+filepath,__name__)
        hkcon=open(filepath,"r",encoding="utf-8").read()
        hkcon=hkcon.replace("saltzip://","")
        infolist=hkcon.split("|")
        chuck1,chuck2,chuck3=infolist[0],infolist[1],infolist[2]
        chuck3=des.b64d(chuck3).split("/!")
        chuck2=des.b64d(chuck2).split("/!")
        xxhash,name,date=chuck3[0],chuck3[1],chuck3[2]
        logpr.infolog("发布者为"+name,__name__)
        logpr.infolog("发布日期为"+date,__name__)
        logpr.infolog("文件特征码(xxhash)为"+xxhash,__name__)
        key,iv=chuck2[0],chuck2[1]
        password=des.decodeStringhash(chuck1,key,iv)
        logpr.infolog("密码为"+password,__name__)
        ##"7z x \""+target+"\" -o\""+here+"\" -p"+password
        dictory=dirname(filepath)
        commandlist=[]
        commandlist.append("7z x \""+unfilepath+"\" -o\""+dictory+"\" -p"+password)
        if setting["VERxxhash"] =="True":
            if Ixxhash.getfilehash(unfilepath,65565,getsize(unfilepath)) != xxhash and xxhash != "0000000000000000":
                logpr.warnlog("XXHASH不同，文件可能损坏，是否继续",__name__)
                input()
        else:
            logpr.infolog("已经跳过xxhash验证",__name__)
        systemwheel.systemrunner(commandlist)
    elif mode == "h2k":
        lenstr=filepath.replace(".h2k","").split(".")[-1]
        res=BitString.readrbtostring(filepath,int(lenstr)+64+10)
        password=des.decodeStringhash(res[:32],res[32:40],res[40:48])
        xxhash=res[48:64]
        name=res[64:64+int(lenstr)]
        date=res[64+int(lenstr):]
        logpr.infolog("发布者为"+name,__name__)
        logpr.infolog("发布日期为"+date,__name__)
        logpr.infolog("文件特征码(xxhash)为"+xxhash,__name__)
        logpr.infolog("密码为"+password,__name__)
        dictory=dirname(filepath)
        unfilepath=filepath.replace(lenstr+".h2k","sip")
        if not exists(unfilepath):
            logpr.warnlog(unfilepath+" 不存在，是否回车继续",__name__)
            input()
        commandlist=[]
        commandlist.append("7z x \""+unfilepath+"\" -o\""+dictory+"\" -p"+password)
        if setting["VERxxhash"] =="True":
            selfhash=Ixxhash.getfilehash(unfilepath,65565,getsize(unfilepath))
            if selfhash != xxhash and xxhash != "0000000000000000":
                logpr.warnlog("XXHASH不同，文件可能损坏，是否继续",__name__)
                input()
        else:
            logpr.infolog("已经跳过xxhash验证",__name__)
        systemwheel.systemrunner(commandlist)