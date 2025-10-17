import pandas as pd
import requests
from io import StringIO

# url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"

def extract_csv_from_url(url:str) -> pd.DataFrame:
    response = requests.get(url) # request the url for data 
    response.raise_for_status #checks for the status of the url != 200 then bad
    csv_data = StringIO(response.text) # converts the csv text to a file like object
    return pd.read_csv(csv_data) # uses panda to reads the file like dataframes   

def extract_csv_from_api(api:str) -> pd.DataFrame:
    response = requests.get(api)
    response.raise_for_status
    csv_data = StringIO(response.text)
    return pd.read_csv(csv_data)

