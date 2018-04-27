import smtplib
import email.mime.multipart
import email.mime.text
import email.header
import config.readconfig
import datetime
nowtime=datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
def send_mail(smtp_server,port,sender,psw,receiver,fujian):
    msg=email.mime.multipart.MIMEMultipart()
    msg['subject']=email.header.Header('自动化测试报告%s'%nowtime,'utf-8')
    msg["from"]=sender
    msg['to']=receiver
    content='''附件是自动化报告请查收,谢谢'''
    msg.attach(email.mime.text.MIMEText(content,'plain','utf-8'))
    att=email.mime.text.MIMEText(open(fujian,"rb").read(),'base64','utf-8')
    att['Content-Type']='application/octet-stream'
    att['Content-Disposition']='attachment;filename="testreport%s.html"'%nowtime
    msg.attach(att)
    try:
        smtp=smtplib.SMTP()
        smtp.connect(smtp_server,port)
        smtp.login(sender,psw)
        smtp.sendmail(sender,receiver,msg.as_string())
        print("send mail success")
        smtp.quit()
    except smtplib.SMTPException:
        print("send mail fail")

# a=config.readconfig.getconfvalue("email")
# send_mail(a[0],a[4],a[1],a[2],a[3])





