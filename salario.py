salario = float(input("Informe seu salário: "))

if salario <=980:
    novosalario = salario * 1.20
    print("Aumento de 20%")
    print("Seu salário antigo era {}" .format(salario))
    print("Seu novo salário é {}" .format(novosalario))
elif salario >980 and salario <=1700:
    novosalario = salario * 1.15
    print("Aumento de 15%")
    print("Seu salário antigo era {}" .format(salario))
    print("Seu novo salário é {}" .format(novosalario))
elif salario >1701 and salario <=2500:
    novosalario = salario * 1.10
    print("Aumento de 10%")
    print("Seu salário antigo era {}" .format(salario))
    print("Seu novo salário é {}" .format(novosalario))
elif salario >2501:
    novosalario = salario * 1.05
    print("Aumento de 5%")
    print("Seu salário antigo era {}" .format(salario))
    print("Seu novo salário é {}" .format(novosalario))