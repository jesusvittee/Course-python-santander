#lerr archivo
archivo = open("datos.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()
#Escribir
archivo = open("datos.txt", "w")
archivo.write("Hola, mundo!")
archivo.close()
#Importante cerrar los documentos


#Abrir archivos de manera automatica
with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

