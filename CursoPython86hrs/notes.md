# 'Universidad Python'

## Hola mundo con python

Es el primer programa que se hace para conocer un lenguaje

```python
print("Hola mundo!")
```

## Variables en python

Una variable es un nombre que almacena valor guardado en la memoria de la pc. En python son dinámicas, cambian su
tipo de acuerdo a lo que se le almacena.

Las variables pueden cambiar su contenido de acuerdo a la ejecución y modificaciones en el mismo programa, por ello
su nombre, variables.

Para cambiar o modificar el valor de una variable solo es necesario volver a llamarla e igualarla a un nuevo valor.

``` python
edad = 28
print(edad)
edad = 30
print(edad)
```

En python las variables son de tipo dinámico, esto es, pueden cambiar el tipo de dato que almacenan.

### Reglas de nombre de variables en python

Reglas:

- Los nombres de las variables pueden tener letras, dígitos y guiones.
- El nombre no puede comenzar con dígitos.
- NO se pueden usar palabras reservadas del lenguaje (keyword) para nombrar variables. Ej. for, if, class, try, etc.
- Python es sensible a mayúsculas y minusculas. Ej. mi_nombre es distinto a Mi_nombre.

Convenciones y buenas prácticas:

- snake case: Es recomendable usar la notación de snake case, es decir, palabras en minúsculas separadas por guión
bajo. Ej. nombre_usuario, nombre_completo, etc.
- Nombres descriptivos: Los nombres de las variables deben reflejar el contenido de la variable. Ej. no usar e, sino edad. No usar n, sino nombre, etc.
- Evitar nombres de un sólo caracter, ya que no son descriptivos y pueden ser confusos.

### Tipos de datos

Python es un lenguaje de tipado dinámico, por lo que no hay necesidad de indicar el tipo de la variable al momento de declararla.

Los valores que pueden almacenar las variables son de distintos tipos, como:

- Números (int): Son números sin la parte decimal, Ej 42, -109.
- Números con punto flotante (float): ej 3.141569, -0.001.
- Cadenas de texto (str): secuencia de caracteres, ej 'Hola mundo'. Los valores cadena pueden definirse con comillas simples '' o dobles "", no se pueden combinar comillas.
- Booleanos: almacenan un valor lógico de verdadero (True) o falso (False), este tipo de valores se usan para
controlar el flujo de un programa.
- None: Es un tipo especial en Python que representa ausencia de valor.
- Para obtener el tipo de una variable cuando no lo conocemos podemos usar type:

```python
x = 'Hola'
print(type(x)) #para obtener el tipo de dato de x, en este caso string
```

## Constantes en Python

A diferencia de otros lenguajes, en Python no existe un tipo específico para definir una constante, se usan convenciones.
Python no impide cambiar el valor de una variable, pero podemos seguir las siguiente convención al declarar el nombre de una variable en mayúsculas y con ello indicamos que el valor de esta variable NO debe ser modificado una vez inicializada la variable, y tratarse como una constante.

``` python
# Sintaxis para uso de constantes 
NOMBRE_CONSTANTE = valor

# Ejemplos de constantes 
PI = 3.14159
MENSAJE_ERROR = 'Usuario Inválido'
NOMBRE_USUARIO_VALIDO = 'admin'
```

## Manejo de cadenas

Una cadena o string es un tipo de dato que se utiliza para almacenar una secuencia de caracteres.
Las cadenas se deben encerrar entre comilla doble o simple.
Los caracteres pueden ser letras, números, símbolos o espacios.

```python
#Cadenas en Python
cadena1 = "Hola Mundo"
```

### Detalle de una Cadena

Los caracteres de una cadena están indexados de manera secuencial.
Por lo tanto, podemos acceder a cada caracter indicando el índice del caracter que deseamos recuperar.

### Inmutabilidad de una cadena

Una vez que se crea una cadena, los caractéres dentro de ella no pueden ser modificados.
Si deseamos modificar una cadena entonces tenemos que crear una nueva cadena.
Las cadenas no se pueden modificar, son inmutables.

### Caracteres Especiales

