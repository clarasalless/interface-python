import customtkinter as ctk
from myframe import MyFrame


# Definição de funções
def addFrame(master):
    '''
    Adiciona um novo frame seletor de arquivos no frame inicial
    '''
    new_frame = MyFrame(master)
    new_frame.pack(fill=ctk.BOTH, expand=ctk.TRUE)


class InitFrame(ctk.CTkScrollableFrame):
    '''
    Frame inicial que contém o primeiro seletor de arquivos
    e pode adicionar novos frames seletores
    '''

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # cria o primeiro seletor de arquivos
        self.frameteste = MyFrame(self)
        self.frameteste.pack(fill=ctk.BOTH, expand=ctk.TRUE)

        # botão para adicionar novo frame
        self.add_frame = ctk.CTkButton(
            self, text="+", width=35, command=lambda: addFrame(self))
        self.add_frame.pack(side=ctk.BOTTOM)
