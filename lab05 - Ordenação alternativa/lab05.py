def conta_maiusculas (string):
    ''' Verifica a quantidade i de letras maiusculas em uma string.'''
    i = 0
    for x in string:
        if x.isupper():
            i+= 1
    return i

def conta_minusculas (string):
    '''Verifica a quantidade i de letras minusculas em uma string.'''
    i = 0
    for x in string:
        if x.islower():
            i+= 1
    return i

def conta_letras (string):
    '''Verifica a quantidade i de letras em uma string.'''
    i = 0
    for x in string:
        if x.isalpha():
            i+= 1
    return i

def conta_palavras (string):
    '''Verifica a quantidade i de palavras em uma string.'''
    i = 0
    for x in string:
        c = ord(x)
        if c == 32:
            i += 1 
    return i + 1

def conta_ascii (string):
    '''Soma os valores ASCII dos caracteres de uma string.'''
    i = 0
    for x in string:
        c = ord(x)
        i += c 
    return i

def imprime (lista):
    '''Imprime os elementos de uma lista um em cada linha.'''
    j = 0
    while j < len (lista):
        print(lista[j])
        j += 1

n = str(input( ))
n_separado = n.split(' ')
dia = n_separado [0]
quantidade = int(n_separado[1])

contador = 0
rua = []
while contador < quantidade:
    rua.append (str(input( )))
    contador += 1

if dia == 'Segunda':
    lista_ordenada = sorted(rua, key=conta_minusculas)
elif dia == 'Terca':
    lista_ordenada = sorted(rua, key=conta_maiusculas, reverse=True)
elif dia == 'Quarta':
    lista_ordenada = sorted(rua, key=conta_letras)
elif dia == 'Quinta':
    lista_ordenada = sorted(rua, key=conta_palavras)
else: #Sexta
    lista_ordenada = sorted(rua, key=conta_ascii, reverse=True)

imprime(lista_ordenada)
