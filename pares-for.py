numerototal = 0
impar = 0
for i in range (1,7):
    numero = int(input("Informe o {}° número: " .format(i)))
    if numero % 2 == 0:
        numerototal = numero + numerototal
    else:
        impar = impar - numero
        
print(numerototal)
