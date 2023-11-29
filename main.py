#WilliamAdamDaothid
#WeatherAuguaryDb
#CNE340 Fall 2023

import json
import time
import html2text
import mysql.connector
import requests
from datetime import datetime
import pandas as pd

API_URL = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/seattle%20WA?unitGroup=metric&key=KFH6UKWSHD64C8H57RYLREY4R&contentType=json'


def connect_to_sql():
    conn = mysql.connector.connect(user='root', password='',
                                   host='127.0.0.1', database='WeatherAuguaryDb')
    return conn

def create_tables(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS weather_data (
            id INT PRIMARY KEY auto_increment,
            date DATETIME,
            temp Float,
            humidity FLOAT,
            precip FLOAT,
            windspeed FLOAT,
            conditions VARCHAR 500
            );''')

def query_sql(cursor, query):
    cursor.execute(query)
    return cursor
def fetch_and_insert_weather_data():
    conn = connect_to_sql()
    cursor = conn.cursor()

    # Fetch data from the API
    response = requests.get(API_URL)

    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print('Failed to retrieve data:', response.status_code)
        return None
def process_data_and_insert(data):
    if data:
        days_data = data.get('days', [])
        df = pd.DataFrame(days_data)
        print(df.head())
        conn_string = 'mysql+pymysql://root:@localhost/WeatherAuguaryDb'  # Adjust connection string as needed
        engine = create_engine(conn_string)

        df.to_sql('weather_data', con=engine, if_exists='append', index=False)
    else:
        print('No data to process.')

    weather_data = fetch_weather_data()
    process_data_and_insert(weather_data)

    conn.close()
