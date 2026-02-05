# Programa: Sistema Generador de Id Único

from random import randint

print(f'*** Sistema Generador de Id Único ***')
nombre = input('Ingresa tu nombre: ') #tomar 2 primeras letras en mayúscula
apellido = input('Ingresa tu apellido: ') #tomar 2 primeras letras en mayúscula
year = input('Ingresa tu año de nacimiento (YYYY): ') #tomar 2 últimos dígitos

# Generar uun valor aleatorio de 4 dígitos con randint
aleatorio = randint(1000,9999)

# Normalización de valores
nombre_2 = nombre.strip().upper()[:2]
apellido_2 = apellido.strip().upper()[:2]
year_2 = year.strip()[2:]

# Generar el id
id_unico = f'{nombre_2}{apellido_2}{year_2}{aleatorio}'
# id_unico = nombre[:2].upper() + apellido[:2].upper() + year[-2:] + aleatorio
print(f'''\nHola {nombre},
    Tu ID único generado por el sistema es: 
    {id_unico}
''')
