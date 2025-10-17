import pandas as pd
from sqlalchemy import create_engine
from etl.config import POSTGRES_URL
import logging

def load_to_postgres(df: pd.DataFrame, table_name: str):
    logging.info(f"Loading data into table: {table_name}")
    try:
        engine = create_engine(POSTGRES_URL)
        with engine.begin() as conn:
            df.to_sql(table_name, con=conn, if_exists='append', index=False)
        logging.info("Data loaded successfully!")
    except Exception as e:
        logging.exception(f"Failed to load data into Postgres: {str(e)}")
        raise
