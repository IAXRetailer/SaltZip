from colorama import Fore,init
from . import time

init(autoreset=True)
cFore=Fore
def gettime():
    return time.gettime()
    
#print log
def infolog(msg,name):
    print(Fore.GREEN+f"[INFO | {name} | {gettime()}] "+Fore.WHITE+msg)

def warnlog(msg,name):
    print(Fore.YELLOW+f"[WARN | {name} | {gettime()}] "+Fore.YELLOW+msg)
    
def errorlog(msg,name):
    print(Fore.RED+f"[ERROR | {name} | {gettime()}] "+Fore.RED+msg)
    
def colorprint(msg,color):
    print(color+msg)
    
def colorinput(msg,color):
    print(color+msg,end="")
    return input()