Las cadenas pueden incluir caracteres especiales.
Estos caracteres se introducen usando el carcter de diagonal invertida ('\'). Ej:

- Nueva linea: '\n' --> Inserta un salto de linea.
- Tabulacion: '\t' --> Inserta un tabulador horizontal, útil para alinear texto.
- Comilla Simple: '\'' --> Permite incluircomillas simples en una cadena delimitada por comillas simples.
- Comilla Doble: '\"' --> Permite incluir comillas dobles en una cadena delimitada por comillas dobles.
- Barra invertida: '\\' --> Permite incluir una barra invertida en la cadena

Existen más caracteres especiales, pero estos son los más esenciales.

### Concatenación de cadenas

La concatenación de cadenas es una operación que permite combinat dos o más cadenas para formar una nueva cadena.
En Python existen varias formas:

- Uso de operador +: El operador + es el más directo para concatenar cadenas simplemente tenemos que poner el operador + entre las cadenas que deseamos unir: concatenación = "Hola" + "Mundo"
- Uso de la función join: La función join nos permite unir tantas cadenas como necesitemos. Solo necesitamos pasar cada cadena a concatenar separadas por una coma: "".join(["cadena1", "cadena2", "cadena3"])

### Formateo de cadenas

Python ofrece varias maneras de formatear cadenas, que incluyen la capacidad de concatenar texto, variables e incluso dar otro tipo de formateo, como por ejemplo indicar el número de decimales a utilizar en el formato.

- f-string (Python 3.6+): Esta es la opción más recomendada, por ser la más sencilla, rápida y legible: resultado = f'Hola {variable}.'
- Método format. Es muy versátil y poderoso. Permite construir cadenas muy complejas: resultado = 'Hola {}'.format(variable)

### Métodos de Cadenas

Las cadenas en Python vienen con una serie de métodos útiles que facilitan su manipulación. Por ejemplo:

- upper(): Cambia las letras a mayúsculas
- lower(): Cambia las letras a minúsculas
- strip(): Elimina espacios en blanco al inicio y al final de la cadena.

### Obtener el largo de una cadena

Para obtener la longitud de una cadena, utilizamos la función incorporada len().
La funci+on len funciona con varios tipos de datos incluyendo cadenas, listas, etc.
Cuando se calcula el largo de una cadena se toman en cuenta todos los caracteres de una cadena, incluyendo espacios en blanco, caracteres especiales, etc.

```python
cadena1 = 'Hola Mundo!'
longitud = len(cadena1) #devuelve largo de 12
```

### Subcadenas en Python

Una subcadena es una parte de una cadena principal, y hay varias maneras de extraer subcadenas en Python.
Podemos extraerr subcadenas, buscarlas, reemplazarlas, entre otras operaciones:

- Extracción cadenas (Slicing): El slicing o segmentación permite indicar el índice de inicio y el indice final (sin incluir este último caracter): subcadena = cadena[inicio:fin].
- Buscar cadenas (find): El método find() devuelve el índice de la primera aparición de la subcadena. Si no encuentra la subcadena, devuelve -1.

```python
cadena = "Hola mundo"
posicion = cadena.find("mundo")
print(posicion) # imprime 5
```

- Reemplazar subcadenas (replace): El médodo replace() reemplaza una subcadena por otra dentro de una cadena principal.

```Python
cadena = 'Hola mundo'
nueva_cadena = cadena.replace('mundo', 'a todos')
print(nueva_cadena) #'Hola a todos'
```

- Extraer subcadenas separadas por separadores (split): la función split permite dividi8r una cadena en una lista de subcadenas basadas en un caracter separador ej:

```python
datos = 'Juan, 30, México'
lista = datos.split(',')
print(lista) # ['Juan', '30', 'México']
```

## Conversión de tipos de datos

La conversión de tipos de datos, también conocida como casting, es una técnica para manipular datos que no están en el tipo requerido.
Podemos hacer conversiones desde y hacia distintos tipos de datos:

- Convertir a entero: función int()
- Convertir a flotante: función float()
- Convertir a cadena: función str()
- Convertir a booleano: función bool()
