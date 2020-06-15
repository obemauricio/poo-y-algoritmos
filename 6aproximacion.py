numero = int(input("Escoge un numero para obtener su raiz cuadrada: "))
epsilon = 0.01
paso = epsilon**2
respuesta = 0.0 

while abs(respuesta**2 - numero) >= epsilon and respuesta <= numero:
    respuesta += paso
    print(respuesta)
    
if abs(respuesta**2 - numero) >= epsilon: 
    print(f"No se econtro la raiz cuadrada {numero}")
else: 
    print(f"la raiz cuadrada de {numero} es {respuesta}")

