<div align="center">
  <h1>Programación orientada a objetos y Algoritmos con Python</h1>
  <h3>by Mauricio Obe</h3>
</div>
# Tabla de contenidos

- [Programacion orientada a objetos](#Programacion_orientada_a_objetos)
    - [Introduccion](#Introduccion)
    - [Clases](#Clases)
    - [Instancias](#Instancias)
    - [Atributos de la instancia](#Atributos_de_la_instancia)
    - [Metodos de instancia](#Metodos_de_instancia)
    - [Tipos de datos Abstractos](#Tipos_de_datos_Abstractos)
    - [Instancia](#Instancia)
    - [decomposicion](#decomposicion)
    - [abstraccion](#abstraccion)
    - [Encapsulacion, getters and setters](#Encapsulacion,_getters_and_setters)
    - [Herencia](#Herencia)
    - [Polimorfismo](#Polimorfismo)

# ```py
# Programacion orientada a objetos

## Introduccion
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

## Tipos de datos Abstractos
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

## Instancia
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

## decomposicion
Es partir un problema en problemas mas pequeños, las clases permiten crear mayores abstracciones en forma de componentes.
Cada clase se encarga de una parte del problema y el programa se vuelve mas facil de mantener. 

```py
class Automovil:
    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = "en_reposo" #es una variable privada o interna
        self._motor = Motor(cilindros=4) #variable privada
    
    def acelerar(self, tipo="despacio"):
        if tipo == "rapida":
            self.motor.inyecta_gasolina(10)
        else:
            self.motor.inyecta_gasolina(3)
        
        self._estado = "en movimiento"
class Motor:
    def __init__(self, cilindros, tipo="gasolina"): #nuevo tipo de parametro, parametro por defecto
        self.cilindro = cilindro
        self.tipo = tipo
        self._temperatura = 0
    
    def intecta_gasolina(self, cantidad):
        pass
```

## abstraccion
```py
class Lavadora:
   
    def __init__(self):
        pass
    
    def lavar(self, temperatura="caliente"):
        self._llenar_tanque_de_agua(temperatura)
        self._anadir_jabon()
        self._lavar()
        self._centrifugar()
    
    def _llenar_tanque_de_agua(self, temperatura):
        print(f"llenando el tanque con agua {temperatura}")

    def _anadir_jabon(self):
        print("anadiendo jabon")
    
    def _lavar(self):
        print("lavando la ropa")

    def _centrifugar(self):
        print("centrifugando la ropa")

if __name__ == "__main__":
    lavadora = Lavadora() 
    lavadora.lavar()
```
En la parte final cuando colocamos:
```py
if__name__ == "__main__":
    lavadora = Lavadora()  #crea la instancia lavadora
    lavadora.lavar()       #la instancia lavar continua despues de la inicializacion
```
if__name__ == "__main__":
    lavadora = Lavadora()  #crea la instancia lavadora
    lavadora.lavar()       #la instancia lavar continua despues de la inicializacion

```py
llenando el tanque con agua caliente
anadiendo jabon
lavando la ropa
centrifugando la ropa
```

## Encapsulacion, getters and setters
la encapsulacion permite agrupar datos y su comportamieto, permite agrupar datos y previene modificaciones no autorizadas.
las clases nos permiten tener son variables de instancias, metodos internos (privados o publicos) y todo esto se encuentra en un solo lugar por tal motivo se entiende que es programacion orientada a objetos.
lo importante de la encapsulacion, tiene que ver con la programacion defensiva, lo cual permite el acceso a esos datos y la modificacion de esos datos, dado que python es muy abierto a ser modificado por tal motivo existe la programacion defensiva que controla este aspecto.

```py
class CasillaDeVotacion:
    def __init__(self, identificador, pais):
        self._identificador = identificador
        self._pais = pais
        self._region = None

    #getters, Decoradores, property significa que es funcion que se definira como propiedad 
    #se accede a esta funcion a travez de dot notation
    @property 
    def region(self):
        return self._region
    #Funcion que nos permite modificar valores
    @region.setter 
    def set_region(self, region):
        if region in self._pais:
            self._region = region

            raise ValueError(f"La region {region} no es valida en {self._pais}")
#introduce de identificador, y las regiones dentro de la variable pais.
>>> casilla = CasillaDeVotacion(123, ["Ciudad de Mexico", "Morelos"])
# al introducir la nueva instancia casilla seguido de la instancia region nos rebota una variable privada. 
>>> casilla.region
None
>>> casilla.region = "Ciudad de Mexico"
>>> casilla.region
"Ciudad de Mexico"
```

## Herencia
Permite modelar una jerarquia de objetos o clases, nos permite compartir cierto comportamiento comun en la jerarquia.
Al padra se le conoce como superclase y al hijo como subclase. 
las super clases se las menciona asi por que estan arriba.
las sub clases se les llama asi porque heredan el codigo de las super clases

```py
class Rectangulo:

    def __init_(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

class Cuadrado(Rectangulo):
# Para heredar el comportamiento se define la super clase que es el rectangulo, porque esta arriba.
    
    def __init__(self, lado):
    #solo necesitamos un lado para definir un cuadrado
        super().__init__(lado, lado)
        #super nos permite tener una referencia de la super clase

if __name__ == "__main__":
    rectangulo = Rectangulo(base=3, altura=4)
    print(rectangulo.area())

    cuadrado = Cuadrado(lado=5)
    print(cuadado.area())
    #ejecutamos el metodo area  dentro de la clase cuadrado, es decir estamos heredando el metodo de la super clase
```

## Polimorfismo
Es la habilidad de tomar varias formas, en python, nos permite cambiar el comportamiento de una superclase para adaptarlo a subclase.

```py
class Persona:
    
    def __init__(self, nombre):
        self.nombre = nombre
    
    def avanza(self):
        print("Ando caminando")

class Ciclista(persona):
#la clase ciclista extiende persona, asi se lee
#Es una subclase que hereda una superclase
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def avanza(self):
        print("ando moviendome en mi bicicleta")

def main():
    persona = Persona("David")
    persona.avanza()

    ciclista = Ciclista("Daniel")
    ciclista.avanza()

if __name__ == "__main__":
    main()
```

# Introduccion a la complejidad algoritmica
## Aproximacion
Nos permite comparar la eficiencia entre dos algoritmos, esto nos ayuda a predecir el tiempo que se tarda en resolver un problema.
podemos definirla como T(n) funcion de tiempo.
podemos tener aproximaciones:
- Cronometrar el tiempo en el que corre un algoritmo, depende de la computadora y es muy inestable de comparar. 
- Contar los pasos con una medida abstracta de operacion. 
- contar los pasos conforme nos aproximamos al infinito.

```py
import time

def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1
        # 5*1, 5-1, 4*1, 4-1, 3*1, 3-1, 3*1, 3-1, 2*1, 2-1, 1.
    return respuesta
    
def factorial_r(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)

if __name__ == "__main__":
    n = 1000

    comienzo = time.time()
    print(factorial(n))
    final = time.time()
    print(final - comienzo)

    comienzo = time.time()
    print(factorial_r(n))
    final =time.time()
    print(final - comienzo)
```

## Conteo abstracto
la anterior forma de contar no era eficiente, el conteo abstracto trata de una aproximacion mas matematica.

```py
def f(x): #la variable es x
    respuesta = 0
    for i in range (1000): #correra 1000 veces sin importar x, es una constante
    for i in range(x): #si depende de x
        respuesta += x
    for i int range(x): # 
        for j in range(x):
            respuesta += 1
            respuesta += 1
    return respuesta
```

## Notacion asintotica
en este caso no importan variaciones pequeñas, el enfoque se centra en lo que pasa conforme el tamaño del problema se acerca al infinito. 
En el Big O notation solo importa el valor de mayor tamaño, es decir que genera resultados grandes. 

```py
#Ley de la suma 
def f(n):
    for i in range(n):
        print(i)
    for i in range(n):
        print(i)
# 0(n) + (0)n = 0(n + n) ; 0(2n) ; funcion lineal
```
ahora veamos otro ejemplo.
```py
#Ley de la suma
def f(n):
    for i in range(n):
        print(i)
    for i in range(n * n):
        print(i)
# 0(n) + 0(n * n) = 0 (n + n^2) = 0(n^2)
```
ahora veamos un ejemplo de ley de multiplicacion
```py
#ley de la multiplicacion
def f(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
# 0(n) * 0(n) = 0(n * n) = 0(n^2) 
```
ahora veamos un ejemplo de recursividad multiple
```py
#Recursividad multiple
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
#0(2^n)
```

## Clases de complegidad algoritmica
- O(1) Constante; como no existe variable, el loop se tardara lo mismo cada vez.
- O(n) Lineal; se tardara el mismo numero de veces que el valor de la variable.
- O(Log n) Logaritmica; al principio crecera mucho, pero luego crecera poco hacia el infinito.
- O(n Log n) Log lineal; 
- O(n^2) Polinomial
- O(2^n) Exponencial
<div align="center"> 
  <img src="complejidad algoritmica.JPG" width="1000">
</div>


