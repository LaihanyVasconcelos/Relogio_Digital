from tkinter import *
import tkinter
from datetime import datetime

#add font digital
import pyglet 
pyglet.options['win32_gdi_font'] = True
pyglet.font.add_file("digital-7.ttf")


#cores
cor1 = "#3d3d3d" #preto
cor2 = "#fafcff" #branco
cor3 = "#9703ad" #roxo
fundo = cor1
cor = cor3

#criando a janela
janela=Tk()
janela.title("Relógio Digital") #titulo do app
janela.geometry("440x180") #tamanho do app
janela.resizable(width=FALSE, height=FALSE) #nao alterar o tamanho do app
janela.configure(bg=cor1)
#criando função
def relogio():
    #variavel
    tempo = datetime.now()

    #para obter a hora.  
    hora = tempo.strftime("%H:%M:%S")
    #obter dia da semana.  A= dia da semana
    dia_semana = tempo.strftime("%A")
    dia = tempo.day
    #obter mes da semana
    mes = tempo.strftime("%B")
    #obter o ano. Y= anos em ingles
    ano = tempo.strftime("%Y")

    label1.config(text=hora)     
    #passando a hora estatica para dinamica (para ela sempre ficar mudando)
    label1.after(200, relogio) #recursão
    #intervalo  no caso:depois de 200 milessimos vai ter que executar a função relogio denovo
    label2.config(text=dia_semana +"  " + str(dia) + "/" + str(mes) + "" + str(ano))

#label de mostrar a hora
label1 =Label(janela, text="", font=("digital-7", 110), bg=fundo, fg =cor)
label1.grid(row=0, column=0, sticky=NW, padx=5) 

#label de mostrar o dia da semana
label2 =Label(janela, text="", font=("digital-7", 17), bg=fundo, fg =cor)
label2.grid(row=1, column=0, sticky=NW, padx=5) 

#para torna-lo um relogio digital esteticamente, baixei font de letras e numeros digitais,
#e tbm baixei uma bilioteca de python (pygle) pelo terminal
#apos isso importei a fonte la em cima dentro da minha aplcação
relogio()
janela.mainloop()
