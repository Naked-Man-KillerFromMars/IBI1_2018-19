## -*- coding: utf-8 -*-
#"""
#Spyder Editor
#
#This is a temporary script file.
#"""
#
import re
xfile = open(r'C:\Users\11601\Desktop\IBI\IBI1_2018-19\Practical6\address_information.csv','r')

for cheese in xfile:
    unit = cheese.split(',')
    print(unit)
    name = unit.pop(0)
    print(name)
    address = unit.pop(0)
    print(address)
    text = unit.pop(0)
    print(text)
    
    


#
#
#
#




    
    import smtplib
    from email.mime.text import MIMEText
    from email.header import Header
    
    
#    for person in address:        #loop for sending emails
    mail = open('body.txt')    #open the file and replace user names
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
        print ("fail")
    if mail:
        mail.close        
if xfile:
    xfile.close
    
#close the txt file
#remember to close the file








