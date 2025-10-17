from sqlalchemy import create_engine
import pandas as pd

def load_to_postgres(df: pd.DataFrame, table_name: str, db_url: str):
    engine  create_engine