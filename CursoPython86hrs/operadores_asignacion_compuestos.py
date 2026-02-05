print('*** Operadores Asignación Compuestos ***')
a, b = 10, 15
print(f'Valor inicial a: {a}, b: {b}')

# Operador compuesto de suma +=
a += b # a = a + b
print(f'Operador a += b es: {a}')

# Operador compuesto de resta -=
a = 10 # reiniciamos la variable a
a -= b # a = a - b
print(f'Operador a -= b es: {a}')

# Operador compuesto de multiplicación *=
a = 10
a *= b # a = a * b
print(f'Operador a *= b es: {a}')

# Operador compuesto de división /=
a = 10
a /= b # a = a / b
print(f'Operador a /= b es: {a:.2f}')
