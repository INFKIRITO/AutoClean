import argparse
from etl.extract import extract_csv_from_api
from etl.extract import extract_csv_from_url
from etl.transform import clean_data
from etl.load import load_to_postgres
