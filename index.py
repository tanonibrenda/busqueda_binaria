datos = [2, 3, 5, 6, 8, 11, 12, 15, 18, 21, 23, 24, 29, 30]
buscado = 23
def busqueda_binaria(lista, elemento):
    inicio = 0
    final = len(lista) - 1

    while inicio <= final:
        medio = (inicio + final) // 2
        if lista[medio] == elemento:
            return True
        elif lista[medio] < elemento:
            inicio = medio + 1
        else:
            final = medio - 1

    return False

print(busqueda_binaria(datos, buscado))
