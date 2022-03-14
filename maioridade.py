from datetime import date
m = 0

for i in range(1, 8):
    pessoa = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(i)))

    if date.today().year - pessoa < 18:
        m += 1
print('{} são maiores e {} são menores.'.format(7 - m, m))
