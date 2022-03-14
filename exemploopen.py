arquivo = open('arquivo.txt', 'r')
conteudo = arquivo.read()
print(conteudo)


arquivo = open('arquivo.txt','r')
for linha in arquivo.readlines():
    print(linha)
