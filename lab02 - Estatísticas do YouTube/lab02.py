nome_canal = str(input())
n = int(input())

contador = v2018 = v2019 = v2020 = total2018 = total2019 = total2020 = 0
while contador < n:
    data = str(input()).split("-")
    visualizacoes = int(input())

    if data[0] == "2018":
        v2018 += visualizacoes
        total2018 += 1
    elif data[0] == "2019":
        v2019 += visualizacoes
        total2019 += 1
    elif data[0] == "2020":
        v2020 += visualizacoes
        total2020 += 1

    contador+= 1

v2018 = round(v2018, 2)
v2019 = round(v2019, 2)
v2020 = round(v2020, 2)

total_trienio = v2018 + v2019 + v2020
if total_trienio != 0:
    porcentagem2018 = (v2018 * 100)/ total_trienio
    porcentagem2019 = (v2019 * 100)/ total_trienio
    porcentagem2020 = (v2020 * 100)/ total_trienio
else:
    porcentagem2018 = porcentagem2019 = porcentagem2020 = 'indeterminada'

print('Canal:', nome_canal)
print('Total de views do trienio:', total_trienio)
print('Media de views do trienio: {:.2f}'.format(total_trienio / (total2018 + total2019 + total2020)))
print("")
print('2018')
print('Total:', v2018)
print('Porcentagem das views do trienio: {:.2f}'.format(porcentagem2018))
print('Media: {:.2f}'.format(v2018 / total2018))
print("")
print('2019')
print('Total:', v2019)
print('Porcentagem das views do trienio: {:.2f}'.format(porcentagem2019))
print('Media: {:.2f}'.format(v2019 / total2019))
print("")
print('2020')
print('Total:', v2020)
print('Porcentagem das views do trienio: {:.2f}'.format(porcentagem2020))
print('Media: {:.2f}'.format(v2020 / total2020))

