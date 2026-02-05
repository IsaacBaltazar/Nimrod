# Programa: función bool

# 1. Número (it y float)
print(bool(0))      # False (el vacío numérico)
print(bool(0.0))    # False
print(bool(42))     # True (Existe valor)

# 2. Texto (strings)
# Cadena vacía = Nada = Flase
print(bool(""))     # False

# Cadena con espacio o texto = Algo = True
print(bool(" "))    # True
print(bool("Hola")) # True

# 3. None (Ausencia total)
vacio = None
print(bool(vacio))  # False

print(bool(False))  # False
print(bool(True))   # True