
tabela = ['_','_','_','_','_','_','_','_','_']

print(" =-=-=-=-=-= Jogo Da Velha =-=-=-=-=-=-=")

print("""
             |     |
          1  | 2   | 3
        _____|_____|_____
             |     |
          4  | 5   | 6
        _____|_____|_____
             |     |
          7  | 8   | 9
             |     |    """) 
                

print(' ')

def desenha_tabela(jogo):
    jogovelha = ''
    for i in range(len(jogo)):
        if(i == 2 or i == 5 or i == 8):
            jogovelha = jogovelha + " " + jogo[i] + " \n"
        else :
            jogovelha = jogovelha + " " + jogo[i] + " |"
    return jogovelha

def verifica_tabela(jogo, posicao):
    resultado = False
    if(jogo[posicao] == '_'):
        resultado = True
    return resultado


def verifica_vitoria(jogo,simbolo):
    resultado = False
    # /// verifica linha /// 
    if(jogo[0] == simbolo and jogo[1] == simbolo and jogo[2] == simbolo):
        resultado = True
    elif(jogo[3] == simbolo and jogo[4] == simbolo and jogo[5] == simbolo):
        resultado = True
    elif(jogo[6] == simbolo and jogo[7] == simbolo and jogo[8] == simbolo):
        resultado = True
    # /// Verifica Coluna /// 
    elif(jogo[0] == simbolo and jogo[3] == simbolo and jogo[6] == simbolo):
        resultado = True
    elif(jogo[1] == simbolo and jogo[4] == simbolo and jogo[7] == simbolo):
        resultado = True
    elif(jogo[2] == simbolo and jogo[5] == simbolo and jogo[8] == simbolo):
        resultado = True
    # /// Verifica Vertical ///
    elif(jogo[0] == simbolo and jogo[4] == simbolo and jogo[8] == simbolo):
        resultado = True
    elif(jogo[6] == simbolo and jogo[4] == simbolo and jogo[2] == simbolo):
        resultado = True
    return resultado

# /// Analise se ouve algum empate nas jogadas /// 
def verificar_empate(jogo):
    resultado = True
    for i in jogo:
        if(i == '_'):
            resultado = False
    return resultado

# /// Variaveis inseridas no jogo /// 

jogador = 1
jogador_numero_1 = 0
jogador_numero_2 = 0
jogadas = 0

while(True):
    while jogadas < 9:
        jogadas = jogadas + 1
        # /// Analisa se é a vez do jogador 1 /// 
        if(jogador == 1):
            jogador_numero_1 = int(input('Jogador 1 Digite uma posição de 1 a 9 : '))  
            if(verifica_tabela(tabela,int(jogador_numero_1)-1)):
                tabela[int(jogador_numero_1)-1] = 'X'
                jogador = 2
                print(desenha_tabela(tabela))
            else :
                print(desenha_tabela(tabela))
                print('Posicao ja ocupada! Jogue Novamente...')
        if(verifica_vitoria(tabela,'X')):
            print('=-=-=-=-= JOGADOR NUMERO 1 GANHOU!! =-=-=-=-=')
            break
        if(verificar_empate(tabela)):
            print('Empate')
            break
    
        # ///  Analisa se é a vez do jogador 2  /// 
        if(jogador == 2):
            jogador_numero_2 = input('Jogador 2 Digite uma posição de  1 a 9 : ')
            if(verifica_tabela(tabela,int(jogador_numero_2)-1)):
                tabela[int(jogador_numero_2)-1] = 'O'
                jogador = 1
                print(desenha_tabela(tabela))
            else :
                print(desenha_tabela(tabela))
                print('Posição ja ocupada! Jogue Novamente...')
        if(verifica_vitoria(tabela,'O')):
            print('=-=-=-=-=-= JOGADOR NUMERO 2 GANHOU!! =-=-=-=-=-=-=')
            break
        if(verificar_empate(tabela)):
            print('DEU EMPATE!')
    
    continuar = input('Deseja continuar ? [s/n] ')
    
    if (continuar == 'n'):
        print('=-=-=-= Jogo Finalizado! =-=-=-=-=')
        break
    elif(continuar == 's'):
        print(" =-=-=-=-=-= Jogo Da Velha  =-=-=-=-=-=-=")

        print("""
             |     |
          1  | 2   | 3
        _____|_____|_____
             |     |
          4  | 5   | 6
        _____|_____|_____
             |     |
          7  | 8   | 9
             |     |    """) 

        jogadas = 0
        jogador = 1
        tabela = ['_','_','_','_','_','_','_','_','_']

