class carro():
    def movimiento(self):
        print("Me muevo usando 4 ruedas")

class moto():
    def movimiento(self):
        print("Me muevo usando 2 ruedas")

class camion():
    def movimiento(self):
        print ("Me muevo usando 12 ruedas")

mivehiculo= moto()
mivehiculo.movimiento()
mivehiculo2= carro()
mivehiculo2.movimiento()
mivehiculo2= camion()
mivehiculo2.movimiento()

def movimientovehiculo(vehiculo):
    vehiculo.movimiento()

micamion=carro()
movimientovehiculo(micamion)