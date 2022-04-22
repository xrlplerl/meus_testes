# E necessario ter a biblioteca pillow e a qrcode para poder execultar
import sys,os,time,qrcode

if(len(sys.argv) > 2):
    if("-c" in sys.argv):
        conteudo = sys.argv[sys.argv.index("-c") + 1]
        conteudo = (conteudo.replace("_"," ")).replace("\\","\n")
    else:
        print("Use o -c 'conteudo do qr' para poder gerar o qrcode")
        exit()
    if("-i" in sys.argv):
        img = sys.argv[sys.argv.index("-i") + 1]
        if(img != "s" and img != "n"):
            print("Não existe essa opição para -i use 's' ou 'n'")
        else:
            pass
    else:
        img = "s"
    if('-n' in sys.argv):
        nome = sys.argv[sys.argv.index("-n") + 1]
    else:
        nome = "teste"
    qr = qrcode.make(conteudo)
    if(img == "s" or img == "S"):
        qr.save(f"{nome}.png")
        os.system(f"start {nome}.png")
    elif(img == "n" or img == "N"):
        qr.save(f"{nome}.png")
        os.system(f"start {nome}.png")
        time.sleep(5)
        if(sys.platform != "linux" or sys.platform != "Linux"):
            os.system(f"del {nome}.png")
        else:
            os.system(f"rm {nome}.png")
    else:
        exit()

else:
    pass