salarioinicial = 1000
aumento = 0
salario = 0
ano = 7
salariofinal = 0

print ("Em 2005 o salario inicial desse funcionario era de R$:{}".format(salarioinicial))
aumento = 1.5
print("O funcionario recebe o aumento de quantos % {}".format(aumento))

aumento = (aumento/100)+1
salario = aumento

print ("Em 2006 o salário desse funcionario foi de R$: {}".format(salario))
porcentagem = 3
print("\n Em 2007 o funcionario teve aumento de quantos %? {}".format(porcentagem))

salario = salario*((porcentagem/100)+1)

print ("O salario desse funcionario no ano de 20007 foi de R$: {}".format(salario))

for j in range(1,15):
    ano = ano+1
    porcentagem = porcentagem*2
    salario = salario*((porcentagem/100)+1)
    print("Em DOIS MIL E", ano, "o salario desse funcionario foi de R$: {}".format(salario))

salarioFINAL = salario
print ("O salário atual desse funcionário é de R$: {}".format(salariofinal))