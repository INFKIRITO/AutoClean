import argparse
import logging
from etl.extract import extract_csv_from_url
from etl.transform import clean_data
from etl.load import load_to_postgres
from etl.utils import setup_logger

def main():
    setup_logger()

    parser = argparse.ArgumentParser(description="Run ETL pipeline")
    parser.add_argument(
    '--source',
    type=str,
    default="https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv",
    help='Data Source URL'
    )
    parser.add_argument('--table', type=str, default="etl_winequality", help='DB Table name')
    args = parser.parse_args()

    # Fallback defaults
    source = args.source 
    table = args.table 

    logging.info(f"ETL started with source: {source} | table: {table}")

    try:
        # Extract
        df_raw = extract_csv_from_url(source)

        # Transform
        df_clean = clean_data(df_raw)

        # Load
        load_to_postgres(df_clean, table)
        logging.info("ETL job completed successfully!")

    except Exception as e:
        logging.exception(f"ETL job failed: {str(e)}")


if __name__ == "__main__":
    main()
