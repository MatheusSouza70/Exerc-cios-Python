cont = 0
consoantes = []
print("Informe 10 Letras")
for i in range(5):
    consoantes.append(str(input("Letra " + str(i))))
    consoanteB=[]
    if consoanteB not in ("a", "e", "i", "o", "u"):
        cont += 1

print("Há no total {} " .format(cont))