import socket, threading

host = "0.0.0.0"
port = 315

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host,port))
clientes = []
users = []
def env_global(msg):
    for cli in clientes:
        s.sendto(f"]==> {msg.decode('ascii')}".encode("ascii"),cli)
while True:
    msg, cliente = s.recvfrom(1024)
    if(cliente in clientes):
        pass
    else:
        clientes.append(cliente)
        users.append(msg.decode("ascii"))
        
    env_global(msg)
    
    