def digitos_separados(n):
    '''Separa os dígitos de um número n na base 10, colocando-os em uma nova lista.'''
    lista = [ ]
    lista_digitos = [ ]
    while n > 0:
        m = n%10
        lista.append(m)
        n = n // 10
    for i in range(len(lista) -1, -1, -1):
        lista_digitos.append(lista[i])
    return lista_digitos

def semelhancas (x, y):
    '''Compara dois números x e y, ambos na base 10, retornando a quantidade de dígitos iguais que eles possuem.'''
    i = 0
    soma = 0
    while i < len(digitos_separados(x)):
        if digitos_separados(x)[i] == digitos_separados(y)[i]:
            soma += 1
        i += 1
    return soma

senhaT = str(input( ))
senhaT_separada = senhaT.split (" ")
senha_mestra = int(senhaT_separada [0])
T = int(senhaT_separada [1])

contador = 0
while T > contador:
    senha_usuario = int(input( ))
    if senha_usuario == senha_mestra:
        print("Senha reconhecida. Desativando defesas...")
        break
    else:
        print ("Senha incorreta")
        if len(digitos_separados(senha_mestra)) != len(digitos_separados(senha_usuario)):
            print ("Semelhanca: Erro: quantidade de digitos incongruente")
        else:
            print ("Semelhanca:", semelhancas(senha_mestra, senha_usuario))
        print ("Tentativas restantes:", T -1 -(contador))
        print ( )
    contador += 1

if T == contador:
    print("Tentativas esgotadas. Acionando defesas...")


