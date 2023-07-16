from tkinter import *

# criação da janela
janela = Tk()
janela.title("Essa é a minha janela")
janela.geometry("600x400")

# frame geral
frame_master = Frame(janela, borderwidth=5, relief="ridge")
frame_master.pack(fill=BOTH, expand=TRUE)

# primeiro texto
texto_inicial = Label(frame_master, text="Files(Download)")
texto_inicial.pack(anchor=NW)

# frame 1
frame1 = Frame(frame_master)
frame1.pack(expand=TRUE, fill=BOTH)

# checkbox 1
box1 = Checkbutton(frame1)
box1.pack(padx=10, pady=10, side=LEFT, anchor=N)

# controlador 1
texto_c1 = Label(frame1, text="controlador 1")
texto_c1.pack(padx=10, pady=10, ipady=2, side=LEFT, anchor=N)

# botão 1
botao1 = Button(frame1, text="selecionar aquivo")
botao1.pack(pady=10, padx=10, side=LEFT, anchor=N)

# frame 2
frame2 = Frame(frame_master, background="yellow")
frame2.pack(expand=TRUE, fill=BOTH)

# checkbox 2
box2 = Checkbutton(frame2)
box2.pack(padx=10, pady=10, side=LEFT, anchor=N)

# controlador 2
texto_c2 = Label(frame2, text="controlador 1")
texto_c2.pack(padx=10, pady=10, ipady=2, side=LEFT, anchor=N)

# botão 2
botao2 = Button(frame2, text="selecionar aquivo")
botao2.pack(pady=10, padx=10, side=LEFT, anchor=N)

# frame 3
frame3 = Frame(frame_master, background="cyan")
frame3.pack(expand=TRUE, fill=BOTH)

# checkbox 3
box3 = Checkbutton(frame3)
box3.pack(padx=10, pady=10, side=LEFT, anchor=N)

# controlador 3
texto_c3 = Label(frame3, text="controlador 1")
texto_c3.pack(padx=10, pady=10, ipady=2, side=LEFT, anchor=N)

# botão 3
botao3 = Button(frame3, text="selecionar aquivo")
botao3.pack(pady=10, padx=10, side=LEFT, anchor=N)


janela.mainloop()
