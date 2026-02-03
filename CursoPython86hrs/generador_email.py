##Generador de email
#Crea un programa para generar un email  a partir de los siguientes datos
print('***  Generador de Email  ***')
nombre = ' Ubaldo Acosta Soto '
print(f'Nombre del usuario: {nombre}')
nombre_normailzado = nombre.strip()
nombre_normailzado =  nombre_normailzado.lower().replace(' ', '.')
print(f'Nombre de usuario normalizado: {nombre_normailzado}')
empresa = 'Global Mentoring'
print(f'Nombre de la empresa: {empresa}')
dominio = '.com.mx'
print(f'Extensión del dominio: {dominio}')
dominio_normalizado = '@' + empresa.lower().replace(' ','') +  dominio
print(f'Dominio del email normalizado: {dominio_normalizado}')
#resultado esperado 
#email: ubaldo.acosta.soto@globalmentoring.com.mx
email = nombre_normailzado + dominio_normalizado
print(f'Email final generado: {email}') 