estudiantes ={
    "Bolivia": 4, 
    "Chile": 2,
    "Brazil": 5,  
}
print("Nombre de Paises")
for paises in estudiantes:
    print(f"-pais: {paises}")
print()
print("Numero de estudiantes")
for mostrar in estudiantes.values():
    print(f"# de estudianes: {mostrar}")
print()
print("Paises y numero de estudiantes")
for paises, mostrar in estudiantes.items():
    print(f"Pais: {paises} ; # de estudiantes: {mostrar}")