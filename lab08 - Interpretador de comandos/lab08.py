resultados = {}
variaveis = {}
erro = {}
resultados_b = []

def aritmetica (lista):
    '''Calcula o resultado de expressões aritmeticas de acordo com uma lista de dados '''
    i = 2
    if lista[0].isdigit():
        m = int(lista[0])
    if lista[0][0].isalpha():
        if lista[0] in variaveis:
            m = int(variaveis[lista[0]])
        else:
            m = 'erro de atribuicao' 
            i = len(lista) + 1
            erro[m] = lista[0]
    if i < len(lista):
        if not lista[0][0].isalpha() and len(lista[0]) > 1:
            for x in lista[0]:
                if x.isalpha():
                    m = 'erro de sintaxe'
                    erro[m] = lista[0]
                    i = len(lista) + 1
                    break 
    if i < len(lista):
        if not lista[0].isalnum():
            m = 'erro de sintaxe'
            erro[m] = lista[0]
            i = len(lista) + 1
    while i < len(lista):
        if lista[i].isdigit():
            if lista[i-1] == '+':
                m += int(lista[i])
            else: 
                m -= int(lista[i])
        if lista[i][0].isalpha():
            if lista[i] in variaveis:
                if lista[i-1] == '+':
                    m += int(variaveis[lista[i]])
                else:
                    m -= int(variaveis[lista[i]])
            else:
                m = 'erro de atribuicao'
                erro[m] = lista[i]
                i = len(lista) + 1
        if i < len(lista):
            if not lista[i].isalnum():
                m = 'erro de sintaxe'
                erro[m] = lista[i]
                i = len(lista) + 1
        if i < len(lista):
            if not lista[i][0].isalpha() and len(lista[i]) > 1:
                for x in lista[i]:
                    if x.isalpha():
                        m = 'erro de sintaxe'
                        erro[m] = lista[i]
                        i = len(lista) + 1
                        break 
        i += 2
    return m 

def divide_calcula (parte1, contador):
    '''Divide os dados iniciais separando as expressões booleanas (se houver), permitindo que as partes menores sejam calculadas na função aritmetica. '''
    if '==' not in parte1 and '!=' not in parte1 and '<' not in parte1 and '>' not in parte1 and '<=' not in parte1 and '>=' not in parte1:
        resultados[contador] = aritmetica(parte1)
        if resultados[contador] == 'erro de atribuicao' or resultados[contador] == 'erro de sintaxe':
            i = len(lista_dados) + 1
        contador += 1
    if '==' in parte1 or '!=' in parte1 or '<' in parte1 or '>' in parte1 or '<=' in parte1 or '>=' in parte1:
        k = 0
        while k < len(parte1):
            if '==' not in parte1 and '!=' not in parte1 and '<' not in parte1 and '>' not in parte1 and '<=' not in parte1 and '>=' not in parte1:
                resultados[contador] = aritmetica(parte1)
                if resultados[contador] == 'erro de atribuicao' or resultados[contador] == 'erro de sintaxe':
                    i = len(lista_dados) + 1
                    k = len(lista_dados) + 1
                contador += 1
                break
            if parte1[k] == '==' or parte1[k] == '!=' or parte1[k] == '<' or parte1[k] == ">" or parte1[k] == '<=' or parte1[k] == ">=":
                parte3 = parte1[0:k] 
                parte4 = parte1[k+1:len(parte1)]
                resultados[contador] = aritmetica(parte3)
                if resultados[contador] == 'erro de atribuicao' or resultados[contador] == 'erro de sintaxe':
                    i = len(lista_dados) + 1
                    k = len(lista_dados) + 1
                else:
                     k = -1
                contador += 1
                parte1 = parte4
            k += 1
    return contador

def dic_lista (dicionario):
    '''Transforma os valores de um dicionário em uma lista '''
    k = 0
    lista = []
    while k < len(dicionario):
        x = dicionario[k]
        lista.append(x)
        k += 1
    return lista 

