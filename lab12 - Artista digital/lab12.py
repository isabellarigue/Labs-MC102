def distancia_pontos(i, j, x, y):
    '''Calcula a distancia entre o ponto (i, j), que representa as coordenadas do centro, e um ponto (x, y).'''
    return ((i - x)**2 + (j - y)**2)**(1/2) 

def cria_matriz(l, c, valor):
    '''Cria uma matriz com l linhas e c colunas, com todos os elementos iguais ao valor.'''
    m = []
    for i in range(l):
        linha = []
        for j in range(c):
            linha.append(valor)
        m.append(linha)
    return m

def desenha_quadrado(i, j, lado, m, x):
    '''Desenha recursivamente um quadrado em uma matriz m, de acordo com o centro (i, j), o lado e um indíce x.'''
    if x == len(m):
        return m 
    else:
        for y in range(len(m[x])):
            if x >= (i - (lado//2)) and x <= (i + (lado//2)):
                if y >= (j - (lado//2)) and y <= (j + (lado//2)):
                    m[x][y] = 'x'
        return desenha_quadrado(i, j, lado, m, x + 1) 

def desenha_circulo(i, j, raio, m, x):
    '''Desenha recursivamente um circulo em uma matriz m, de acordo com o centro (i, j), o raio e um indíce x.'''
    if x == len(m):
        return m 
    else:
        for y in range(len(m[x])):
            if distancia_pontos(i, j, x, y) <= raio:
                m[x][y] = 'x'
        return desenha_circulo(i, j, raio, m, x + 1) 

def altera_matriz(m, num_formas):
    ''''Altera certos elementos de uma matriz m de acordo com as formas geometricas dadas.'''
    if num_formas == 0:
        pass
    else:
        forma = input().split(' ')
        i = int(forma[1])
        j = int(forma[2])
        if forma[0] == 'quadrado':
            lado = int(forma[3])
            desenha_quadrado(i, j, lado, m, 0)
        else: #circulo
            raio = int(forma[3])
            desenha_circulo(i, j, raio, m, 0)   
        num_formas -= 1
        return altera_matriz(m, num_formas)

def imprime_matriz(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end=' ')
        print()


entrada = input().split(' ')
linhas = int(entrada[0])
colunas = int(entrada[1])
num_formas = int(input())

matriz = cria_matriz(linhas, colunas, '-')
altera_matriz(matriz, num_formas)
imprime_matriz(matriz)

