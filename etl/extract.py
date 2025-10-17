import pandas as pd
import requests
from io import StringIO
import logging

def extract_csv_from_url(url: str) -> pd.DataFrame:
    logging.info(f"Downloading data from {url}")
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        csv_data = StringIO(response.text)
        df = pd.read_csv(csv_data)
        logging.info(f"Downloaded {len(df)} rows, {len(df.columns)} columns")
        return df
    except Exception as e:
        logging.exception(f"Failed to download CSV: {str(e)}")
        raise
