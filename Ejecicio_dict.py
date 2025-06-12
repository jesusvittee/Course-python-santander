estudiante = {
    'nombre' : 'Shanks',
    'carrera' : 'Navegación',
    'edad' : '30',
    'materias_aprobadas': '3 de 5'
}

#Imprime su contenido.
print(estudiante)
#Usa .get() para obtener "promedio" con valor por defecto 0.
print(estudiante.get('promedio', 0))

#Actualiza "edad".
estudiante.update({'edad':31})
print(estudiante)
#Agrega una nueva clave "promedio".
estudiante.update({'promedio': 10})
print(estudiante)
#Elimina "materias_aprobadas".
del estudiante['materias_aprobadas']
print(estudiante)
#Imprime las claves y valores.
print(estudiante.keys())
print(estudiante.values())

estudiante.pop('carrera')
print(estudiante)



#Primera correccion en ves de =  son :