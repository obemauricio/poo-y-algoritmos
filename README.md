# poo-y-algoritmos by Obe
# Programacion orientada a objetos
Uno de los elementos más importantes de los lenguajes de programación
es la utilización de clases para organizar programas en módulos y abstracciones
de datos.

Las clases se pueden utilizar de muchas diversas maneras. Pero en este artículo
hablaremos de cómo utilizarlas en el contexto de la programación orientada a objetos.
La clave para entender la programación orientada a objetos es pensar en objetos
como agrupaciones de datos y los métodos que operan en dichos datos.

Por ejemplo, podemos representar a una persona con propiedades como nombre,
edad, género, etc. y los comportamientos de dicha persona como caminar, cantar,
comer, etc. De la misma manera podemos representar unos audífonos con propiedades
como su marca, tamaño, color, etc. y sus comportamientos como reproducir música,
pausar y avanzar a la siguiente canción.

Puesto de otra manera, la programación orientada a objetos nos permite modelar
cosas reales y concretas del mundo y sus relaciones con otros objetos.

Las ideas detrás de la programación orientada a objetos tienen más de 50 años
y han sido ampliamente aceptadas y practicadas en los últimos treinta. A
mediados de la década de los setenta se comenzaron a escribir artículos académicos
explicando los beneficios de esta aproximación a la programación. También durante
esos años se comenzaron a escribir los primeros lenguajes de programación que
incorporaban estas ideas (como Smalltalk y CLU). Pero no fue hasta la llegada
de Java y C++ que la idea consiguió un número importante de seguidores.

Hasta ahora, en el curso previo de esta serie
hemos utilizado programación orientada a objetos de manera implícita. Cuando
decimos "Los objetos son las principales cosas que un programa de Python
manipula. Cada objeto tiene un tipo que define qué cosas puede realizar un
programa con dicho objeto.", nos estamos refiriendo a las ideas principales
de la programación orientada a objetos. Hemos utilizado los tipos lista y
diccionario, entre muchos otros, así como los métodos asociados a dichos tipos.
Así como los creadores de un lenguaje de programación sólo pueden diseñar una
fracción muy pequeña de todas las funciones útiles (como abs, float, type,
etc.), también pueden escribir una fracción muy pequeña de los tipos útiles
(int, str, dict, list, etc.). Ya sabemos los mecanismos que nos
permiten crear funciones, ahora veremos los mecanismos que nos permiten crear
nuevos tipos (o clases).

## Clases 
Las estructuras primitivas con las que hemos trabajado hasta ahora nos permiten
definir cosas sencillas, como el costo de algo, el nombre de un usuario, las
veces que debe correr un bucle, etc. Sin embargo, existen ocasiones cuando
necesitamos definir estructuras más complejas, por ejemplo un hotel. Podríamos
utilizar dos listas: una para definir los cuartos y una segunda para definir
si el cuarto se encuentra ocupado o no.

```py
cuartos_de_hotel = [101, 102, 103, 201, 202, 203]
cuarto_ocupado = [True, False, False, True, True, False]
```
Sin embargo, este tipo de organización rápidamente se sale de control. ¿Qué
tal que quisieramos añadir más propiedades, cómo si el cuarto ya fue aseado o
no? ¿Si el cuarto tiene cama doble o sencilla? Esto nos lleva a una falta fuerte
de organización y es justamente el punto que justifica la existencia de clases.

Las clases nos permiten crear nuevos tipos que contiene información arbitraria
sobre un objeto. En el caso del hotel, podríamos crear dos clases Hotel() y
Cuarto() que nos permitiera dar seguimiento a las propiedades como número de
cuartos, ocupación, aseo, tipo de habitación, etc.

Es importante resaltar que las clases sólo proveen estructura. Son un molde con
el cual podemos construir objetos específicos. La clase señala las propiedades
que los hoteles que modelemos tendrán, pero no es ningún hotel específico. Para
eso necesitamos las instancias.

## Instancias
Mientras que las clases proveen la estructura, las instancias son los objetos
reales que creamos en nuestro programa: un hotel llamado PlatziHotel o Hilton.
Otra forma de pensarlo es que las clases son como un formulario y una vez que
se llena cada copia del formulario tenemos las instancias que pertenecen a
dicha clase. Cada copia puede tener datos distintos, al igual que cada instancia
es distinta de las demás (aunque todas pertenecen a una misma clase).

Para definir una clase, simplemente utilizamos el keyword class. Por ejemplo:

```py
class Hotel:
    pass
```
Una vez que tenemos una clase llamada Hotel podemos generar una instancia
llamando al constructor de la clase.

```py
hotel = Hotel()
```

## Atributos de la instancia

Todas las clases crean objetos y todos los objetos tienen atributos. Utilizamos
el método especial __init__ para definir el estado inicial de nuestra instancia.
Recibe como primer parámetro obligatorio self (que es simplemente una
referencia a la instancia).
```py
class Hotel:    
    def __init__(self, numero_maximo_de_huespedes, lugares_de_estacionamiento):
        self.numero_maximo_de_huespedes = numero_maximo_de_huespedes
        self.lugares_de_estacionamiento = lugares_de_estacionamiento
        self.huespedes = 0


hotel = Hotel(numero_maximo_de_huespedes=50, lugares_de_estacionamiento=20)
print(hotel.lugares_de_estacionamiento) # 20
```
## Metodos de instancia

Mientras que los atributos de la instancia describen lo que representa el
objeto, los métodos de instancia nos indican qué podemos hacer con las
instancias de dicha clase y normalmente operan en los mencionados atributos.
Los métodos son equivalentes a funciones dentro de la definición de la clase,
pero todos reciben self como primer argumento.

