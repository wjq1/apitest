# import os
# import xlrd
# def getcase(xls_name,sheet_name):
#     cls=[]
#     nowpath=os.path.realpath(__file__)    #当前文件路径  D:\apitest\common\common.py
#     path1=os.path.split(nowpath)[0]       #当前文件路径的前面  D:\apitest\common
#     path2=os.path.split(path1)[0]         #上行路径的前面   D:\apitest\
#     xlspath=os.path.join(path2,xls_name)  #得出xls文件的路径 D:\apitest\testcase.xlsx
#     file=xlrd.open_workbook(xlspath)       #open xls file
#     sheet=file.sheet_by_name("login")     #get sheet by name
#     nrows=sheet.nrows                      #get one sheet's rows 行数
#     for i in range(nrows):
#         cls.append(sheet.row_values(i))
#     print(cls[1][2])
#     return cls


import smtplib
import email.mime.multipart
import email.mime.text
import email.header
import config.readconfig
def send_mail(smtp_server,port,sender,psw,receiver):
    msg=email.mime.multipart.MIMEMultipart()
    msg['Subject']='report'
    msg["From"]=sender
    msg['To']=receiver
    content='''
    Dear all:
            附件是自动化报告，请查收！'''
    msg.attach(email.mime.text.MIMEText(content,'plain','utf-8'))
    smtp=smtplib.SMTP()
    smtp.connect(smtp_server,port)
    print("1")
    smtp.login(sender,psw)
    print("11")
    smtp.sendmail(sender,receiver,msg.as_string())
    print("1111")
    smtp.quit()

a=config.readconfig.getconfvalue("email")
send_mail(a[0],a[4],a[1],a[2],a[3])





