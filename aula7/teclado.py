import pyautogui
import time

#abre uma janela de entrada de dados
pergunta = pyautogui.prompt("O que deseja saber hoje?")

#pressiona um atalho do teclado 
#(win + d minimiza janelas e mostra desktop)
pyautogui.hotkey("win", "d")
#pressiona a tecla win
pyautogui.press('win')
#digita um texto onde o curso está
pyautogui.write('chrome')
#pressiona a tecla enter
pyautogui.press('enter')

#faz uma pausa de 2 segundos
time.sleep(2)

#maximiza a janela do chrome
pyautogui.hotkey('win', 'up')

#digita um endereço na url
pyautogui.write('http://www.chatgpt.com')
pyautogui.press('enter')

#faz uma pausa
time.sleep(3)

#digita o texto armazenado na variavel pergunta
pyautogui.write(pergunta)
pyautogui.press('enter')


while True:
    #faz uma pausa
    time.sleep(2)
    try:
        #localiza a coordenadas na imagem na tela
        xy = pyautogui.locateCenterOnScreen('aula7\\seta_scroll.png', confidence=0.8)
        #clica na imagem
        pyautogui.click(xy)
        break
    except:
        print('Ainda processando ...')


#faz uma pausa
time.sleep(2)

#localiza a coordenadas na imagem na tela
xy = pyautogui.locateCenterOnScreen('aula7\\copiar.png', confidence=.98)
#clica na imagem
pyautogui.click(xy)

#faz uma pausa
time.sleep(2)

#abre outra guia no chrome
pyautogui.hotkey('ctrl', 't')

#faz uma pausa
time.slep(1)

#digita o endereço
pyautogui.write('http://www.gmail.com')
pyautogui.press('enter')
time.sleep(3)

#clica no botão escrever
xy = pyautogui.locateCenterOnScreen('aula7\\escrever.png', confidence=0.95)
pyautogui.click(xy)

#faz uma pausa
time.sleep(2)

#gigita o endereco
pyautogui.write("softip@gmail.com")
time.sleep(2)
pyautogui.press("tap")
pyautogui.write("pesquisa automatizada")
pyautogui.press("tap")
pyautogui.hotkey("ctrl", "v")

#clica no boato enviar
xy = pyautogui.locateCenterOnScreen('aula7\\enviar.png', confidence=0.95)
pyautogui.click(xy)

#termina
pyautogui.alert("terminei o trabalho ")