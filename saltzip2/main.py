import library.LiteLog as myLog
import library.Core as myCore
from prcon import *
while True:
    myLog.logpr.infolog("SaltZip START SUCCESSFULLY!",__name__)
    myLog.logpr.infolog("初始化中请稍后...",__name__)
    myLog.logpr.colorprint(modechose,myLog.logpr.Fore.LIGHTGREEN_EX)
    m0cres=False
    while m0cres == False:
        m0c=myLog.logpr.colorinput("选择(输入数字)",myLog.logpr.Fore.LIGHTGREEN_EX)
        m0cres=myCore.Brain.chosemode(m0c,modelist)
    if m0cres == "EXIT":
        exit(0)
    if m0c =="1":
        myCore.Brain.choser.c1cer()
    if m0c =="2":
        myCore.Brain.choser.c2cer()
        