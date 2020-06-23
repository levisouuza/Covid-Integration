import pandas as pd
import time
import os

def transform(dir):

    data_raw = pd.read_csv(os.path.join(dir,'caso_full.csv'))

    data_raw.drop(['city', 'city_ibge_code', 'is_last', 'is_repeated', 'last_available_confirmed_per_100k_inhabitants', 'last_available_date',
                    'last_available_death_rate','order_for_place'], axis= 1, inplace = True)

    data_raw.rename(columns = {'last_available_confirmed': 'confirmed', 'last_available_deaths': 'deaths'}, inplace=True)

    dataState = data_raw.query("place_type== 'state'")

    #dataState.rename(columns = {'last_available_confirmed': 'confirmed', 'last_available_deaths': 'deaths'}, inplace=True)

    data_transformed = dataState[['date', 'epidemiological_week', 'estimated_population_2019', 'place_type', 'state', 'confirmed', 'new_confirmed', 'deaths', 'new_deaths']]

    os.remove(os.path.join(dir,'caso_full.csv'))

    time.sleep(2)

    data_transformed.to_csv((os.path.join(dir,'caso_full.csv')), index=False)
