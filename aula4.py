from tkinter import * 
janela = Tk ()
janela["bg"] = "orange"
app = Frame (janela)
app.grid()

def escrever():
    print(entryNome.get())
    print(entryIdade.get())

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

