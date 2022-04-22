from kivy.app import App
from kivy.uix.videoplayer import VideoPlayer
from bs4 import BeautifulSoup as bs
import requests,sqlite3,os

def cls():
    os.system("cls")

def URL(url):
    head = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    pag = bs(requests.get(url,headers = head).text,"html.parser")
    cont = pag.find_all("a")
    for c in cont:
        if("http://download" in str(c)):
            c = ((str(c).replace('<a aria-label="Download file" class="input popsok" href="','')).replace('">','')).replace(" ","")
            c = (c .replace("</a>","")).replace("Download","")
            c = str((c.split("\n"))[0])
            return c

class DB():
    def __init__(self,aq):
        self.aq = aq
        self.arq = sqlite3.connect(self.aq)
        self.c = self.arq.cursor()
        self.c.execute("select * from player")
        self.cont = self.c.fetchall()
    
    def li(self):
        self.li = []
        for c in self.cont:
            self.id = str(c[0])
            self.nome = str(c[1])
            self.resu = "[{}] ]---> {}".format(self.id, self.nome)
            self.li.append(self.resu)
        return self.li

    def rep(self,id):
        self.id = str(id)
        self.c.execute("select link from player where id = {};".format(self.id))
        return self.c.fetchall()

class Player(App):
    def build(self):
        video = VideoPlayer(source = url)
        video.state = "play"
        return video

cls()
dados = DB("lista.db")
for d in dados.li():
    print(d)

id = int(input("O numero do intem desejado: "))
url = str((dados.rep(id)[0])[0])
url = URL(url)
Player().run()
cls()