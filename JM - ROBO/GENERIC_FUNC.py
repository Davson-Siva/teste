import os.path
import os
from datetime import datetime



def verifica_arquivo_txt():
    return os.path.isfile("log.txt")

def limpa_pasta_temp():
    resultado = os.system('del /q/f/s C:\\Users\\%USERNAME%\\AppData\\Local\Temp\\*')
    return resultado
    

def ultra_debug(frase):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    path_final_log = dir_path + str("\\log.txt")
    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M:%S')
    if verifica_arquivo_txt() == True:
        with open(path_final_log, "a") as arquivo:
            arquivo.write(str(data_e_hora_em_texto + " = " + frase) + '\n')
            return True
    else:
        arquivo = open(path_final_log, 'w+')
        arquivo.writelines(frase + '\n')





