# Condicionales [Python]
# Ejercicios de profundización

# Autor: Edwin Yepez
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con texto
'''
Enunciado:
Realice un programa que solicite por consola 3 palabras cualesquiera
Luego el programa debe consultar al usuario como quiere ordenar las palabras
1 - Ordenar por orden alfabético (usando el operador ">")
2 - Ordenar por cantidad de letras (longitud de la palabra (len) y operador ">")

Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor

Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor

IMPORTANTE: Para ordenar las palabras deben realizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido.
'''

print('Ejercicios de práctica con cadenas')
# Empezar aquí la resolución del ejercicio
texto_1 = str(input('Ingrese la primera palabra: '))
texto_2 = str(input('Ingrese la segunda palabra: '))
texto_3 = str(input('Ingrese la tercera palabra: '))
long_1 = len(texto_1)
long_2 = len(texto_2)
long_3 = len(texto_3)
entrada = int(input('Ingrese 1 si desea ordenar las palabras por orden alfabetico o ingrese 2 si desea ordenar las palabras por su cantidad de letras: '))
if(entrada == 1):
    if(texto_1 > texto_2) and (texto_2 > texto_3):
        print('Palabra mayor: {} palabra media: {} palabra menor: {}'.format(texto_1,texto_2,texto_3))
    elif(texto_1 > texto_3) and (texto_3 > texto_2):
        print('Palabra mayor: {} palabra media: {} palabra menor: {}'.format(texto_1,texto_3,texto_2))
    elif(texto_2 > texto_1) and (texto_1 > texto_3):
        print('Palabra mayor: {} palabra media: {} palabra menor: {}'.format(texto_2,texto_1,texto_3))
    elif(texto_2 > texto_3) and (texto_3 > texto_1):
        print('Palabra mayor: {} palabra media: {} palabra menor: {}'.format(texto_2,texto_3,texto_1))
    elif(texto_3 > texto_1) and (texto_1 > texto_2):
        print('Palabra mayor: {} palabra media: {} palabra menor: {}'.format(texto_3,texto_1,texto_2))
    elif(texto_3 > texto_2) and (texto_2 > texto_1):
        print('Palabra mayor: {} palabra media: {} palabra menor: {}'.format(texto_3,texto_2,texto_1))
    else:
        print('Existen palabras iguales!!!')
elif(entrada == 2):
    if(long_1 > long_2) and (long_2 > long_3):
        print('Palabra longitud mayor: {} palabra longitud media: {} palabra longitud menor: {}'.format(texto_1,texto_2,texto_3))
    elif(long_1 > long_3) and (long_3 > long_2):
        print('Palabra mayor: {} palabra media: {} palabra menor: {}'.format(texto_1,texto_3,texto_2))
    elif(long_2 > long_1) and (long_1 > long_3):
        print('Palabra mayor: {} palabra media: {} palabra menor: {}'.format(texto_2,texto_1,texto_3))
    elif(long_2 > long_3) and (long_3 > long_1):
        print('Palabra mayor: {} palabra media: {} palabra menor: {}'.format(texto_2,texto_3,texto_1))
    elif(long_3 > long_1) and (long_1 > long_2):
        print('Palabra mayor: {} palabra media: {} palabra menor: {}'.format(texto_3,texto_1,texto_2))
    elif(long_3 > long_2) and (long_2 > long_1):
        print('Palabra mayor: {} palabra media: {} palabra menor: {}'.format(texto_3,texto_2,texto_1))
    else:
        print('Existen palabras iguales!!!')
else:
    print('OPCION NO VALIDA!!!')


    
    
    