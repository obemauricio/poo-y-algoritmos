numero = int(input("Escoge un numero para obtener su raiz cuadrada: "))
epsilon = 0.01
bajo = 0.0 
alto = max(1.0, numero)
respuesta = (alto + bajo) / 2

while abs(respuesta**2 - numero) >=  epsilon:
    print(f"bajo: {bajo} ; alto: {alto} ; respuesta: {respuesta}")
    if respuesta**2 < numero:
        bajo = respuesta
    else:
        alto = respuesta
    
    respuesta = (alto + bajo) / 2 
print(f"La raiz cuadrada de {numero} es {respuesta}")