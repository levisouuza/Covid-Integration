
import pandas as pd
import os

def trans_arquivos(dir_inicial, arquivos,dir_final):
    '''
    Função que transformará os datasets do covid-19 que estão com formatos diferentes para um formato padrão.

    :param dir_inicial: diretório de origem dos arquivos que serão transformados.
    :param arquivos:  lista que terá todos arquivos que serão transformados.
    :param dir_final:  diretório destino dos arquivos que serão transformados
    '''
    for i in arquivos:
        file = os.path.join(dir_inicial, i)
        arq = pd.read_csv(file)

        arq.drop(columns=['FIPS','Admin2','Active','Combined_Key'], inplace=True)
        arq.rename(columns={'Lat': 'Latitude','Long_':'Longitude', 'Country_Region':'Country/Region'}, inplace=True)
        new_file = arq[['Province_State', 'Country/Region', 'Last_Update', 'Confirmed', 'Deaths', 'Recovered','Latitude','Longitude']]

        new_file.to_csv(os.path.join(dir_final,i), index=False)
