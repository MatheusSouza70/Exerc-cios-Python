cont = 0
soma = 0
media = 0
contm = 0
contn = 0
maior = 0
menor = 0

for i in range (1,5):
    nome = str(input("Informe o seu nome: "))
    idade = int(input("Informe sua idade: "))
    print("M para Masculino")
    print("F para Feminino")
    sexo = str(input("Informe seu sexo: "))

    cont = cont + 1

    soma = soma + idade

    if idade > maior:
            maior = idade
            nomem = nome
    else:
        menor = idade

    if idade > 20 and sexo == "F":
        contm = contm + 1
    elif idade < 20 and sexo == "F":
        contn = contn + 1

media = soma / cont

print("A média de idade é {:.2f}" .format(media))
print("O nome da pessoa mais velha é {:.2f}", nomem)
print("Há {:.2f} mulheres menores de 20.", contn)