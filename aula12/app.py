import pyautogui
import pandas as pd
import time


def preencher (imagem, deslocamentoY = 0, valor = None):
    campo = pyautogui.locateCenterOnScreen(imagem, confidence=0.9)
    pyautogui.click(campo.x, campo.y + deslocamentoY)
    if valor:
        pyautogui.write(valor)
    pyautogui.scroll(-150)
    time.sleep(2)

planilha = pd.read_excel('aula12\\dados_automacao.xlsx')
for indice, linha in planilha.iterrows():

    #variaveis
    nome  = linha["nome"]
    matricula = str(linha["matricula"])
    curso = linha["curso"]
    genero = linha["genero"]
    preencher("aula12\\email.png")
    preencher("aula12\\nome.png", 50, nome)
    preencher("aula12\\matricula.png", 50, matricula)
    preencher("aula12\\curso.png",50, curso)
    preencher(f"aula12\\{genero}.png")
    preencher("aula12\\enviar.png")
    preencher("aula12\\registrar.png")