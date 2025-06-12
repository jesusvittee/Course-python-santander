#Ejercicio 1
num = int(input('Ingresa un numero: '))
match num:
    case 1:
        print('Lunes')
    case 2:
        print('Martes')
    case 3:
        print('Miercoles')
    case 4:
        print('Jueves')
    case 5:
        print('Viernes')
    case 6:
        print('Sabado')
    case 7:
        print('Domingo')
    case _:
        print('Número invalido')

#Ejercio 2
"""
0 a 11 → "Niño"
12 a 17 → "Adolescente"
18 a 59 → "Adulto"
60 o más → "Adulto mayor"
"""
edad = int(input('Escribe la edad que tengas: '))
match edad:
    case _ if 0 <= edad <=11:
        print('Niño')
    case  _ if 12 <= edad <=17:
        print('Adolecente')
    case  _ if 18 <= edad <=59:
        print('Adulto')
    case  _ if edad <=60:
        print('Adulto Mayor')
""""""
#Ejercicio 3
"""
"Alto" si es rojo
"Precaución" si es amarillo
"Avanza" si es verde
Otro → "Color desconocido"
"""
color = input('Color del semaforo: ')
match color:
    case 'rojo':
        print('Alto')
    case 'amarillo':
        print('Precaucion')
    case 'verde':
        print('Avanza')
    case _:
        print('Color desconocido.')

#Ejercicio 4
"""
Pide dos números y una operación ("+", "-", "*", "/"), y muestra el resultado de la operación.
"""
valor1 = int(input('Ingrese primer valor: '))
valor2 = int(input('Ingrese segundo valor: '))

operacion = input('Operacion: ')

match operacion:
    case 'suma':
        suma = valor1 + valor2
        print(suma)
    case 'resta':
        resta = valor1 - valor2
        print(resta)
    case 'suma':
        suma = valor1 + valor2
        print(suma)
    case 'multiplicacion':
        multiplicacion = valor1 * valor2
        print(multiplicacion)
    case 'division':
        division = valor1 / valor2
        print(division)
        
#Ejercicio 5
"""
10 → "Excelente"
8-9 → "Muy bien"
6-7 → "Regular"
0-5 → "Reprobado"
Otro → "Calificación no válida"
"""
calf = int(input('Ingresa calificación: '))
match calf:
    case 10:
        print('Exelente')
    case _ if calf in(8,9):
        print('Muy bien')
    case _ if calf in (6,7):
        print('Regular')
    case _ if 0<= calf <= 5:
        print('Reprobado')
    case _ :   
        print('Calificacion no válida')

#Ejercicio 6
"""
Si está en el origen → "En el origen"
Si está en el eje X → "En el eje X en x = <valor>"
Si está en el eje Y → "En el eje Y en y = <valor>"
Si no, imprime las coordenadas: "En el punto (<x>, <y>)"
"""
#tupla
x=0
y=6
coordenada = (x,y)
match coordenada:
    case (0,0):
        print('En el origen')
    case (_,0):
        print(f'En el eje X en x = {x}')
    case (0,_):
        print(f'En el eje Y en y = {y}')
    case _ :
        print(f'En el punto = ({x},{y})')
        
#Ejercicio 7
"""
Si edad es menor de 18 → "Jesús es menor de edad"
Si edad es 18 o más → "Jesús es mayor de edad"
Si falta alguna clave → "Datos incompletos"
"""
persona = {"nombre": "Jesús", "edad": 21}
edad = persona.get('edad')
match edad:
    case _ if edad < 18:
        print('Jesus es menor de edad')
    case _ if edad >= 18:
        print('Jesus es mayor de edad')
    case _ :
        print('Falta alguna clave')