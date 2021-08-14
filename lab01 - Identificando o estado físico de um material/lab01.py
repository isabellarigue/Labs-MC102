material = str   (input())
fusao    = float (input())
ebulicao = float (input())
temp     = float (input())

#convertendo Fahrenheit para Celsius:
tempc = (( temp - 32)/9)*5
tempc = round(tempc, 2)


print("Material:", material)
print("Ponto de fusao (Celsius): {:.2f}".format(fusao))
print("Ponto de ebulicao (Celsius): {:.2f}".format(ebulicao))
print("Temperatura atual (Celsius): {:.2f}".format(tempc))

if tempc >= fusao and tempc < ebulicao:
    print("Estado fisico do material: Liquido")
elif tempc >= ebulicao:
    print("Estado fisico do material: Gasoso")
else:
    print("Estado fisico do material: Solido")
    




