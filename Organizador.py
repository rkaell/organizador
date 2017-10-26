#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Criado por Rhuann Kael Souza Nascimento - 11/10/2017 - 15:36
Atualização 18/10/2017 - 10:38
"""
from tkinter import *
import tkinter.filedialog
from tkinter import messagebox as mBox
import os
import datetime


#FUNÇÕES - Backend_____________________________________________________________________________________________________________
"""Entrada de dados"""
#Função Verificando Pastas
def verif_criar_pasta(anos):
    anos = int(anos)
    a = int(datetime.date.today().year) - anos
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    try:
        while a >= 0:
            if os.path.exists(str(a + anos)):
                print("renomear a pasta %s existente" % (a + anos), file=open("galeria.log", "a"))
            else:
                print("criando_pasta %s" % (a + anos), file=open("galeria.log", "a"))
                os.mkdir(str(anos + a))
                for mes in meses:
                    os.mkdir(str(anos + a)+"/%s" % mes)
                    print("criada subpasta de %s" % mes, file=open("galeria.log", "a"))
                print("pasta criada", file=open("galeria.log", "a"))
            a = a - 1
    except:
        print("erro", file=open("galeria.log", "a"))

"""........................................................................................................................."""
#Função para mover arquivos
def lendo_arquivos_movendo():
    files = os.listdir(os.getcwd())
    try:
        files.remove("galeria.log")
        files.remove("Galeria.py")
    except:
        print("arquivo não existe")
    for arquivo in files:
        try:
            arq = str(datetime.datetime.fromtimestamp(os.path.getmtime(arquivo)))
            if os.path.isfile(arquivo):
                src_file = os.getcwd()+"\\"+arquivo
                meses = {"Janeiro": "01", "Fevereiro": "02", "Março": "03", "Abril": "04", "Maio": "05", "Junho": "06",
                     "Julho": "07", "Agosto": "08", "Setembro": "09", "Outubro": "10", "Novembro": "11",
                     "Dezembro": "12"}
                for mes in meses:
                    if arq[5:7] == meses[mes]:
                        os.rename(src_file, os.getcwd() + "\\" + arq[0:4] + "\\"+ mes +"\\" + arquivo)
                        print((src_file + "salvo na pasta de "+ mes + arq[0:4]),file=open("galeria.log","a"))
                    else:
                        pass
            else:
                print("pasta %s" % arquivo, file=open("galeria.log","a"))
        except:
            pass
    mBox.showinfo("CONCLUIDO", "SUCESSO!")
"""........................................................................................................................."""
#Função para verificar arquivo mais antigo
def arquivo_mais_antigo():
    files_antigo = os.listdir(os.getcwd())
    #print(files_antigo)
    list_ano_arq = []
    mais_antigo = ()
    for file_antigo in files_antigo:
        if os.path.isfile(file_antigo):
            arq_list_antigo = str(datetime.datetime.fromtimestamp(os.path.getmtime(file_antigo)))
            list_ano_arq.append(int(arq_list_antigo[0:4]))
        else:
            pass
    try:
        #print(list_ano_arq)
        mais_antigo = max(list_ano_arq)
    except:
        mais_antigo = "Diretório sem arquivos"
    return mais_antigo

"""..........................................................................................................................."""
#GUI - Organizador de Fotos____________________________________________________________________________________________________
raiz = Tk()
raiz.iconbitmap("organizador.ico")

navegar = ""
navegar2 = ""
imagem = tkinter.PhotoImage(file="organizador.png")
image2 = tkinter.PhotoImage(file="titulo.png")
class Janela:
    def __init__(self, janela1):
        janela1.title("Organizador de Fotos")

        self.navegar = ""

        self.container1 = Frame(janela1)
        self.container1.grid()

        self.imagemtitulo = Label(self.container1, image=imagem, bg="white")
        self.imagemtitulo.grid(row=0, column=0, rowspan=10, sticky=N+S)

        self.titulo = Label(self.container1, text="Organize Suas Fotos\n Por Ano e Mês", font=("times", "20", "bold"), image=image2)
        #self.titulo["width"]=26
        #self.titulo["height"]=3
        self.titulo["bg"]="white"
        #self.titulo["fg"]= "white"
        self.titulo.grid(row=0, column=1, columnspan=3, rowspan=1, sticky=N+S)

#primeira label de entrada de arquivos

        self.diret = Button(self.container1, text="Local das Fotos", command=self.file_objeto, font=("times", "16", "bold", "underline"),fg="blue", bg="light blue", highlightthickness=8, borderwidth=6, padx=10, pady=10, activebackground="blue")
        self.diret.grid(row=1, column=1, columnspan=3, rowspan=1, sticky=W+E)

        self.lugar = Label(self.container1, text=navegar)
        self.lugar.grid(row=2, column=1, sticky=W, columnspan=2)

#escolha do ano:
        self.ano_txt = Label(self.container1, text="Ano:", font=("times", "16", "bold"))
        self.ano_txt.grid(row=3, column=1, columnspan=1, sticky=E)

        self.ano = Entry(self.container1, width=4, borderwidth=6)
        self.ano.grid(row=3, column=2, columnspan=1, sticky=W)


#bloco de botoes
        self.botao = Button(self.container1, text="Cancelar", command=self.cancelar, bg="red", fg="white", padx=2, pady=2)
        self.botao["font"] = ("times", "16", "bold")
        self.botao.grid(row=4, column=1, sticky=W+E)

        self.botao2 = Button(self.container1, font=("times","16","bold", "underline"), command=self.ok, bg="light blue", padx=2, pady=2, activebackground="blue")
        self.botao2["text"] = "OK"
        self.botao2["fg"] = "blue"
        self.botao2.grid(row=4, column=2, columnspan=2, sticky=W+E)

        tkinter.messagebox.showinfo("Tutorial","Programa voltado a organização de fotos:\n\n\tescolha o diretório em que suas fotos e arquivos estão na raiz\n\tou mova os arquivos para uma pasta e organize dentro delas")
        tkinter.messagebox._show("Tutorial", "\tEm ano, digite o referente a data mais antiga\n\tque deseja organizar seus arquivos\n\tExemplo: 2009")
#Bloco de Funções dos Botões

    #Botão de OK verificar e captar as variáveis
    def ok(self):
        LUGAR = self.file_objeto
        anos = self.ano.get()
        #DESTINO = self.file_objeto modificado para navegar
        if type(anos) != str or type(LUGAR) != str:
            mBox.showerror("ERRO","Problema encontrado: \n Caminho de arquivos errados ou não encontrados \n Selecionar novamente os Diretórios!")
        elif anos == "" or LUGAR == "":
            mBox.showerror("ERRO","Problema encontrado: \n Caminho de arquivos errados ou não encontrados \n Selecionar novamente os Diretórios!")
        elif len(anos) < 4:
            mBox.showerror("ERRO","Problema encontrado: \n Caminho de arquivos errados ou não encontrados \n Selecionar novamente os Diretórios!")
        else:
            os.chdir(LUGAR)
            verif_criar_pasta(anos)
            lendo_arquivos_movendo()
        for _, _, arquivo in os.walk("."):
            print(os.path.abspath(str(arquivo)), file=open("movidos.txt", "a"))

#cancelamento da operação
    def cancelar(self):
        raiz.quit()

#funções para navegar e escolher as pastas
    def file_objeto(self):
        navegar = tkinter.filedialog.askdirectory(initialdir=".")
        os.chdir(navegar)
        self.lugar["text"] = navegar + "\n o arquivo mais antigo é de: " + str(arquivo_mais_antigo())
        self.file_objeto = navegar

Janela(raiz)
raiz.mainloop()