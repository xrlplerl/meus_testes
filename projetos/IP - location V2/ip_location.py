from bs4 import BeautifulSoup as bs
import requests,sys,os,webbrowser

if(len(sys.argv) > 1):
    if("-i" in sys.argv):
        ip = str(sys.argv[sys.argv.index("-i")+1])
    else:
        print("Passe o ip com -i [IP] ou execulte o arquivo e espere a solicitação do ip!")
        exit()
else:
    ip = str(input("Digite o ip: "))
try:
    print("\n")
    head = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    pagina = bs(requests.get("https://ipapi.com/ip_api.php?ip={}".format(ip),headers=head).text,"html.parser")
    cont = str(pagina).replace("{","")
    cont = cont.replace("}","")
    cont = cont.replace("'","")
    cont = cont.replace('"',"")
    cont = cont.split(",")
    for c in range(0,13):
        try:
            print(cont[c])
        except:
            pass
    l = [cont[11],cont[12]]
    la = (l[0].split(":"))[1]
    lo = (l[1].split(":"))[1]
    desj = str(input("\nVocê deseja ver essas coordenadas no google maps Y para sim e N para não: "))
    if(desj == ("y" or "Y")):
        webbrowser.open("https://www.google.com.br/maps/search/?api=1&query={},{}".format(la,lo))
    elif(desj == ("n" or "N")):
        exit()
    else:
        pass

except:
    pass

input()

