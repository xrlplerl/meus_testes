import socket, threading

host = "::1"
port = 456
server = (host,port)
cod = "ascii"
nick = str(input("Nick: "))

s = socket.socket(socket.AF_INET6,socket.SOCK_DGRAM)
s.connect(server)
msg = nick.encode(cod)
s.sendto(msg,server)
def receber():
    while True:
        print(s.recv(1024).decode(cod))
        
def enviar():
    while True:
        msg = str(input(""))
        s.sendto(msg.encode(cod),server)
        
threading.Thread(target=receber).start()
threading.Thread(target=enviar).start()