#WilliamAdamDaothid
#WeatherAuguaryDb
#CNE340 Fall 2023
#For this project we cloned a Github Repository added a Weather API Showed a graph for
#Temperature Wind Speed and Precipitation

import pandas  as pd
import requests
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from sqlalchemy import text
hostname = "127.0.0.1"
username = "root"
pwd = ""
dbname = "WeatherAuguaryDb"

api_url = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/seattle%20WA?unitGroup=metric&key=KFH6UKWSHD64C8H57RYLREY4R&contentType=json'
response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    weather_df = pd.DataFrame(data['days'])
    weather_df['datetime'] = pd.to_datetime(weather_df['datetime'])
    weather_df['windspeedkm'] = weather_df['windspeed'] * 1.60934


    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 15))

# Plot temperature
    ax1.plot(weather_df['datetime'], weather_df['tempmax'], label='Max Temperature')
    ax1.plot(weather_df['datetime'], weather_df['tempmin'], label='Min Temperature')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Temperature (°C)')
    ax1.set_title('Weather Trends in Seattle - Temperature')
    ax1.legend()
    ax1.grid(True)

# Plot wind speed
    ax2.plot(weather_df['datetime'], weather_df['windspeedkm'], color='green', label='Wind Speed (km/h)')
    ax2.set_xlabel('Date')
    ax2.set_ylabel('Wind Speed (km/h)')
    ax2.set_title('Weather Trends in Seattle - Wind Speed')
    ax2.legend()
    ax2.grid(True)

# Plot precipitation
    ax3.bar(weather_df['datetime'], weather_df['precip'], color='blue', label='Precipitation')
    ax3.set_xlabel('Date')
    ax3.set_ylabel('Precipitation')
    ax3.set_title('Weather Trends in Seattle - Precipitation')
    ax3.legend()
    ax3.grid(True)

    plt.tight_layout()
    plt.show()
    engine = create_engine(f"mysql+pymysql://{username}:{pwd}@{hostname}/{dbname}")
    connection = engine.connect()

    #table_name = 'weather_data'
    #weather_df.to_sql(table_name, con=engine, if_exists='replace', index=False)
    #connection.close()