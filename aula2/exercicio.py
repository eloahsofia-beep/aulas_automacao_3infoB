'''Crie um app que solicite duas notas do usuario,
 após calcule a média das notas. Se a media for maior ou igual a 6
 mostre uma mensagem dizendo que o aluno esta aprovado.
 se a media for menor que 6, peça para o aluno digitar a nota do exxame final. calcule
 novamente a media apos o exame final ((media+exame final)/2). se a media for maior que 6 mostre a mesnagem de aprovado, 
 senao mostre que o alunos foi reprovado'''

nota1 = int(input("Digite a sua primeira nota:"))
nota2 = int(input("Digite a sua segunta nota:"))

media = nota1 + nota2 /2
if media > 6:
    print("Você foi aprovado!")
  
else :
    ef = float(input("Digite a nota do exame final: "))
    media2 = (media + ef)/2
    if media2 > 6:
        print("Você foi aprovado!")
    else:
        print("Você foi reprovado!")