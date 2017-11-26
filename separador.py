#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Criado por Rhuann Kael Souza Nascimento - 11/10/2017 - 15:36
Atualização 18/10/2017 - 10:38
"""

import os
import shutil
import datetime
from tkinter import messagebox as mBox

def verif_criar_pasta(anos):
    """Função Verificando Pastas"""
    anos = int(anos)
    a = int(datetime.date.today().year) - anos
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    try:
        while a >= 0:
            if os.path.exists(str(a + anos)):
                print("renomear a pasta %s existente" % (a + anos), file=open("organizador.log", "a", encoding="utf-8"))
            else:
                data = str(datetime.datetime.now())
                print("%s criando_pasta %s" % (data, (a + anos)), file=open("organizador.log", "a"))
                os.mkdir(str(anos + a))
                try:
                    for mes in meses:
                        os.mkdir(str(anos + a)+"/%s" % mes)
                        print("criada subpasta de %s" % mes, file=open("organizador.log", "a"))
                    print("%s pastas criadas" % data, file=open("organizador.log", "a"))
                except:
                    print("erro em %s" % mes, file=open("organizador.log", "a"))
            a = a - 1
    except:
        print("erro %s" % (a + anos), file=open("organizador.log", "a"))

def lendo_arquivos_movendo():
    """Função para mover arquivos"""
    files = os.listdir(os.getcwd())
    if "separador.py" in files:
        files.remove("separador.py")
    elif "Organizador.py" in files:
        files.remove("Organizador.py")
    elif "organizador.log" in files:
        files.remove("organizador.log")
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
                        try:
                            os.makedirs(os.getcwd() + "\\" + arq[0:4] + "\\"+ mes)
                            shutil.move(src_file, os.getcwd() + "\\" + arq[0:4] + "\\" + mes + "\\" + arquivo)
                            print((src_file + "\n\tsalvo na pasta de "+ mes + arq[0:4]),file=open("organizador.log","a"))
                        except:
                            shutil.move(src_file, os.getcwd() + "\\" + arq[0:4] + "\\" + mes + "\\" + arquivo)
                            print((src_file + "\n\tsalvo na pasta de " + mes + arq[0:4]),file=open("organizador.log", "a"))
                    else:
                        print("erro")
            else:
                print("pasta %s" % arquivo, file=open("organizador.log","a"))
        except:
            print("falha grave em %s" % arquivo, file=open("organizador.log", "a"))

def arquivo_mais_antigo():
    """Função para verificar arquivo mais antigo"""
    files_antigo = os.listdir(os.getcwd())
    list_ano_arq = []
    for file_antigo in files_antigo:
        if os.path.isfile(file_antigo):
            arq_list_antigo = str(datetime.datetime.fromtimestamp(os.path.getmtime(file_antigo)))
            list_ano_arq.append(int(arq_list_antigo[0:4]))
        else:
            pass
    try:
        mais_antigo = min(list_ano_arq)
    except:
        mais_antigo = "Diretório sem arquivos"
    return mais_antigo
