x = open("F.txt","r")
usu = str(x.readline()).split(",")
pas = str(x.readline()).split(",")

u = str(input("[&] }===> Digite o nome: "))
c = 0
for r in usu:
    if(r == u):
        print("Usuario: {} \nTipo: {}".format(usu[c],pas[c]))
        break
    c = c + 1
