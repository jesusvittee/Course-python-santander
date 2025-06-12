"""
#Ejercio 1
personaje = {
    'nombre':'Monkey D. Luffy',
    'recompensa':'300000000',
    'fruta_del_diablo':'Gomu Gomu no MI',
    'tripulación':'Muguiwara'
}
print(personaje)
recompensa = personaje.get('recompensa')
print(recompensa)
haki = personaje.get('haki', 'No especificado')
print(haki)

#Ejercicio 2
personaje.update({'recompensa': 5000000000})
personaje.update({'haki': 'Observación, armadura, rey'})
print(personaje)

#Ejercicio 3
del personaje['fruta_del_diablo']
personaje.pop('tripulación')
print(personaje)
"""

"""
#Ejercicio 4
sombrero_de_paja = {
    "luffy": {"rol": "Capitán", "recompensa": 5000000000},
    "zoro": {"rol": "Espadachín", "recompensa": 1111000000},
    "nami": {"rol": "Navegante", "recompensa": 366000000}
}

zoro = sombrero_de_paja.get('zoro')
recompenza_zoro = zoro.get('recompensa')
print(recompenza_zoro)

llave = sombrero_de_paja.keys()
print(llave)

#Recorre el diccionario con un for y muestra:
#"Luffy es Capitán con recompensa de 5000000000 berries." (para todos).


#"{key} es {rol} con recompensa de {recompensa}} berries."

for key in sombrero_de_paja:
   datos = sombrero_de_paja.get(key)
   [rol,recompensa] = datos.values()
   print(f"{key} es {rol} con recompensa de {recompensa} berries.")
"""
   
#Ejercicio 5
sombrero_de_paja = {
    "luffy": {"rol": "Capitán", "recompensa": 5000000000},
    "zoro": {"rol": "Espadachín", "recompensa": 1111000000},
    "nami": {"rol": "Navegante", "recompensa": 366000000}
}

#Nombre y recompensas de cada miembro
def mostrar_recompensas(muguiwaras):
    Total = 0
    for muguiwara_key in muguiwaras:
        muguiwara_value2 = muguiwaras.get(muguiwara_key)  
        recompensa = muguiwara_value2.get('recompensa')
        print(f"{muguiwara_key}: {recompensa} berries")
        Total += recompensa       
    print(f'\nRecompensa total de los muguiwara: {Total}')
    
mostrar_recompensas(sombrero_de_paja)
