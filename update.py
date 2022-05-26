from colorama import Fore,init
from json import loads
from requests import get
from requests import packages
from os import system,listdir,mkdir
from shutil import rmtree

port=open("update.txt","r",encoding="utf-8").read()
proxies = { "http": port, "https": port, } 
init(autoreset=True)
packages.urllib3.disable_warnings()
url=open("github.txt","r",encoding="utf-8").read()
tag=open("version.txt","r",encoding="utf-8").read()
r = get(url,verify=False,proxies=proxies)
c =loads(r.text)
t =c["tag_name"]
print(Fore.GREEN+"当前版本号"+Fore.LIGHTGREEN_EX+tag)
print(Fore.GREEN+"最新版本号"+Fore.LIGHTRED_EX+t)
if t != tag:
    print("##################")
    print(Fore.LIGHTGREEN_EX+"#更新内容#")
    print(Fore.LIGHTGREEN_EX+c["body"])
    print("##################")
    print(Fore.GREEN+"是否更新至"+Fore.LIGHTRED_EX+t)
    chose=input("(y/n)--->")
else:
    print(Fore.LIGHTGREEN_EX+"已是最新版本")
    system("pause")
    exit()
if chose == "y":
    for i in c['assets']:
        if "browser_download_url" in i:
            url=i["browser_download_url"]
            Fname=url.split("/")[-1]
            print(Fore.LIGHTGREEN_EX+"下载中，请耐心等待...")
            if "update" not in listdir():
                mkdir("update")
            #a=open("./update/"+Fname,"w")
            #a.close()
            #print(get(url,verify=False).status_code)
            #print("./update/"+Fname)
            with open("./update/"+Fname,"wb") as f:
                f.write(get(url,verify=False,proxies=proxies).content)
            print(Fore.LIGHTGREEN_EX+"请输入'Y'替换文件")
            system("7z x "+"\"./update/"+Fname+"\"")
            rmtree("update")
            print(Fore.LIGHTGREEN_EX+"更新完毕")
else:       
    print(Fore.RED+"已取消")
    system("pause")
    exit()