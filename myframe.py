import customtkinter as ctk
from tkinter import filedialog
from PIL import Image


# Definição de funções
def toggleCheckbox(button, entry):
    if (button.cget('state') == ctk.DISABLED and entry.cget('state') == ctk.DISABLED):
        button.configure(state=ctk.NORMAL)
        entry.configure(state=ctk.NORMAL)
        entry.configure(placeholder_text="Endereço")
    else:
        button.configure(state=ctk.DISABLED)
        entry.configure(placeholder_text="")
        entry.configure(state=ctk.DISABLED)


def selecionaArquivo(frame, texto):
    frame.filename = filedialog.askopenfilename(title="Selecione o arquivo do seu firmware", filetypes=[
                                                ("Arquivos .txt", ".txt"), ("Arquivos .hex", ".hex")])
    texto.insert('end', frame.filename)


def delFrame(frame):
    frame.pack_forget()


class MyFrame(ctk.CTkFrame):
    all = []

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame, for example:
        self.checkbox = ctk.CTkCheckBox(
            self, text='', command=lambda: toggleCheckbox(self.btn, self.address), height=35, width=25)
        self.checkbox.pack(padx=10, pady=10, side=ctk.LEFT, anchor=ctk.N)

        self.address = ctk.CTkEntry(
            self, state=ctk.DISABLED, height=35, width=70)
        self.address.pack(expand=True, padx=10, pady=10,
                          side=ctk.LEFT, anchor=ctk.N)

        self.btn = ctk.CTkButton(
            self, text="Escolher Arquivo", state=ctk.DISABLED, height=35, command=lambda: selecionaArquivo(self, self.file))
        self.btn.pack(pady=10, padx=10, side=ctk.LEFT, anchor=ctk.N)

        self.file = ctk.CTkTextbox(self, height=35)
        self.file.pack(expand=True, padx=10, pady=10,
                       side=ctk.LEFT, anchor=ctk.N)

        self.txt1 = ctk.CTkTextbox(self, height=35, width=60)
        self.txt1.pack(expand=True, padx=10, pady=10,
                       side=ctk.LEFT, anchor=ctk.N)

        self.txt2 = ctk.CTkTextbox(self, height=35, width=60)
        self.txt2.pack(expand=True, padx=10, pady=10,
                       side=ctk.LEFT, anchor=ctk.N)

        img = ctk.CTkImage(Image.open('excluir.png'), size=(20, 20))
        self.bin = ctk.CTkButton(
            self, text='', image=img, width=35, height=35, command=lambda: delFrame(self))
        self.bin.pack(pady=10, padx=10, side=ctk.LEFT, anchor=ctk.N)
