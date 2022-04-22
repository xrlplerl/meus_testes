from pytube import YouTube

local = str(input('Caminho de onde sera salvo: '))
link = str(input('LINK: '))

yt = YouTube(link)
video = yt.streams.get_highest_resolution()
video.download(local)