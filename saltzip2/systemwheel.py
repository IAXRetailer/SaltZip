from os import system
from library.LiteLog import logpr
def systemrunner(systemList):
    for i in systemList:
        logpr.infolog(i,__name__)
        system(i)