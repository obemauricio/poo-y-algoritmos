import random

def ordenamiento_de_burbujas(lista):
    n = len(lista) #contador de los elementos de lista

    for i in range(n): #la funcion i enumera verticalmente una lista de 0 a n, pero n se repite  veces.
        for j in range(0, n - i - 1): # crea una lista, vertical dentro de i la cual ordena en cada iteracion.
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j+1], lista[j]
    return lista #devuelve la lista ordenada

if __name__ == "__main__":
    tamano_de_lista = int(input("de que tamano sera la lista?: "))
    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]

    lista_ordenada = ordenamiento_de_burbujas(lista)
    print(lista_ordenada)
