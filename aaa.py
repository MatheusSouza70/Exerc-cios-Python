x = 0


while x != 1:

    salario = int(input("Quanto você ganha por hora trabalhada: "))
    hora = int(input("Quantas horas você trabalhou no mês: "))

    salmes = salario * hora
    inss = (salmes * 0.08)
    renda = (salmes * 0.11)
    sindicato = (salmes * 0.05)
    desconto = inss + renda + sindicato
    bruto = salmes - desconto

    print("Recebe R${}" .format(salmes))
    print("Pagou R${} ao INSS" .format(inss))
    print("Pagou R${} ao Imposto de Renda" .format(renda))
    print("Pagou R${} ao Sindicato" .format(sindicato))
    print("Seu salário liquido é R${}" .format(bruto))


    print("0 para continuar, 1 para sair.")
    x = int(input("Deseja continuar?"))
