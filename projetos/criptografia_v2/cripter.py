import sys

class Cripter():
    def __init__(self,aq,sen,cr):
        self.aq = aq
        self.sen = sen
        self.cr = cr

    def Cripto(self):
        self.arquivo = open(self.aq,"r")
        self.conteudo = self.arquivo.readlines()
        linhas = []
        palavra = ""
        self.arquivo = open(self.aq,"w")
        for l in self.conteudo:
            lin = list(l)
            for le in lin:
                letra = chr(ord(le)+self.sen)
                palavra = palavra + letra
            linhas.append(palavra)
            palavra = ""
        for linha in linhas:
            self.arquivo.write(linha)
        self.arquivo.close()

    def Decripto(self):
        self.arquivo = open(self.aq,"r")
        self.conteudo = self.arquivo.readlines()
        linhas = []
        palavra = ""
        self.arquivo = open(self.aq,"w")
        for l in self.conteudo:
            lin = list(l)
            for le in lin:
                letra = chr(ord(le)-self.sen)
                palavra = palavra + letra
            linhas.append(palavra)
            palavra = ""
        for linha in linhas:
            self.arquivo.write(linha)
        self.arquivo.close()

if(len(sys.argv) > 2):
    if("-a" in sys.argv):
        arq = str(sys.argv[int(sys.argv.index("-a")+1)])
    else:
        print("]=====> Erro:\n]=====> Passe o nome do arquivo: py cripter.py -a [nome do arquivo]")
    if("-s" in sys.argv):
        s = int(sys.argv[int(sys.argv.index("-s")+1)])
    else:
        s = 2
    if("-c" in sys.argv):
        c = str(sys.argv[int(sys.argv.index("-c")+1)])
    else:
        c == "cripto"

else:
    exit()

text = Cripter(arq,s,c)
if(text.cr == "cripto"):
    text.Cripto()
elif(text.cr == "decripto"):
    text.Decripto()
else:
    exit()