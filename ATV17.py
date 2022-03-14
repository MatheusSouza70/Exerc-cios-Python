valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

if(valor1>valor2):
    print("Operação Inválida")
for i in range(valor1,valor2):
    x = i%2
    if(x==1):
        print("Número ímpar: ", i)
        resultado = i+x



