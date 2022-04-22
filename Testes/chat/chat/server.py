import socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("0.0.0.0",4567))
while True:
    server.listen(5)
    (obj,usu) = server.accept()
    obj.sendall(b'Seja Bem Vindo')
    while True:
        data = str(obj.recv(1024))
        data = data.replace('b','')
        data = data.replace("'","")
        data = data.replace("'","")
        data = "[+] ]===> " + data
        print("")
        print(data)
        print("")
        obj.sendall(bytes(input("}===> "),"ascii"))

server.close()
