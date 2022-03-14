n = int(input("Informe uma nota de 0 a 10: "))

while n <0 or n >10:
    print("A nota informada é inválida, tente novamente. ")
    n = int(input("Informe uma nota de 0 a 10: "))
print("A nota informada foi {}" .format(n))
