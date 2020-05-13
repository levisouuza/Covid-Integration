import os
import re
import shutil
import pandas as pd
from datetime import datetime
import time

format_dif = list()

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
        arq.rename(columns={'Lat': 'Latitude','Long_':'Longitude', 'Country_Region':'Country/Region','Province_State': 'Province/State'}, inplace=True)
        new_file = arq[['Province/State', 'Country/Region', 'Last_Update', 'Confirmed', 'Deaths', 'Recovered','Latitude','Longitude']]

        new_file.to_csv(os.path.join(dir_final,i), index=False)


def verification(dir_initial, dir_final):
    '''
    Função que irá extrair os dados do diretório local e enviará para seu diretório destino.

    :param dir_initial: Diretório que terá os arquivos em que será armazenado o repositório local do github que será clonado.
    :param dir_final: Diretório que irá receber os novos arquivos.
    '''
    if os.path.exists(dir_initial):
        for arq in os.listdir(dir_initial):

            # Condição que verifica o formato dos arquivo e direciona para sua respectiva estrutura de dados.
            if re.search('csv', arq):

                if arq[:2] == '03' and arq[3:5] >= '22' and arq[6:10] == '2020':
                    format_dif.append(arq)
                elif arq[:2] >= '04' and arq[6:10] >= '2020':
                    format_dif.append(arq)

        # transformação e carga no diretório master dos arquivos com formato distinto.
        trans_arquivos(dir_initial, format_dif, dir_final)
        return print('Arquivos extraídos e transformados com sucesso')

    else:
        print('Diretório não encontrado.')








