def enumeracion_exahustiva(p_objetivo):
    objetivo = p_objetivo
    respuesta = 0

    while respuesta**2 < objetivo
    print(respuesta)
    respuesta += 1

    if respuesta**2 == objetivo:
        print(f"La raiz cuadrada de {objetivo} es {respuesta}")
    else: 
        print("{objetivo} no tiene raiz cuadrada")

def aproximacion(p_objetivo):
    objetivo = p_objetivo
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0 
    
    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo: 
        print(abs(respuesta**2 - objetivo), respuesta)
        respuesta += paso
    
if abs(respuesta**2 - objetivo) >= epsilon: 
    print(f"no se encontro raiz cuadrada para {objetivo}")
else:
    print(f"la raiz cuadrada de {objetivo} es {respuesta}")

def busqueda_binaria(p_objetivo):
    objetivo = p_objetivo
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - respuesta) >= epsilon:
        print(f"bajo: {bajo} ; alto: {alto} ; respuesta: {respuesta}")
        if respuesta**2 < objetivo: 
            bajo = respuesta
        else: 
            alto = respuesta
        
        respuesta = (alto + bajo ) / 2 
        print("--------------------------------------------------------------------------------------------")
        print(f"la raiz cuadrada de {objetivo} es {respuesta}")
        print("--------------------------------------------------------------------------------------------")
    
    def mostrar_menu_numero():
        print("--------------------------------------------------------------------------------------------")
        print(f"ingrese el numero del cual desea saber la raiz cuadrada: ")
        print("--------------------------------------------------------------------------------------------")
        int(input("numero: "))
        print("--------------------------------------------------------------------------------------------")
        return p_objetivo
    def mostrar_menu_algoritmos(): 
        print("--------------------------------------------------------------------------------------------")
        print("tiene 3 algoritmos para resolver la raiz cuadrada de la incognita")
        print("opcion 1 = enumeracon exahustiva")
        print("opcion 2 = aproximacion a soluciones")
        print("opcion 3 = busqueda binaria")
        print("¿que opcion deseas utilizar")
        print("--------------------------------------------------------------------------------------------")
        opcion = int(input("opcion= "))
        print("--------------------------------------------------------------------------------------------")
        return opcion
    
    def mostrar_despedida():
        print("--------------------------------------------------------------------------------------------")
        print("Gracias por usar la aplicacion, hasta la proxima!")
        print("--------------------------------------------------------------------------------------------")
    
    def calcular(p_objetivo, opcion):
        if opcion == 1:
            enumeracion_exahustiva(p_objetivo)
        elif opcion == 2:
            aproximacion(p_objetivo)
        elif opcion == 3: 
            busqueda_binaria(p_objetivo)
    def ejecutar():
        mostrar_bienvenida()
        p_objetivo = mostrar_menu_numero()
        opcion = mostrar_mene_algoritmo()
        calcular(p_objetivo, opcion)
        mostrar_despedida()
    ejecutar()