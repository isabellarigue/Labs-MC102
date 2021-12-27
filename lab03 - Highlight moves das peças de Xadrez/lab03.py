n = int(input())
while n != 0:
    tabuleiro = n
    entrada = input().split(" ")
    peca = entrada[0]
    coluna = entrada[1]
    posicao_coluna_ord = ord(coluna)
    posicao_linha = int(entrada[2])

    print(f'Movimentos para a peca {peca} a partir da casa {coluna}{posicao_linha}.')
    for linha in range(n):
        print(tabuleiro, end=' ')
        tabuleiro -= 1
        for coluna in range(2, (n + 2), 1):
            if peca == "Torre":
                if coluna != (posicao_coluna_ord - 95) and posicao_linha == (tabuleiro + 1):
                    print('x', end= ' ')
                elif (tabuleiro + 1) == posicao_linha and coluna == (posicao_coluna_ord - 95):
                    print('o', end= ' ')
                elif coluna == (posicao_coluna_ord - 95) and (tabuleiro + 1) != posicao_linha:
                    print('x', end= ' ')
                else:
                    print('-', end= ' ')
            elif peca == "Bispo":
                posicaoxl = (tabuleiro + 1) - posicao_linha
                if tabuleiro + 1 != posicao_linha:
                    if (coluna - 1) == (posicao_coluna_ord - 96 - posicaoxl):
                        print('x', end= ' ')
                    elif (coluna - 1) == (posicao_coluna_ord - 96 + posicaoxl):
                        print('x', end= ' ')
                    else:
                            print('-', end= ' ')
                else:
                    if (coluna - 1) == (posicao_coluna_ord - 96):
                            print('o', end= ' ')
                    else:
                        print('-', end= ' ')
            elif peca == "Dama":
                posicaoxl = tabuleiro + 1 - posicao_linha 
                if tabuleiro + 1 != posicao_linha and (coluna - 1) == (posicao_coluna_ord - 96 - posicaoxl):
                    print('x', end= ' ')
                elif tabuleiro + 1 != posicao_linha and (coluna - 1) == (posicao_coluna_ord - 96 + posicaoxl):
                    print('x', end= ' ')
                elif coluna != (posicao_coluna_ord - 95) and posicao_linha == (tabuleiro + 1):
                    print('x', end= ' ')
                elif (tabuleiro + 1) == posicao_linha and coluna == (posicao_coluna_ord - 95):
                    print('o', end= ' ')
                elif coluna == (posicao_coluna_ord - 95) and (tabuleiro + 1) != posicao_linha:
                    print('x', end= ' ')
                else:
                    print('-', end=' ')     
            elif peca == "Rei":
                if coluna == (posicao_coluna_ord - 95) and linha == (n - posicao_linha):
                    print ('o', end=' ')
                elif coluna == (posicao_coluna_ord - 94) and linha == (n - posicao_linha):
                    print ('x', end= ' ')
                elif coluna == (posicao_coluna_ord - 96) and linha == (n - posicao_linha):
                    print ('x', end= ' ')
                elif coluna == (posicao_coluna_ord - 95) and linha == (n - posicao_linha + 1):
                    print ('x', end= ' ')
                elif coluna == (posicao_coluna_ord - 95) and linha == (n - posicao_linha - 1):
                    print ('x', end= ' ')
                elif coluna == (posicao_coluna_ord - 94) and linha == (n - posicao_linha + 1):
                    print ('x', end= ' ')
                elif coluna == (posicao_coluna_ord - 94) and linha == (n - posicao_linha - 1):
                    print ('x', end= ' ')
                elif coluna == (posicao_coluna_ord - 96) and linha == (n - posicao_linha + 1):
                    print ('x', end= ' ')
                elif coluna == (posicao_coluna_ord - 96) and linha == (n - posicao_linha - 1):
                    print ('x', end= ' ')
                else:
                    print('-', end= ' ')
            elif peca == "Cavalo":
                if (posicao_linha + 2) < tabuleiro + 1 or tabuleiro + 1 < (posicao_linha - 2):
                    print('-', end= ' ')
                elif (posicao_linha + 2) == tabuleiro + 1 or (posicao_linha - 2) == tabuleiro + 1:
                    if coluna != (posicao_coluna_ord - 96) and coluna != (posicao_coluna_ord - 94):
                        print('-', end= ' ')
                    else:
                        print('x', end= ' ')
                elif (posicao_linha + 1) == tabuleiro + 1 or (posicao_linha - 1) == tabuleiro + 1:
                    if coluna != (posicao_coluna_ord - 97) and coluna != (posicao_coluna_ord - 93):
                        print('-', end= ' ')
                    else:
                        print('x', end= ' ')
                elif posicao_linha == tabuleiro + 1:
                    if coluna != (posicao_coluna_ord - 95):
                        print('-', end= ' ')
                    else:
                        print('o', end= ' ')                  
                else:
                    print('x', end= ' ')
            else: #Peao
                if posicao_linha == 2:
                    if coluna == (posicao_coluna_ord - 95) and linha == (n - posicao_linha):
                        print ('o', end=' ')
                    elif coluna == (posicao_coluna_ord - 95) and linha == (n - posicao_linha - 2):
                        print ('x', end= ' ')
                    elif coluna == (posicao_coluna_ord - 95) and linha == (n - posicao_linha - 1):
                        print ('x', end= ' ')
                    else:
                        print('-', end= ' ')
                else:
                    if coluna == (posicao_coluna_ord - 95) and linha == (n - posicao_linha):
                        print ('o', end=' ')
                    elif coluna == (posicao_coluna_ord - 95) and linha == (n - posicao_linha - 1 ):
                        print ('x', end= ' ')
                    else:
                        print('-', end= ' ')
        print()
    print(' ', end=' ')
    for linha in range(n + 1):
        for i in range(n):
            print(chr(ord('a') + i), end=' ')
        break

    n = int(input())