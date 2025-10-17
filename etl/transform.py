import pandas as pd

def clean_data(df:pd.DataFrame) -> pd.DataFrame:
    df.columns = [col.strip().lower().replace(" ","_") for col in df.columns]
    df = df.dropna(how="all") #drops rows with null values
    df = df.fillna(value={"column1":"N/A", "column2": 0}) #handles missing values
    df["data_column"] = pd.to_datetime(df["date_column"], errors='coerce')
    return df