from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

# Definição de funções
def disableButton(botao):
    if(botao['state'] == DISABLED):
        botao['state'] = NORMAL
    else:
        botao['state'] = DISABLED
        
def selecionaArquivo(frame,texto):
    frame.filename = filedialog.askopenfilename(title = "Selecione o arquivo do seu firmware", filetypes = [("Arquivos .txt", ".txt"), ("Arquivos .bin", ".bin")])  
    texto.insert('end',frame.filename)
    
def gerarbinario():
    if(botao1['state']==NORMAL or botao2['state']==NORMAL or botao3['state']==NORMAL):
        response = messagebox.showinfo(title = "Mensagem", message="Seu arquivo binário foi gerado com sucesso")
    else:
        response = messagebox.showerror(title="Mensagem", message="Selecione pelo menos um arquivo")

# criação da janela
janela = Tk()
janela.title("Essa é a minha janela")
janela.geometry("540x320")

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
box1 = Checkbutton(frame1, command = lambda: disableButton(botao1))
box1.pack(padx=10, pady=10, side=LEFT, anchor=N)

# botão 1
botao1 = Button(frame1, text="Microcontrolador 1",state = DISABLED, command = lambda: selecionaArquivo(frame1, texto_p1))
botao1.pack(pady=10, padx=10, side=LEFT, anchor=N) 

# Filename 1 
texto_p1 = Text(frame1, height=1)
texto_p1.pack(expand=True, padx=10, pady=10, ipady=2, side=LEFT, anchor=N)

# frame 2
frame2 = Frame(frame_master)
frame2.pack(expand=TRUE, fill=BOTH)

# checkbox 2
box2 = Checkbutton(frame2, command = lambda: disableButton(botao2))
box2.pack(padx=10, pady=10, side=LEFT, anchor=N)

# botão 2
botao2 = Button(frame2, text="Microcontrolador 2",state = DISABLED, command = lambda: selecionaArquivo(frame2, texto_p2))
botao2.pack(pady=10, padx=10, side=LEFT, anchor=N)

# Filename 2
texto_p2 = Text(frame2, height=1)
texto_p2.pack(expand=True, padx=10, pady=10, ipady=2, side=LEFT, anchor=N)

# frame 3
frame3 = Frame(frame_master)
frame3.pack(expand=TRUE, fill=BOTH)

# checkbox 3
box3 = Checkbutton(frame3, command = lambda: disableButton(botao3))
box3.pack(padx=10, pady=10, side=LEFT, anchor=N)

# botão 3
botao3 = Button(frame3, text="Microcontrolador 3",state = DISABLED, command = lambda: selecionaArquivo(frame3, texto_p3))
botao3.pack(pady=10, padx=10, side=LEFT, anchor=N)

# Filename 3 
texto_p3 = Text(frame3, height=1)
texto_p3.pack(expand=True, padx=10, pady=10, ipady=2, side=LEFT, anchor=N)

# frame 4
frame4 = Frame(frame_master)
frame4.pack(expand=TRUE, fill=BOTH)

# botao 4
botao4 = Button(frame4, text="Gerar binário", command = gerarbinario)
botao4.pack()


janela.mainloop()
