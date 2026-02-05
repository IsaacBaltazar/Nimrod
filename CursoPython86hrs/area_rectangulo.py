print('*** Cálculo de área y perímetro de un rectángulo ***')

base = float(input('Ingresa la base del rectángluo: '))
altura = float(input('Ingresa la altura del rectángulo: '))

# Realizar cálculos
area = base * altura
perimetro = 2 * (base + altura) # aplicando la precedencia de operadores
print(f'El área del rectángulo es: {area}')
print(f'El perímetro del rectángulo es: {perimetro}')