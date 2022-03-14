x = 0
while x != 1:
    medida = float(input('informe a quantidade de metros quadrados: '))
    
    litros = medida / 3
    qtd_latas18 = medida / 18
    qtd_latas36 =medida / 3.6

    print('a quantidade de latas de 18L a ser usado é: {}'.format(qtd_latas18))
    print('a quantidade de galões de 3,6L a ser usado é: {}'.format(qtd_latas36))

    valor_total18 = qtd_latas18 * 450
    valor_total36 = qtd_latas36 * 190

    print('o valor total em latas de 18L é: R${}'.format(valor_total18))
    print('o valor total em galões de 3,6L é: R$ {}'.format(valor_total36))
    print("0 para continuar, 1 para sair.")
    x = int(input("Deseja continuar?"))


  