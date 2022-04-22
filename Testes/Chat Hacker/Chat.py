import socket
import sys
import time
import os

class Chat():
    def __init__(self,ip,port,pas):
        self.ip = ip
        self.port = port
        self.pas = pas
    def server(self):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind((self.ip,self.port))
        s.listen(1)
        try:
            os.system("cls")
        except:
            os.system("clear")
        while True:
            obj,usu = s.accept()
            if(self.pas != ""):
                p = obj.recv(1024)
                if(p == pas):
                    obj.send(b" Seja Bem Vindo !")
                else:
                    print("[!] }==> Alguem tentou se conectar sem autorização !")
                    obj.send(b" Acesso Negado")
                    obj.close()
                    s.close()
                    time.sleep(4)
                    exit()
            else:
                obj.send(b" Seja Bem Vindo !")
                print("[+] ]==> O IP {} se conectou".format(usu[0]))
            while True:
                msg = bytes(input("}===> "),"utf-8")
                obj.send(msg)
                print("}==> " + str(obj.recv(1024)))
    def cliente(self):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((self.ip,self.port))
        try:
            os.system("cls")
        except:
            os.system("clear")
        if(self.pas != ""):
            s.sendall(self.pas)
            print("}==> " + str(s.recv(1024)))
        else:
            print("}==> " + str(s.recv(1024)))
        while True:
            print("}==> " + str(s.recv(1024)))
            msg = bytes(input("}===> "),"utf-8")
            s.send(msg)

            
soc = str(sys.argv[1])
ip = str(sys.argv[2])
port = int(sys.argv[3])
try:
    pas = bytes(sys.argv[4],"utf-8")
except:
    pas = ""

chat = Chat(ip,port,pas)
if(soc == "s"):
    chat.server()
if(soc == "c"):
    chat.cliente()
else:
    exit()
