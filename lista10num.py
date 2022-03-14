listanumeros=[]
print("Informe os 10 números")
for i in range (10):
     listanumeros.append(int(input("Numero " + str(i))))
listanumeros.reverse()
print(listanumeros)  