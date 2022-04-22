local = str(input("Digite o nome do arquivo: "))
arquivo = open(local+".txt","r")
x = arquivo.readlines()
text=[]
cont = 0
def cript(valor):
    t = []
    mac = ""
    for c in text:
        c = list(c)
        for k in c:
            h = str(chr(ord(k)+valor))
            mac = mac+h
        t.append(mac)
        mac = ""
    return(t)

def decript(valor):
    t = []
    mac = ""
    for c in text:
        c = list(c)
        for k in c:
            h = str(chr(ord(k)-valor))
            mac = mac+h
        t.append(mac)
        mac = ""
    return(t)
        
            
for l in x:
    try:
        text.append(l)
    except:
        break
    cont = cont + 1

tk = int(input("Digite (1:Para Criptografar e 2:Para Descriptografar): "))
cri = int(input("Digite a chave: "))
arquivo.close()
try:
    arquivo = open(local+".txt","w")
    if(tk == 1):
        resu = cript(cri)
        for es in resu:
            arquivo.write(es)
            print(es)
            
    else:
        resu = decript(cri)
        for es in resu:
            arquivo.write(es)
            print(es)

    arquivo.close()
except:
    print("Erro")
    arquivo.close()
exit()

