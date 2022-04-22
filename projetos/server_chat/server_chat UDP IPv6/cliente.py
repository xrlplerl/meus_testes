import socket, threading

host = str(input("HOST: "))
porta = int(input("PORTA: "))
s = socket.socket(socket.AF_INET6,socket.SOCK_DGRAM)
s.connect((host,porta))
def receber():
    while True:
        msg, cliente  = s.recvfrom(1024)
        print(msg.decode("ascii"))
    
def enviar():
    while True:
        msg = (str(input(""))).encode("ascii")
        s.sendto(msg,(host,porta))

threading.Thread(target=receber).start()
threading.Thread(target=enviar).start()