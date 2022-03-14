login = input("Login: ")
senha = input('Digite a senha: ')

while senha == login:
    print("Sua senha deve ser diferente do login. Tente novamente.")
    senha = input("Informe a senha novamente")
print("Ok. Login e Senha válidos.")
