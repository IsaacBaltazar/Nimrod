# Sistema de empleados

print(f"*** SISTEMA DE EMPLEADOS ***")
nombre_empleado = input("Intruduce el nombre del empleado: ")
edad_empleado = int(input("Introduce la edad del empleado: "))
salario_empleado = float(input("Introduce el salario del empleado: "))
es_jefe = input("¿Es jefe de departamento? (Introduce 'Si' o 'No'): ")

# Convertir a bool la variable es_jefe
es_jefe = es_jefe.lower() == 'si'

# Imprimir los valores del empleado 
print('\nDatos del empleado')
print(f'Nombre: {nombre_empleado}')
print(f'Edad: {edad_empleado}')
print(f'Salario: {salario_empleado:.2f}')
print(f'Es jefe de Departamento? {es_jefe}')