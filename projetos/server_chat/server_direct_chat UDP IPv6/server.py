import socket
import threading

host = "::"
port = 456
cod = "ascii"

s = socket.socket(socket.AF_INET6,socket.SOCK_DGRAM)
s.bind((host,port))

clientes = []
nicks = []

def ms(nick,m,cliente):
    if(nick in nicks):
        user = clientes[nicks.index(nick)]
        nome = nicks[clientes.index(cliente)]
        msg = f"{nome} ]===> {m}"
        s.sendto(msg.encode(cod),user)
    else:
        msg = f"{nick} esta off"
        s.sendto(msg.encode(cod),cliente)

def geral(msg,cliente):
    if("|" in msg):
        msg = msg.split("|")
        ms(msg[0],msg[1],cliente)
    else:
        print("erro 01")
    

while True:
    msg, cliente = s.recvfrom(1024)
    if(cliente in clientes):
        geral(str(msg.decode(cod)),cliente)
    else:
        nick = msg.decode(cod)
        nicks.append(nick)
        clientes.append(cliente)
    
        