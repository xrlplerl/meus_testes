from DI import * #O arquivo DI que foi importado em um arquivo biblioteca
url = str(input('URL: '))
n = str(input('Nome do arquivo a ser salvo: '))
t = str(input('Digite o formato do arquivo: '))
loc = str(input('Local do save: '))
img = Img(url,n,t,loc)
img.Download()