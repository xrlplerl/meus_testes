from tkinter import *
from tkinter import ttk

tela = Tk()
tela.geometry("800x400")

fr = Frame(tela)
sc = Scrollbar(fr,orient=VERTICAL)
sc.pack(side=RIGHT,fill=Y)
cx = Listbox(fr,height=5,width=10)
for m in range(0,1001):
    cx.insert(END,str(m))

cx.pack(side=LEFT, fill=BOTH)
sc.config(command=cx.yview)
fr.place(x=10,y=10)
tela.mainloop()