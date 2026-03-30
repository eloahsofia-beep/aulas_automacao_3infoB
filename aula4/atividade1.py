'''
Crie um script que solicite o usuário e a senha de um estudante.
Enquanto o estudante não digitar o usuário e a senha corretamente
o programa deve continuar solicitando as credenciais. Quando o usuário 
digitá-las corretamente, o programa deve imprimir a mensagem de Bem-vindo 
e terminar. O usuário e a senha deve ser fixo(padrão).
'''
#jeito1
while True:
    usuario = input("Digite seu login: ")
    senha = input("Digite sua senha: ")

    if(usuario == "admin" or senha == "admin123"):
        print("Bem Vindos ao sistema.")
        break
    else:
        print("Usuários e senha inválidos.")

#jeito2

usuario = " "
senha = " "

while (usuario != "admin" or senha != "admin123"):
     usuario = input("Digite seu login: ")
     senha = input("Digite sua senha: ")

print("Bem Vindos ao sistema.")


