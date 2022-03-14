while True:
  def horas():
     hora = int(input("Informe as horas: "))
     minu = int(input("Informe os minutos: "))

     if hora < 12 and minu <= 59:
          print(hora, ":", minu, "AM")
     else:
          novahora = hora - 12
          print(novahora, ":", minu, "PM")

     if novahora == 0:
        novahora = 1

  x = int(input("Deseja continuar? 1 Para sim, 0 para não: "))
  if x == 1:
      horas()
  else:
      exit()
