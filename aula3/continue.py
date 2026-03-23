#Comando continue: Ignora o restante dos comandos
#dentro do loop e continua do inicio na próxima interação

aluno1 = {"nome" : "Pablo", "idade": 17, "sexo" : "M"}
aluno2 = {"nome" : "Carlos", "idade": 18, "sexo" : "M"}
aluno3 = {"nome" : "Samara", "idade": 17, "sexo" : "F"}

#lista com dic
alunos = [aluno1, aluno2, aluno3]

for aluno in alunos:
    if aluno['idade'] >= 18:
        continue
    print("Olá", aluno['nome'], "qual éseu passa tempo")
    aluno['hobbie'] = input("")

print(alunos)