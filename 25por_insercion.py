# Cuando se usa el bucle: crea una lista, 
# pero cuando solo se usa la variable del bucle crea un int con el valor tota de la lista 
#
def ordenamiento_por_insercion(lista):
    for indice in range(1, len(lista)): # indice indica el rango de 1 a n(lista)
        valor_actual = lista[indice] # elemento de lista de acuerdo al numero de orden
        posicion_actual = indice # numero de orden segun el rango de 1 a n

    while posicion_actual > 0 and lista[posicion_actual -1] > valor_actual:
        lista[posicion_actual] = lista[posicion_actual - 1]
        posicion_actual -= 1

    lista[posicion_actual] = valor_actual