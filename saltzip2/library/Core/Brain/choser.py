from library.LiteLog import logpr
from library.Core.Brain import bridge,runner
from library.UI.File import filechose
from prcon import *
def c2cer():
    logpr.colorprint(m2c,logpr.Fore.LIGHTGREEN_EX)
    m0cres=False
    while m0cres == False:
        m0c=logpr.colorinput("选择(输入数字)",logpr.Fore.LIGHTGREEN_EX)
        m0cres=bridge.c2c(m0c,m2c)
    if m0cres == 1:
        filepath=""
        while filepath == "":
            filepath=filechose.chosefile("file")
            if filepath == "":
                logpr.warnlog("不可输入空路径",__name__)
            else:
                logpr.infolog(filepath,__name__)
        runner.enfile(filepath)