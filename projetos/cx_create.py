import sys,os

bas = None
if(len(sys.argv) >= 2):
    if("-p" in sys.argv):
        pak = (sys.argv[int(sys.argv.index("-p"))+1]).split(",")
    else:
        pak = []
    if("-i" in sys.argv):
        inc = (sys.argv[int(sys.argv.index("-i"))+1]).split(",")
    else:
        inc = []
    if("-f" in sys.argv):
        files = (sys.argv[int(sys.argv.index("-f"))+1]).split(",")
    else:
        files = []
    if("-v" in sys.argv):
        ver = sys.argv[int(sys.argv.index("-v"))+1]
    else:
        ver = "1.0"
    if("-d" in sys.argv):
        des = sys.argv[int(sys.argv.index("-d"))+1]
    else:
        des = ""
    if("-ico" in sys.argv):
        icon = sys.argv[int(sys.argv.index("-ico"))+1]
    else:
        icon = ""
    if("-w" in sys.argv):
        if sys.platform == "win32":
            bas = "Win32GUI"
    else:
        pass
    if("-h" in sys.argv):
        print("\n[+] ====> use -n para declarar o nome do aquivo.py\n[+] ====> -p para incluir as bibliotecas a serem importadas ex: tkinter,pyttsx3\n[+] ====> -i para includes\n[+] ====> -f para incluir arquivos\n[+] ====> -v para declarar a versão do aplicação\n[+] ====> -d para descição\n[+] ====> -w caso queira usar interface grafica\n[+] ====> -ico para declarar o icone desejado")
        exit()
    else:
        pass
    if("-n" in sys.argv):
        nome = sys.argv[int(sys.argv.index("-n"))+1]
    else:
        print("[!] ]====> E necessario declarar o nome do arquivo com -n")
        exit()
else:
    print("\n[+] ====> use -n para declarar o nome do aquivo.py\n[+] ====> -p para incluir as bibliotecas a serem importadas ex: tkinter,pyttsx3\n[+] ====> -i para includes\n[+] ====> -f para incluir arquivos\n[+] ====> -v para declarar a versão do aplicação\n[+] ====> -d para descrição\n[+] ====> -w caso queira usar interface grafica\n[+] ====> -ico para declarar o icone desejado")
    exit()

topo = """
from cx_Freeze import setup, Executable
from cx_Freeze.dist import build_exe
import sys
"""
for p in pak:
    topo = topo + f"import {p}\n"

base = f"""
executable = [Executable('{nome}', base = '{bas}', icon = '{icon}')]
buildOptions = dict(packages = {pak},includes = {inc},include_files={files},excludes = [])
setup(name = '{str(nome.replace(".py",""))}',version='{ver}',description='{des}',options=dict(build_exe = buildOptions),executables=executable)
"""
a = open("setup.py","w")
a.write(topo+base)
a.close()

os.system("py setup.py build")
os.system("del setup.py")