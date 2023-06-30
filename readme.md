# Entregas Data Engineering
PRIMER ENTREGA:
Script Python para extraer datos desde 'Series de tiempo' en formato JSON para su posterior guardado en un diccionario de Python. Luego se crea un dataframe con datos.

Script SQL para crear una tabla con las respectivas columnas del dataframe creado en Python.

El script SQL fue ejecutado con éxito en el esquema 'francogidaszewski_coderhouse' en la database 'data-engineer-database' alojada en Redshift.

SEGUNDA ENTREGA:
Se modifica el Script Python para extraer más datos, en este caso de 'Tasa politica monetaria'.
Luego se crean los respectivos DataFrames y se combinan ambos utilizando la columna de fecha para hacer la combinación.

Se realiza la conexión a Redshift con Psycopg y utilizando las credenciales en el archivo .env ('Fueron eliminadas antes del push'), para luego ejecutar la query en donde se crea la tabla 'indicadores_economicos' con las respectivas columnas del DF.
Se implementa el uso de distkey y sortkey que habia faltado en la primer entrega.

Luego se realiza una conexión a Redshift utilizando SQLAlchemy para cargar los datos en la tabla creada.

Falta realizar algun tipo de transformación en los datos debido a que aún no lo se hacer. Realizaré un commit cuando haga dichas transformaciones.
