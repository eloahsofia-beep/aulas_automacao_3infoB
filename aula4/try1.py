'''
Crie um script que solicita que o usuário digite
dois número, após mostre o resultado da divisão
do primeiro pelo segundo número.
'''
while True:
    try:
        n1 = int(input('Digite o número 1: '))
        n2 = int(input('Digite o número 2: '))
        resultado = n1 / n2
        print('O resultado da divisão é', resultado)
        break
    except ValueError:
        print('O valor digitado é inválido')
    except ZeroDivisionError:
        print('Você não pode dividir por 0')
    except Exception as e:
        print('Ocorreu um erro', e)