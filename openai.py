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
        prompt = 'Me forneça 3 alternativas, assim como suas aplicações codificadas, para solucionar o seguinte erro do código: '
        prompt += mensagem_operacao + '.\n\n'

    elif tipo_operacao == 'leg':
        prompt = 'Me forneça possíveis mudanças que melhorariam a legibilidade e qualidade do código, evitando ao máximo modularização desnecessária.\n\n'

    elif tipo_operacao == 'alt':
        prompt = 'Desejo alterar o código abaixo. Me forneça 3 alternativas, assim como suas aplicações codificadas, para codificar a seguinte ideia: '
        prompt += mensagem_operacao + '.\n\n'

    elif tipo_operacao == 'out':
        prompt = mensagem_operacao + '.\n\n'

    if prompt:
        text_area.send_keys(prompt)
        # Pasting code from clipboard
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')


def copiar_codigo_vscode():
    # Focando na janela do Visual Studio
    pyautogui.click(500, 250)  # Ajuste as coordenadas conforme necessário
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')


def main():
    parser = argparse.ArgumentParser(description='CLI para interagir com ChatGPT e Visual Studio Code.')
    parser.add_argument('tipo_operacao', choices=['err', 'leg', 'alt', 'out'], help='Tipo de operação a ser realizada.')
    parser.add_argument('mensagem_operacao', nargs='*', help='Mensagem descrevendo a operação.')
    args = parser.parse_args()

    mensagem_operacao = ' '.join(args.mensagem_operacao)
    copiar_codigo_vscode()
    abrir_chatgpt(args.tipo_operacao, mensagem_operacao)


if __name__ == "__main__":
    main()
