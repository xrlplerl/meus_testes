from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
import smtplib, time 
 
class se_email(): 
    def __init__(self,email,senha): 
        self.email = email 
        self.senha = senha 

    def iniciar(self): 
        self.server = smtplib.SMTP("smtp.gmail.com",587) 
        self.server.ehlo() 
        self.server.starttls() 
        self.server.login(self.email,self.senha) 

    def envia(self,send_mail,titulo,msg,tipo): 
        self.send_mail = send_mail 
        self.titulo = titulo 
        self.msg = msg 
        self.tipo = tipo 
        self.email_msg = MIMEMultipart() 
        self.email_msg["From"] = self.email 
        self.email_msg["To"] = self.send_mail 
        self.email_msg["Subject"] = self.titulo 
        if(self.tipo == 1): 
            self.email_msg.attach(MIMEText(self.msg,"plain")) 
        elif(self.tipo == 2): 
            self.email_msg.attach(MIMEText(self.msg,"html")) 
        else: 
            return "Erro no tipo email" 
        self.server.sendmail(self.email_msg["From"],self.email_msg["To"],self.email_msg.as_string()) 

    def fechar(self): 
        self.server.quit() 
 