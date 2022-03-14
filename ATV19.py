alunos = 3
a = 0
reprovados = 0
aprovado = 0
exame  = 0
media = 0

while a < alunos:
    a = a+1

    nome  = str(input("Qual é o nome do aluno?: "))
    nota1 = float(input("Qual é a primeira nota?: "))
    nota2 = float(input("Qual é a segunda nota? : "))

    mediaAluno = (nota1+ nota2)/2
    if (mediaAluno <=10)and (mediaAluno >=7):
             print("Aprovado!!!")
             aprovado = aprovado+1
    elif (mediaAluno >= 3)and (mediaAluno <= 7):
             print("Exame!!!")
             exame = exame +1
    elif (mediaAluno <= 3):
             print("Reprovado!!!")
             rep = reprovados+1

    media = mediaAluno + media
    
media = media / alunos

print('A quantidade de alunos que foram Aprovados é de {}'.format(aprovado))
print('A quantidade de alunos que estão Reprovados é de {}'.format(exame))
print('A média da sala é {}'.format(media))

