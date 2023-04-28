from tkinter import *
from tkinter import ttk

#Criando janela
janela = Tk()
janela.geometry("500x400")#500px de largura e 350px de altura
janela.resizable(width=False, height=False)#Usuário não pode alterar o tamanho da tela
janela.title("Índice de massa corporal") #Título
janela.iconbitmap("icone.ico") #Definindo o icone
janela.configure(bg="#483D8B") #Definindo cor de fundo



#Lógica do Programa
def calcula():
    #Pegando a Altura e Peso dos Entrys
    altura = float(e_altura.get().replace(",",".")) #Replace para caso a pessoa digite vírgula invés de ponto o programa executar da mesma forma
    peso = float(e_peso.get().replace(",", "."))

    
    #Fazendo o Calculo do IMC
    imc= float("{:.2f}".format(peso / (altura*altura)))#Uma pequena alteração com o "{:.2f}" para o resultado sair com somente 2 casas decimais

    l_imc["text"] = imc #Passando o valor para a label que imprime na tela

    #Vendo se o IMC é bom ou não
    if imc < 18.5:
        l_resultado["text"] = "Seu IMC é: Abaixo do Peso Ideal" #Passando o valor para a label que imprime na tela
    elif imc < 24.9:
        l_resultado["text"] = "Seu IMC é: Peso Ideal" #Passando o valor para a label que imprime na tela
    elif imc < 29.9:
        l_resultado["text"] = "Seu IMC é: Sobrepeso" #Passando o valor para a label que imprime na tela
    elif imc < 39.9:
        l_resultado["text"] = "Seu IMC é: Obesidade" #Passando o valor para a label que imprime na tela
    else:
        l_resultado["text"] = "Seu IMC é: Obesidade Mórbida" #Passando o valor para a label que imprime na tela




def limpar():
    #Varíavel para limpar os valores da tela

    l_imc["text"] = "00.00"
    l_resultado["text"] = "Seu IMC é:"
    
    #O método Delete exclue os valores de um Entry, ai colocamos como parametro (0, END) para que depois da exclusão não fique nenhum valor como "0" na caixa
    e_altura.delete(0, END) 
    e_peso.delete(0, END)



#Divindo a tela em dois frames e 1 bordas

#Borda cima

borda_cima = Frame(janela, width=500, height=20, bg="#483D8B")
borda_cima.grid(row=0, column=0)

#Primeiro Frame

frame_cima = Frame(janela, width=460, height=80,bg="#FFFFFF",)
frame_cima.grid(row=1, column=0)


#Frame do meio

borda_meio = Frame(janela, width=500, height=20, bg="#483D8B")
borda_meio.grid(row=2, column=0)

#Segundo Frame
frame_baixo = Frame(janela, width=460, height=260, bg='#FFFFFF')
frame_baixo.grid(row=3, column=0)




#Configurando a label de Cima

l_cima = Label(frame_cima, text="Calculadora de IMC", width=28, height=2, padx=0, 
               relief="flat", anchor="center", font="Arial 20 bold", bg="#FFFFFF")
l_cima.place(x=0, y=0)



#Configurando as labels de Baixo


l_altura = Label(frame_baixo, text="Insira sua Altura:", font="Arial 12 bold", fg="#484D8B", bg="#FFFFFF")
l_altura.place(x=20, y=12)


l_peso = Label(frame_baixo, text="Insira seu Peso(KG):", font="Arial 12 bold", fg="#484D8B", bg="#FFFFFF")
l_peso.place(x=20, y=50)



#Configurando label do Resultado

l_imc = Label(frame_baixo, text="00.00", width=11, height=3, bg="#484D8B", 
                    font="Arial 20 bold", fg="#FFFFFF")
l_imc.place(x=255, y=10)



# Configurando as entry de baixo

e_altura = Entry(frame_baixo, width=5, relief=SOLID) #Entry da altura
e_altura.place(x=199, y=14)


e_peso = Entry(frame_baixo,width=5, relief=SOLID) #Entry do Peso
e_peso.place(x=199, y=54)


#Configurando botão de calcular

b_calcula = Button(frame_baixo, text="Calcular IMC", width=42, height=1, fg="#FFFFFF", bg="#484D8B",
                   font="Arial 12 bold", relief=SOLID, overrelief=RIDGE, bd=4, command=calcula)
b_calcula.place(x=12, y=210)


#Configurando botão de limpar

b_calcula = Button(frame_baixo, text="Limpar IMC", width=42, height=1, fg="#FFFFFF", bg="#484D8B",
                   font="Arial 12 bold", relief=SOLID, overrelief=RIDGE, bd=4, command=limpar)
b_calcula.place(x=12, y=160)


#Configurando label do resultado da IMC
l_resultado = Label(frame_baixo, text="Seu IMC é: ", font="Arial 12 bold", 
                    fg="#484D8B", bg="#FFFFFF")
l_resultado.place(x=20, y=120)


janela.mainloop()