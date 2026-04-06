'''
crie um script que usa a função quadrada criada 
no arquivo exercicio_f1.py. Esse script deve pedir
para o usuário digiar um número, depois deve calcular 
o quadrado usando a função e depois imprimir o resultado.
'''

import exercicio_f1 as eloah

eloah.imprimir("Digite o número 1: ")
n1 = eloah.ler()
eloah.pulalinha()
eloah.pulalinh()
resposta = eloah.quadrado(n1)
eloah.imprimir(f"O resultado é {resposta}")
 