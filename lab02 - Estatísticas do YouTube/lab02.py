nome_canal = str(input())
n = int(input())

lista1 = []
data_separada1 = [] 
i = 0
j = 0
valor2018 = 0
valor2018T = 0
valor2019 = 0
valor2019T = 0
valor2020 = 0
valor2020T = 0
contador2018 = 0
contador2019 = 0
contador2020 = 0

while i < 2*n:
    lista1.append (str(input()))
    i += 1

i = 0
while i < 2*n:
    data_separada1 =lista1[i].split('-')
    j =  data_separada1[0].split('-')
    t = int(j[0])
    
    if ( t < 2018 or t > 2020): 
        i = i + 2
    elif (t == 2018):
        i = i + 1
        valor2018 = (lista1[i])
        valor2018T = valor2018T + int(valor2018)
        contador2018 += 1
        i += 1
    elif (t == 2019):
        i = i + 1
        valor2019 = (lista1[i])
        valor2019T = valor2019T + int(valor2019)
        contador2019 += 1
        i += 1
    else:
        i = i + 1
        valor2020 = (lista1[i])
        valor2020T = valor2020T + int(valor2020)
        contador2020 += 1
        i += 1

valor2018T = round (valor2018T, 2)
valor2019T = round (valor2019T, 2)
valor2020T = round (valor2020T, 2)

total_trienio = valor2018T + valor2019T + valor2020T

if total_trienio != 0:
    porcentagem2018 = (valor2018T * 100)/ total_trienio
    porcentagem2019 = (valor2019T * 100)/ total_trienio
    porcentagem2020 = (valor2020T * 100)/ total_trienio
else:
    porcentagem2018 = str('indeterminada')
    porcentagem2019 = str('indeterminada')
    porcentagem2020 = str('indeterminada')

media_trienio = total_trienio/ n
media2018 = valor2018T/ contador2018
media2019 = valor2019T/ contador2019
media2020 = valor2020T/ contador2020

print ('Canal:', nome_canal)
print ('Total de views do trienio:', total_trienio)
print ('Media de views do trienio: {:.2f}'.format(media_trienio))
print ( )
print ('2018')
print ('Total:', valor2018T)
print ('Porcentagem das views do trienio: {:.2f}'.format(porcentagem2018))
print ('Media: {:.2f}'.format(media2018))
print ( )
print ('2019')
print ('Total:', valor2019T)
print ('Porcentagem das views do trienio: {:.2f}'.format(porcentagem2019))
print ('Media: {:.2f}'.format(media2019))
print ( )
print ('2020')
print ('Total:', valor2020T)
print ('Porcentagem das views do trienio: {:.2f}'.format(porcentagem2020))
print ('Media: {:.2f}'.format(media2020))






