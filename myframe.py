import customtkinter as ctk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image


# Definição de funções
def disableButton(button):
    if (button.cget('state') == ctk.DISABLED):
        button.configure(state=ctk.NORMAL)
    else:
        button.configure(state=ctk.DISABLED)


def selecionaArquivo(frame, texto):
    frame.filename = filedialog.askopenfilename(title="Selecione o arquivo do seu firmware", filetypes=[
                                                ("Arquivos .txt", ".txt"), ("Arquivos .bin", ".bin")])
    texto.insert('end', frame.filename)


def gerarbinario():
    for frame in MyFrame.all:
        if (frame.btn.cget('state') == ctk.NORMAL):
            response = messagebox.showinfo(
                title="Mensagem", message="Seu arquivo binário foi gerado com sucesso")
            return

    response = messagebox.showerror(
        title="Mensagem", message="Selecione pelo menos um arquivo")


def addFrame(master):
    new_frame = MyFrame(master)
    new_frame.pack(fill=ctk.BOTH, expand=ctk.TRUE)
    MyFrame.all.append(new_frame)


class InitFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame...
        self.frameteste = MyFrame(self)
        self.frameteste.pack(fill=ctk.BOTH, expand=ctk.TRUE)
        MyFrame.all.append(self.frameteste)

        self.add_frame = ctk.CTkButton(
            self, text="+", width=35, command=lambda: addFrame(self))
        self.add_frame.pack(side=ctk.BOTTOM)


class MyFrame(ctk.CTkFrame):
    all = []

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame, for example:
        self.checkbox = ctk.CTkCheckBox(
            self, text='', command=lambda: disableButton(self.btn), height=35, width=25)
        self.checkbox.pack(padx=10, pady=10, side=ctk.LEFT, anchor=ctk.N)

        self.address = ctk.CTkTextbox(self, height=35, width=60)
        self.address.pack(expand=True, padx=10, pady=10,
                          side=ctk.LEFT, anchor=ctk.N)

        self.btn = ctk.CTkButton(
            self, text="Escolher Arquivo", state=ctk.DISABLED, height=35, command=lambda: selecionaArquivo(self, self.text))
        self.btn.pack(pady=10, padx=10, side=ctk.LEFT, anchor=ctk.N)

        self.file = ctk.CTkTextbox(self, height=35)
        self.file.pack(expand=True, padx=10, pady=10,
                       side=ctk.LEFT, anchor=ctk.N)

        img = ctk.CTkImage(Image.open('excluir.png'), size=(20, 20))
        self.bin = ctk.CTkButton(
            self, text='', image=img, width=35, height=35)
        self.bin.pack(pady=10, padx=10, side=ctk.LEFT, anchor=ctk.N)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")
        self.title("Essa é a minha janela")
        self.iconbitmap("weg-logo-5.ico")

        init_label = ctk.CTkLabel(
            self, text="Files(Download)", padx=5, pady=5)
        init_label.pack(anchor=ctk.NW)
        self.init_frame = InitFrame(
            master=self, corner_radius=0, fg_color="transparent")
        self.init_frame.pack(fill=ctk.BOTH, expand=ctk.TRUE)
        self.generate_binary = ctk.CTkButton(
            self, text="Gerar Binário", command=gerarbinario)
        self.generate_binary.pack(pady=10, padx=10)


app = App()
app.mainloop()
