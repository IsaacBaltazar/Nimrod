print('*** Operadores de asignación ***')
numero = 5
print(f'Valor de numero: {numero}')
numero = 10
print(f'Valor de numero: {numero}')
cadena = 'Saludos desde Python'
print(f'Valor de la cadena: {cadena}')

# Asignación múltiple
x, y, z = 5, 'Hola', -9.15
print(f'Valor de x = {x}, y = {y}, z = {z}')

# Asignación encadenada
a = b = c = 10
print(f'Valor a = {a}, b = {b}, c = {c}')

# Intercambio de valores de una variable, sin utilizar variables temporales
x, y = 5, 10
print(f'Valores iniciales x = {x}, y = {y}')
# Aplicando el concepto de asignación múltiple, intercambiamos los valores
x, y = y, x
print(f'Valor de x = {x}, y = {y}')

#Recibir múltiples valores de entrada por usuario
nombre, apellido = input('Ingresa tu nombre y apellido separados por una coma: ').split(',')
print(f'Tu nombre es: {nombre.strip()} y tu apellido es: {apellido.strip()}')