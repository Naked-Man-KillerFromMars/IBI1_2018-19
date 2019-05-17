## -*- coding: utf-8 -*-
#"""
#Spyder Editor
#
#This is a temporary script file.
#"""
#
import re
xfile = open(r'address_information.csv','r')

for cheese in xfile:
    unit = cheese.split(',')
    name = unit.pop(0)
    address = unit.pop(0)
    print(address)
    com = []
    add = list(address)
    a = add.pop(-1)
    b = add.pop(-1)
    c = add.pop(-1)
    d = add.pop(-1)
    com.append(d)
    com.append(c)
    com.append(b)
    com.append(a)
    com = ''.join(com)
    if com == '.com':
        print('this address is valid')
    else:
        print('this address is invalid')
    
    text = unit.pop(0)
    print(text)
    

    
    import smtplib
    from email.mime.text import MIMEText
    from email.header import Header
    
    
    mail = open('body.txt')
    content = mail.read()
    content = re.sub(r'User',name,content)
    
    
    
        
    mail_host="smtp.zju.edu.cn" 
    mail_user="3180111427@zju.edu.cn"    
    mail_pass="Zwy690816"  
    
    sender = '3180111427@zju.edu.cn'
    receivers = [address]

    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = Header("Zhu wenyuan", 'utf-8')  
    message['To'] =  Header(name, 'utf-8')        
 
    subject = text
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)   
        smtpObj.login(mail_user,mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print ("Mail sent successfully")
    except smtplib.SMTPException:
        print ("Failed")
    if mail:
        mail.close        
if xfile:
    xfile.close









