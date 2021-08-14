def codifica (string, E, base):
    '''Substitui os caracteres de uma string pelos valores ASCII em hexadecimal/octal sem o prefixo, de acordo com o enxerto.'''
    if base == 'octal':
        string = string[::-1]
    i = 0
    z = ''
    while i < len (string):
        for x in string:
            if base == 'hexadecimal':
                y = str(hex(ord(x))) #convertendo o valor ASCII de cada letra para hexadecimal
            else: #base octal
                y = str(oct(ord(x))) #convertendo o valor ASCII de cada letra para octal
            y2 = (y[2:len(y)]).upper()  #y sem o prefixo e maiúsculo
            y_preenchido = y2.zfill(E)
            z += y_preenchido
            i += 1
    print(z)


def decodifica (string, E, base):
    '''Transforma uma string de códigos ASCII em hexadecimal/octal para base 10, de acordo com o enxerto. 
    Depois transforma os valores ASCII em caracteres.'''
    i = 0
    z = ''
    while i < len(string):
        str_separada = string[i:i+E] #dividindo a string em partes de acordo com o enxerto
        if base == 'hexadecimal':
            str_convertida = int(str_separada, 16)
        else: #base octal
            str_convertida = int(str_separada, 8)
        str_convertida2 = chr(str_convertida)
        z += str_convertida2
        i += E
    if base == 'octal':
        z = z[::-1]
    print(z)

dados = input().split(' ')
modo = dados[0]
enxerto = int(dados[1])
linhas = int(dados[2])

contador = 1
while contador <= linhas:
    string = str(input())
    if contador % 2 != 0: #linha impar
        if modo == '1':
            codifica(string, enxerto, 'hexadecimal')
        else:
            decodifica(string, enxerto, 'hexadecimal')
    else:   #linha par
        if modo == '1':
            codifica(string, enxerto, 'octal')
        else:
            decodifica(string, enxerto, 'octal')
    contador += 1




