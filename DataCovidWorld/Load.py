import psycopg2 as pg
import pandas as pd
import time


dir_inicial = '/home/levis/covidWorld/covid_brasil_full2.csv'

connection = pg.connect(
        host= 'localhost',
        database= 'postgres',
        user= 'postgres',
        password= '1123581321'
)

cursor = connection.cursor()

dataset = pd.read_csv(dir_inicial)

for row in range(len(dataset)):
    province = dataset['Province/State']
    country = dataset['Country/Region']
    last_update = dataset['Last Update']
    confirmed = dataset['Confirmed']
    deaths = dataset['Deaths']
    recovered = dataset['Recovered']
    dt_registro = dataset['Dt_registro']

    print((province), (country), (last_update), (confirmed), (deaths), (recovered), (dt_registro))
'''
    cursor.execute("insert into public.data_covid_world(province_state,country_region, last_update,confirmed, deaths, recovered, dt_registro)  values (%s,%s,%s,%s,%s,%s,%s)",
                    (province, country, last_update, confirmed, deaths, recovered, dt_registro))

    time.sleep(0.5)

    connection.commit()

    time.sleep(0.75)
'''
