
#opcional 16 -> 18 / 65 ->
#obrigatorio 18 -> 65
nasc = int(input("Informe o ano de seu nascimento: "))
idade = 2021
idtotal = idade - nasc

def voto():
    
    if idtotal >=16 and idtotal <=18:
        print("Seu voto é opcional.")
    elif idtotal >=18 and idtotal <=65:
        print("Seu voto é obrigatório.")
    elif idtotal <16:
        print("Não é eleitor.")
    else:
        print("Seu voto é facultativo.")

print(voto())