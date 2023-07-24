import customtkinter as ctk
from tkinter import messagebox
from myframe import MyFrame
from InitFrame import InitFrame


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
