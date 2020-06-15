import time

def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1

    return respuesta

def factorial_r(n):
    if n == 1:
        return 1
    
    return n * factorial(n - 1)

if __name__ == "__main__":
    n = 100000

    #comienzo significa que estamos ejecutando el modulo time y dentro de ese modulo existe una funcion time.
    comienzo = time.time() 
    factorial(n) #ejecutamos la funcion para especificar el metodo que se pondra a prueba.
    final = time.time()
    print(final - comienzo)

    comienzo = time.time()
    factorial_r(n)
    final =time.time()
    print(final - comienzo)
