from tkinter import * 
janela = Tk ()
janela["bg"] = "orange"
app = Frame (janela)
app.grid()


menuPrincipal = Menu(app)
janela.config(menu=menuPrincipal)

fileMenu = Menu(menuPrincipal)
fileMenu.add_command(label="cadastrar", command=iniciarTelaCadastro)
menuPrincipal.add_cascade(label="função" ,menu=fileMenu)

def escrever():
    print("O meu nome é;", entryNome.get()
    , "e minha idade é:", entryIdade.get())
    
    

LabelMsg = Label (janela,text="Informe seu nome:",font="Times",
bg="orange",foreground="black")
LabelMsg.place(x=1,y=1)

entryNome = Entry(janela)
entryNome.place ( x=119,y=1)

LabelMsg = Label (janela,text="Informe sua idade:",font="Times",
bg="orange",foreground="black")
LabelMsg.place(x=1,y=30)

entryIdade = Entry(janela)
entryIdade.place ( x=118, y= 33)

btnFalarNome = Button(janela,width=20,text= "Clicar", command=escrever)
btnFalarNome.place(x=100,y=58)

title="Sistema Tarumã"                               
janela.title(title)
janela.geometry("800x400")
janela.resizable(False,False)
janela.mainloop()
janela.destroy()

