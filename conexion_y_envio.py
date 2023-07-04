import os
import psycopg2
from dotenv import load_dotenv
from extraccion_y_dataframe import combined_df
from sqlalchemy import create_engine

#Conexión
load_dotenv('.env')

host = os.getenv('AWS_REDSHIFT_HOST')
port = os.getenv('AWS_REDSHIFT_PORT')
dbname = os.getenv('AWS_REDSHIFT_DBNAME')
user = os.getenv('AWS_REDSHIFT_USER')
password = os.getenv('AWS_REDSHIFT_PASSWORD')
schema = os.getenv('AWS_REDSHIFT_SCHEMA')
table = 'indicadores_economicos'

conn = psycopg2.connect(
    host=host,
    port=port,
    dbname=dbname,
    user=user,
    password=password
)

#Creo tabla en el schema
cursor = conn.cursor()
cursor.execute(f"""
create table if not exists {schema}.indicadores_economicos (
    id INT NOT NULL,
    fecha DATE distkey,
    tipo_de_cambio decimal(10,2),
    tasa_politica_monetaria decimal(10,2)
) sortkey(fecha);
""")
conn.commit()
cursor.close()
print("Se realizó con éxito")

#Conexión con RedShift
engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}", echo=True)

#Cargo los datos en la tabla indicadores_economicos
try:
    with engine.connect() as conn:
        conn.execute(f"CREATE SCHEMA IF NOT EXISTS {schema};")
        combined_df.to_sql(table, conn, schema=schema, if_exists='replace', index=False, method='multi')
        print("Se cargaron los datos")
except Exception as e:
    print("Error en la carga", e)
    engine.dispose()
