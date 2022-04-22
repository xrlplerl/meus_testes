from tkinter import *
import os

def Exit():
    exit()

def cad():
    global caix1,caix2,caix3,caix4,caix5,caix6
    if(caix1.get() == "" or caix2.get() == "" or caix3.get() == "" or caix4.get() == "" or caix5.get() == "" or caix6.get() == ""):
        erro()
    else:
        arquivo = open("{}.txt".format(caix1.get()),"w")
        arquivo.write((caix2.get())+"\n")
        arquivo.write((caix3.get())+"\n")
        arquivo.write((caix4.get())+"\n")
        arquivo.write((caix5.get())+"\n")
        arquivo.write((caix6.get())+"\n")

class cadastro():
    def __init__(self):
        global caix1,caix2,caix3,caix4,caix5,caix6
        self.tela = Tk()
        self.tela.title("Biblioteca - Cadastro")
        self.tela.geometry("500x300+200+200")
        self.text1 = Label(self.tela,text="Nome: ",font="Arial 12")
        self.text1.place(x=10,y=10)
        caix1 = Entry(self.tela,font="Arial 12",width=47)
        caix1.place(x=60,y=12)
        self.text2 = Label(self.tela,text="Auto: ",font="Arial 12")
        self.text2.place(x=10,y=50)
        caix2 = Entry(self.tela,font="Arial 12",width=48)
        caix2.place(x=50,y=52)
        self.text3 = Label(self.tela,text="Edição: ",font="Arial 12")
        self.text3.place(x=10,y=90)
        caix3 = Entry(self.tela,font="Arial 12",width=46)
        caix3.place(x=70,y=92)
        self.text4 = Label(self.tela,text="Editora: ",font="Arial 12")
        self.text4.place(x=10,y=130)
        caix4 = Entry(self.tela,font="Arial 12",width=46)
        caix4.place(x=70,y=132)
        self.text5 = Label(self.tela,text="Estante: ",font="Arial 12")
        self.text5.place(x=10,y=170)
        caix5 = Entry(self.tela,font="Arial 12",width=46)
        caix5.place(x=70,y=172)
        self.text6 = Label(self.tela,text="Descrição: ",font="Arial 12")
        self.text6.place(x=10,y=210)
        caix6 = Entry(self.tela,font="Arial 12",width=44)
        caix6.place(x=90,y=212)
        self.bt = Button(self.tela,font="Arial 12",text="Cadastra",fg="#fff",bg="red",command=cad)
        self.bt.place(x=180,y=250)
        self.tela.mainloop()

class busca():
    def __init__(self):
        global listi,caixt
        global ag1,ag2,ag3,ag4,ag5,ag6
        self.tela = Tk()
        self.tela.title("Biblioteca - Busca")
        self.tela.geometry("500x300+200+200")
        self.text1 = Label(self.tela,text="Nome: ",font="Arial 12")
        self.text1.place(x=10,y=10)
        ag1 = Label(self.tela,font="Arial 12")
        ag1.place(x=60,y=12)
        self.text2 = Label(self.tela,text="Auto: ",font="Arial 12")
        self.text2.place(x=10,y=50)
        ag2 = Label(self.tela,font="Arial 12")
        ag2.place(x=50,y=52)
        self.text3 = Label(self.tela,text="Edição: ",font="Arial 12")
        self.text3.place(x=10,y=90)
        ag3 = Label(self.tela,font="Arial 12")
        ag3.place(x=70,y=92)
        self.text4 = Label(self.tela,text="Editora: ",font="Arial 12")
        self.text4.place(x=10,y=130)
        ag4 = Label(self.tela,font="Arial 12")
        ag4.place(x=70,y=132)
        self.text5 = Label(self.tela,text="Estante: ",font="Arial 12")
        self.text5.place(x=10,y=170)
        ag5 = Label(self.tela,font="Arial 12")
        ag5.place(x=70,y=172)
        self.text6 = Label(self.tela,text="Descrição: ",font="Arial 12")
        self.text6.place(x=10,y=210)
        ag6 = Label(self.tela,font="Arial 12")
        ag6.place(x=90,y=212)
        if(caixt.get() == ""):
            erro()
        else:
            for n in listi:
                if(n.replace(".txt","") == caixt.get()):
                    arquivo = open(n,"r")
                    ag1["text"] = n.replace(".txt","")
                    ag2["text"] = arquivo.readline()
                    ag3["text"] = arquivo.readline()
                    ag4["text"] = arquivo.readline()
                    ag5["text"] = arquivo.readline()
                    ag6["text"] = arquivo.readline()
        self.tela.mainloop()

        

