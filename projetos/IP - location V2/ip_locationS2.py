from tkinter import *
from bs4 import BeautifulSoup as bs
import requests,sys,os,webbrowser
resp = ""
def IP(ip):
    global resp
    if(ip != ""):
        try:
            head = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
            pagina = bs(requests.get("https://ipapi.com/ip_api.php?ip={}".format(ip),headers=head).text,"html.parser")
            cont = str(pagina).replace("{","")
            cont = cont.replace("}","")
            cont = cont.replace("'","")
            cont = cont.replace('"',"")
            resp = cont.split(",")
        except:
            resp = ""
    else:
        resp = ""

tela = Tk()
tela.title("IP Geolocation V2")
tela.geometry("500x510+10+10")
tela.resizable(width=False,height=False)
text1 = Label(tela,text="IP: ",font="Arial 15")
text1.place(x=20,y=50)
caixa1 = Entry(tela,width=30,font="Arial 15")
caixa1.place(x=60,y=50)
text2 = Label(tela,text="",font="Arial 15")
text2.place(x=40,y=80)
text3 = Label(tela,text="",font="Arial 15")
text3.place(x=40,y=110)
text4 = Label(tela,text="",font="Arial 15")
text4.place(x=40,y=140)
text5 = Label(tela,text="",font="Arial 15")
text5.place(x=40,y=170)
text6 = Label(tela,text="",font="Arial 15")
text6.place(x=40,y=200)
text7 = Label(tela,text="",font="Arial 15")
text7.place(x=40,y=230)
text8 = Label(tela,text="",font="Arial 15")
text8.place(x=40,y=260)
text9 = Label(tela,text="",font="Arial 15")
text9.place(x=40,y=290)
text10 = Label(tela,text="",font="Arial 15")
text10.place(x=40,y=320)
text11 = Label(tela,text="",font="Arial 15")
text11.place(x=40,y=350)
text12 = Label(tela,text="",font="Arial 15")
text12.place(x=40,y=380)
text13 = Label(tela,text="",font="Arial 15")
text13.place(x=40,y=410)
text14 = Label(tela,text="",font="Arial 15")
text14.place(x=40,y=440)

def navg():
    webbrowser.open("https://www.google.com.br/maps/search/?api=1&query={},{}".format((resp[11].split(":"))[1],(resp[12].split(":"))[1]))

def navg1(event):
    if(resp != ""):
        webbrowser.open("https://www.google.com.br/maps/search/?api=1&query={},{}".format((resp[11].split(":"))[1],(resp[12].split(":"))[1]))
    else:
        pass

bt2 = Button(tela,text="Ver no google maps",font="Arial 12",fg="#fff",bg="#096",command=navg)

def Pro():
    IP(str(caixa1.get()))
    if(resp == ""):
        text2["text"] = ""
        text3["text"] = ""
        text4["text"] = ""
        text5["text"] = ""
        text6["text"] = ""
        text7["text"] = ""
        text8["text"] = ""
        text9["text"] = ""
        text10["text"] = ""
        text11["text"] = ""
        text12["text"] = ""
        text13["text"] = ""
        text14["text"] = ""
        bt2.place(x=-50,y=-50)
    else:
        text2["text"] = resp[0]
        text3["text"] = resp[1]
        text4["text"] = resp[2]
        text5["text"] = resp[3]
        text6["text"] = resp[4]
        text7["text"] = resp[5]
        text8["text"] = resp[6]
        text9["text"] = resp[7]
        text10["text"] = resp[8]
        text11["text"] = resp[9]
        text12["text"] = resp[10]
        text13["text"] = resp[11]
        text14["text"] = resp[12]
        bt2.place(x=40,y=470)

def Pro1(event):
    IP(str(caixa1.get()))
    if(resp == ""):
        text2["text"] = ""
        text3["text"] = ""
        text4["text"] = ""
        text5["text"] = ""
        text6["text"] = ""
        text7["text"] = ""
        text8["text"] = ""
        text9["text"] = ""
        text10["text"] = ""
        text11["text"] = ""
        text12["text"] = ""
        text13["text"] = ""
        text14["text"] = ""
        bt2.place(x=-50,y=-50)

    else:
        text2["text"] = resp[0]
        text3["text"] = resp[1]
        text4["text"] = resp[2]
        text5["text"] = resp[3]
        text6["text"] = resp[4]
        text7["text"] = resp[5]
        text8["text"] = resp[6]
        text9["text"] = resp[7]
        text10["text"] = resp[8]
        text11["text"] = resp[9]
        text12["text"] = resp[10]
        text13["text"] = resp[11]
        text14["text"] = resp[12]
        bt2.place(x=40,y=470)

bt1 = Button(tela,text="Procurar",bg="#096",font="Arial 12",fg="#fff",command=Pro)
bt1.place(x=410,y=50)
tela.bind("<Return>",Pro1)
tela.bind("<R>",navg1)
tela.mainloop()
