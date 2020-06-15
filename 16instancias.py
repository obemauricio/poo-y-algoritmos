class Coordenada: #permite definir el tipo de datos abstractos.                  
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # def es una funcion, pero dentro de una clase es un metodo
    def distancia(self, otra_coordenada): #otra_coordenada es una instancia de Coordenada
        x_diff = (self.x - otra_coordenada.x)**2 # metodo euclidiano
        y_diff = (self.y - otra_coordenada.y)**2

        return (x_diff + y_diff)**0.5

if __name__ == "__main__": # inicializa la clase init con dos instancias (x, y)
    coord_1 = Coordenada(3, 30)
    coord_2 = Coordenada(4, 8)

    print(coord_1.distancia(coord_2))
    print(isinstance(coord_2, Coordenada)) #si alguna de estas coordenadas es instancia de coordenada