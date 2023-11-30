#WilliamAdamDaothid
#WeatherAuguaryDb
#CNE340 Fall 2023

import pandas  as pd
import requests
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from sqlalchemy import text
hostname = "127.0.0.1"
username = "root"
pwd = ""
dbname = "WeatherAuguaryDb"

engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
.format(host=hostname, db=dbname, user=username, pw=pwd))
api_url = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/seattle%20WA?unitGroup=metric&key=KFH6UKWSHD64C8H57RYLREY4R&contentType=json'
response = requests.get(api_url)
if response.status_code == 200:
    data = response.json()
    weather_df = pd.DataFrame(data['days'])
    weather_df['datetime'] = pd.to_datetime(weather_df['datetime'])
plt.figure(figsize=(10, 6))
plt.plot(weather_df['datetime'], weather_df['tempmax'], label='Max Temperature')
plt.plot(weather_df['datetime'], weather_df['tempmin'], label='Min Temperature')
plt.xlabel('Date')
plt.ylabel('Temperature (°F)')
plt.title('Weather Trends in Seattle')
plt.legend()
plt.grid(True)
plt.show()