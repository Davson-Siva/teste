import time
import time
import os.path
import pyautogui
import sys
import os
from banco_query import *
import mysql.connector
from mysql.connector import Error
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from reaproveita_sessao import *
from GENERIC_FUNC import *


def procura_imagem(caminho_imagem):
    ultra_debug("procura_imagem(caminho_imagem) - INIIO")
    cont = 0
    while cont <= 3:
        try:
            cords = pyautogui.locateCenterOnScreen(caminho_imagem)
            if str(cords) == "None":
                ultra_debug("IMAGEM AINDA NAO CARREGADA")
                cont += 1
                time.sleep(1)
                
            else:
                ultra_debug("Imagem carregada")
                return True
        except:
            ultra_debug("Nao foi possivel procurar pela imagem")
    
    ultra_debug("IMAGEM NAO FOI APRESENTADA NA TELA")
    return False

def procura_imagem_e_clica(caminho_imagem):
    ultra_debug("procura_imagem_e_clica(caminho_imagem) - INIIO")
    cont = 0
    while cont <=3:
        try:
            cords = pyautogui.locateCenterOnScreen(caminho_imagem)
            if str(cords) == "None":
                ultra_debug("IMAGEM AINDA NAO CARREGADA")
                cont +=1
                time.sleep(1)
                
            else:
                ultra_debug("Imagem carregada")
                pyautogui.moveTo(cords)
                time.sleep(3)
                ultra_debug("clicando na imagem")
                pyautogui.click(cords)
                return True
        except:
            ultra_debug("Nao foi possivel procurar pela imagem")
    ultra_debug("IMAGEM NAO FOI APRESENTADA NA TELA")
    return False
   

def login(user, password):
    if(procura_imagem_e_clica("usuario.PNG")):
        ultra_debug("digitando usuario")
        pyautogui.write(user, interval=0.15)
        time.sleep(3)
        if(procura_imagem_e_clica("senha.PNG")):
            ultra_debug("Digitando senha")
            pyautogui.write(password, interval=0.15)
            time.sleep(3)
            if(procura_imagem_e_clica("acessar.PNG")):
                ultra_debug("Acessando site")
                return True
    else:
       ultra_debug("NAO foI POSSIVEL LOCALIZARaSIMAGENS PARA rEALIZAR LOGIN")
       return False
