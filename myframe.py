import customtkinter as ctk
from tkinter import filedialog
from PIL import Image


# Definição de funções
def toggleCheckbox(frame):
    '''
    Controla a ativação dos widgets de acordo com a marcação na 
    checkbox
    '''

    # ativa os widgets quando a checkbox é marcada e desativa quando desmarcada
    if (frame.btn.cget('state') == ctk.DISABLED and frame.address.cget('state') == ctk.DISABLED):
        frame.btn.configure(state=ctk.NORMAL)
        frame.address.configure(state=ctk.NORMAL)
        frame.file.configure(state=ctk.NORMAL)
        frame.txt1.configure(state=ctk.NORMAL)
        frame.txt2.configure(state=ctk.NORMAL)
        frame.address.configure(placeholder_text="Endereço")
    else:
        frame.btn.configure(state=ctk.DISABLED)
        frame.address.configure(placeholder_text="")
        frame.address.configure(state=ctk.DISABLED)
        frame.file.configure(state=ctk.DISABLED)
        frame.txt1.configure(state=ctk.DISABLED)
        frame.txt2.configure(state=ctk.DISABLED)


def selecionaArquivo(frame):
    '''
    Permite a seleção de arquivos .txt e .hex 
    '''
    frame.filename = filedialog.askopenfilename(title="Selecione o arquivo do seu firmware", filetypes=[
                                                ("Arquivos .txt", ".txt"), ("Arquivos .hex", ".hex")])
    frame.file.insert('end', frame.filename)


def clear():
    for frame in MyFrame.all:
        frame.delFrame()


class MyFrame(ctk.CTkFrame):
    '''
    Cria novo frame com widgets para seleção de arquivos 
    '''

    all = []
    
    
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        MyFrame.all.append(self)

        # checkbox
        self.checkbox = ctk.CTkCheckBox(
            self, text='', command=lambda: toggleCheckbox(self), height=35, width=25)
        self.checkbox.pack(padx=10, pady=10, side=ctk.LEFT, anchor=ctk.N)

        # primeira entrada de texto (endereço)
        self.address = ctk.CTkEntry(
            self, state=ctk.DISABLED, height=35, width=70)
        self.address.pack(expand=True, padx=10, pady=10,
                          side=ctk.LEFT, anchor=ctk.N)

        # botão para abrir a seleção de arquivos
        self.btn = ctk.CTkButton(
            self, text="Escolher Arquivo", state=ctk.DISABLED, height=35, command=lambda: selecionaArquivo(self))
        self.btn.pack(pady=10, padx=10, side=ctk.LEFT, anchor=ctk.N)

        # campo de texto que exibe o path do arquivo selecionado
        self.file = ctk.CTkEntry(self, state=ctk.DISABLED, height=35)
        self.file.pack(expand=True, padx=10, pady=10,
                       side=ctk.LEFT, anchor=ctk.N)

        # segunda entrada de texto
        self.txt1 = ctk.CTkEntry(self, state=ctk.DISABLED, height=35, width=60)
        self.txt1.pack(expand=True, padx=10, pady=10,
                       side=ctk.LEFT, anchor=ctk.N)

        # terceira entrada de texto
        self.txt2 = ctk.CTkEntry(self, state=ctk.DISABLED, height=35, width=60)
        self.txt2.pack(expand=True, padx=10, pady=10,
                       side=ctk.LEFT, anchor=ctk.N)

        # botão para apagar o frame
        img = ctk.CTkImage(Image.open('img\excluir.png'), size=(20, 20))
        self.bin = ctk.CTkButton(
            self, text='', image=img, width=35, height=35, command=lambda: self.delFrame())
        self.bin.pack(pady=10, padx=10, side=ctk.LEFT, anchor=ctk.N)
    
    
    def delFrame(self):
        '''
        Retira o respectivo frame seletor da janela 
        '''
        self.all.remove(self)
        self.pack_forget()