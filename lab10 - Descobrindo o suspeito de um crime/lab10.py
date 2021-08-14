#Primeiro é criada uma lista de dicionários
#Cada dicionário contém as caracteristicas dos individuos
lista = []
entrada = input()
while entrada != '--':
    d = {}
    while entrada != '-' and entrada != '--':
        caracteristica = entrada.split(':')[0]
        valor = (entrada.split(':')[1]).strip()
        d[caracteristica] = valor
        entrada = input()
    lista.append(d)
    if entrada != '--':
        entrada = input()

#É criado um dicionário de evidencias:
evidencias = input()
dict_evidencias = {}
while evidencias != '---':  
    caracteristica = evidencias.split(':')[0]
    valor = (evidencias.split(':')[1]).strip()
    dict_evidencias[caracteristica] = valor
    evidencias = input()

#Percorre-se a lista em busca de dicionários que contenham todos os itens do dict_evidencias:
suspeitos = []
for x in lista:
    for chave, valor in dict_evidencias.items():
        if chave in x.keys() and x[chave] == valor:
            suspeito = True 
        else:
            suspeito = False
            break
    if suspeito:
        suspeitos.append(x['Nome'])

if suspeitos == []:
    print('Nenhum suspeito(a) com essas caracteristicas foi identificado(a).')
elif len(suspeitos) == 1:
    print("Suspeito(a):")
    print(suspeitos[0])
else:
    nomes = sorted(suspeitos)
    print('Suspeitos(as):')
    for x in nomes:
        print(x)
      
