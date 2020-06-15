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