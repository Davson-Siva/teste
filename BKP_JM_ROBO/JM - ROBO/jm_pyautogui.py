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
from func_pyautogui_jm import *

url = ""
user = ""
password = ""
        

def realiza_consulta():

    
    consulta = consulta = consulta_chamados()

    if str(consulta) == "None":
        ultra_debug("Não há nenhuma chamado para realizar")
        return "-1"
    else:
        motivo_id = consulta[0]
        cpf_cliente = consulta[1]
        cliente_prec_cp = consulta[2]
        ultra_debug("PEGANDO INFORMAÇÕES DO CHAMADO")
        ultra_debug(str(motivo_id))
        ultra_debug(str(cpf_cliente))
        ultra_debug(str(cliente_prec_cp))
    
    
    # ABRE O GOOGLE NA PORTA 9222 PARA CONECTAR COM O SELENIUM POSTERIORMENTE
    resultado = os.system('start chrome --remote-debugging-port=9222')
    time.sleep(5)
    ultra_debug("Tempo de espera para abrir o google finalizado")


    #VERIFICA SE NA BARRA DE PESQUISA DE URL NO GOOGLE ESTÁ COM ALGO ESCRITO. CASO NÃO ENCONTRE, SIGNIFICA QUE O CURSOR ESTÁ FOCADO NA BARRA E É POSSÍVEL DIGITAR A URL SEM CLICAR
    imagem = procura_imagem_e_clica("pesquisa_google.PNG")

    if imagem == False:
        ultra_debug("imagem não estava na tela. Não há necessidade de clicar para digitar url")
        pyautogui.write(url, interval=0.15)
        ultra_debug("finalizado a digitação da url")
        pyautogui.press('enter')

    else:
        #DIGITA A URL NO SITE
        pyautogui.write(url, interval=0.15)
        ultra_debug("finalizado a digitação da url")
        pyautogui.press('enter')
        ultra_debug("Navegando até o site")

    #VERIFICA SE O LOGO DO SITE ESTÁ ABERTO
    site_aberto = procura_imagem("logo_jm.PNG")

    if site_aberto == True:
        ultra_debug("site aberto. Aguardando mais alguns segundos para o site carregar por completo")
        #AGUARDA 25 SEGUNDOS PARA TER CERTEZA QUE A PÁGINA CARREGOU TOTALMENTE (JÁ QUE NÃO ESTÁ SENDO UTILIZADO O SELENIUM PREVIAMENTE
        time.sleep(25)

    else:
        ultra_debug("Site não foi aberto")
        time.sleep(2)
        os.system("TASKKILL /im chrome.exe")
        time.sleep(1)
        return False

    logado = login(user, password)

    if logado == True:
        #vai verificar se o login foi feito corretamente
        if(procura_imagem("nova_consulta.PNG")):
            ultra_debug("Logado")
        else:
            ultra_debug("Não está logado")
            ultra_debug("FECHANDO CHROME")
            os.system("TASKKILL /im chrome.exe")
            time.sleep(2)
            return False

    time.sleep(2)

    imagem = procura_imagem_e_clica("nova_consulta.PNG")

    if imagem == True:
        ultra_debug("clicado em nova consulta")
        ultra_debug("aguardando tela carregar")
        if(procura_imagem("digitar_cpf.PNG")):
            ultra_debug("Tela carregada")
    else:
        ultra_debug("Não foi possivel clicar em nova consulta")
        ultra_debug("FINALIZANDO O CHROME")
        os.system("TASKKILL /im chrome.exe")
        time.sleep(2)

    time.sleep(4)

    imagem = procura_imagem_e_clica("digitar_cpf.PNG")
    if imagem == True:
        ultra_debug("DITITANDO CPF")
        pyautogui.write(cpf_cliente, interval=0.18)
        ultra_debug("cpf digitando.")
        ultra_debug("Realizando consulta")
        time.sleep(2)
        if(procura_imagem_e_clica("button_consultar.PNG")):
            ultra_debug("consulta realizada")
            time.sleep(4)
            if(procura_imagem("erro_pop_up.PNG")):
                ultra_debug("SITE DETECDOU QUE É UM ROBÔ.")
                ultra_debug("ENCERRANDO CHROME")
                os.system("TASKKILL /im chrome.exe")
                ultra_debug("AGUARDANDO 10 MINUTOS PARA RODAR NOVAMENTE")
                time.sleep(600)
                return False
                    
            else:
                ultra_debug("POP-UP DE ERRO NÃO FOI APRESENTADO")
            driver = use_existing_browser()
            time.sleep(4)
            ultra_debug("Reaproveitamento finalizado")
            senha_eb = pega_senha(driver)
            ultra_debug(str(senha_eb))
            if senha_eb != False:
                ultra_debug("Senha pega")
                ultra_debug(senha_eb)
                if senha_eb == "":
                    senha_eb = "SENHA NAO ENCONTRADO"

            else:
                senha_eb = "SENHA NAO ENCONTRADO"
                ultra_debug("SENHA NAO ENCONTRADO")
        else:
            ultra_debug("NÃO FOI ENCONTRADO O BOTÃO PARA REALIZAR A CONSULTA")
            ultra_debug("FINALIZANDO CHROME")
            os.system("TASKKILL /im chrome.exe")
            time.sleep(2)
            return False
    else:
        ultra_debug("CAMPO PARA DIGITAR CPF NÃO FOI ENCONTRADO")
        ultra_debug("ENCERRANDO CHROME")
        time.sleep(2)
        os.system("TASKKILL /im chrome.exe")
        return False

    ultra_debug("ENCERRANDO SELENIUM")
    driver.quit()
    ultra_debug("SELENIUM FINALIZADO")
    os.system("TASKKILL /im chrome.exe")



    respondido = responde_chamado(str(motivo_id), str(senha_eb))

    if respondido == True:
        ultra_debug("Chamado respondido")
        ultra_debug("senha_eb " + str(senha_eb))
        time.sleep(1)
        atualiza_chamado = atualizar_chamado(motivo_id)
        if atualiza_chamado == True:
            if senha_eb != "SENHA NAO ENCONTRADO":
                ultra_debug("excluindo campo prec_cp")
                time.sleep(1)
                if(excluir_senha(cliente_prec_cp)):
                    ultra_debug("prec_cp excluido")
                    ultra_debug("atualizando senha")
                    senha_eb = str(senha_eb)
                    time.sleep(1)
                    cliente_prec_cp = str(cliente_prec_cp)
                    if(atualiza_senha(senha_eb, cliente_prec_cp)):
                        ultra_debug("senha atualizada")
                        ultra_debug("CHAMADO FINALIZADO")
                        return True
            else:
                ultra_debug("NÃO FOI ENCONTRADO NENHUMA SENHA NO SITE. Não é preciso atualizar a senha")                
                return "-2"
        else:
            ultra_debug("Falha ao atualizar chamado")
            return False
            

    else:
        ultra_debug("Falha ao responder o chamado")
        return False
    
    
    

    
    

    
