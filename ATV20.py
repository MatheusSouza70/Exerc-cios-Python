
A = float(input("Digite o valor do primeiro lado:"))
B = float(input("Digite o valor do segundo lado:"))
C = float(input("Digite o valor do lado lado:"))

Alt = float(A*((3/2)**0.5))

if A < (B + C) and B < (C + A) and C < (A + B) and A > 0 and B > 0 and C > 0:
Res = input(" Deseja continuar a operação (S/N) ")
if Res == 'S' or Res == 's':
Area = float ((A * Alt)/2)
print ("A altura desse triângulo é", Alt)
print("A área do triângulo é:", Area)

elif Res == 'N' or Res == 'n':
print("Fim da operação.")

else:
print("Isso não é um triangulo")



