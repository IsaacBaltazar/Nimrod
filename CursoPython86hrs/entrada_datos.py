# Programa: Entrada Datos Python
nombre = input("Proporciona tu nombre: ")
print(f"Tu nombre es: {nombre}")

# Cuidado con la conversión de tipos al trabajar con valores numéricos
# Forma correcta: Envolver con int() o float()

# Para enteros (edad, cantidad)
edad = int(input("Introduce tu edad: "))
print(f"Tu edad es: {edad}")
year = int(input("Introduce el año actual: "))
nacimiento = year - edad
print(f"Naciste en el año: {nacimiento}") 

# Para decimales (precio, altura)

altura = float(input("Introduce tu altura: "))
print(f"Tu altura es: {altura} metros")
