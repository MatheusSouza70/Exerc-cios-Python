valor1 = int(input("informe o primeiro valor: "))
valor2 = int(input("informe o segundoo valor: "))
valor3 = int(input("informe o terceiro valor: "))
if valor1 > valor2:
    print("o maior valor é: {} " .format(valor1))
elif valor1 < valor2:
    print("o maior valor é: {} " .format(valor2))
elif valor3 > valor2:
    print("o maior valor é: {} " .format(valor3))
elif valor3 > valor1:
    print("o maior valor é: {} " .format(valor3))   
else:
    print(" os números informados são iguais.")