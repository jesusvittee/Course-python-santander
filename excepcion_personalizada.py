def funcion():
    # Código que puede generar una excepción personalizada
    if True:
        raise Exception("Descripción del error")


try:
    funcion()
except Exception as e:
    print(f"Error: {str(e)}")
    
    
#---------------------------------------
