import pandas as pd
import logging

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    logging.info("Cleaning data...")

    # Standardize column names
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    # Drop rows where all values are null
    df = df.dropna(how="all")

    # Fill missing values
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].fillna("N/A")
        else:
            df[col] = df[col].fillna(0)

    # Parse date columns automatically
    for col in df.columns:
        if "date" in col:
            df[col] = pd.to_datetime(df[col], errors='coerce')

    logging.info(f"Cleaned data: {len(df)} rows, {len(df.columns)} columns")
    return df
