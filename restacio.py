hcheg = float(input("Informe a hora de chegada: "))
mcheg = float(input("Informe os minutos de chegada: "))
hsai = float(input("Informe a hora de saída: "))
msai = float(input("Informe os minutos de saída: "))

if hcheg < hsai:
    horas = hsai - hcheg
elif hcheg > hsai:
    horas = (24 - hcheg) + hsai

if mcheg <= msai:
    horamin = int ((msai - mcheg)/60)
elif mcheg >= msai:
    horamin = int (((60 - mcheg)+msai)/60)

tt = horas + horamin

if tt < 3:
    valor = 20
elif tt >= 3 and tt < 5:
    valor = 32
elif tt >= 5:
    valor = (tt*8)

print ("O valor a ser pago é :{:.2f}" .format(valor))
print ("O tempo permanecido no estacionamento foi de:{:.2f}" .format(horas))