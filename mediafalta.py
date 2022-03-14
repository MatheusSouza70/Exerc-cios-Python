nota1 =int(input("Informe a primeira nota: "))
nota2 =int(input("Informe a segunda nota: "))
media = (nota1 + nota2) / 2 
frequencia = int(input("Informe a frequencia de aulas do aluno: "))

if media >= 7 and frequencia >= 75:
    print("Aluno Aprovado")
elif media <5 and frequencia <=75:
    print ("Aluno Reprovado")
elif media >= 0 and media <=7 or frequencia >=50 and frequencia <=75:
    print("Recuperação")