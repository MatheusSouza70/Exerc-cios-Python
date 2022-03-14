frase = str(input("Informe algo entre 1 a 10 caracteres: "))

def fraseprincipal():
    if len(frase) > 10:
        print("Acima do limite de caracteres.")
        return False
    elif len(frase) < 1:
        print("Abaixo do número necessário de caracteres.")
        return False
    else:
        print("Está dentro dos limites.")
        return True

print(fraseprincipal())