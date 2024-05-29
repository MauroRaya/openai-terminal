import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import argparse

WAIT_TIME = 10


def abrir_chatgpt(tipo_operacao, mensagem_operacao):
    driver = webdriver.Firefox()
    driver.get("https://chatgpt.com/?oai-dm=1")
    WebDriverWait(driver, WAIT_TIME).until(EC.presence_of_element_located((By.ID, "prompt-textarea")))
    text_area = driver.find_element(By.ID, "prompt-textarea")
    
    prompt = ''

    if tipo_operacao == 'err':
        prompt = 'Corrija o seguinte erro do código, forneçendo 3 possiveis alternativas de soluções: '

    elif tipo_operacao == 'leg':
        prompt = 'Melhore a legibilidade e qualidade do código: '

    elif tipo_operacao == 'alt':
        prompt = 'Modifique o código para realizar a seguinte ideia: '

    elif tipo_operacao == 'exp':
        prompt = 'Reescreva o código abaixo, escrevendo uma documentação explicando cada linha como se estivesse ensinando a uma criança de 5 anos: '


    elif tipo_operacao == 'out':
        prompt = 'Saia do programa: '

    if prompt:
        text_area.send_keys(prompt + mensagem_operacao)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')


def copiar_codigo_vscode():
    pyautogui.click(500, 250)  
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')


def main():
    parser = argparse.ArgumentParser(description='CLI para interagir com ChatGPT e Visual Studio Code.')
    parser.add_argument('tipo_operacao', choices=['err', 'leg', 'alt', 'exp', 'out'], help='Tipo de operação a ser realizada.')
    parser.add_argument('mensagem_operacao', nargs='*', help='Mensagem descrevendo a operação.')
    args = parser.parse_args()

    mensagem_operacao = ' '.join(args.mensagem_operacao)
    copiar_codigo_vscode()
    abrir_chatgpt(args.tipo_operacao, mensagem_operacao)


if __name__ == "__main__":
    main()
