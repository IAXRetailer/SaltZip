from library.LiteLog import logpr
from library.Core.Brain import bridge,runner
from library.UI.File import filechose
from prcon import *
def c1cer():
    logpr.colorprint(m1c,logpr.Fore.LIGHTGREEN_EX)
    m0cres=False
    while m0cres == False:
        m0c=logpr.colorinput("选择(输入数字)",logpr.Fore.LIGHTGREEN_EX)
        m0cres=bridge.c2c(m0c,m1clist)
        if m0cres == 0:
            return
        
    if m0cres == 1:
        filepath=""
        while filepath == "":
            logpr.infolog("请选择.hk文件",__name__)
            filepath=filechose.chosefile("hk")
            if filepath == "":
                logpr.warnlog("不可输入空路径",__name__)
            else:
                logpr.infolog("选择了 "+filepath,__name__)
        runner.unsip(filepath,"hk")

    if m0cres == 2:
        filepath=""
        while filepath == "":
            filepath=filechose.chosefile("h2k")
            if filepath == "":
                logpr.warnlog("不可输入空路径",__name__)
            else:
                logpr.infolog(filepath,__name__)
        runner.unsip(filepath,"h2k")

def c2cer():
    logpr.colorprint(m2c,logpr.Fore.LIGHTGREEN_EX)
    m0cres=False
    while m0cres == False:
        m0c=logpr.colorinput("选择(输入数字)",logpr.Fore.LIGHTGREEN_EX)
        m0cres=bridge.c2c(m0c,m2clist)
        if m0cres == 0:
            return
        
    if m0cres == 1:
        filepath=""
        while filepath == "":
            filepath=filechose.chosefile("file")
            if filepath == "":
                logpr.warnlog("不可输入空路径",__name__)
            else:
                logpr.infolog(filepath,__name__)
        runner.enfile(filepath)
    if m0cres == 2:
        filepath=""
        while filepath == "":
            filepath=filechose.chosefile("folder")
            if filepath == "":
                logpr.warnlog("不可输入空路径",__name__)
            else:
                logpr.infolog(filepath,__name__)
        runner.enfolder(filepath)