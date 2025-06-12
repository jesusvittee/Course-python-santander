"""
try:
    # Código que puede generar una excepción
    resultado = 10 / 0  # División por cero
    print(resultado)
except ZeroDivisionError:
    print("Error: División por cero")
except ValueError:
    print("Error: Valor inválido")
    
#*******************************  
  
try:
    # Código que puede generar una excepción
    archivo = open("archivo.txt", "r")
    # Realizar operaciones con el archivo
except FileNotFoundError:
    print("Error: Archivo no encontrado")
finally:
    archivo.close()  # Cerrar el archivo siempre, incluso si ocurre una excepción
"""
#Ejercicio 1
"""
1. Conversión simple de número
✅ Escribe un programa que:
Pida un número al usuario.
Lo convierta a entero.
Si el usuario escribe algo que no sea número, muestra: "Eso no es un número válido".

try:
    int(input('Agregar un número: '))
except ValueError:
    print('Este no es un número válido')
"""

#Ejercicio 2
"""
División entre cero
✅ Escribe un programa que:
Pida dos números.
Los divida.
Si el segundo número es cero, muestra: "No se puede dividir entre cero".

try:
    num1 = int(input('Ingresa primer numero: '))
    num2 = int(input('Ingresa segundo numero: '))
    div = num1 / num2
except ZeroDivisionError:
    print('No se puede dividir entre cero')
"""
"""
#Ejecicio 3
try:
    num1 = int(input('Ingresa primer numero: '))
    num2 = int(input('Ingresa segundo numero: '))
    div = num1 / num2
except ZeroDivisionError:
    print('No se puede dividir entre cero')
finally:
    print('Programa terminado')
"""
#Ejercico 4
""" 
Capturar múltiples errores
✅ Escribe un programa que:
Pida dos números.
Divida el primero entre el segundo.
Si el usuario escribe algo que no es número, muestra: "Valor no válido".
Si intenta dividir entre cero, muestra: "Error: división entre cero".

try:
    num1 = int(input('Ingresa valor 1:'))
    num2 = int(input('Ingresa valor 2:'))
    div = num1 / num2
    print(div)
except ValueError:
    print('Valor no válido')
except ZeroDivisionError:
    print('No se puede dividir entre zero')
"""
#Ejercicio 5
"""
Escribe un programa que intente abrir un archivo llamado "datos.txt":
Si no existe, muestra: "Archivo no encontrado".
Siempre imprime: "Fin del intento de abrir archivo" con finally.
(No necesitas tener el archivo de verdad; es solo para probar el código).

try:
    open = open('datos.txt')
except FileNotFoundError:
    print('Archivo no encontrado.')
finally:
    print('Fin del intento de abrir del archivo')
"""
#Ejercicio 6
"""
✅ Escribe un programa que:
Pida al usuario escribir 5 números uno por uno.
Si escribe algo que no es número, captura el error y vuelve a pedir el número.
Al final, imprime la lista con los 5 números válidos ingresados.
⚠️ Debes usar try y un ciclo (while o for) para pedir los números hasta que todos sean válidos.

try:
    valor = {1:'primer', 2:'segundo',3:'tercer', 4:'cuarto', 5:'quinto'}
    num = 1
    list_num = []
    while num <= 5:
        lugar = valor.get(num)
        numbers = int(input(f'Ingresa el {lugar} numero: '))
        list_num.append(numbers)    
        num +=1
    print(list_num)
except ValueError:
    print('vuelve a ingresar el numero')
"""
#Ejercicio 7
"""
Escribe una mini-calculadora que:
Pida dos números.
Pida una operación: + - * /.
Realice la operación.
Si la operación es inválida (por ejemplo, escribe “&”), muestra un error.
Si divide entre cero, muestra un error.
Siempre imprime: "Gracias por usar la calculadora." con finally.



try:
    num1 = int(input('Ingresa primer valor: '))
    num2 = int(input('Ingresa segundo valor: '))
    select = input('Ingresa operacions. \nsuma \nresta\nmultiplicacion\ndivision \nSELECCIONAR. ')
    match select:
        case 'suma':
            print(num1 + num2)
        case 'resta':
            print(num1 - num2)
        case 'multiplicacion':
            print(num1 * num2)
        case 'division':
            print(num1 / num2)
except ValueError:
    print('solo se admiten numeros.')
except ZeroDivisionError:
    print('No se puede dividir entre cero.')
finally:
    print('Gracias por usar la calculadora.')
"""
