#Importar biblioteca pandas 
import pandas as pd

#Carregar uma planilha do excel:
#lê o arquivo que está no caminho e armazena na variável df
df = pd.read_excel("esquenta_prova/planilha.xlsx")
print(df.head())

#Compreender o funcionamento do loc
print(df.loc[0]) #Imprime a primeira linha
print(df.loc[0, "Nome"])                #Imprime a coluna nome da primeira linha
print(df.loc[0:3])                      #Imprime a primeira e terceira linha (use o : para definir as linhas desejadas)
print(df.loc[4:6, "Nome"])              #Seleciona a coluna Nome das linhas entre 4, 5 e 6
print(df.loc[4:6, ["Nome", "Idade"]])   #Seleciona as colunas nome e idade das linhas 4, 5 e 6 (use [] para selecionar varias colunas)
print(df.loc[ : , "Nome"])              #localizar uma única coluna - todas as linhas (use nomente os : que ele entende que são todas as linhas da coluna selecionada)

df2 = df.loc[3:6, ["Nome", "Sexo"]]
print(df2)

print(df2.loc[[True, False, False, True], ["Nome", "Sexo"]])

#Inserir novos dados da planilha
#Esse loc adiciona novos dados e o len, lê qual seria o número da proxima linha e exibe
df.loc[len(df)] = "Isis", "Feminino", 18, "Técnico em Informática", "Automação T", 10  
print(df)

#Atualizar dados da planilha
#Na linha 30 ele vai atualaizar os valores das colunas curso e Disciplina
#Se fosse para atualizar tudo, seria: df.loc[30] = "Isis", "Feminino", 18, "Artes", "Teatro", 10  

df.loc[30, ["Curso", "Disciplina"]] = ["Artes", "Teatro"]
print(df)

#Filtrar dados
#Ele vai selecionar só os elementos com a idade 20 anos e sexo Feminino
#se eu não colocar o loc ele vai exibir todos os elemntos da lista e exibir true e false.
condicao1 = df["Idade"] == 20
condicao2 = df["Sexo"] == "Feminino"
print(df.loc[condicao1 & condicao2])

#Classificar dados
#Classifica os nomes em ordem alfabética em ordem crescente.
tabela_ordenada = df.sort_values("Nome", ascending = True)
print(tabela_ordenada)

#Contar Dados
#Ele vai pegar tudo oq é igual, agrupar e contar
tabela_contagem = df.value_counts("Sexo")
print(tabela_contagem)

#Agrupar dados
#A diferença de value_counts para groupby e que no groupby da para calcular outras coisas além de contar, tipo sun-soma mead-media
tabela_agrupada = df.groupby("Curso")["Curso"].count()
print(tabela_agrupada)

#Exportar dados
df.to_excel("esquenta_prova\\nova_planilhaesquenta.xlsx")


