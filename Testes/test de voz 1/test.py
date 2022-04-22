from tkinter import *
import pyttsx3
tela = Tk()
fala = pyttsx3.init()
vois = fala.getProperty('voices')
def speaks():
    speak(str(ct1.get()))
def speak(texto):
    for voice in vois:
        if (voice.name == 'brazil'):
            fala.setProperty('voice',voice.id)
    fala.say(texto)
    fala.runAndWait()
tela.geometry("500x500+1+1")
tela.title("Falado")
tex1 = Label(tela,text="Fala: ")
tex1.place(x=50,y=150)
ct1 = Entry(tela,width=50)
ct1.place(x=100,y=150)
bt1 = Button(tela,width=20,text="Falar",command=speaks)
bt1.place(x=90,y=180)
tela.mainloop()
