autorizacaomae = str(input("Maria recebe sua autorização para viajar?: "))
autorizacaopai = str(input("Marcos recebe sua autorização para viajar?: "))
nota = int(input("Qual foi a nota de Carla na escola?: "))
decimomae = str(input("Maria recebe seu 13° antes de 12 de Dezembro?: "))
decimopai = str(input("Marcos recebe seu 13° antes de 12 de Dezembro?: "))
gastos = str(input("As passagens vão ser compradas em até 3 dias antes do embarque?: "))
pontos = 0
valordiaria = 1700
total = 1700 * 9

if autorizacaomae and autorizacaopai == "Sim":
    pontos = pontos + 1
elif autorizacaomae or autorizacaopai == "Não":
    pontos = pontos - 1

if nota >= 7:
    pontos = pontos + 1
else:
    pontos = pontos - 1

if decimomae or decimopai == "Sim":
    pontos = pontos + 1
elif decimomae and decimopai == "Não":
    pontos = pontos - 1

if gastos == "Sim":
    gastototal = 1.100 * 3
elif gastos == "Não":
    gastototal = 890 * 3

    total = total + gastototal

if pontos == 4 and total <=10000:
    print("Vocês poderam viajar.")
    print("O total gasto será R${:.2f}" .format(total))
else:
    print("Vocês não poderam viajar.")
    print("O total gasto será R${:.2f}" .format(total))