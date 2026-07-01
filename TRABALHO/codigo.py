#Importar bibliotecas
import pyautogui
import pandas as pd
import time

#Conteúdo da aula 7 :)
pyautogui.hotkey("ctrl", "l")
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(2)
pyautogui.hotkey('win', 'up')
pyautogui.write('https://form.jotform.com/261815361073050')
pyautogui.press('enter')
time.sleep(3)

def preencher(imagem, deslocamentoY = 0, valor = None):
    campo = pyautogui.locateCenterOnScreen(imagem, confidence=0.8)
    pyautogui.click(campo.x, campo.y + deslocamentoY)
    if valor:
        pyautogui.write(valor)
        pyautogui.scroll(-150)
    time.sleep(2)

planilha = pd.read_excel('consultas.xlsx')
for indice, linha in planilha.iterrows():

    #variáveis
    nome = linha["nome"]
    telefone = str(linha["telefone"])
    data = linha["data"]
    horario = linha["horario"]
    medico = linha["medico"]
    cpf = str(linha["cpf"])

    #Preenchimento automático
    preencher("nome.png", 50, nome)
    preencher("telefone.png", 50, telefone)
    preencher("cpf.png", 50, cpf)
    preencher("medico.png", 50, medico)
    preencher("data.png", 50, str(data))
    preencher("horario.png", 50, str(horario))
    preencher("agendar.png",10)
