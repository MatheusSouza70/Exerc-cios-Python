def fatorial():
    numero = int(input("Valor a ser fatorado: "))
    fat = 1
    i = 2
    while i <= numero:
        fat = fat * i
        i = i + 1
    print("O valor de", numero, "! é: ", fat)

fatorial()