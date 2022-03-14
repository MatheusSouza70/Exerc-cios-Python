espectador = 0
regular = 0
otimo = 0
bom = 0
mediaIDADE = 0
media = 0
porcentagem = 0

for j in range(1,6):
    espectador = espectador+1
    print ("Espectador",espectador)
    idade = int(input("Digite sua idade: "))
    nota = float(input("Digite sua nota para o filme: (De 1 a 3) "))

    if (nota==1):
        regular=regular+1
    elif (nota==2):
        bom=bom+1
    elif (nota==3):
        otimo=otimo+1
        mediaIDADE=idade+mediaIDADE
        media = mediaIDADE/otimo
    
    porcentagem = (bom/j)*100

print ("A media de idade das pessoas que respondeu OTIMO é de ", media)
print ("A quantidade de pessoas que respondeu regular foi: ", regular)
print ("A porcentagem de pessoas que respondeu bom é de: ", porcentagem, "%")
