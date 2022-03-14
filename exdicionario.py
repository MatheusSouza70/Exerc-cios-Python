voos={}

while True:
    numero = input ("\nVoo:")
    origem = input ("Origem: ")
    dest = input ("Destino: ")
    
    voos.update({numero: [origem, dest]})
    resp=input("\n Deseja Continuar? [S/N]")
    if resp == "n" or resp == "N":
        print("\n")
        break



for trecho in voos.values():
    if trecho[1].upper() == "RECIFE":
        del trecho[1], trecho[0]

print(voos)