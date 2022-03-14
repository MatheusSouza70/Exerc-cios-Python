s = 0  # Contador de soma
for num in range(1, 501):  # de 1 até 500
    if num % 2 == 1:  # Ímpares
        if num % 3 == 0:  # Ímpares múltiplos de 3
            s += num  # soma = soma + num
print("A soma dos múltiplos é: {}.".format(s))