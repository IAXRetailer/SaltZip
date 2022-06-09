from json import loads
modechose='''

1.解压

2.压缩

3.生成秘钥

0.退出程序

'''

m1c='''

1.解压（hk格式）

2.解压（h2k格式）

0.返回

'''
m1c1='''

1.sip压缩格式解压

2.zip压缩压缩格式解压

0.返回

'''

m2c='''

1.压缩文件

2.压缩文件夹

0.返回

'''

modelist=[0,1,2,3]
m1clist=[0,1,2]
m2clist=[0,1,2]
setting=loads(open("setting.json","r").read())
