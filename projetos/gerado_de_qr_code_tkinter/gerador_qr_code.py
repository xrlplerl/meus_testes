from tkinter import *
from tkinter import filedialog
from PIL import ImageTk
import qrcode

def salvar():
    try:
        arquivo = filedialog.asksaveasfile(mode='w', defaultextension = ".png")
        diretorio = str(arquivo.name)
        ((qrcode.make(str(cx1.get(1.0,END)))).get_image()).save(diretorio)
        
    except:
        pass

def gerar():
    global im
    img = ImageTk.PhotoImage(((qrcode.make(str(cx1.get(1.0,END)))).get_image()).resize((350,350)))
    im = Label(tela,image=img,bg="#fff",width=400,height=350)
    im.image = img
    im.place(x=45,y=5)
    bt1.destroy()
    but2()
    
def voltar():
    bt2.destroy()
    bt3.destroy()
    but1()
    im.destroy()
    
def but1():
    global bt1
    bt1 = Button(tela,text="Gerar QR CODE",fg="#fff",bg="#096",font="Arial 14 bold",width=20,command=gerar)
    bt1.place(x=110,y=400)
    
def but2():
    global bt2,bt3
    bt2 = Button(tela,text="Voltar",fg="#fff",bg="red",font="Arial 14 bold",width=20,command=voltar)
    bt2.place(x=110,y=400)
    bt3 = Button(tela,text="Salvar",fg="#fff",bg="#098",font="Arial 14 bold",width=10,command=salvar)
    bt3.place(x=165,y=450)

tela = Tk()
tela.title("Gerador de QR CODE")
tela.iconbitmap("qr.ico")
tela.geometry("500x500")
tela.resizable(False,False)
tela['bg'] = "#fff"
cx1 = Text(tela,height=20,width=50,bg="#DCDCDC")
cx1.place(x=45,y=5)
but1()
tela.mainloop()