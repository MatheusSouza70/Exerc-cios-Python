nome = str(input("Por favor, Informe o seu nome: "))
cnh = int(input("Informe o número de sua CNH (9 dígitos): "))
dia = int(input(" Em que dia você nasceu?:  "))
mes = int(input(" Em que mês você nasceu?:  "))
ano = int(input(" Em que ano você nasceu?:  "))
km = int(input("Quantos KM foram rodados com o veículo?: "))
dias = int(input("Informe quantos dias você esteve em posse do veículo: "))
print("1 para veículo (Porte pequeno) = R$180,00")
print("2 para veículo (Porte médio) = R$220,00")
print("3 para veículo (Porte grande) = R$270,00")
veiculo = int(input("Qual veiculo você alugou?: "))
mlk = 0
idade = 2021 - ano

if veiculo == 1:
    custo_dias = (dias * 180)
elif veiculo == 2:
    custo_dias = (dias * 220)
elif veiculo == 3:
    custo_dias = (dias * 270)
else:
    print("Valor de veículo inválido.")

if idade < 21:
    mlk = (dias * 120)


custo_km = (km * 3.95)
total = (custo_dias + custo_km + mlk)

print("Olá, {}" .format(nome))
print("Portador da CNH: {:.2f}" .format(cnh))
print("Nasceu no dia:{}" .format(dia))
print("Do mês {} " .format(mes))
print("de {}" .format(ano))
print("O total a pagar será de R${}" .format(total))