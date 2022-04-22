from tkinter import *
import threading,random,time

Xb = random.choice(range(0,250))
Yb = 450
Xo = random.choice(range(0,450))
Yo = 1
ix = 5
iy = 5
pointb = 0
pointo = 0
n = 0.05

class Game():
    def __init__(self):
        global Bar
        global Bol
        global text1,text2
        self.title = "NTS"
        self.tela = Tk()
        self.tela.geometry("600x500+10+10")
        self.tela.title(self.title)
        self.tela["bg"] = "#fff"
        Bar = Label(self.tela,width=10,bg="#000")
        Bar.place(x=Xb,y=Yb)
        text1 = Label(self.tela,text="Xb: {} Yb: {} | Xo: {} Yo: {}".format(Xb,Yb,Xo,Yo),bg="#fff",fg="#000",font="Arial 10")
        text1.place(x=1,y=1)
        text2 = Label(self.tela,text="Bola X Barra\n{}     {}".format(pointo,pointb),fg="#000",bg="#fff",font="Arial 20")
        text2.place(x=400,y=1)
        Bol = Label(self.tela,width=2,bg="#000")
        Bol.place(x=Xo,y=Yo)
        self.tela.bind("<Key>",control)
        self.tela.mainloop()

    def bar():
        global Bar
        Bar.place(x=Xb,y=Yb)

    def bol():
        global Bol
        Bol.place(x=Xo,y=Yo)

    def cor():
        global Bol
        Bol["bg"] = random.choice(["#000","silver","red","#096","#097","#098","#099","blue"]) 
    
    def text1():
        global text1
        text1["text"] = "Xb: {} Yb: {} | Xo: {} Yo: {}".format(Xb,Yb,Xo,Yo)

    def text2():
        global text2
        text2["text"] = "Bola X Barra\n{}     {}".format(pointo,pointb)


class Gr():
    def __init__(self):
        self.tela = Tk()
        self.tela.title("Fim")
        self.tela.geometry("300x100")
        self.text1 = Label(self.tela,text="Gamer Over",fg="red",font="Arial 30")
        self.text1.place(x=5,y=5)
        self.tela.mainloop()

class Gr1():
    def __init__(self):
        self.tela = Tk()
        self.tela.title("LIKE")
        self.tela.geometry("300x100")
        self.text1 = Label(self.tela,text="Vitoria",fg="#096",font="Arial 30")
        self.text1.place(x=5,y=5)
        self.tela.mainloop()
    
def control(event):
    global Xb
    car = str(event.char)
    if(car == "a"):
        Xb = Xb - 10
    elif(car == "d"):
        Xb = Xb + 10
    elif(car == "A"):
        Xb = Xb - 10
    elif(car == "D"):
        Xb = Xb + 10
    else:
        pass
    if(Xb < 0):
        Xb = 0 
    elif(Xb > 530):
        Xb = 530
    else:
        pass

    Game.bar()

def over():
    Gr()
    Game.tela.destroy()

def ver():
    Gr1()
    Game.tela.destroy()

def Mov():
    global Xo,Yo,ix,iy,pointb,pointo,n
    while True:
        if(Xo in range(Xb,Xb + 60) and Yo in range(440,450)):
            iy = iy * -1
            Game.cor()
            pointb = pointb + 1
        else:
            pass
        Xo = Xo + ix
        Yo = Yo + iy
        if(Xo < 0):
            Xo = 0
            ix = 5
        elif(Xo > 580 or Xo == 580):
            Xo == 580
            ix = -5
        else:
            pass

        if(Yo < 0):
            Yo = 0
            iy = 5
        elif(Yo > 480 or Yo == 480):
            Yo == 480
            iy = -5
            pointo = pointo + 1
        else:
            pass
        if(pointb > 5 or pointb == 5):
            n = 0.03
        elif(pointb > 10 or pointb == 10):
            n = 0.01
        elif(pointb > 20 or pointb == 20):
            n = 0.005
        elif(pointb > 23 or pointb == 25):
            n = 0.003
        elif(pointb > 30 or pointb == 30):
            n = 0.001
        else:
            pass
        if(pointo == 3 or pointo > 3):
            over()
        else:
            pass
        if(pointb == 40 or pointb > 40):
            ver()
        else:
            pass
        time.sleep(n)
        Game.bol()
        Game.text1()
        Game.text2()



game = threading.Thread(target=Game,name="Game",daemon=True)
game.start()
mov = threading.Thread(target=Mov,name="mov")
mov.start()


