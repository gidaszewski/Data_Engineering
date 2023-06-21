import pandas as pd
import requests
import urllib.parse

def get_api_call(ids, **kwargs):
    API_BASE_URL = "https://apis.datos.gob.ar/series/api/"
    kwargs["ids"] = ",".join(ids)
    return "{}{}?{}".format(API_BASE_URL, "series", urllib.parse.urlencode(kwargs))

api_call = get_api_call(["168.1_T_CAMBIOR_D_0_0_26"], start_date="2022-10-30")

data = requests.get(api_call).json()
#print(data)

time_series = data["data"]

df = pd.DataFrame(time_series, columns=["date", "tipo_de_cambio"])
print(df)