from library.LiteLog import logpr
from library.Core.Brain import runner,choser



def chose(mode,modelist):
    try:
        logpr.infolog(f"输入了{mode}",__name__)
        mode=int(mode)
        if mode == 0:
            logpr.infolog("正在退出程序",__name__)
            return "EXIT"
        if mode == 2:
            return True
        if mode not in modelist:
            logpr.warnlog("不存在的模式",__name__)
            return False
    except:
        logpr.warnlog("对象不是一个数字",__name__)
        return False

def c2c(mode,modelist):
    try:
        logpr.infolog(f"输入了{mode}",__name__)
        mode=int(mode)
        if mode in modelist:
            return mode
        else:
            logpr.warnlog("不存在的模式",__name__)
            return False
    except:
        logpr.warnlog("对象不是一个数字",__name__)
        return False