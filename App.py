import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from myframe import MyFrame
from InitFrame import InitFrame

def onOpen():
    print(filedialog.askopenfilename(initialdir = "/",title = "Abrir arquivo",filetypes = (("Arquivos .lesc","*.lesc"),("Todos os arquivos","*.*"))))
 
def onSave():
    data = [('Arquivos .lesc', '*.lesc')]
    file = filedialog.asksaveasfilename(initialdir = "/",title = "Salvar como",filetypes = data, defaultextension = data)
    with open(file, "w") as f:
        f.write("teste")

def gerarbinario():
    for frame in MyFrame.all:
        if (frame.btn.cget('state') == ctk.NORMAL):
            response = messagebox.showinfo(
                title="Mensagem", message="Seu arquivo binário foi gerado com sucesso")
            return

    response = messagebox.showerror(
        title="Mensagem", message="Selecione pelo menos um arquivo")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("Essa é a minha janela")
        self.iconbitmap("weg-logo-5.ico")
        self.init_frame = InitFrame(
            master=self, corner_radius=0, fg_color="transparent")
        self.init_frame.pack(fill=ctk.BOTH, expand=ctk.TRUE)
        self.generate_binary = ctk.CTkButton(
            self, text="Gerar Binário", command=gerarbinario)
        self.generate_binary.pack(pady=10, padx=10)
        self.menubar = tk.Menu(self)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Abrir arquivo", command=onOpen)
        self.filemenu.add_command(label="Salvar", command=onSave)
        self.menubar.add_cascade(label="Arquivo", menu=self.filemenu)
        self.config(menu=self.menubar)



app = App()
app.mainloop()
