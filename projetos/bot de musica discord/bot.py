from discord.ext import commands
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL
import discord,sys,threading,time,dotenv,os

dotenv.load_dotenv(dotenv.find_dotenv())

exe = ""

if(sys.platform == "win32"):
    exe = "windows/bin/ffmpeg.exe"
else:
    exe = "linux/bin/ffmpeg"

def teste_fun(r):
    n = dir(r)
    for ops in n:
        print(ops)

bot = commands.Bot("/")

@bot.event
async def on_ready():
    print('oi')

@bot.event
async def on_message(message):
    if(message.author != bot.user):
        await bot.process_commands(message)
    else:
        pass

@bot.command(name="in")
async def entrar_voz(ctx):
    try:
        canal = ctx.author.voice.channel
        await canal.connect()
    except:
        await ctx.send("Você não está em um chat de voz!")
        return ""

@bot.command(name="play")
async def play(ctx,url):
    async def musica(ctx,url):
        ydl = {'format':'bestaudio'}
        FFMPEG_OPTION = {'before_options':'-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options':'-vn'}
        with YoutubeDL(ydl) as y:
            info = y.extract_info(url,download=False)
            url2 = info['formats'][0]['url']
            ctx.voice_client.play(FFmpegPCMAudio(url2,**FFMPEG_OPTION,executable=exe))
    await musica(ctx,url)

@bot.command(name='out')
async def sair_voz(ctx):
    try:
        await ctx.voice_client.disconnect()
    except:
        ctx.send("O bot precisa está no canal para poder ser removido!")
    

bot.run(os.getenv("token"))