def bool_simples (parte1):
    '''Calcula as expressões booleanas simples, a partir de uma lista de dados (parte1), originando uma lista de resultados.'''
    k = 1
    while k < len(parte1):
        if parte1[k] == '==':
            x = resultados_lista[0] == resultados_lista[1]
            resultados_lista.pop(1) 
            resultados_lista.pop(0)
        if parte1[k] == '!=':
            x = resultados_lista[0] != resultados_lista[1]
            resultados_lista.pop(1)
            resultados_lista.pop(0)
        if parte1[k] == '>=':
            x = resultados_lista[0] >= resultados_lista[1]
            resultados_lista.pop(1)
            resultados_lista.pop(0)
        if parte1[k] == '<=':
            x = resultados_lista[0] <= resultados_lista[1]
            resultados_lista.pop(1)
            resultados_lista.pop(0)
        if parte1[k] == '>':
            x = resultados_lista[0] > resultados_lista[1]
            resultados_lista.pop(1)
            resultados_lista.pop(0)
        if parte1[k] == '<':
            x = resultados_lista[0] < resultados_lista[1]
            resultados_lista.pop(1)
            resultados_lista.pop(0)
        k += 2
    resultados_b.append(x)

while True:
    try:
        lista_dados = []
        i = 0
        dados = input()
        if ' ' not in dados:
            lista_dados.append(dados)
            dados_iniciais = lista_dados
            dados_iniciais2 = lista_dados 
        contador = 0
        j = 0
        if ' ' in dados: #verificando se é uma variavel de atribuição, e se ela for valida é armazenada em um dicionario 
            lista_dados = dados.split(' ')
            dados_iniciais = lista_dados
            dados_iniciais2 = lista_dados
            if lista_dados[0].isalnum():
                if lista_dados[0][0].isalpha() and lista_dados[1] == '=': #é variavel de atribuição
                    lista_dados = lista_dados[2:len(dados_iniciais)]
                    j = 3
                if j != 3:
                    if not lista_dados[0][0].isalpha() and lista_dados[1] == '=': #variavel invalida que começa com um caractere diferente de letra
                        resultados[contador] = 'erro de sintaxe'
                        erro['erro de sintaxe'] = lista_dados[0]
                        contador += 1
                        i = len(lista_dados) + 1
            else: #o nome da variavel é invalido, pois não é composto apenas por letras e numeros
                resultados[contador] = 'erro de sintaxe'
                erro['erro de sintaxe'] = lista_dados[0]
                contador += 1
                i = len(lista_dados) + 1

        #a ideia é dividir a lista_dados a cada vez que aparecer um AND ou OR, e ir calculando as expressões aritmeticas anteriores ao AND ou OR;
        #quando acaba esse processo com a parte anterior ao AND ou OR, repete o mesmo com a parte posterior;
        #e assim por diante até não haver mais AND ou OR para dividir a lista_dados;
        #os resultados são armazenados em ordem em um dicionário, permitindo realizar depois as operações booleanas seguindo a ordem que aparecem.
        while i < len(lista_dados):
            if lista_dados[i] == 'AND' or lista_dados[i] == 'OR':
                parte1 = lista_dados[0:i]
                parte2 = lista_dados[i+1:len(lista_dados)]
                contador = divide_calcula(parte1, contador)
                if 'erro de atribuicao' not in resultados.values() and 'erro de sintaxe' not in resultados.values():
                    lista_dados = parte2
                    i = -1
            if ('AND' not in lista_dados and 'OR' not in lista_dados) and ('erro de atribuicao' not in resultados.values() and 'erro de sintaxe' not in resultados.values()):
                i = len(lista_dados) + 1
                parte1 = lista_dados
                contador = divide_calcula(parte1, contador)
            i += 1

        #a ideia aqui é a mesma da de cima, porém dividindo os dados conforme forem aparecendo expressões booleanas simples (se existirem);
        #são calculadas tais expressões, e os resultados são armazenados em ordem em uma lista.
        resultados_lista = dic_lista(resultados)
        k = 1
        if 'erro de atribuicao' in resultados.values() or 'erro de sintaxe' in resultados.values():
            k = len(dados_iniciais) + 1
        if ('AND' in dados_iniciais or 'OR' in dados_iniciais) and ('==' in dados_iniciais or '!=' in dados_iniciais or '<' in dados_iniciais or '>' in dados_iniciais or '<=' in dados_iniciais or '>=' in dados_iniciais):
            if k < len(dados_iniciais):
                i = 1
                while i < len(dados_iniciais):
                    if dados_iniciais[i] == 'AND' or dados_iniciais[i] == 'OR':
                        parte1 = dados_iniciais[0:i]
                        parte2 = dados_iniciais[i+1:len(dados_iniciais)]
                        bool_simples(parte1)
                        if 'AND' in parte2 or 'OR' in parte2:
                            dados_iniciais = parte2
                            i = -1
                        else:
                            bool_simples(parte2)
                    i += 2

        if ('AND' not in dados_iniciais and 'OR' not in dados_iniciais) and ('==' in dados_iniciais or '!=' in dados_iniciais or '<' in dados_iniciais or '>' in dados_iniciais or '<=' in dados_iniciais or '>=' in dados_iniciais):
            if k < len(dados_iniciais):
                bool_simples(dados_iniciais)


        #como os resultados foram armazenados na ordem, aqui realiza-se as booleanas "and" ou "or" utilizando tais informações na ordem que aparecem.
        if 'AND' or 'OR' in dados_iniciais2:
                    k = 1
                    p = 0
                    if 'erro de atribuicao' in resultados_lista or 'erro de sintaxe' in resultados_lista:
                        k = len(dados_iniciais2) + 1
                    if '==' not in dados_iniciais2 and '!=' not in dados_iniciais2 and '<' not in dados_iniciais2 and '>' not in dados_iniciais2 and '<=' not in dados_iniciais2 and '>=' not in dados_iniciais2:
                        resultados_b = dic_lista(resultados)
                    while k < len(dados_iniciais2): 
                        if dados_iniciais2[k] == 'AND':
                            x = resultados_b[0] and resultados_b[1]
                            resultados_b[0] = x
                            del resultados_b[1]
                        if dados_iniciais2[k] == 'OR':
                            x = resultados_b[0] or resultados_b[1]
                            resultados_b[0] = x
                            del resultados_b[1]
                        k += 2

        if j == 3:
            if 'erro de sintaxe' in resultados.values():
                x = erro['erro de sintaxe']
                print(f'Erro de sintaxe: {x} nao e um nome permitido para uma variavel.')  
            elif 'erro de atribuicao' in resultados.values():
                x = erro['erro de atribuicao']
                print(f'Erro de referencia: a variavel {x} nao foi definida.') 
            else: 
                if resultados_b != []:                        
                    variaveis[dados_iniciais2[0]] = resultados_b[0]
                else:
                    variaveis[dados_iniciais2[0]] = resultados[0]
        elif 'erro de sintaxe' in resultados.values():
            x = erro['erro de sintaxe']
            print(f'Erro de sintaxe: {x} nao e um nome permitido para uma variavel.')
        elif 'erro de atribuicao' in resultados.values():
            x = erro['erro de atribuicao']
            print(f'Erro de referencia: a variavel {x} nao foi definida.')
        elif resultados_b != []:
            if resultados_b[0] == True:
                print(1)
            elif resultados_b[0] == False:
                print(0)
            else:
                print(resultados_b[0])
        elif resultados[0] == True:
            print(1)
        elif resultados[0] == False:
            print(0) 
        else:
            print(resultados[0])
        resultados.clear()
        resultados_b.clear()

    except EOFError:
        print("Encerrando... Bye-bye.")
        break
        