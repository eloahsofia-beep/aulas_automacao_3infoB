#Pandas: biblioteca em py que permite a manipulação de arquivos
#Em formato tabular, Ex:Plannilhas e Tabelas

#Ediçaõ de dados (Inserir, Atualizar e Excluir)

#Instalação
#pip instal pandas
#Importar biblioteca (as renomeia o pacote "abreviação")
import pandas as pd

#Ler uma planilha do Excel
#Cria variavel planilha que vai guardar a planilha do Excel
#Em pandas chamamos a planilha de DataFrame
planilha = pd.read_excel("aula9\\Dados_3infob.xlsx")

#imprime os dados da planilha
#print(planilha)

#Imprime a cabeça da planilha: Quanas linhas da parte de cima
#eu quero imprimir
print(planilha.head(6))

#imprimir as últimas 3 linhas
#print(planilha.tail(5))

nova = planilha.head(4)
print(nova.tail(2))
#Inserir um novo registro na planilha: DataFrame
planilha.loc[len(planilha)] = ["Pablo", 52, 1.8, "M"]
print(planilha)

#atualizar um registro
planilha.loc[16] = ["Pablo", 52, 1.8, "Masculino"]
print(planilha)

#atualizar um registro,apenas uma coluna
planilha.loc[16, "Nome"] = "Pablo Sandi"
print(planilha)

#atualizar um registro, duas ou mais colunas
planilha.loc[16, ["Peso", "Altura"]] = [53, 1.81]
print(planilha)

#Remover um registro da planilha
planilha.drop(13, inplace=True)
print(planilha)