soma = 0
quantidadeVALORES = 0
somaPAR = 0
mediaPAR = 0
porcentagemIMPAR = 0
quantidadePAR = 0
quantidadeIMPAR = 0
media = 0
maiorNUMERO = 0
menorNUMERO = 0


for j in range (1,11):
    valor = float(input("Digite um valor: "))
    soma = valor+soma
    quantidadeVALORES = quantidadeVALORES+1
    media = soma/quantidadeVALORES

    resultado = valor%2
    if (resultado==0):
        somaPAR = valor+somaPAR
        quantidadePAR = quantidadePAR+1
        mediaPAR = somaPAR/quantidadePAR
    elif (resultado==1):
        quantidadeIMPAR = quantidadeIMPAR+1
        porcentagemIMPAR = (quantidadeIMPAR/10)*100

    if (valor>maiorNUMERO):
        maiorNUMERO = valor

    if (valor<menorNUMERO) and (j>1):
        menorNUMERO = valor
    elif (j==1):
        menorNUMERO = valor

print ("A soma dos números digitados é: ", soma)
print ("A quantidade de numeros digitados foi: ", quantidadeVALORES)
print ("A media dos valores digitados é: ", media)
print ("O maior número digitado é: ", maiorNUMERO)
print ("O menor númro digitado é: ", menorNUMERO)
print ("A media dos valores pares é: ", mediaPAR)
print ("A porcentagem de numeros ímpares é: ", porcentagemIMPAR, "%")
    