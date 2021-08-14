from math import log
import sys
sys.setrecursionlimit(2000)

def AdicionaElemento(dic, x):
    '''Adiciona um nivel no dicionario ou soma mais um no d[nivel] correspondente, se o nivel ja estiver nas chaves do dicionario.'''
    nivel = log(x)/log(2)
    if nivel in dic.keys():
        dic[nivel] += 1
    else:
        dic[nivel] = 1

def MaiorPotencia(num):
    '''Devolve a maior potencia de base 2 (2^x) que um numero pode ser escrito.'''
    x = 0
    while 2**x <= num:
        x += 1
    return 2**(x - 1) 

def VerificaPotencias(x):
    '''Verifica se um numero pode ser escrito como uma potencia de base 2.'''
    num = str(log(x)/log(2))
    return num[-2] == '.' and num[-1] == '0' #verificando se o resultado é inteiro, exemplo 3.0


def DividirConquistar(a, b, dic):
    '''Procura o maior quadrado, de lados do tipo 2^x, possivel dentro de um retangulo de lados ab (sendo 'a' sempre menor ou igual ao lado 'b');
       A informação encontrada é armazenada em um dicionario. Após 'retirar' o quadrado da área orginal, se ainda houver uma área retangular ou quadrada
       é feita a recursão da função, já se houver mais de uma área, essa é guardada em uma lista de tuple para ser calculada posteriormente usando a função Resto abaixo.'''

    if VerificaPotencias(a) == True:
        AdicionaElemento(dic, a)
        if a == b: #caso base
            return dic
        else:
            b -= a 
            if a > b:
                a, b = b, a
            return DividirConquistar(a, b, dic)

    else: #se 'a' não é uma potencia de base 2, então encontra-se o valor da potencia de base 2 mais proxima de 'a' para ser o lado do quadrado
          #ja a area restante é dividida em retangulos para serem calculados recursivamente 
        a_antigo = a
        a = MaiorPotencia(a)
        copia_a = a
        AdicionaElemento(dic, a)
        copia_b = b - a
        if a > copia_b:
            a, copia_b = copia_b, a
        mem.append((a, copia_b))
        return DividirConquistar(a_antigo - copia_a, b, dic)

    
def Resto(lista, dic):
    '''Faz a chamada para calcular os maiores quadrados de lados 2^x possiveis dentro de retangulos (cujos lados estão armazenados em uma lista).'''
    if len(lista) == 0: #caso base, não há mais retangulos na lista 
        return dic
    else:
        DividirConquistar(lista[0][0], lista[0][1], dic)
        lista.pop(0)
        return Resto(lista, dic) 


mem = []
dic = {}

entrada = input().split(' ')
a = int(entrada[0])
b = int(entrada[1])
if a > b: 
    a , b = b , a #para a função funcionar o lado 'a' sempre deve ser menor ou igual a 'b'

DividirConquistar(a, b, dic)
Resto(mem, dic)

total_submagias = 0
total_PM = 0
print("---")
print("Grimorio de Teraf L'are")
print("---")
for x in range(len(dic)):
    print(f'{dic[sorted(dic)[x]]} submagia(s) de nivel {int(sorted(dic)[x])}')
    total_submagias += dic[sorted(dic)[x]]
    total_PM += (2**(sorted(dic)[x]))*dic[sorted(dic)[x]]
print("---")
print(f'Total de submagia(s) conjurada(s): {int(total_submagias)}')
print(f'Total de PM gasto: {int(total_PM)}')
print("---")


    

