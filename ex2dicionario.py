from collections import OrderedDict

series = {'Serie1': {'Nome1': 'Demolidor', 'Ator11': 'Charlie Cox', 'Ator12': 'Deborah Ann Woll'},
        'Serie2': {'Nome2': 'Justiceiro', 'Ator21': 'Jon Bernthal', 'Ator22': 'Ben Barnes'}}


print("--------------Catálogo de Filmes--------------")
print("Demolidor -> 1")
print("Justiceiro -> 2")
print("\n")
pergunta = int(input("Deseja ver informações de quais séries?: "))


if pergunta == 1:
    print("-----------Série------------")
    print(series['Serie1']['Nome1'])
    print("-----------Atores------------")
    
    print("-----------Atores------------")

if pergunta == 2:
    print("-----------Série------------")
    print(series['Serie2']['Nome2'])
    print("-----------Atores------------")
   
    print("-----------Atores------------")
    print("--------------Catálogo de Filmes--------------")

