import requests,time,dotenv,os

dotenv.load_dotenv(dotenv.find_dotenv())

class bot():
    def __init__(self,token):
        self.token = token
        self.url = f"https://api.telegram.org/bot{self.token}"

    def ver_update(self):
        self.update = f"{self.url}/getUpdates"
        return requests.get(self.update).json()

    def send_msg(self,chat,msg):
        self.send = f"{self.url}/sendMessage?chat_id={chat}&text={msg}"
        requests.get(self.send)

    def send_img(self,chat,url):
        self.img = f"{self.url}/sendPhoto?chat_id={chat}&photo={url}"
        requests.get(self.img)
    
    def send_gif(self,chat,url):
        self.animation = f"{self.url}/sendAnimation?chat_id={chat}&photo={url}"
        requests.get(self.animation)

    def send_audio(self,chat,url):
        self.audio = f"{self.url}/sendAudio?chat_id={chat}&audio={url}"
        requests.get(self.audio)


mr = bot(os.getenv("chave"))

def ver_msg(msg):
    de = msg["message"]["from"]
    id_msg = int(msg["message"]["message_id"])
    chat = msg["message"]["chat"]
    chat_id = msg["message"]["chat"]["id"]
    text = msg["message"]["text"]
    bot_name = os.getenv("nome")
    com = """
    Ola esses são os comandos:
    * /comandos
    """

    if(text == "/comandos" or text == f"/comandos{bot_name}"):
        mr.send_msg(chat_id,com)

    elif (text == "/start" or text == f"/start{bot_name}"):
        mr.send_msg(chat_id,com)

        
    print({"chat":chat_id,"De":de,"msg":text})
        
update = 0
loop = 0

while True:
    msgs = mr.ver_update()["result"]
    if(loop == 0):
        update = (msgs[len(msgs)-1])['update_id']
        print("Iniciando o bot...")
    else:
        for msg in msgs:
            up = int(msg["update_id"])
            if(up > update):
                update = up
                ver_msg(msg)
            else:
                pass
    
        
    loop = loop + 1
    time.sleep(2)