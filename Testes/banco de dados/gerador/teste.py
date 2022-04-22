import sqlite3,os,random

if(os.path.exists("teste.db") == True):
    s = sqlite3.connect("teste.db")
    c = s.cursor()

else:
    s = sqlite3.connect("teste.db")
    c = s.cursor()
    c.execute("create table login(id integer primary key autoincrement, nome varchar(60), senha varchar(60));")
    c.execute('insert into login(id,nome,senha) values(1,"admin","admin");')
    s.commit()

def add(nome,senha):
    c.execute('insert into login(nome,senha) values("{}","{}");'.format(nome,senha))
    s.commit()

def gerador(n,minimo,maximo):
    le = ["a","A","b","B","c","C","d","D","e","E","f","F","g","G","h","H","j","J","k","K","l","L","ç","Ç","q","Q","w","W","e","E","r","R","t","T","y","Y","u","U","i","I","o","O","p","P","z","Z","x","X","c","C","v","V","b","B","n","N","m","M"]
    ln = range(0,10)
    ls = [le,ln]
    l1 = []
    l2 = []
    for i in range(0,n):
        r = random.choice(range(minimo,maximo))
        user = ""
        senha = ""
        for k in range(0,r):
            m = random.choice(ls)
            l = random.choice(m)
            user = user + str(l)
        l1.append(user)
        for k in range(0,r):
            m = random.choice(ls)
            l = random.choice(m)
            senha = senha + str(l)
        l2.append(senha)

    for a in range(0,n):
        add(l1[a],l2[a])

num = int(input("Digite a quantidade que sera gerada: "))
mi = int(input("Digite o valor da quantidade minima de caracteris: "))
ma = int(input("Digite o valor da quantidade maxima de caracteris: "))
if(mi == 0):
    mi = 1
else:
    pass
if(ma == 0):
    ma = 8
else:
    pass
gerador(num,mi,ma)
c.execute("select * from login;")
res = c.fetchall()
for rt in res:
    print(rt)
c.close()
s.close()