import os
 
altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em kg: "))
 
imc = peso / (altura * altura)
 
print("Seu IMC é: {:.1f}" .format(imc))
 
if imc < 16:
	print("Baixo peso muito grave")
elif imc < 17:
	print("Baixo peso grave")
elif imc < 18.5:
	print("Baixo peso")
elif imc < 25:
	print("Peso normal")
elif imc < 30:
	print("Sobrepeso")
elif imc < 35:
	print("Obesidade Grau I")
elif imc < 40:
	print("Obesidade Grau II (severa)")
else:
	print("Obesidade Grau III (mórbida)")
 
os.system("pause")