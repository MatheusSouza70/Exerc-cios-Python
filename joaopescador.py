x = 0

while x != 1:
    peso = int(input("Informe o peso do peixe: "))
    if peso >50:
        excedente = peso - 50
        multa = 40 * excedente
        print("vai pagar R$ {}" .format(multa))
        x = int(input("Digite 1 para continuar ou 0 para sair: "))
    else:
        print("não há multa") 
        x = int(input("Digite 1 para sair ou 0 para continuar: "))
