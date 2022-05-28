完全修复了编码解码错误，目前解压缩不限目录

使用教程如下

前言
这几天电脑坏了，本来想录个视频也没来得及，所以匆忙写了这个教程


SaltZip是什么
我花了几个星期写的一个小软件，主要用于傻瓜式安全解压缩


对于解压者
1.从https://github.com/IAXRetailer/SaltZip/releases/latest下一个最新版本的saltzip.7z

2.解压saltzip.7z

3.下载使用saltzip压缩的资源（.hk和.zip都不能少，并且必须位于同一目录下）

4.运行saltzip内的解压（解密）.bat会出现弹窗

4.5.如果长时间cmd窗口没有出现saltzip字样或者没有跳出选择窗口，你应该重新启动这个程序，怎么样都没有用你应该去https://github.com/IAXRetailer/SaltZip/issues发布一个issue

5.用弹窗选择下载的.hk文件，等待解压

5.5.如果觉得计算xxhash太慢可以在.setting.txt，把CK_XXHASH的True改成False


对于压缩者
1-3步同上

4.根据需要运行压缩文件&压缩文件夹会有弹窗出现

4.5同上

5.选择你的文件/文件夹，等待

5.5.如果觉得计算xxhash太慢，可以把.setting.txt中的GEN_XXHASH的True改成False

6.签名，你可以写github.com也可以写你的id，总之写什么都可以，但中文并不推荐

7.将.hk和.zip一起分享

ex如果需要自定义解压码可以通过生成.hk.bat来操作

附录：视频演示
https://h2spublic.vercel.app/zh-CN/WaterMoon/saltzip%E6%95%99%E7%A8%8B.mp4
#############################################################
如果要运行更新，不要删除任何一个txt
如果要运行更新，不要删除任何一个txt
如果要运行更新，不要删除任何一个txt
如果要运行更新，不要删除任何一个txt

update.txt 存储本地代理端口
version.txt 存储版本号
github.txt 存储仓库信息API