```py
class Hotel:

    ...

    def anadir_huespedes(self, cantidad_de_huespedes):
        self.huespedes += cantidad_de_huespedes

    def checkout(self, cantidad_de_huespedes):
        self.huespedes -= cantidad_de_huespedes

    def ocupacion_total(self):
        return self.huespedes


hotel = Hotel(50, 20)
hotel.anadir_huespedes(3)
hotel.checkout(1)
hotel.ocupacion_total() # 2
```

# Tipos de datos Abstractos
En python todo es un objeto y tiene un tipo. cualquier cosa en la vida real tiene un tipo, por ejemplo existen tipos de pan, tipos de queso, tipos de servicio, tipos de actividades, etc. La programacion orientada a objeto nos permite modelar el mundo a su manera.
Con los objetos se puede:
- Crear
- Manipular
- Destruir

en python se pueden eliminar directamente cuando nadie mas esta usando el objeto con el garbash Colector
tambien existe el metodo del para destruir.

Ventajas: 
- Decomposicion (descomponer en partes el objeto)
- Abstraccion
- Encapsular (esconder ciertos datos que no son importantes)

```py
# Definicion de clase

class <nombre de clase>(<super_clase>): #permite definir el tipo datos abstractos 
    def __unit__(self, <params>): #init. se lo conoce como el contructor, los metodos siempre inician con el parametro self, siempre usar SELF.
        <expresion>
    def <nombre_del_metodo>(self,<params>): #antes se usaba para funcion, pero tambien para metodos
        <expresion> #la expresion invoca lo que hace el metodo.
```
Ejemplo: 
```py
#Definicion
Class Persona:
    def__init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def saluda(self, otra_persona):
        return f"Hola {otra_persona.nombre}, me llamo {self.nombre}."
# Uso
>>> david = Persona("David", 35)
>>> Erika = Persona("Erika", 32)

>>> david.saluda(erika)
"hola Erika, me llamo David"
```
### Instancia
Mienstras que la clase es un molde, a los objeto se lo conoce como instancia, imagina que tienes un molde que hace botella, la clase es el molde y cada vez que se hace una botella, a eso se lo conoce como instancia.
las instancias pueden tener atributos distintos, diferentes colores, formas, etc.
cada vez que generamos una nueva instancia se genera un nuevo contructor (donder.init) double guion bajo.
los atributos de clase nos permiten hacer varias cosas: 
-variables de instancia
-metodos
-variables privadas (convenciones (_) )
```py
class Coordenada:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # def es una funcion, pero dentro de una clase es un metodo    
    def distancia(self, otra_coordenada): #otra_coordenada es una instancia de Coordenada
        x_diff = (self.x - otra_coordenada.x)**2 # metodo euclidiano
        y_diff = (self.y - otra_coordenada.y)**2

        return (x_diff + y_diff)**0.5

if __name__ == "__main__":
    coord_1 = Coordenada(3, 30)
    coord_2 = Coordenada(4, 8)

    print(coord_1.distancia(coord_2))
    print(isinstance(coord_2, Coordenada))
```
Primero empecemos con las definiciones:

- class es una clase.
- def es una función, pero dentro de un class es un metodo, por lo tanto en nuestro ejemplo es un método.
- constructor es el primer método que se ejecuta.
- instancia es lo que esta dentro de un método, después de self. Ejm.: (self, otra_coordenada).

```py
class Coordenada:
	def__init__(self, x, y):#hasta aquí lo que esta después de self, solo son parametros.
		self.x = x
		self.y = y  
		# Aquí estamos inicializando las variables de instancia
```
luego escribimos el método que nos indica que hará el programa usando las instancias que se definieron en el constructor.

```py
def distancia(self, otra_coordenada): #el parametro otra_coordenada es una instancia, que hara uso del molde en la primer clase de inicializacion, la cual usaremos despues, tomar atencion.
	x_diff = (self.x - otra_coordenada.x)**2
	y_diff = (self.y - otra_coordenada.y)**2

	return (x_diff +y_diff)**0.5
	#estos solo son una representación matemática de lo que hará el programa (lo explicare después)
```
luego tenemos que permitir que el programa corra desde nuestro terminal con:

```py
#mi caso yo prefiero usar comillas dobles, depende de ustedes.
if__name__ == "__main__": 
	coord_1 = Coordenada(3, 30)
	coord_2 = Coordenada(4, 8)
	#estas dos expresiones son instancias que usan el molde que es el primer método de inicializacion.
```
luego para ver el output que nos arroja el programa corremos print, este print hace uso de la instancia con las clases.

```py
print(coord_1.distancia(coord_2))
#"coord_1" hace uso dela primer instancia, mientras que coord_2 al estar dentro del metodo distancia, ocupa el lugar de otra_coordenada. (entender esta parte es muy importante)
```
lo que vimos hasta ahora es la parte del código, pero matemáticamente pasa lo siguiente:
- los parametros (x, y) en init son las ultimas instancias que definimos:
- (3, 30) = (x, y) ------------------------- primer instancia
- (4, 8) = (x, y) ------------------------- segunda instancia

ahora, recuerda que nuestro print fue:
```py
print(coord_1.distancia(coord_2))
```

coord_1 tomaria el lugar del primer metodo, es decir:
- self.x = 3
- self.y = 30

luego como coord_2 esta dentro del método distancia tomaría el lugar de la instancia “otra_coordenada” pero lo mas interesante es que esta instancia hace uso del molde en el primer método:
- otra_coordenada.x = 4
- otra_coordenada.y = 8

por tal motivo matemáticamente quedaría de la siguiente manera:
- x_diff = (3 - 4)^2 = 1
- y_diff = (30 - 8)^2 = 484

return (x_diff + y_diff)**0.5 quedaría de la siguiente manera:
- (1 + 484)^(1/2) = 22.0227, su raiz cuadrada el resultado final.