from selenium.webdriver.common.by import By


def buscar_por_xpath(driver, xpath):
    try:
        titulo_elemento = driver.find_element(By.XPATH, xpath)
        return titulo_elemento
    except Exception as e:
        print(f"Erro ao coletar o xpath {xpath}")
        return None

def verificar_elemento_por_xpath(driver, xpath):
    try:
        elemento = driver.find_element(By.XPATH, xpath)
        # print("Elemento está presente na página")
        return elemento
    except Exception as e:
        print("Elemento não encontrado")
