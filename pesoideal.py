altura = float(input("Informe sua altura em centimetros: "))
sexo = str(input("Informe seu sexo: "))

x = 1
while 'x' != 1:
    if sexo == "Feminino" or sexo == "Mulher" or sexo == "feminino" or sexo == "mulher" or sexo == "f" or sexo == "F":
        pesoideal = (72.7 * altura)-58
        print("O seu peso ideal é: {} " .format(pesoideal))
    if sexo == "Masculino" or sexo == "masculino" or sexo == "Homem" or sexo == "homem" or sexo == "h" or sexo == "H":
        pesoideal = (62.1 * altura)-44.7
        print("O seu peso ideal é: {} " .format(pesoideal))

    

    