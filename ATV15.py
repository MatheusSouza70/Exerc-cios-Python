print('TABUADA')

numero = int(input('Digite o numero da Tabuada: '))

for x in range(1,11):
    total =  (numero*x)
    print('{} x {} = {}'.format(x , numero, total))