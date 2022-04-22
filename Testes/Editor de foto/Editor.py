from os import path
from PIL import Image, ImageEnhance

class Editor():
    img = None
    img_formato = None
    img_local = None
    img_nome = None
    img_ext = None

    def resetar(self):
        self.img = None
        self.img_formato = None
        self.img_local = None
        self.img_nome = None
        self.img_ext = None

    def carregar_imagem(self,imagem):
        try:
            self.img = Image.open(imagem)
            self.img_formato = self.img.format
            self.img_local = path.dirname(path.realpath(imagem))
            self.img_nome,self.img_ext = path.splitext(path.basename(imagem))
            print("Imagem carregada!")
            return True
        except:
            print("Falha ao carregar a imagem.")
            return False

    def girar_imagem(self,sentido,angulo = 90):
        if(sentido == "horario"):
            self.img = self.img.rotate(angulo * -1,expand = True)
        else:
            self.img = self.img.rotate(angulo,expand = True)

    def remover_cor_imagem(self):
        conversor = ImageEnhance.Color(self.img)
        self.img = conversor.enhance(0)

    def salvar(self,local,nome_image):
        ln = local + "/" + nome_image + self.img_ext
        self.img.save(ln,self.img_formato)
        self.resetar()

ed = Editor()
ed.carregar_imagem("lobo3.jpg")
ed.girar_imagem("horario")
ed.girar_imagem("horario")
ed.remover_cor_imagem()
ed.img.show()
ed.salvar(ed.img_local,ed.img_nome + "_Editada")
