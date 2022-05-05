from getpass import getpass
from hashlib import md5, sha256
import time, os

def cls():
    os.system('cls')

man = ['']

nome = str(input('Digite o nome("Sem acentos ou caracteres especiais"): '))
nem1 = nome.upper()
nem2 = nome.lower()
nem3 = nem1.replace(" ",'')
nem4 = nem2.replace(" ","")
nem5 = nem1.split()
nem6 = nem2.split()

telefone = str(input('Digite o telefone ("Só numeros, sem espaços"): '))

cpf = str(input('Digite o cpf ("Só numeros, sem espaço"): '))

rg = str(input('Digite o rg ("Só numero, sem espaços): '))

data = str(input('Digite a data de nacimento("dd/mm/aaaa"): '))
data1 = data.replace("/","")

if (telefone != ""):
    for t in telefone:
        man.append(t)
    man.append(telefone)

if (cpf != ""):
    for c in cpf:
        man.append(c)
    man.append(cpf)

if (rg != ""):
    for r in rg:
        man.append(r)
    man.append(rg)

if (data  != ""):
    for d in data1:
        man.append(d)
    man.append(data1)

man.append(nem1)
man.append(nem2)
man.append(nem3)
man.append(nem4)

for no1 in nem3:
    man.append(no1)

for no2 in nem4:
    man.append(no2)

for n1 in nem5:
    man.append(n1)

for n2 in nem6:
    man.append(n2)

man.append(nome)

man.append(" ")

for n1 in man:
    for n2 in man:
        for n3 in man:
            for n4 in man:
                for n5 in man:
                    for n6 in man:
                        for n7 in man:
                            for n8 in man:
                                senha = str(n1+n2+n3+n4+n5+n6+n7+n8)
                                md = md5(senha.encode('utf8')).hexdigest()
                                sha = sha256(senha.encode('utf8')).hexdigest()
                                print(f'Senha: {senha} | md5: {md} | sha256: {sha}')