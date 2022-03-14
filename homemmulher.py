altura = float(input("Informe sua altura em centimetros: "))
sexo = str(input("Informe seu sexo: "))

if sexo == "Feminino" or sexo == "Mulher" or sexo == "feminino" or sexo == "mulher":
    peso = (altura - 100) * 0.85
    print("O seu peso ideal é: {} " .format(peso))
if sexo == "Masculino" or sexo == "masculino" or sexo == "Homem" or sexo == "homem":
    peso = (altura - 100) * 0.90
    print("O seu peso ideal é: {} " .format(peso))