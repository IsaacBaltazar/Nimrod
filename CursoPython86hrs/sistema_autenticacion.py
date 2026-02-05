print('*** Sistema Autenticación ***')

USUARIO_VALIDO = 'admin'
PASSWORD_VALIDO = '123'
usuario = input('Ingresa tu usuario: ')
password = input('Ingresa la contraseña: ')

datos_correctos = usuario == USUARIO_VALIDO and password == PASSWORD_VALIDO
print(f'¿Usuario autorizado? {datos_correctos}')