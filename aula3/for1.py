#Estrutura de Repetição For: Ultilizando para repetir um conjunto
#instruções - comandos, quando sabemos quantas vezes a intrução deve ser repetida

#Exemplo 1
#for variável in range(valor inicial, valor final, passo)
#range -> intervalo de valores

#range(1,10,1): intervalo Gerado -> 1, 2, 3, 4, 5, 6, 7, 8, 9
for i in range(1, 10, 1):
    print(i, end=" ")

print("\n")
     
#range(1,7,2): intervalo Gerado -> 1, 3, 5,
for i in range(1, 7, 2):
    print(i, end=" ")

print("\n")

#range(0, -4, -1): intervalo Gerado -> 0, -1, -2, -3, 
for i in range(0, -4, -1):
    print(i, end=" ")

print("\n")

#range(10): intervalo Gerado -> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
for i in range(10):
    print(i, end=" ")

print("\n")


