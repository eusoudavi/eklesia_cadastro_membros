import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from ler_planilha import ler_planilha
from nav_util import buscar_por_xpath, verificar_elemento_por_xpath


def fluxo_duplicidade(driver, elemento):
    data = buscar_por_xpath(driver, f'/html/body/eks-root/app-layout/div/section/div/ng-component/div[3]/div/div[1]/ng-component/eks-form/form/div[2]/div/eks-panel/div/div/div[2]/div[1]/eks-input-data/div/input')
    data.clear()
    data.send_keys(elemento.data_nascimento.replace(" ", ""))

    time.sleep(0.5)

    email = buscar_por_xpath(driver, f'/html/body/eks-root/app-layout/div/section/div/ng-component/div[3]/div/div[1]/ng-component/eks-form/form/div[2]/div/eks-panel/div/div/div[2]/div[2]/ek-input[1]/div/div/input')
    email.clear()
    if elemento.email != 'VAZIO':
        email.send_keys(elemento.email.replace(" ", ""))

    time.sleep(0.5)

    telefone = buscar_por_xpath(driver, f'/html/body/eks-root/app-layout/div/section/div/ng-component/div[3]/div/div[1]/ng-component/eks-form/form/div[2]/div/eks-panel/div/div/div[2]/div[2]/ek-input[2]/div/div/input')
    telefone.clear()
    telefone.send_keys(elemento.telefone)

    time.sleep(0.5)

    select_sexo = buscar_por_xpath(driver, f'//*[@id="id"]')
    select_sexo.clear()
    if (elemento.sexo == 'Masculino'):
        select_sexo.send_keys("MASCULINO")
    else:
        select_sexo.send_keys("FEMININO")
    select_sexo.send_keys(Keys.RETURN)

    time.sleep(1)

    try:
        #   CLICAR EM SALVAR
        btn_salvar = buscar_por_xpath(driver, f'/html/body/eks-root/app-layout/div/section/div/ng-component/div[3]/div/div[2]/eks-panel-buttons[1]/div/div/div/div/button')
        btn_salvar.click()
    except:
        print(f"NÃO FOI POSSIVEL SALVAR ATUALIZAÇÃO PARA {elemento.nome_completo}")

    try:
        time.sleep(1)
        msg_erro = verificar_elemento_por_xpath(driver, f'/html/body/eks-root/toaster-container/div/div/div/div[2]/div')
        print(msg_erro.text)
        btn_fechar_salvar = verificar_elemento_por_xpath(driver, f'/html/body/eks-root/toaster-container/div/div/button')
        btn_fechar_salvar.click()
    except:
        pass

    try:
        time.sleep(1)
        btn_arrolamentos = buscar_por_xpath(driver, f'/html/body/eks-root/app-layout/div/section/div/ng-component/div[3]/div/div[2]/eks-panel-buttons/div/div/div/div/a[4]/button')
        btn_arrolamentos.click()
    except:
        print(f"NÃO FOI POSSIVEL CLICAR NO BOTÃO DE ARROLAMENTO PARA {elemento.nome_completo}")

    time.sleep(1)

    status = buscar_por_xpath(driver, f'//*[@id="id"]')
    if (elemento.status == 'Membro'):
        status.send_keys("MEMBRO_24")
    if (elemento.status == 'Frequentador'):
        status.send_keys("FREQUENTADOR_24")
    time.sleep(1)
    status.send_keys(Keys.RETURN)

    try:
        time.sleep(1)
        btn_add_arrolamento = buscar_por_xpath(driver, f'/html/body/eks-root/app-layout/div/section/div/ng-component/div[3]/div/div[1]/ng-component/eks-form/form/eks-panel/div/div/div[2]/div[2]/div[2]/button')
        btn_add_arrolamento.click()
    except:
        print(f"NÃO FOI POSSIVEL SALVAR O ARROLAMENTO PARA {elemento.nome_completo}")

