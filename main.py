from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui as pg
from time import sleep

# Iniciar o webdriver
driver = webdriver.Edge()


def acessar_pagina():
    driver.get("https://precos-de-produtos.netlify.app/")  # acessar a página
    sleep(10)  # aguardar a página carregar


def carregar_produtos_pagina():
    botao_carregar_mais = driver.find_element(
        By.XPATH, "//button[@id='loadMoreButton']")
    sleep(2)
    botao_carregar_mais.click()
    sleep(1)


def importar_planilha():
    # localizar botão Subir Planilha de Preços
    botao_importar_planilha = driver.find_element(
        By.XPATH, "//button[@class='btn btn-primary btn-custom']")
    sleep(2)

    # clicar no botão Subir Planilha de Preços
    botao_importar_planilha.click()
    sleep(1)

    # a pasta que contem as planilhas sempre estará no mesmo lugar
    # escrever o caminho completo do arquivo
    pg.write(r'C:\Users\Bruna\Desktop\planilhas\precos-produtos-atualizados.xlsx')
    sleep(1)

    # pressionar o botão enter para confirmar o carregamento do arquivo
    pg.press("enter")
    sleep(1)


def atualizar_preco():
    # localizar botão Atualizar Preço
    botao_atualizar_preco = driver.find_element(
        By.XPATH, "[@class='btn btn-secondary btn-custom']")
    sleep(2)

    # clicar em atualizar preço
    botao_atualizar_preco.click()
    sleep(1)


def main():
    acessar_pagina()
    carregar_produtos_pagina()
    importar_planilha()
    atualizar_preco()

    # fechar o navegador
    driver.quit()


if __name__ == "__main__":
    main()
