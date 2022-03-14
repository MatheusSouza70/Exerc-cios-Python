# pegar os 9 numeros (sem 2 ultimos), multiplicar da esquerda pra direita iniciando por 10 e decrescendo até 2 (1 digito por 10, 2 digito por 9...)
# soma dos resultados em sequencia esquerda pra direita.
# (valor * 10) / 11
# resultado é o resto da divisão.


while True:

    def calculo():
        print('V - Informe o CPF - V')
        cpf = input()
        if len(cpf) < 9:
            print("CPF inválido")
            exit()
        int(cpf)
        #colocando cada um dos digitos do cpf em uma variável.
        num1 = int(cpf[0])
        num2 = int(cpf[1])
        num3 = int(cpf[2])
        num4 = int(cpf[3])
        num5 = int(cpf[4])
        num6 = int(cpf[5])
        num7 = int(cpf[6])
        num8 = int(cpf[7])
        num9 = int(cpf[8])
        if num1 == num2 == num3 == num4 == num5 == num6 == num7 == num8 == num9:
            print('CPF inválido')
            exit()

        #primeiro digito
        digitopt1 = num1 * 10 + num2 * 9 + num3 * 8 + num4 * \
            7 + num5 * 6 + num6 * 5 + num7 * 4 + num8 * 3 + num9 * 2
            
        primeirodig = (digitopt1 * 10) % 11

        if primeirodig == 10:  # caso o resto se torne uma dezena, vire unidade.
            primeirodig = 0

        #segundo digito
        digitopt2 = num1 * 11 + num2 * 10 + num3 * 9 + num4 * 8 + num5 * 7 + \
            num6 * 6 + num7 * 5 + num8 * 4 + num9 * 3 + primeirodig * 2
        segundodig = (digitopt2 * 10) % 11

        if segundodig == 10:  # caso o resto se torne uma dezena, vire unidade
            segundodig = 0

        print("Digitos")
        print(primeirodig, segundodig)
    print("Verificação de CPF")
    x = int(input("Digite 1 para iniciar e 0 para finalizar o programa: "))
    if x == 1:
        calculo()
    else:
        exit()