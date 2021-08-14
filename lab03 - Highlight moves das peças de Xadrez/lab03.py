n = int(input())
lista1 = []
tabuleiro = []
dados = []
nome = []
posicao_letra = []
posicao_num = []
casa = [ ]
numero = [ ]
m = 0

#separando os dados em listas:
i=0
while n != 0:
    tabuleiro.append (n)
    lista1.append (str(input()))
    n = int(input())
    dados = lista1[i].split(' ')
    nome.append (dados[0])
    posicao_letra.append (ord(dados[1]))
    posicao_num.append (int(dados[2]))
    i += 1
while m < len(posicao_num):
    casa.append(chr(posicao_letra[m]))
    numero.append (str(posicao_num[m]))
    m +=1

j = 0
while j < len(tabuleiro):
    n = tabuleiro [j]
    print ('Movimentos para a peca',nome[j],'a partir da casa',casa[j]+ numero[j]+'.') 
    if nome [j] == 'Torre':
            for linha in range (tabuleiro[j]):
                print(n,end=' ')
                n -=1
                for coluna in range (2, (tabuleiro[j]+2), 1):
                    if coluna != (posicao_letra[j] - 95) and posicao_num [j] == (n+1):
                        print('x', end= ' ')
                    elif (n + 1) == posicao_num [j] and coluna == (posicao_letra[j] - 95):
                        print('o', end= ' ')
                    elif coluna == (posicao_letra[j] - 95) and (n + 1) != posicao_num [j]:
                        print('x', end= ' ')
                    else:
                        print('-', end= ' ')
                print ( )
            print (' ', end=' ')    
            for linha in range (tabuleiro[j] + 1):
                for i in range(tabuleiro[j]):
                    print(chr(ord('a')+i), end=' ')
                break
    elif nome [j] == 'Bispo':
            for linha in range (tabuleiro[j]):
                print(n,end=' ')
                n -=1
                posicaoxl = (n+1) - posicao_num [j]
                for coluna in range (2, (tabuleiro[j]+2), 1):
                    if n+1 != posicao_num[j]:
                        if (coluna - 1) == (posicao_letra[j] - 96 - posicaoxl):
                            print('x', end= ' ')
                        elif (coluna - 1) == (posicao_letra[j] - 96 + posicaoxl):
                            print('x', end= ' ')
                        else:
                                print('-', end= ' ')
                    else:
                        if (coluna - 1) == (posicao_letra[j] - 96):
                             print('o', end= ' ')
                        else:
                            print('-', end= ' ')
                print ( )
            print (' ', end=' ') 
            for linha in range (tabuleiro[j] + 1):
                for i in range(tabuleiro[j]):
                    print(chr(ord('a')+i), end=' ')
                break
    elif nome [j] == 'Dama':
        for linha in range (tabuleiro[j]):
            print(n,end=' ')
            n -=1
            posicaoxl = n+1 - posicao_num [j]
            for coluna in range (2, (tabuleiro[j]+2), 1):
                if n+1 != posicao_num[j] and (coluna - 1) == (posicao_letra[j] - 96 - posicaoxl):
                    print('x', end= ' ')
                elif n+1 != posicao_num[j] and (coluna - 1) == (posicao_letra[j] - 96 + posicaoxl):
                    print('x', end= ' ')
                elif coluna != (posicao_letra[j] - 95) and posicao_num [j] == (n+1):
                    print('x', end= ' ')
                elif (n + 1) == posicao_num [j] and coluna == (posicao_letra[j] - 95):
                    print('o', end= ' ')
                elif coluna == (posicao_letra[j] - 95) and (n + 1) != posicao_num [j]:
                    print('x', end= ' ')
                else:
                    print('-', end=' ')     
            print ( )   
        print (' ', end=' ')    
        for linha in range (tabuleiro[j] + 1):
            for i in range(tabuleiro[j]):
                print(chr(ord('a')+i), end=' ')
            break
    elif nome[j] == 'Rei':
            for linha in range (tabuleiro[j]):
                print(n,end=' ')
                n -=1
                for coluna in range (2, (tabuleiro[j]+2), 1):
                    if coluna == (posicao_letra[j] - 95) and linha == (tabuleiro[j] - posicao_num [j]):
                        print ('o', end=' ')
                    elif coluna == (posicao_letra [j] - 94) and linha == (tabuleiro[j] - posicao_num [j]):
                        print ('x', end= ' ')
                    elif coluna == (posicao_letra [j] - 96) and linha == (tabuleiro[j] - posicao_num [j]):
                        print ('x', end= ' ')
                    elif coluna == (posicao_letra [j] - 95) and linha == (tabuleiro[j] - posicao_num [j] + 1):
                        print ('x', end= ' ')
                    elif coluna == (posicao_letra [j] - 95) and linha == (tabuleiro[j] - posicao_num [j] - 1):
                        print ('x', end= ' ')
                    elif coluna == (posicao_letra [j] - 94) and linha == (tabuleiro[j] - posicao_num [j] + 1):
                        print ('x', end= ' ')
                    elif coluna == (posicao_letra [j] - 94) and linha == (tabuleiro[j] - posicao_num [j] - 1):
                        print ('x', end= ' ')
                    elif coluna == (posicao_letra [j] - 96) and linha == (tabuleiro[j] - posicao_num [j] + 1):
                        print ('x', end= ' ')
                    elif coluna == (posicao_letra [j] - 96) and linha == (tabuleiro[j] - posicao_num [j] - 1):
                        print ('x', end= ' ')
                    else:
                        print('-', end= ' ')
                print ( )
            print (' ', end=' ')    
            for linha in range (tabuleiro[j] + 1):
                for i in range(tabuleiro[j]):
                    print(chr(ord('a')+i), end=' ')
                break
    elif nome [j] == 'Cavalo':
            for linha in range (tabuleiro[j]):
                print(n,end=' ')
                n -=1
                for coluna in range (2, (tabuleiro[j]+2), 1):
                    if (posicao_num [j] + 2) < n+1 or n+1 < (posicao_num [j] - 2):
                        print('-', end= ' ')
                    elif (posicao_num [j] + 2) == n+1 or (posicao_num [j] - 2) == n+1:
                        if coluna != (posicao_letra[j] - 96) and coluna != (posicao_letra[j] - 94):
                            print('-', end= ' ')
                        else:
                            print('x', end= ' ')
                    elif (posicao_num [j] + 1) == n +1 or (posicao_num [j] - 1) == n +1:
                        if coluna != (posicao_letra[j] - 97) and coluna != (posicao_letra[j] - 93):
                            print('-', end= ' ')
                        else:
                            print('x', end= ' ')
                    elif posicao_num [j] == n+1:
                        if coluna != (posicao_letra[j] - 95):
                            print('-', end= ' ')
                        else:
                            print('o', end= ' ')                  
                    else:
                        print('x', end= ' ')
                print ( )
            print (' ', end=' ')    
            for linha in range (tabuleiro[j] + 1):
                for i in range(tabuleiro[j]):
                    print(chr(ord('a')+i), end=' ')
                break
    else: #Peao
            for linha in range (tabuleiro[j]):
                print(n,end=' ')
                n -=1
                for coluna in range (2, (tabuleiro[j]+2), 1):
                    if posicao_num [j] == 2:
                        if coluna == (posicao_letra[j] - 95) and linha == (tabuleiro[j] - posicao_num [j]):
                            print ('o', end=' ')
                        elif coluna == (posicao_letra [j] - 95) and linha == (tabuleiro[j] - posicao_num [j] -2):
                            print ('x', end= ' ')
                        elif coluna == (posicao_letra [j] - 95) and linha == (tabuleiro[j] - posicao_num [j] -1):
                            print ('x', end= ' ')
                        else:
                            print('-', end= ' ')
                    else:
                        if coluna == (posicao_letra[j] - 95) and linha == (tabuleiro[j] - posicao_num [j]):
                            print ('o', end=' ')
                        elif coluna == (posicao_letra [j] - 95) and linha == (tabuleiro[j] - posicao_num [j] -1):
                            print ('x', end= ' ')
                        else:
                            print('-', end= ' ')
                print ( )
            print (' ', end=' ')    
            for linha in range (tabuleiro[j] + 1):
                for i in range(tabuleiro[j]):
                    print(chr(ord('a')+i), end=' ')
                break
    j+= 1
    print ( )
    print ( )
