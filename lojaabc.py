idade = int(input('Informe sua idade'))
cliente = str(input('É cliente da nossa loja? (s) sim e (n) não'))
if cliente == 's':
    clienteA = int(input('Informe a quantos anos é cliente: '))
elif cliente == 'n':
    print('Ok.')

totalc = float(input('Informe o total da compra '))
parc = int(input('Informe a quantidade de parcelas (Se a compra foi a vista digite (0))'))

if parc == 0 and totalc >= 5000:
    desc = totalc / 1.15
    print('R$ %.2f' % desc)
    print('Houve o desconto de 15%')
elif parc > 0 and parc <= 6 and totalc >= 5000:
    desc = totalc / 1.10
    print('R$ %.2f' % desc)
    print('Houve o desconto de 10%')
elif parc > 6 and totalc >= 5000:
    print('Não houve desconto pelo total de parcelas')
elif parc == 0 and idade >= 60:
    desc = totalc / 1.15
    print('R$ %.2f' % desc)
    print('Houve o desconto de 15%')
elif parc > 0 and parc <= 6 and idade >= 60:
    desc = totalc / 1.10
    print('R$ %.2f' % desc)
    print('Houve o desconto de 10%')
elif parc > 6 and idade >= 60:
    print('Não houve desconto pelo total de parcelas')
elif parc == 0 and clienteA >= 10:
    desc = totalc / 1.15
    print('R$ %.2f' % desc)
    print('Houve o desconto de 15%')
elif parc > 0 and parc <= 6 and clienteA >= 10:
    desc = totalc / 1.10
    print('R$ %.2f' % desc)
    print('Houve o desconto de 10%')
elif parc > 6 and clienteA >= 10:
    print('Não houve desconto pelo total de parcelas')
elif parc == 0:
    totalv = totalc / 1.10
    print('R$ %.2f' % totalv)
    print('Houve o desconto de 10%')
elif parc > 0 and parc <= 6:
    totalp = totalc / 1.05
    print('R$ %.2f' % totalp)
    print('Houve o desconto de 5%')
elif parc > 6:
    print('Não houve desconto')
