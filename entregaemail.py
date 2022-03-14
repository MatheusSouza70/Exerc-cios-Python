placaval = []

opcao = ""

while opcao.upper() != 'X':
    letras = 0
    numeros = 0
    print("-"*50)
    placa = input("Informe a placa do veículo:")

    if len(placa) == 7:
        for i, item in enumerate(placa):
            if item.isalpha():
                letras += 1
            elif item.isnumeric():
                numeros += 1

        if (letras == 3 and numeros == 4):
            print('Placa válida!')
            print("Placa do Modelo Antigo (AAA9999)")
            print("-"*50)
            placaval.append(placa)
            
        elif (letras == 4 and numeros == 3):
            print('Placa válida!')
            print("Placa do Modelo Mercosul (AAA9A99)")
            print("-"*50)
            placaval.append(placa)
        else:
            print('Placa inválida. Por favor, insira uma placa válida:')

    else:
        print("Placa inválida. Por favor, insira uma placa válida:")
    print("\n\n")
    opcao = str(input("Pressione ENTER para continuar ou 'X' para sair:"))
    print("\n\n")
    print("-"*50)

print("-"*50)
print("Placas Válidas")
for placaslist in placaval:
    print("Placa:{}" .format(placaslist))
print("-"*50)