check = float(input("Informe um número para converter a temperatura: 1- Celsius para Fahrenheit, 2- Celsius para Kelvin, 3- Fahrenheit para Celsius, 4- Fahrenheit para Kelvin, 5- Kelvin para Celsius, 6- Kelvin para Fahrenheit: "))
temperatura = float(input("Informe o valor a ser convertido: "))
resultado = float
if check == 1: 
    resultado = (temperatura * 1.8) + 32
elif check == 2:
    resultado = temperatura + 273
elif check == 3:
    resultado = 5* (temperatura - 32) / 9 
elif check == 4:
    resultado = (temperatura-32) * 5/9 + 273
elif check == 5:
    resultado = temperatura - 273
elif check == 6:
    resultado = (temperatura - 273) *1.8 + 32

print("O valor escolhido foi convertido para: {}" .format(resultado))




