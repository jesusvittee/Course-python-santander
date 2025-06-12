#continue, break, pass

#Imprime todos los números del 1 al 10 excepto el número 5.
""""
for num in range(10):
    if num == 5:
        continue
    print(num)
""" 
#Imprimir solo numeros impares
""""
for i in range(10):

    if i % 2 == 1:
        continue
    print(i)
"""""
#Imprime los números del 1 al 10, pero detente cuando llegues al número 6. 
"""  
for num in range(10):
    if num == 6:
        break
    print(num)
"""  
#Pide números al usuario infinitamente hasta que escriba un número negativo
"""
num = int(input('Ingresa un numero: '))
while num >= 0:
    num = int(input('Ingresa un numero: '))
    if num < 0:
        break
    print(f'{num}')
"""
#Crea una función llamada mi_funcion que aún no haga nada (pendiente por implementar).
"""
def mi_funcion():
    pass

mi_funcion()   
"""
#Recorre una lista con una estructura if, pero no hagas nada si el número es 0.
"""
list = [3,4,5,6,0,8]
for num in list:
    if num == 0:
        #pass no hará nada sin embargo reserva un codido para despues.
        pass
    print('se hace algo en {}'.format(num))
"""
#Si el número es 3, imprime "Número prohibido" y usa continue.
"""
num = 10
while num >= 0:
    if num ==5:
        num -=1
        print('Numero prohibido!')
        continue
    print(num)
    num -=1
"""
#Si el número es 7, imprime "¡Alto!" y usa break.
"""
lista = [1,3,4,5,342333,7,23232,10]
print(lista)
for i in lista:
    if i == 7:
        print('Alto!')
        break
    print(i)
"""
#Si el número es 5, simplemente usa pass (no hagas nada especial).
"""
insertar = int(input('Ingresa un numero: '))

while True:
    insertar = int(input('Ingresa un numero: '))
    if insertar == 5:
        pass
    elif insertar != 5:
        print('Numero aceptable')
"""
#Ejercicio final
"""
Enunciado:
Tienes la siguiente lista de números:
numeros = [10, -5, 0, 15, 20, -3, 5, 7, 0, 30]
Recorre esta lista con un ciclo for y aplica las siguientes reglas:

Si el número es negativo, imprime "Número inválido" y usa continue para pasar al siguiente número (no hagas nada más con ese número).

Si el número es 0, usa pass porque este número "aún no tiene tratamiento definido" (no hagas nada, ni imprimir).

Si encuentras un número mayor que 25, imprime "Número demasiado grande. Deteniendo..." y usa break para terminar el ciclo de inmediato.

Para todos los demás números, imprime "Número válido:" seguido del número.
"""
# Mi codigo
"""
numeros = [10, -5, 0, 15, 20, -3, 5, 7, 0, 30]
for numero in numeros:
    if numero < 0:
        print('Número inválido')
        continue
    elif numero == 0:
        pass
    elif numero > 25:
        print('Número demasiado grande. Deteniendo...')
        break
    else:
        print('Número valido: {}'.format(numero))
"""



