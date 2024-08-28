from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui as pg
from time import sleep

# Iniciar o webdriver. Escolha o navegador que deseja usar, alterando "Edge" para "Chrome", "Firefox", etc.
# Substitua 'Edge' pelo navegador de sua preferência, como webdriver.Chrome() ou webdriver.Firefox.
driver = webdriver.Edge()


def acessar_pagina():
    # Acessa a página especificada.
    driver.get("https://precos-de-produtos.netlify.app/")
    # Aguarda 10 segundos para que a página carregue completamente. Ajuste o tempo conforme necessário.
    sleep(10)


def carregar_produtos_pagina():
    # Localiza o botão "Carregar Mais" para visualizar mais produtos na página.
    botao_carregar_mais = driver.find_element(
        By.XPATH, "//button[@id='loadMoreButton']")
    # Aguarda 2 segundos antes de interagir com o botão. Ajuste o tempo conforme necessário.
    sleep(2)
    botao_carregar_mais.click()  # Clica no botão "Carregar Mais".
    # Aguarda 1 segundo para garantir que a ação seja concluída. Ajuste o tempo conforme necessário.
    sleep(1)


def importar_planilha():
    # Localiza o botão "Subir Planilha de Preços" na página.
    botao_importar_planilha = driver.find_element(
        By.XPATH, "//button[@class='btn btn-primary btn-custom']")
    # Aguarda 2 segundos antes de interagir com o botão. Ajuste o tempo conforme necessário.
    sleep(2)

    # Clica no botão "Subir Planilha de Preços".
    botao_importar_planilha.click()
    # Aguarda 1 segundo para que a janela de seleção de arquivo seja aberta. Ajuste o tempo conforme necessário.
    sleep(1)

    # Insira o caminho completo do arquivo da planilha no formato adequado para o seu sistema.
    # Substitua pelo caminho do arquivo em sua própria máquina.
    pg.write(r'C:\Projects\automacao-para-subir-planilha-para-site-admin\data\precos-produtos-atualizados.xlsx')
    # Aguarda 1 segundo após digitar o caminho do arquivo. Ajuste o tempo conforme necessário.
    sleep(1)

    # Pressiona "Enter" para confirmar e iniciar o carregamento do arquivo.
    pg.press("enter")
    # Aguarda 1 segundo para garantir que a ação seja concluída. Ajuste o tempo conforme necessário.
    sleep(1)


def atualizar_preco():
    # Localiza o botão "Atualizar Preço" na página.
    botao_atualizar_preco = driver.find_element(
        By.XPATH, "[@class='btn btn-secondary btn-custom']")
    # Aguarda 2 segundos antes de interagir com o botão. Ajuste o tempo conforme necessário.
    sleep(2)

    # Clica no botão "Atualizar Preço".
    botao_atualizar_preco.click()
    # Aguarda 1 segundo para garantir que a ação seja concluída. Ajuste o tempo conforme necessário.
    sleep(1)


def main():
    acessar_pagina()
    carregar_produtos_pagina()
    importar_planilha()
    atualizar_preco()

    # Fecha o navegador após concluir todas as ações.
    driver.quit()


if __name__ == "__main__":
    main()
