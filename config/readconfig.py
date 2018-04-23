#import configparser
# config=configparser.ConfigParser()
# config.read("config.ini")
# try:
#     config.add_section("test_db")
#     config.set("test_db","ip","50.23.190.57")
#     config.set("test_db","port","3306")
#     config.set("test_db","username","pretestadmin")
#     #config.set("test_db","password","AyGr%DHUmp")
# except configparser.DuplicateOptionError:
#     print("config is already exists")
# config.write(open("config.ini","w"))
#
# x=config.get("test_db","port")
# print(x)

# import configparser
# import os
# nowfile=os.path.realpath(__file__)                    #当前文件路径  值为：D:\apitest\readconfig.py
# nowfile1=os.path.split(nowfile)[0]                    #取当前文件路径的前面 D:\apitest\
# configpath=os.path.join(nowfile1,"config.ini")     #拼接D:\apitest 和 ipconfig.ini 得出ipconfig.ini的路径
# class Getconfigvalue():
#     def __init__(self):
#         self.config=configparser.ConfigParser()
#         self.config.read(configpath)                   #读取配置文件
#         self.conf={'host':'','port':'','username':'','password':''}
#     def get_conf(self,name):
#         self.conf['host']=self.config.get("test_db",'host')
#         self.conf['port']=self.config.get("test_db",'port')
#         self.conf['username']=self.config.get("test_db",'username')
#         self.conf['password']=self.config.get("test_db",'password')
#         self.conf['host1']=self.config.get("hosts",'host1')
#         print(self.conf)
#         return self.conf
# if __name__=="__main__":
#     Getconfigvalue()

#

#得到指定section的所有值
import configparser
import os
nowpath=os.path.realpath(__file__)
path1=os.path.split(nowpath)[0]
confpath=os.path.join(path1,"config.ini")
def getconfvalue(section):
    value=[]
    config=configparser.ConfigParser()
    config.read(confpath)
    key=config.items(section)
    for i in key:
        value.append(i[1])
    return value