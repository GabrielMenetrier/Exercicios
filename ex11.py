lista0 = [["Leite" , 10], ["abacaxi", 6], ["macaco", 40],["lasanha", 400]]

def filtro (lista, min, max):
    nova_lista = []
    for i in range (len(lista)):
        if min <= lista[i][1] <= max:
            nova_lista.append(lista[i][0])
    return nova_lista

print(filtro(lista0, 10,50))