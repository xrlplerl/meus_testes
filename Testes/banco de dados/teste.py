import sqlite3,os

while True:
    if(os.path.exists("teste.db") == True):
        s = sqlite3.connect("teste.db")
        c = s.cursor()
    else:
        s = sqlite3.connect("teste.db")
        c = s.cursor()
        c.execute("create table login(id integer, nome varchar(60), senha varchar(60));")
        c.execute('insert into login(id,nome,senha) values(1,"f","host");')
        s.commit()

    def consulta():
        c.execute("select * from login")
        return c.fetchall()

    def cadastra(u,p):
        c.execute('insert into login(id,nome,senha) values(1,"{}","{}");'.format(u,p))
        s.commit()

    print("[1] Login\n[2] Cadastra")
    op = int(input("Digite o valor: "))

    if(op == 1):
        user = str(input("Usruario: "))
        senha = str(input("Senha: "))
        rs = consulta()
        n = False
        for l in rs:
            if(l[1] == user):
                if(l[2] == senha):
                    n = True
                    break
                else:
                    pass
            else:
                pass
        if(n == True):
            print("Login bem sucedido")
        else:
            print("login incorreto")
    elif(op == 2):
        user = str(input("Usruario: "))
        senha = str(input("Senha: "))
        cadastra(user,senha)
    else:
        exit()
    
    c.close()
    s.close()