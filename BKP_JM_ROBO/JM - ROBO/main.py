import time
import pyautogui
import os
from jm_pyautogui import *
from GENERIC_FUNC import *
import schedule
from func_email_report import *


def main_exec():

    ultra_debug("INICIO EXEC")

    email = "robomaaf@gmail.com"
    senha = "maaf@2021"
    email_destino = "davson.silva@grupomaaf.com.br"

    apaga_temp = limpa_pasta_temp()

    if apaga_temp == 0:
        
        ultra_debug("Pasta Temp limpa")
    else:
        ultra_debug("Não foi possível limpar a pasta temp")    

    finalizado = False
    while finalizado == False:
        chamado_finalizado = realiza_consulta()

        if chamado_finalizado == True:
            ultra_debug("CHAMADO FOI FINALIZADO")
            print("CHAMADO FOI FINALIZADO")
            data_e_hora_atuais = datetime.now()
            data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M:%S')
            assunto = "SUCESSO - Robo JM - SUCESSO"
            mensagem = "SUCESSO AO RESPONDER O CHAMADO. FOI ALTERADO A SENHA NO BANCO DE DADOS. DATA E HORA DE FINALIZAÇÃO: " + str(data_e_hora_em_texto)
            if(email_report(email, senha, email_destino, assunto, mensagem)):
                ultra_debug("Email de report enviado")
                finalizado = True
            else:
                ultra_debug("EMAIL DE REPORT FALHOU. TENTANDO NOVAMENTE")
                time.sleep(10)
                if(email_report(email, senha, email_destino, assunto, mensagem)):
                    ultra_debug("EMAIL DE REPORT ENVIADO")
                    finalizado = True
                else:
                    ultra_debug("FALHA AO ENVIAR EMAIL DE REPORT PELA SEGUNDA VEZ")
                    finalizado = True


        elif chamado_finalizado == "-1":
            ultra_debug("NÃO POSSUI CHAMADOS PENDENTES")
            print("NÃO POSSUI CHAMADOS PENDENTES")
            finalizado = True

        elif chamado_finalizado == "-2":
            ultra_debug("NÃO ENCONTROU NENHUMA SENHA NO SITE. NÃO FOI ATUALIZADO NO BD")
            print("NÃO ENCONTROU NENHUMA SENHA NO SITE. NÃO FOI ATUALIZADO NO BD")
            data_e_hora_atuais = datetime.now()
            data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M:%S')
            assunto = "SUCESSO - Robo JM - SUCESSO"
            mensagem = "SUCESSO AO RESPONDER O CHAMADO. NÃO FOI ENCONTRADO NENHUMA SENHA NO SITE NÃO FOI ALTERADO A SENHA NO BANCO DE DADOS. DATA E HORA DE FINALIZAÇÃO: " + str(data_e_hora_em_texto)
            if(email_report(email, senha, email_destino, assunto, mensagem)):
                ultra_debug("Email de report enviado")
                finalizado = True
            else:
                ultra_debug("EMAIL DE REPORT FALHOU. TENTANDO NOVAMENTE")
                time.sleep(10)
                if(email_report(email, senha, email_destino, assunto, mensagem)):
                    ultra_debug("EMAIL DE REPORT ENVIADO")
                    finalizado = True
                else:
                    ultra_debug("FALHA AO ENVIAR EMAIL DE REPORT PELA SEGUNDA VEZ")
                    finalizado = True
            
            
        elif chamado_finalizado == False:
            ultra_debug("FALHA AO ATENDER O CHAMADO")
            print("FALHA AO ATENDER O CHAMADO")
            data_e_hora_atuais = datetime.now()
            data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M:%S')
            assunto = "FALHA - Robo JM - FALHA"
            mensagem = "FALHA AO REALIZAR PASSO A PASSO PARA EXECUTAR A CONSULTA NO SITE. DATA E HORA DE FINALIZAÇÃO: " + str(data_e_hora_em_texto)
            if(email_report(email, senha, email_destino, assunto, mensagem)):
                ultra_debug("Email de report enviado")
                continue
            else:
                ultra_debug("EMAIL DE REPORT FALHOU. TENTANDO NOVAMENTE")
                time.sleep(10)
                if(email_report(email, senha, email_destino, assunto, mensagem)):
                    ultra_debug("EMAIL DE REPORT ENVIADO")
                    continue
                else:
                    ultra_debug("FALHA AO ENVIAR EMAIL DE REPORT PELA SEGUNDA VEZ")
                    continue

schedule.every(1).minutes.do(main_exec)

while True:
    hora_agora = datetime.now()
    hora_execucao = hora_agora.replace(hour=20, minute=0, second=0, microsecond=0)
    hora_inicial = hora_agora.replace(hour=8, minute=30, second=0, microsecond=0)
    if hora_agora < hora_execucao:
        if hora_agora > hora_inicial:
            schedule.run_pending()
            time.sleep(1)
    else:
        time.sleep(10)
    

    