class pesquisa():
    def __init__(self):
        global listi,caixt
        self.tela = Tk()
        self.tela.title("Biblioteca - Pesquisa")
        self.tela.geometry("500x50+10+10")
        self.arq = os.listdir()
        listi = []
        for iten in self.arq:
            if((iten.split("."))[1] == "txt"):
                listi.append(iten)
            else:
                pass
        self.pes = Label(self.tela,text="Pesquisa: ",font="Arial 12")
        self.pes.place(x=10,y=10)
        caixt = Entry(self.tela,width=35,font="Arial 12")
        caixt.place(x=90,y=12)
        self.bt = Button(self.tela,text="Pesquisa",font="Arial 12",fg="#fff",bg="#099",command=busca)
        self.bt.place(x=415,y=6)
        self.tela.mainloop()

class pag2():
    def __init__(self):
        self.tela = Tk()
        self.tela.title("Biblioteca")
        self.tela.geometry("230x60+10+10")
        self.pes = Button(self.tela,text="Pesquisa",font="Arial 15",bg="#096",fg="#fff",command=pesquisa)
        self.pes.place(x=10,y=10)
        self.pes2 = Button(self.tela,text="Cadastro",font="Arial 15",bg="red",fg="#fff",command=cadastro)
        self.pes2.place(x=120,y=10)
        self.tela.mainloop()

class erro():
    def __init__(self):
        self.tela = Tk()
        self.tela.title("ERRO!")
        self.tela.geometry("200x50+100+100")
        self.text = Label(self.tela,text="ERRO!",font="Arial 12",fg="red")
        self.text.place(x=70,y=10)
        self.tela.mainloop()

def logar(event):
    global caixa1,caixa2,pagin
    try:
        if(str(caixa1.get()) == "f" and str(caixa2.get()) == "host"):
            caixa1.destroy()
            caixa2.destroy()
            caixa1 = Entry(tela,text="",font="Arial 12")
            caixa1.place(x=80,y=12)
            caixa2 = Entry(tela,text="",font="Arial 12")
            caixa2.place(x=80,y=42)
            pag2()
        else:
           erro()
    except:
        pass

def loga():
    global caixa1,caixa2,pagin
    try:
        if(str(caixa1.get()) == "f" and str(caixa2.get()) == "host"):
            caixa1.destroy()
            caixa2.destroy()
            caixa1 = Entry(tela,text="",font="Arial 12")
            caixa1.place(x=80,y=12)
            caixa2 = Entry(tela,text="",font="Arial 12")
            caixa2.place(x=80,y=42)
            pag2()
        else:
            erro()
    except:
        pass

class In():
    def __init__(self):
        global caixa1,caixa2,tela
        tela = Tk()
        tela.title("Biblioteca")
        tela.geometry("300x100+50+50")
        self.name1 = Label(tela,text="Usuario: ",font="Arial 12")
        self.name1.place(x=10,y=10)
        caixa1 = Entry(tela,text="",font="Arial 12")
        caixa1.place(x=80,y=12)
        self.name2 = Label(tela,text="Senha: ",font="Arial 12")
        self.name2.place(x=10,y=40)
        caixa2 = Entry(tela,text="",font="Arial 12")
        caixa2.place(x=80,y=42)
        self.bt1 = Button(tela,text="Entra",width=10,fg="#fff",bg="#096",command=loga)
        self.bt1.place(x=80,y=70)
        tela.bind("<Return>",logar)
        self.bt2 = Button(tela,text="Sair",width=10,fg="#fff",bg="red",command=Exit)
        self.bt2.place(x=170,y=70)
        tela.mainloop()


pagin = In()