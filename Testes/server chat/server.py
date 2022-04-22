import socket
ip = '0.0.0.0'
port = 1800
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((ip,port))
server.listen(5)
while True:
    (obj,usu) = server.accept()
    print(usu)
    while True:
        user = usu[0]
        m = bytes(input("}==> "),"ascii")
        obj.send(m)
        print("\n")
        r = obj.recv(1024)
        r = str(r)
        rs = r.replace("b'","")
        rsd = rs.replace("'"," \n")
        rsd = ("["+str(user)+"] ]===>"+rsd)
        print (rsd)
server.close()
