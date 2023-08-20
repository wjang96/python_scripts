#Created By-:Wei Jin
#Script to send emails to multiple recipents
# python smtp_email.py "Email Header" "xxx@hotmail.com,yyy@gmail.com,zzz@outlook.com" "/tmp/test.txt,/tmp/test2.txt,/tmp/test3.txt" "SERVERNAME" "Email message"
import smtplib 
import os 
import sys 
from email.MIMEMultipart import MIMEMultipart 
from email.MIMEBase import MIMEBase 
from email.MIMEText import MIMEText 
from email import Encoders 

header = sys.argv[1] 
sender = sys.argv[2]  
rec_list = sys.argv[3].split(',') 
file_list = sys.argv[4].split(',') 
smtp_server = sys.argv[5] 
body= sys.argv[6] 

msg = MIMEMultipart() 
msg['Subject'] = header 
msg['From'] = sender 
msg['To'] = ', '.join(rec_list) 


if sys.argv[4] == "":
    None
else:
    for filepath in file_list: 
        try:
            part = MIMEBase('application', "octet-stream") 
            part.set_payload (open(filepath, "rb").read())
            Encoders.encode_base64(part) 
            part.add_header('Content-Disposition', 'attachment; filename="{}".format(os.path.basename(filepath)))
            msg.attach(part)
        except:
            print ("Attach File I/O error: ", filepath) 
text = MIMEText (body, 'html') 
msg.attach (text)

server = smtplib.SMTP (smtp_server) 
server.sendmail (sender, rec_list, msg.as_string()) 
