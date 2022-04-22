import socket, threading

#Vamos definir o host, a porta e o nome do usuario. 
host = str(input("Digite o host: "))
port = int(input("Digite a porta: "))
username = str(input("Nome do usuario:"))
#Definindo o codigo do encode e decode.
cod = "ascii"
#Definindo que a conexão vai ser IPV4 com o socket.AF_INET / para usar IPV6 use socket.AF_INET6 .
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#Conectando no servidor
s.connect((host,port))
#Enviando o nick name(nome de usuario).
s.send(username.encode(cod))
#Criando as funções de envio e recepição de mensagens
def receber():
    #Lope
    while True:
        #Esperando receber a mensagem
        msg = s.recv(1024).decode(cod)
        print(msg)
    
def enviar():
    #Lope
    while True:
        #Recebendo o input e enviando a mensagem
        msg = str(input(""))
        s.send(msg.encode(cod))
        
#Criando as Threads de receber e enviar mensagem
receber_msg = threading.Thread(target=receber).start()
enviar_msg = threading.Thread(target=enviar).start()
