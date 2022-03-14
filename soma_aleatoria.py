from random import randint 

x = (int(input("Informe a quantidade de números: ")))
soma = 0

for contador in range (x):
    numero_sorteado = randint(1,10)
    print(numero_sorteado)
    soma = soma + numero_sorteado

print("A soma é ", soma)
