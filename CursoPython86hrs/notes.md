# 'Universidad Python'

## Hola mundo con python

Es el primer programa que se hace para conocer un lenguaje

```
print("Hola mundo!")
```

## Variables en python

Una variable es un nombre que almacena valor guardado en la memoria de la pc. En python son dinámicas, cambian su 
tipo de acuerdo a lo que se le almacena.

Las variables pueden cambiar su contenido de acuerdo a la ejecución y modificaciones en el mismo programa, por ello 
su nombre, variables.

Para cambiar o modificar el valor de una variable solo es necesario volver a llamarla e igualarla a un nuevo valor.

```
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

Convenciones y buenas prácticas
- snake case: Es recomendable usar la notación de snake case, es decir, palabras en minúsculas separadas por guión 
bajo. Ej. nombre_usuario, nombre_completo, etc.
- Nombres descriptivos: Los nombres de las variables deben reflejar el contenido de la variable. Ej. no usar e, sino 
edad. No usar n, sino nombre, etc.
- Evitar nombres de un sólo caracter, ya que no son descriptivos y pueden ser confusos. 

### Tipos de datos

Python es un lenguaje de tipado dinámico, por lo que no hay necesidad de indicar el tipo de la variable al momento de 
declararla.

Los valores que pueden almacenar las variables son de distintos tipos, como:
- Números (int): Son números sin la parte decimal, Ej 42, -109.
- Números con punto flotante (float): ej 3.141569, -0.001.
- Cadenas de texto (str): secuencia de caracteres, ej 'Hola mundo'.
- Booleanos: almacenan un valor lógico de verdadero (True) o falso (False), este tipo de valores se usan para 
controlar el flujo de un programa.
- None: Es un tipo especial en Python que representa ausencia de valor.

## Constantes en Python


