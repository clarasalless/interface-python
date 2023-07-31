import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from myframe import MyFrame
from InitFrame import InitFrame
from MenuFrame import MenuFrame


# aparêcia
ctk.set_appearance_mode('light')

# Definição de funções


def gerarbinario():
    '''
    Função chamada pelo botão gerar binário
    '''
    for frame in MyFrame.all:
        if not str(frame.file.get(1.0, ctk.END)).isspace():
            response = messagebox.showinfo(
                title="Mensagem", message="Seu arquivo binário foi gerado com sucesso")
            return

    response = messagebox.showerror(
        title="Mensagem", message="Selecione pelo menos um arquivo")


class App(ctk.CTk):
    """
    Janela principal
    """

    def __init__(self):
        super().__init__()
        # configuração inicial
        self.geometry("800x600")
        self.title("Seleção de Arquivos")
        self.iconbitmap("img\weg-logo-5.ico")

        self.menu = MenuFrame(master=self)
        self.menu.pack(fill=ctk.BOTH)

        # frame global que contém todos os seletores de arquivos
        self.init_frame = InitFrame(
            master=self, corner_radius=0, fg_color="transparent")
        self.init_frame.pack(fill=ctk.BOTH, expand=ctk.TRUE)

        # botão para a função de gerar arquivo binário
        self.generate_binary = ctk.CTkButton(
            self, text="Gerar Binário", command=gerarbinario)
        self.generate_binary.pack(pady=10, padx=10)

        # menubar
        # self.menubar = tk.Menu(self, background='blue')
        # self.filemenu = tk.Menu(self.menubar, tearoff=0)
        # self.filemenu.add_command(label="Abrir arquivo", command=onOpen)
        # self.filemenu.add_command(label="Salvar", command=onSave)
        # self.menubar.add_cascade(label="Arquivo", menu=self.filemenu)
        # self.config(menu=self.menubar)


# janela funcionando
app = App()
app.mainloop()
