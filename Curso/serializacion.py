## BIBLIOTECA "PICKLE"
    ## METODO "dump()" VOLCADO DE DATOS AL FICHERO BINARIO EXTERNO
    ## METODO "load()" CARGA DE LOS DATOS DEL FICHERO BINARIO EXTERNO
import pickle

nombres = ["Juan","Sofia","Andres","Isabel"]

fichero_binario = open("nombres","wb")

pickle.dump(nombres,fichero_binario)

fichero_binario.close()


