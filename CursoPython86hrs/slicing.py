# Programa: Aplicar el concepto de slicing

texto = "PROGRAMACIÓN"

# 1. Básico [inicio:fin]
print(texto[0:4]) # "PROG"

# 2. Atajo desde el inicio [:fin]
print(texto[:4]) # "PROG" (Asume inicio 0)

# 3. Atajo hasta el final [incio:]
print(texto[8:]) # "CIÓN" (Hasta el último char)

# 4. Índices negativos
print(texto[-4:]) # "CIÓN" (los últimos 4)

# 5. Pasos [::paso] (paso negativo para invertir cadena)
print(texto[::-1])