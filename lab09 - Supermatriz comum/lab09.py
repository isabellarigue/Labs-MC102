ordem = input().split(' ')

while ordem != ['0','0']:
    i = 0
    matriz_m = []
    elementos1 = []
    while i < int(ordem[0]):
        matriz_m.append(input().split(' ')) #matriz no formato lista dentro de lista
        elementos1 += matriz_m[i]           #matriz linearizada
        i += 1

    i = 0
    matriz_n = []
    elementos2 = []
    while i < int(ordem[1]):
        matriz_n.append(input().split(' '))
        elementos2 += matriz_n[i]
        i += 1

    if int(ordem[0]) < int(ordem[1]):
        matriz_menor = matriz_m
        ordem2 = int(ordem[0]) #dimensoes da matriz menor
        matriz_maior = matriz_n
        ordem1 = int(ordem[1]) #dimensoes da matriz maior
        elementos = elementos1 #elementos da matriz menor
    else: #ordem[0] > ordem[1] ou o caso que as matrizes tenham o mesmo tamanho (ai é arbitrario chamar uma de maior e outra de menor)
        matriz_menor = matriz_n
        ordem2 = int(ordem[1])
        matriz_maior = matriz_m
        ordem1 = int(ordem[0])
        elementos = elementos2 

    #irei iterar pelos extremos da matriz maior em busca de um elemento em comum com a matriz menor:
    m = ''
    i = 0
    elemento_comum = ''
    while i < ordem1: #parte de cima
        if matriz_maior[0][i] in elementos:
            elemento_comum = matriz_maior[0][i]
            i_matriz1 = 0
            j_matriz1 = i 
            m = 'encontrado'
            break
        i += 1

    if m != 'encontrado':
        i = 0
        while i < ordem1:  #lateral esquerda
            if matriz_maior[i][0] in elementos:
                elemento_comum = matriz_maior[i][0]
                i_matriz1 = i
                j_matriz1 = 0
                m = 'encontrado'
                break
            i += 1

    if m != 'encontrado':
        i = 0
        while i < ordem1: #parte de baixo (ultima linha)
            if matriz_maior[ordem1-1][i] in elementos:
                elemento_comum = matriz_maior[ordem1-1][i]
                i_matriz1 = ordem1-1
                j_matriz1 = i 
                m = 'encontrado'
                break
            i += 1

    if m != 'encontrado':
        i = 0
        while i < ordem1: #lateral direita
            if matriz_maior[i][ordem1-1] in elementos:
                elemento_comum = matriz_maior[i][ordem1-1]
                i_matriz1 = i
                j_matriz1 = ordem1-1
                break 
            i += 1

    #as dimensoes da super matriz a priori são as próprias dimensoes da maior matriz:
    p = ordem1
    q = ordem1

    #obs: se não há um elemento em comum percorrendo os extremos da matriz maior, então a matriz menor está contida na matriz maior
    #dessa forma, as dimensões da super matriz são as proprias dimensoes da matriz maior
    if elemento_comum != '':
        k = elementos.index(elemento_comum)
        i_matriz2 = k // ordem2
        j_matriz2 = k % ordem2

        #verificando quantas linhas restam abaixo e acima do elemento em comum, análogo para colunas a esquerda e a direita
        linhas_baixo2 = ordem2 - i_matriz2 - 1
        linhas_cima2 = ordem2 - linhas_baixo2 - 1
        colunas_direita2 = ordem2 - j_matriz2 - 1
        colunas_esquerda2 = ordem2 - colunas_direita2 - 1

        #mesma coisa mas agora para a matriz maior:
        linhas_baixo1 = ordem1 - i_matriz1 - 1
        linhas_cima1 = ordem1 - linhas_baixo1 - 1
        colunas_direita1 = ordem1 - j_matriz1 - 1
        colunas_esquerda1 = ordem1 - colunas_direita1 - 1

        #verificando agr quantas linhas/colunas sobram qnd sobrepoe as matrizes a partir do elemento em comum
        #se der negativo é porque sobra, então isso deverá ser somado nas dimensoes p e q da super matriz
        if (linhas_baixo1 - linhas_baixo2) < 0:
            p += (linhas_baixo1 - linhas_baixo2)*(-1)
        if (linhas_cima1 - linhas_cima2) < 0:
            p += (linhas_cima1 - linhas_cima2)*(-1)
        if (colunas_direita1 - colunas_direita2) < 0:
            q += (colunas_direita1 - colunas_direita2)*(-1)
        if (colunas_esquerda1 - colunas_esquerda2) < 0:
            q += (colunas_esquerda1 - colunas_esquerda2)*(-1)


    print(f'{p} x {q}')

    ordem = input().split(' ')

