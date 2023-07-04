import pandas as pd
import requests
import urllib.parse

#Obtener datos de la API y crear los DataFrames
def get_api_call(ids, **kwargs):
    API_BASE_URL = "https://apis.datos.gob.ar/series/api/"
    kwargs["ids"] = ",".join(ids)
    return "{}{}?{}".format(API_BASE_URL, "series", urllib.parse.urlencode(kwargs))

#Obtener datos del tipo de cambio
tipo_cambio_id = "168.1_T_CAMBIOR_D_0_0_26"
tipo_cambio_api_call = get_api_call([tipo_cambio_id], start_date="2016-10-30")
tipo_cambio_data = requests.get(tipo_cambio_api_call).json()

#Obtener datos de TPM
tpm_id = "89.2_TS_INTE_PM_0_D_16"
tpm_api_call = get_api_call([tpm_id], start_date="2016-10-30")
tpm_data = requests.get(tpm_api_call).json()

#Convertir los datos del tipo de cambio en un DataFrame
tipo_cambio_df = pd.DataFrame(tipo_cambio_data["data"], columns=["fecha", "tipo_de_cambio"])
#print(tipo_cambio_df)

#Convertir los datos del tpm en un DataFrame
tpm_df = pd.DataFrame(tpm_data["data"], columns=["fecha", "tasa_politica_monetaria"])
#print(tpm_df)

#Combinar los DataFrames en uno solo
combined_df = pd.merge(tipo_cambio_df, tpm_df, on="fecha", how="inner")
#print(combined_df)
