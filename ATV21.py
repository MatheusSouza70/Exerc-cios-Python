soma = 0
QuantVa = 0
media = 0
somaPar = 0
QuantPar = 0
QuantImpar = 0
mediaPar = 0
porcentImpar = 0
maiorNum = 0
menorNum = 0
num = 0

for x in range (1,5):
    x = x+1
    valor = float(input("Digite um valor: "))
    soma = valor+soma
    QuantVa = QuantVa+1 
    media = soma/QuantVa 
        
    resultado = valor%2
    if (resultado ==0):
        somaPar = valor+somaPar
        QuantPar = QuantPar+1
        mediaPar = somaPar/QuantPar

    elif(resultado == 1):
        QuantImpar = QuantImpar+1
        porcentImpar = (QuantImpar/10)*100

    if (valor>maiorNum):
        maiorNum = valor

    if (valor<menorNum) and (x>1):
        menorNum = valor
            
    elif (x == 1):
        menorNum = valor 

print('A soma dos Numeros Difitador e {}'.format(soma))
print('A Quantidade de numeros digitados foi {}'.format(QuantVa))
print('A media dos valores digitados é {}'.format(media))
print('O maior Numero dgitado é {}'.format(maiorNum))
print('O menor numero digitado é {}'.format(menorNum))
print('A media dos valores pares digitados é {}'.format(mediaPar))
print('A porcentagem de numeros impares é {}%'.format(porcentImpar))






