import customtkinter as ctk
from tkinter import filedialog
from PIL import Image


def onOpen():
    '''
    Procurar um arquivo .lesc
    '''
    print(filedialog.askopenfilename(initialdir="/", title="Abrir arquivo",
          filetypes=(("Arquivos .lesc", "*.lesc"), ("Todos os arquivos", "*.*"))))


def onSave():
    '''
    Salva um arquivo .lesc
    '''
    data = [('Arquivos .lesc', '*.lesc')]
    file = filedialog.asksaveasfilename(
        initialdir="/", title="Salvar como", filetypes=data, defaultextension=data)
    with open(file, "w") as f:
        f.write("teste")


def fileButtonAction(self):
    salvar = ctk.CTkButton(
        self.option_frame, image=ctk.CTkImage(
            Image.open('img\salvar.png'), size=(40, 40)), text='Salvar',
        height=70, width=70, text_color=('gray10', 'gray70'), fg_color='transparent', hover_color=("gray60", "gray80"), command=onSave)
    salvar.pack(side=ctk.LEFT)
    carregar = ctk.CTkButton(
        self.option_frame, image=ctk.CTkImage(
            Image.open('img\envio.png'), size=(45, 45)), text='Carregar',
        height=70, width=70, text_color=('gray10', 'gray70'), fg_color='transparent', hover_color=("gray60", "gray80"), command=onOpen)
    carregar.pack(side=ctk.LEFT)
    self.arquivo.configure(state=ctk.DISABLED)


class MenuFrame(ctk.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.configure(height=100)

        self.logo = ctk.CTkImage(
            light_image=Image.open('img\logo-weg-512.png'), dark_image=Image.open('img\logo-weg-512.png'),
            size=(90, 90))
        self.logo_label = ctk.CTkLabel(
            self, image=self.logo, text="")
        self.logo_label.pack(side=ctk.LEFT, anchor=ctk.N, padx=5, pady=5)

        self.frame_menu = ctk.CTkFrame(self, height=100)
        self.frame_menu.pack(side=ctk.LEFT, fill=ctk.X, expand=ctk.TRUE)

        self.menu = ctk.CTkFrame(
            self.frame_menu, height=25, corner_radius=0)
        self.menu.pack(fill=ctk.X, expand=ctk.TRUE)

        self.arquivo = ctk.CTkButton(
            self.menu, text='Arquivo', height=30, width=70, corner_radius=0, text_color=('gray10', 'gray70'),
            fg_color='transparent', hover_color=("gray60", "gray80"), command=lambda: fileButtonAction(self))
        self.arquivo.pack(side=ctk.LEFT, anchor=ctk.N)

        self.option_frame = ctk.CTkFrame(
            self.frame_menu, height=70, corner_radius=0)
        self.option_frame.pack(fill=ctk.BOTH, expand=ctk.TRUE)
