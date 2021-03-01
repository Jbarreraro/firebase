from io import open

txt_1 = open("Archivo_1.txt","w")

lineas_texto = txt_1.readlines()

txt_1.close()
print(lineas_texto)