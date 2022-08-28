# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite el ingreso de tres números
enteros, y luego en cada caso informe si el número es par
o impar.
Para cada caso imprimir el resultado en pantalla.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio
numero_1 = int(input('Ingrese el primer numero: '))
numero_2 = int(input('Ingrese el segundo numero: '))
numero_3 = int(input('Ingrese el tercer numero: '))
if(numero_1 > 0):
    print('El numero {} es PAR'.format(numero_1))
elif(numero_1 < 0):
    print('El numero {} es IMPAR'.format(numero_1))
else:
    print('El numero {} es CERO'.format(numero_1))
if(numero_2 > 0):
    print('El numero {} es PAR'.format(numero_2))
elif(numero_2 < 0):
    print('El numero {} es IMPAR'.format(numero_2))
else:
    print('El numero {} es CERO'.format(numero_2))
if(numero_3 > 0):
    print('El numero {} es PAR'.format(numero_3))
elif(numero_3 < 0):
    print('El numero {} es IMPAR'.format(numero_3))
else:
    print('El numero {} es CERO'.format(numero_3))



