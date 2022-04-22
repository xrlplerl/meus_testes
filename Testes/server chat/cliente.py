import socket
ip = str(input("Digite o ip: "))
port = 1800
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.connect((ip,port))
while True:
    r = server.recv(1024)
    r = str(r)
    rs = r.replace("b'","")
    rsd = rs.replace("'"," \n")
    rsd = ("[Server] ]===> " + rsd)
    print (rsd)
    m = bytes(input("}==> "),"ascii")
    server.send(m)
    print("\n")
