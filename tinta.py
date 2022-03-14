medida =float(input("Informe quantos metros quadrados: "))
litros = medida / 3

if medida % 50 == 0:
    latas = medida / 50
else:
    latas = int(medida / 50) + 1

preco = latas * 560
print("%d latas" %latas)
print("R$ %.2f" %preco)