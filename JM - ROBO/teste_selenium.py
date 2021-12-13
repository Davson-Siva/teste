#from func_jm_selenium import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
#from random_user_agent.user_agent import UserAgent
#from random_user_agent.params import SoftwareName, OperatingSystem
import time
import os.path
from GENERIC_FUNC import *

def aguarda_element_class_name(elemento, driver):
    ultra_debug("aguarda_element_class_name(elemento) - INICIO")
    timeOut = 0
    while timeOut <= 11: 
        try:
            if(driver.find_elements_by_class_name(elemento)):
                ultra_debug("Elemento encontrado")
                ultra_debug("aguarda_element_class_name(elemento) - FIM")
                return True 
        except:
            ultra_debug("Elemento ainda nao carregado.")
            timeOut += 1
            time.sleep(1)
    ultra_debug("Elemento nao carregado. TIMEOUT.")
    ultra_debug("aguarda_element_class_name(elemento) - FIM")
    return False


def aguarda_element_id(elemento, driver):
    ultra_debug("aguarda_element_id(elemento) - INICIO")
    timeOut = 0
    while timeOut <= 10:
        try:
            if(driver.find_element_by_id(elemento)):
               ultra_debug("Elemento encontrado")
               ultra_debug("aguarda_element_id(elemento) - FIM")
               return True
        except:
            ultra_debug("Elemento ainda nao carregado.")
            timeOut += 1
            time.sleep(1)

    ultra_debug("Elemento não encontrado. TimeOut.")
    ultra_debug("aguarda_element_id(elemento) - FIM")
    return False

def abrir_site(url, driver):
    ultra_debug("abrir_site(url, driver) - INICIO")
    try:
        driver.get(url)
        ultra_debug("Site aberto com sucesso.")
        ultra_debug("abrir_site(url, driver) - FIM")
        return True
    except:
        ultra_debug("Falha ao abrir site.")
        ultra_debug("abrir_site(url, driver) - FIM")
        return False

def loga_jm(usuario, senha, driver):
    ultra_debug("loga_jm(usuario, senha, driver) - INICIO")
    ultra_debug(usuario)
    ultra_debug("senha: " + str(senha))
    try:
        driver.find_element_by_id("email_usuario").send_keys(usuario)
        time.sleep(1)
        ultra_debug("usuário inserido")
        driver.find_element_by_id("key").send_keys(senha)
        time.sleep(1)
        ultra_debug("senha inserida")
        entrar = driver.find_element_by_id("btnSubmit")
        entrar.click()
        time.sleep(3)
        ultra_debug("Clicado no botão para logar.")
        #aguarda para verificar se o login foi feito com sucesso
        if(aguarda_element_id("menu", driver)):
            print("logado com sucesso")
            return True
        else:
            print("falha ao logar")
            return False
    except:
        ultra_debug("Falha ao logar no sistema")
        ultra_debug("loga_safra(usuario, senha, driver) - FIM")
        return False

def consulta_cpf(driver, cpf):
    print("inici consulta")
    try:
        #acessando oampo "NOVA CONSULTA"
        driver.find_element_by_link_text("Nova Consulta").click()
        #nova_consulta = pyautogui.locateCenterOnScreen("nova_consulta.PNG")
        #pyautogui.moveTo(nova_consulta)
        #print(nova_consulta)
        print("movidi")
        time.sleep(2)
        #pyautogui.click(nova_consulta)
        print("clicado")
        if(aguarda_element_id("input-search-group", driver)):
            print("encontrado")
            time.sleep(2)
            driver.find_elements_by_class_name("form-control")[0].click()
            #digitar_cpf = pyautogui.locateCenterOnScreen("digitar_cpf.PNG")
            print("clicado no form control")
            #pyautogui.moveTo(digitar_cpf)
            time.sleep(3)
            #pyautogui.click(digitar_cpf)
            print("clicando no campo input")
            time.sleep(4)
            driver.find_elements_by_class_name("form-control")[0].clear()
            print("limpando o campo")
            time.sleep(2)
            print("digitando o cpf")
            
            driver.find_elements_by_class_name("form-control")[0].send_keys(cpf)
            #pyautogui.write(cpf, interval=0.15)
            print("cpf difitado")
            time.sleep(1)
            #cords = pyautogui.locateCenterOnScreen("button_consultar.PNG")
            #pyautogui.moveTo(cords)
            
            driver.find_elements_by_class_name("g-recaptcha")[0].click()
            #pyautogui.click(cords)
            """time.sleep(1)
            print("sleep finalizado")
            
            cords = pyautogui.locateCenterOnScreen("button_consultar.PNG")
            print(cords)
            
            pyautogui.moveTo(cords)
            time.sleep(2)
            pyautogui.click(cords)
            try:
                resultado = WebDriverWait(driver, 10).until(EC.alert_is_present())
                ultra_debug(str(type(resultado)))
                if str(type(resultado)) == "<class 'selenium.webdriver.common.alert.Alert'>":
                    driver.switch_to.alert.accept()
                    time.sleep(5)
                    print("Navegando para o dashboard")
                    #driver.find_element_by_link_text("Dashboard").click()
                    driver.find_element_by_partial_link_text("Dashboard").click()
                    time.sleep(6)
                    driver.find_element_by_link_text("Nova Consulta").click()
                    if(aguarda_element_id("input-search-group", driver)):
                        time.sleep(2)
                        driver.find_elements_by_class_name("form-control")[0].click()
                        print("clicando no campo input")
                        time.sleep(1)
                        print("digitando o cpf")
                        #driver.find_elements_by_class_name("form-control")[0].send_keys(cpf)
                        pyautogui.write(cpf, interval=0.25)
                        print("cpf difitado")
                        time.sleep(1)
                        #driver.find_elements_by_class_name("g-recaptcha")[0].click()
                        e = driver.find_elements_by_class_name("g-recaptcha")[0]
                        #pyautogui.press('enter')
                        location = e.location
                        print(location)
                        
                    
                        return True
            except TimeoutException:    
                print("NÃO FOI NECESÁRIO APERTAR O POP-UP")
                print("loga_jm(usuario, senha, driver) - FIM")
                return True"""

    except:
        print("FALHA AO CONSULTAR CPF")
        return False

usuario = "operacional05@maaf.com.br"
senha = "pol35df"
url = "https://app.jmservicoweb.com.br/view/"
#15535266949

#software_names = [SoftwareName.CHROME.value]
#operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]  
#user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
#user_agents = user_agent_rotator.get_user_agents()
#user_agent = user_agent_rotator.get_random_user_agent()
#print(user_agent)


#profile = webdriver.ChromeProfile()
#profile.set_preference("general.useragent.override", user_agent)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(options=chrome_options)
#driver = webdriver.Chrome(profile)
#driver.set_preference("general.useragent.override", user_agent)
#driver = driver = webdriver.Chrome()

if(abrir_site(url, driver)):
    print("site aberto")

pagina_carregada = aguarda_element_id("key", driver)

if pagina_carregada == True:
    print("pagina totalmente carregada")


if(loga_jm(usuario, senha, driver)):
    print("LOGADOS")
    time.sleep(20)
    print("sleep finalizando")
else:
    print("falha ao realizar login")
    print("tentando novamente")
    if(loga_jm(usuario, senha, driver)):
        print("logado na segunda vez")
    else:
        print("falhou novamente")

cpf = "155.352.669-49"
cpf = cpf.replace(".", "")
cpf = cpf.replace("-", "")
#print(cpf)

consulta = consulta_cpf(driver, cpf)

print(consulta)

