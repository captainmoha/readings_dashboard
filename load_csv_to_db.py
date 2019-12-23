import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.types import Integer, String, DateTime, Float

DB_URI = 'sqlite:///flaskapp/data.db'
CSV_PATH = 'task_data.csv'


def get_db_engine(URI):
    # create sqlalchemy database engine
    return create_engine(URI)

def get_csv_df(csv_path):
    # Load csv data into a dataframe
    csv_data = pd.read_csv(csv_path)
    csv_data.set_index(['id'], inplace=True)
    csv_data.index.name = None
    csv_data.columns.name = 'ID'

    return csv_data

def populate_db(csv_path, db_engine):

    # load dataframe contents into a database table called readings

    df = get_csv_df(csv_path)

    df.to_sql('readings',
                    db_engine,
                    if_exists='replace',
                    chunksize=500,
                    dtype={
                        'id': Integer,
                        'timestampe': DateTime,
                        'temprature': Float(precision=14),
                        'duration': String(50)

                    })



if __name__ == '__main__':
    populate_db(CSV_PATH, get_db_engine(DB_URI))
