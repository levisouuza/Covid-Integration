
import pandas as pd
import os

def trans_arquivos(dir_initial, arquivos,dir_final):
    '''
    Função que transformará os datasets do covid-19 que estão com formatos diferentes para um formato padrão.

    :param dir_inicial: diretório de origem dos arquivos que serão transformados.
    :param arquivos:  lista que terá todos arquivos que serão transformados.
    :param dir_final:  diretório destino dos arquivos que serão transformados
    '''
    for i in arquivos:
        file = os.path.join(dir_initial, i)
        arq = pd.read_csv(file)
        dataset = pd.DataFrame(data=arq, columns=arq.columns)

        dataset.rename(columns={'Lat': 'Latitude', 'Long_': 'Longitude', 'Country_Region': 'Country/Region',
                            'Province_State': 'Province/State', 'Last_Update': 'Last Update'}, inplace=True)

        os.remove(file)

        dataset.to_csv(file, index=False)


def feature_date(directory):
    '''
    Função que irá criar a data das ocorrências dos datasets

    :param directory: diretório em que será realizado a busca dos arquivos
    '''
    for arc in os.listdir(directory):
        file = os.path.join(directory, arc)
        arq = pd.read_csv(file)
        dataset = pd.DataFrame(data=arq, columns=arq.columns)

        dataset['Dt_registro'] = arc[:10]  # creating feature data registro = datas das notificações diárias

        new_file = dataset[
            ['Province/State', 'Country/Region', 'Last Update', 'Confirmed', 'Deaths', 'Recovered', 'Dt_registro']]

        new_file.to_csv(file, index=False)

