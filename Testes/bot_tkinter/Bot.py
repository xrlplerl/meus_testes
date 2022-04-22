from tkinter import *
from tkinter import ttk

tela = Tk()
tela.title("bot")
tela.geometry("500x300")

def ins():
        l.insert(END,c.get())
        ms.append(c.get())

def bt():
    global f,c,b,b2,ms,n
    num = len(ms)
    n = 0
    def msg():
        global n
        n = n + 1
        if(num > n):
            l.insert(END,c.get())
            l.insert(END,ms[n])
        else:
            l.insert(END,"Fim...")
    f.destroy()
    c.destroy()
    b.destroy()
    b2.destroy()
    f = Frame(tela)
    s = Scrollbar(f,orient=VERTICAL)
    s.pack(side=RIGHT, fill=Y)
    l = Listbox(f,height= 10, width=50, borderwidth = '10', yscrollcommand=s.set, bd=1)
    l.pack(side=LEFT, fill=BOTH)
    s.config(command=l.yview)

    f.place(x=55,y=6)

    c = Entry(tela,width=40)
    c.place(x=85,y=200)
    b = Button(tela,text="enviar",command=msg)
    b.place(x=110,y=250)
    l.insert(END,ms[n])



ms = []
f = Frame(tela)
s = Scrollbar(f,orient=VERTICAL)
s.pack(side=RIGHT, fill=Y)
l = Listbox(f,height= 10, width=50, borderwidth = '10', yscrollcommand=s.set, bd=1)

l.pack(side=LEFT, fill=BOTH)
s.config(command=l.yview)

f.place(x=55,y=6)

c = Entry(tela,width=40)
c.place(x=85,y=200)

b = Button(tela,text="Adicionar",command=ins)
b.place(x=110,y=250)

b2 = Button(tela,text="Concluir",command=bt)
b2.place(x=200,y=250)

tela.mainloop()