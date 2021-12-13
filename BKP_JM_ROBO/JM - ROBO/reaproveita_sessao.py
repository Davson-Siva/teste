from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

porta = 9222

def use_existing_browser():
    options = Options()
    options.add_experimental_option("debuggerAddress", f"localhost:9222")
    driver = webdriver.Chrome(options=options)
    return driver

def close(driver):
    try:
        close = driver.find_elements_by_class_name("nav-link")
        for elemento in close:
            if elemento.text == "Sair":
                elemento.click()
                return True
            else:
                ultra_debug("Não é igual")
    except:
        return False

def pega_senha(driver):
    try:
        matricula = driver.find_element_by_id("planoMatricula")
        matricula = str(matricula.get_attribute("textContent"))
        close(driver)
        return str(matricula)
        
    except:
        ultra_debug("Não consegui")
        return False
    
