from colorama import Fore,init
from json import loads
from requests import get
from os import system,listdir,mkdir
from shutil import rmtree

init(autoreset=True)
port=open("update.txt","r",encoding="utf-8").read()
if port == "None":
    proxies=None
    print(Fore.YELLOW+"检测到没有设置代理端口，可能导致失败，update.txt中填入[127.0.0.1:*本地代理端口*]即可启用代理")
else:
    proxies = { "http": "http"+port, "https": "https"+port, }
    print(Fore.GREEN+"HTTP  Pick up "+proxies["http"])
    print(Fore.GREEN+"HTTPS Pick up "+proxies["https"])
url=open("github.txt","r",encoding="utf-8").read()
tag=open("version.txt","r",encoding="utf-8").read()
r = get(url,proxies=proxies)
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
if chose == "y":
    
    for i in c['assets']:
        if "browser_download_url" in i:
            url=i["browser_download_url"]
            Fname=url.split("/")[-1]
            print(Fore.LIGHTGREEN_EX+"下载中，请耐心等待...")
            if "update" not in listdir():
                mkdir("update")
            with open("./update/"+Fname,"wb") as f:
                f.write(get(url,proxies=proxies).content)
            print(Fore.LIGHTGREEN_EX+"请输入'Y'替换文件")
            system("7z x "+"\"./update/"+Fname+"\"")
            rmtree("update")
            f=open('version.txt','w',encoding='utf-8')
            f.write(t)
            f.close()
            print(Fore.LIGHTGREEN_EX+"更新完毕")
            system("pause")
else:       
    print(Fore.RED+"已取消")
    system("pause")