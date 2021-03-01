## Herencia
    ## que caracteristicas tienen en comun todos los objetos
    ## que comportamientos tienen en comun todos los objetos
    ## se contruye una clase con todo lo anterior, las caracteristicas especificas de cada objeto en su propia clase
class vehiculos():
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera = False
        self.frena = False
    def arrancar(self):
        self.enmarcha = True
    def acelerar(self):
        self.acelera= True
    def frenar(self):
        self.frena=True
    def estado(self):
        print ("Marca:", self.marca, "\nModelo:",self.modelo, "\nEn Marcha:", self.enmarcha, "\nAcelerando:",self.acelera,"\nFrenando:",self.frena)

class moto(vehiculos):
    hcaballito=""
    def caballito(self):
        self.hcaballito="Si"  
    def estado(self):
        print ("Marca:", self.marca, "\nModelo:",self.modelo, "\nEn Marcha:", self.enmarcha, "\nAcelerando:",self.acelera,"\nFrenando:",self.frena,"\n",self.hcaballito)


mimoto= moto("BMW","gy") 
mimoto.caballito()
mimoto.estado()

class furgon(vehiculos):
    def carga(self,peso):
        self.cargado=peso
        if(self.cargado):
            return "El furgon esta cargado"
        else:
            return"El furgon no esta cargado"

mifurgon=furgon("bus","dibsd")
mifurgon.arrancar()
mifurgon.estado()
print(mifurgon.carga(True))

class electricos():
    def __init__(self):
        self.autonomia = 100
    def cargabateria(self):
        self.cargando = True
    
class bielec(vehiculos,electricos):
    pass
mibicicleta=bielec("GMW","huaus")

## herencia/ super()/ isinstance()
# super() llama el __init__ de la clase padre
class persona():
    def __init__(self,nombre,edad,direccion):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
    def descripcion(self):
        print ("Nombre:",self.nombre,"Edad:",self.edad,"Direccion:",self.direccion)

class empleado(persona):
    def __init__(self,salario,years,nombre_empleado,edad_empleado,direccion_empleado):
        super().__init__(nombre_empleado,edad_empleado,direccion_empleado)
        self.salario= salario
        self.years = years
    def descripcion(self):
        super().descripcion()
        print("Salario",self.salario,"Antigüedad:",self.years)

Juan = empleado(5000,1,"Juan",18,"Colombia")
Juan.descripcion()
## isinstance devuelve si el primer parametro pertence al segundo(clase)
print(isinstance(Juan,empleado))

