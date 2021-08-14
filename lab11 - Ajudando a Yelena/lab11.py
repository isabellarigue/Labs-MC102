def distancia_pontos(xe, ye, y):
    '''Calcula a distancia entre o ponto (xe, ye), que representa as coordenadas de um esconderijo, e um ponto (0, y).'''
    return ((xe)**2 + (ye - y)**2)**1/2 

def distancia_maxima(y):
    '''Calcula as distancias entre os esconderijos e um ponto (0, y), devolvendo a maior distancia.'''
    d_max = distancia_pontos(xe[0], ye[0], y)
    i = 1
    while i < num_esconderijos:    
        d = distancia_pontos(xe[i], ye[i], y)
        if d > d_max:
            d_max = d
        i += 1
    return d_max

def BuscaBinaria(l):
    '''Busca pela menor distancia entre as maiores distancias entre um esconderijo e um ponto (0,y).'''
    e = 1
    d = len(l) - 1
    while e <= d:
        m = (e + d) // 2

        if m == len(l) - 1: 
            return l[m]
        elif m == 0:  
            return l[m]
        else:
            dist_m = distancia_maxima(l[m])
            dist_anterior = distancia_maxima(l[m-1])
            dist_posterior = distancia_maxima(l[m+1])

            if dist_m < dist_anterior and dist_m < dist_posterior: #a menor distancia é um ponto de mínimo 
                return l[m]
            if m != len(l) - 1:
                if dist_m < dist_posterior: #esta para esquerda da lista
                    d = m - 1          
            if m != 0:
                if dist_m < dist_anterior: #esta para direita da lista
                    e = m + 1


entrada = input()
while entrada != '0 0':
    num_esconderijos = int(entrada.split(' ')[0])
    coordenadaY_portao = int(entrada.split(' ')[1])

    contador = 0
    xe = []
    ye = []
    while contador < num_esconderijos:
        coordenadas = input().split(' ')
        xe.append(int(coordenadas[0]))
        ye.append(int(coordenadas[1])) 
        contador += 1

    l = [i for i in range(1, coordenadaY_portao)]
    yi = BuscaBinaria(l)

    print(yi)
    
    entrada = input()