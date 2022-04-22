from flask import Flask, render_template, request, redirect
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os, dotenv, smtplib

dotenv.load_dotenv(dotenv.find_dotenv())

def cript(msg):
    ms = ""
    for m in msg:
        if(m == " "):
            ms = ms + " "
        else:
            ms = ms + chr(ord(m)+int(os.getenv("chave_cript")))

    return ms

def decript(msg):
    ms = ""
    for m in msg:
        if(m == " "):
            ms = ms + " "
        else:
            ms = ms + chr(ord(m)-int(os.getenv("chave_cript")))

    return ms

def send_mail(email,titulo,msg,tipo):
    server = smtplib.SMTP(os.getenv("host_email"),int(os.getenv("port_email")))
    server.ehlo()
    server.starttls()
    server.login(os.getenv("email"),os.getenv("senha"))
    email_msg = MIMEMultipart()
    email_msg["From"] = os.getenv("email")
    email_msg["To"] = email
    email_msg["Subject"] = titulo
    if(tipo == 1):
        email_msg.attach(MIMEText(msg,"plain"))
    elif(tipo == 2):
        email_msg.attach(MIMEText(msg,"html"))
    else:
        return "Erro no tipo email"
    server.sendmail(email_msg["From"],email_msg["To"],email_msg.as_string())
    server.quit()

titulo = "Teste 01"

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    if(request.method == "POST"):
        email_send = request.form.get('email')
        ti = request.form.get('titulo')
        msg = request.form.get('msg')
        send_mail(email_send,ti,msg,1)
        return render_template('index.html')
    else:
        return render_template('index.html')

app.run(debug=True,port=int(os.getenv("port")))