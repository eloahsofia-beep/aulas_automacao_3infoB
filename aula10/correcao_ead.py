'''
1) Considere que a tabela abaixo representa uma planilha do Excel chamada
estudantes.xlsx. Crie o código para importar a bibliote pandas e para ler a planilha
do Excel para um DataFrame chamado tabela.
'''
import pandas as pd 
alunos = pd.read_excel("aula10\\dados.xlsx", sheet_name = "alunos")
'''
2) Crie o código para exibir os 5 primeiros registros do DataFrame.
'''
print(alunos.head(5))
'''
3) Crie o código para Inserir um novo aluno no DataFrame com os seguintes dados:
● RA: 0005
● Nome: Enzo Moreira
● Curso: Técnico em Jogos
● Turma: 1GMA
'''
alunos.loc[len(alunos)] = [8, "Enzo Moreira", "Técnico em jogos" ,"1GMA"]
'''
4) Crie o código para atualizar os dados do estudante Enzo Moreira para:
● Curso: Técnico em Informática
● Turma: 3TE
'''
alunos.loc[7] = [8, "Enzo Moreira", "Técnico em Informática" ,"1TE"]
print(alunos)
'''
5) Crie o código para excluir o estudante que está na linha de índice 1 do
DataFrame.
'''
alunos.drop(0, inplace = True)
print(alunos )
'''
6) Exportar o DataFrame atualizado para uma nova planilha do Excel.
'''
alunos.to_excel("nova_planilha.xlsx")