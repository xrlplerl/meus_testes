import socket, threading

#Definindo que a conexão vai ser IPV4 com o socket.AF_INET / para usar IPV6 use socket.AF_INET6 | o socket.SOCK_STREAM determinas que vamos trabalhar com TCP.
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#Vamos definir o tipo de codificação da comunicação.
cod = 'ascii'
#Vamos definir a porta e o host do nosso servidor.
host = "0.0.0.0"
port = int(input("Digite a porta do server: "))
#Vamos inicar o nosso server.
s.bind((host,port))
#Vamos definir, que o server que ele ira esperar conexões.
s.listen()
#Vamos definir as listas de clientes, e dos username.
clientes = []
user = []

#Vamos criar uma função para mandar mensagem para todos os clientes e outra para receber.
def msg_global(MSG):
    #Vamos criar um lope que percorre todos os clientes do server
    for cli in clientes:
        #Criamos esse tratamento de erro
        try:
            #Enviamos a mensagem para o cliente
            cli.send(MSG.encode(cod))
        except:
            pass
        
#Vamos criar uma função para esperar o envio de mensagens
def receber(client):
    while True:
        try:
            #Esperamos a mensagem chegar
            msg = client.recv(1024).decode(cod)
            #Pegando o nome do cliente
            us = user[clientes.index(client)]
            #Formatando a mensagem
            msg = f"{us} ]===> {msg}"
            #Enviando a mensagem
            msg_global(msg)
            
        except:
            pass
        
#Vamos criar um lope para aceitar todas as conexões.
while True:
    #vamos aceitar a conexão, essa nossa conexão vai nos retornar dos paramentos cliente e ip.
    client, ip = s.accept()
    #Adicionamos o cliente a lista de clientes
    clientes.append(client)
    #Vamos receber o username.
    username = client.recv(1024).decode(cod)
    #Adicionar a lista de nome de usario.
    user.append(username)
    msg = (f"O user {username} se conectou ao chat")
    #Mandamos uma mensagem para os clientes avisando que alguém se conectou
    msg_global(msg)
    #vamos criar uma thread para esse cliente
    threading.Thread(target=receber,args=(client,)).start()
    