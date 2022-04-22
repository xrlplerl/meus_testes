from tkinter import *


tela = Tk()
tela.title("App")
tela.geometry("800x400")
scrollbarLb1 = Scrollbar(tela, orient=VERTICAL)
scrollbarLb1.pack(side=RIGHT, fill=Y)
Lb1 = Listbox(tela,height= 8, width=8, borderwidth = '10', yscrollcommand=scrollbarLb1.set, bd=1)
for ids in range(0,101):
    Lb1.insert(END,str(ids))
Lb1.pack(side=LEFT, fill=BOTH)
scrollbarLb1.config(command=Lb1.yview)
tela.mainloop()