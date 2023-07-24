import customtkinter as ctk
from myframe import MyFrame


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
