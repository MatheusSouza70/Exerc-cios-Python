nota = []
for i in range (4):
    nota.append(int(input("Nota " + str(i))))
resultado = sum(nota)/len(nota)
print(resultado)