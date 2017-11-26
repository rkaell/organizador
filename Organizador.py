#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Criado por Rhuann Kael Souza Nascimento - 11/10/2017 - 15:36
Atualização 18/10/2017 - 10:38
Atualização 06/11/2017 - 10:07
"""
import separador as sp
from tkinter import *
import tkinter.filedialog
from tkinter import messagebox as mBox
import os

#GUI - Organizador de Fotos
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
        self.titulo["bg"]="white"
        self.titulo.grid(row=0, column=1, columnspan=3, rowspan=1, sticky=N+S)
        self.diret = Button(self.container1, text="Local das Fotos", command=self.file_objeto, font=("times", "16", "bold", "underline"),fg="blue", bg="light blue", highlightthickness=8, borderwidth=6, padx=10, pady=10, activebackground="blue")
        self.diret.grid(row=1, column=1, columnspan=3, rowspan=1, sticky=W+E)
        self.lugar = Label(self.container1, text=navegar)
        self.lugar.grid(row=2, column=1, sticky=W, columnspan=2)
        self.botao = Button(self.container1, text="Cancelar", command=self.cancelar, bg="red", fg="white", padx=2, pady=2)
        self.botao["font"] = ("times", "16", "bold")
        self.botao.grid(row=4, column=1, sticky=W+E)
        self.botao2 = Button(self.container1, font=("times","16","bold", "underline"), command=self.ok, bg="light blue", padx=2, pady=2, activebackground="blue")
        self.botao2["text"] = "OK"
        self.botao2["fg"] = "blue"
        self.botao2.grid(row=4, column=2, columnspan=2, sticky=W+E)
        tkinter.messagebox.showinfo("Tutorial","Programa voltado a organização de fotos:\n\n\tEscolha o diretório em que suas fotos e arquivos estão na raiz\n\tou mova os arquivos para uma pasta e organize dentro dela")

    def ok(self):
        """Botão de OK Verificação"""
        LUGAR = self.file_objeto
        os.chdir(LUGAR)
        sp.lendo_arquivos_movendo()
        try:
            for _, _, arquivo in os.walk("."):
                distino = os.path.realpath(str(arquivo))
                print(distino, file=open("organizador.log", "a"))
        except:
            print("caminho muito longo", file=open("organizador.log", "a"))
        mBox._show("ARQUIVOS MOVIDOS","SUCESSO")

    def cancelar(self):
        """Cancelar operação"""
        raiz.quit()

    def file_objeto(self):
        """navegar e escolher pasta"""
        navegar = tkinter.filedialog.askdirectory(initialdir=".")
        os.chdir(navegar)
        self.lugar["text"] = navegar + "\n o arquivo mais antigo é de: " + str(sp.arquivo_mais_antigo())
        self.file_objeto = navegar

Janela(raiz)
raiz.mainloop()