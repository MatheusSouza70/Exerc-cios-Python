menor = None
maior = None

for i in range(0, 6):
    while True:
        try:
            peso = float(
                input('Entre com o peso da pessoa nº{} :'.format(i+1)))
        except ValueError:
            print('parece que você digitou um valor não numérico.')
            continue
        break
    menor = peso if menor is None else min(menor, peso)
    maior = peso if maior is None else max(maior, peso)

print('Menor peso: {}'.format(menor))
print('Maior peso: {}'.format(maior))