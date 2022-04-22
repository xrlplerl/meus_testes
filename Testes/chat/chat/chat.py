import socket
ip = str(input("Digite o ip do chat: "))
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.connect((ip,4567))
while True:
    data = str(server.recv(1024))
    data = data.replace("b","")
    data = data.replace("'","")
    data = data.replace("'","")
    data = "[+] ]===> " + data
    print("")
    print(data)
    print("")
    server.sendall(bytes(input("}===> "),"ascii"))

seler.close()
