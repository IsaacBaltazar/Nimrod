##Generador de email
#Crea un programa para generar un email  a partir de los siguientes datos
print('***  Generador de Email  ***')
nombre = input('Ingresa tu nombre: ') #' Ubaldo Acosta Soto '
apellidos = input('Ingresa tus apellidos: ')
#print(f'Nombre del usuario: {nombre}')
#nombre_normailzado = nombre.strip()
#nombre_normailzado =  nombre_normailzado.lower().replace(' ', '.')
#print(f'Nombre de usuario normalizado: {nombre_normailzado}')
empresa = input('Ingresa el nombre de tu empresa: ') #'Global Mentoring'
#print(f'Nombre de la empresa: {empresa}')
extension_dominio = input('Ingresa la extensión de dominio de tu empresa: ')
dominio = '.com.mx'

#print(f'Extensión del dominio: {dominio}')
#dominio_normalizado = '@' + empresa.lower().replace(' ','') +  dominio
#print(f'Dominio del email normalizado: {dominio_normalizado}')
#resultado esperado 
#email: ubaldo.acosta.soto@globalmentoring.com.mx
#email = nombre_normailzado + dominio_normalizado
#print(f'Email final generado: {email}') 

# Normalización de valores

nombre = nombre.strip().lower().replace(' ', '.')
apellidos = apellidos.strip().lower().replace(' ', '.')
empresa = empresa.strip().lower().replace(' ', '')
extension_dominio = extension_dominio.strip().lower().replace(' ', '')

# Generar el email
email = f'{nombre}{apellidos}@{empresa}{extension_dominio}'

print(f'''\nTu nuevo email generado es:
    {email}
    ''')