def fluxo_cadastro(driver, e):
    data = buscar_por_xpath(driver, f'/html/body/eks-root/app-layout/div/section/div/ng-component/eks-form/form/div[2]/div/eks-panel/div/div/div[2]/div[1]/eks-input-data/div/input')
    data.send_keys(e.data_nascimento.replace(" ", ""))

    email = buscar_por_xpath(driver, f'/html/body/eks-root/app-layout/div/section/div/ng-component/eks-form/form/div[2]/div/eks-panel/div/div/div[2]/div[2]/ek-input[1]/div/div/input')
    if e.email != 'VAZIO':
        email.send_keys(e.email.replace(" ", ""))

    telefone = buscar_por_xpath(driver, f'/html/body/eks-root/app-layout/div/section/div/ng-component/eks-form/form/div[2]/div/eks-panel/div/div/div[2]/div[2]/ek-input[2]/div/div/input')
    telefone.send_keys(e.telefone)

    select_sexo = buscar_por_xpath(driver, f'//*[@id="id"]')
    if (e.sexo == 'Masculino'):
        select_sexo.send_keys("MASCULINO")
    else:
        select_sexo.send_keys("FEMININO")
    select_sexo.send_keys(Keys.RETURN)

    status = buscar_por_xpath(driver, f'//*[@id="codigo"]')
    if (e.status == 'Membro'):
        status.send_keys("MEMBRO_24")
    if (e.status == 'Frequentador'):
        status.send_keys("FREQUENTADOR_24")
    time.sleep(2)
    status.send_keys(Keys.RETURN)

    try:
#   CLICAR EM SALVAR
        btn_salvar = buscar_por_xpath(driver, f'/html/body/eks-root/app-layout/div/section/div/ng-component/eks-form/form/div[2]/div/eks-panel/div/eks-panel-buttons/div/div/div/div/button[1]')
        btn_salvar.click()
    except:
        print(f"NÃO FOI POSSIVEL SALVAR PARA {e.nome_completo}")

    try:
        time.sleep(1)
        msg_erro = verificar_elemento_por_xpath(driver, f'/html/body/eks-root/toaster-container/div/div/div/div[2]/div')
        print(msg_erro.text)
    except:
        pass

    try:
        time.sleep(1)
        btn_conf = buscar_por_xpath(driver, f'/html/body/div[2]/div/div[6]/button[1]')
        btn_conf.click()
    except:
        pass


def action(driver):

    url = 'https://gestaoweb.eklesiaonline.com.br/login'
    driver.get(url)
    time.sleep(1)

    try:
        user = buscar_por_xpath(driver, f'/html/body/eks-root/app-layout-login/div/app-login/div/div[1]/div[1]/div[2]/eks-form/form/div/ek-input[1]/div/div/input')
        user.send_keys("")

        user = buscar_por_xpath(driver, f'/html/body/eks-root/app-layout-login/div/app-login/div/div[1]/div[1]/div[2]/eks-form/form/div/ek-input[2]/div/div/input')
        user.send_keys("")

        btn_login = buscar_por_xpath(driver, f'/html/body/eks-root/app-layout-login/div/app-login/div/div[1]/div[1]/div[2]/eks-form/form/div/div[2]/button')
        btn_login.click()

        time.sleep(2)
        for e in ler_planilha():
            driver.get('https://gestaoweb.eklesiaonline.com.br/membresia/pessoa/criar')

            print(f'Inserindo dados do membro {e.nome_completo}')
            time.sleep(0.5)
            nome = buscar_por_xpath(driver, f'/html/body/eks-root/app-layout/div/section/div/ng-component/eks-form/form/div[2]/div/eks-panel/div/div/div[2]/div[1]/ek-input/div/div/input')
            nome.send_keys(e.nome_completo)

            data = buscar_por_xpath(driver, f'/html/body/eks-root/app-layout/div/section/div/ng-component/eks-form/form/div[2]/div/eks-panel/div/div/div[2]/div[1]/eks-input-data/div/input')
            data.send_keys(e.data_nascimento)

            time.sleep(1)
            duplicidade = verificar_elemento_por_xpath(driver, f'/html/body/eks-root/app-layout/div/section/div/ng-component/eks-form/form/div[1]/div/alert/div/div/button')
            if (duplicidade is not None):
                duplicidade.click()
                time.sleep(0.5)
                elemento_rep = buscar_por_xpath(driver, f'/html/body/eks-root/app-layout/div/section/div/ng-component/eks-form/form/div[1]/div/alert/div/div/div/a')
                elemento_rep.click()
                time.sleep(0.5)
                btn_verificar = verificar_elemento_por_xpath(driver, f'/html/body/div[2]/div/div[6]/button[1]')
                btn_verificar.click()
                fluxo_duplicidade(driver, e)
                time.sleep(1)
                continue

            fluxo_cadastro(driver, e)
            time.sleep(1)

        print('FINALIZANDO')

    except Exception as e:
        print(e)

        # Navegar para a próxima página
        time.sleep(3)

if __name__ == "__main__":
    service = Service("chromedriver.exe")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    action(driver)

    time.sleep(5)
    driver.quit()