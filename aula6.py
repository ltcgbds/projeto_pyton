import tkinter as tk
import mysql.connector

def conexao():
    try:
            conexao = mysql.connector.connect(
                        host = "localhost" , 
                        user = " root",
                        passwd = "",
                        db = "Usuarios"
            )
            print("conectado")
            return conexao
    except mysql.connector.Error as e:
                print(f'Error ao conectar no Servidor')

def createNewWindow():
    newWindow =tk.Toplevel(app)

def cadastroUsuarios():
    janelaUsuarios = tk.Toplevel(app)

    LabelMsg = tk.Label (janelaUsuarios,text="Informe seu nome:"
    ,font="Times"
    ,bg="orange",foreground="black")
    LabelMsg.place(x=1,y=1)

    entryNome = tk.Entry(janelaUsuarios)
    entryNome.place ( x=119,y=5)

    lblSobrenome = tk.Label(janelaUsuarios,text= "informe seu sobrenome:"
    ,font="Times"
    ,bg="orange",foreground= "black")
    lblSobrenome.place(x=1,y=30)

    entrySobrenome = tk.Entry(janelaUsuarios)
    entrySobrenome.place ( x=153,y=33)

    lblDataNascimento= tk.Label (janelaUsuarios,text="Informe sua Data de Nascimento:"
    ,font="Times"
    ,bg="orange",foreground="black")
    lblDataNascimento.place(x=1,y=57)

    entryDataNascimento = tk.Entry(janelaUsuarios)
    entryDataNascimento.place ( x=210,y=63)

    lblCidade= tk.Label (janelaUsuarios,text="Informe sua Cidade:"
    ,font="Times"
    ,bg="orange",foreground="black")
    lblCidade.place(x=1,y=84)

    entryCidade = tk.Entry(janelaUsuarios)
    entryCidade.place ( x=133,y=88)

    lblEstado= tk.Label (janelaUsuarios,text="Informe seu Estado:"
    ,font="Times"
    ,bg="orange",foreground="black")
    lblEstado.place(x=1,y=111)

    entryEstado = tk.Entry(janelaUsuarios)
    entryEstado.place ( x=131,y=113)

    janelaUsuarios.title("Cadastro de Usuários")
    janelaUsuarios.geometry("800x600")

def cadastroProdutos():
    janelaProdutos = tk.Toplevel(app)
    janelaProdutos.title("Cadastro de Produtos")
    janelaProdutos.geometry("800x600")

def salvarUsurio():
    conn = conexao()
    print( " O nome informado foi:",entryNome.get())
    print("O sobrenome informado fi:", entrySobrenome.get())
    print("A Data de nascimento imformada foi:". entryDatadenascimento.get())
    print(" A cidade informada foi:", entryCidade.get())
app = tk.Tk() 

menuPrincipal = tk.Menu(app)
app.config(menu=menuPrincipal)

fileMenu = tk.Menu(menuPrincipal)
fileMenu.add_command(label="cadastrar Usuarios"
        ,command=cadastroUsuarios)
fileMenu.add_command(label="cadastrar Produtos.+"
        ,command=cadastroProdutos)
menuPrincipal.add_cascade(label="função" 
                        ,menu=fileMenu)


buttonExample = tk.Button(app,
                    text="Creat new window" ,
                    command=createNewWindow)
buttonExample.place(x=100,y=50)
app.title("Sistema Tarumã")
app.geometry("800x600")
app.mainloop()
app.destroy()



