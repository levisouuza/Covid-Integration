
# __init__.py
# -*- coding: UTF-8 -*-

import os
import time
import re
from datetime import datetime, timedelta
import schedule
import pandas as pd
import Extract
import Transform
import Delete


dir_inicial = '/home/levis/covidWorld'
format_dif = list()

dt_ini = datetime.now().date() - timedelta(days=3)
dt = dt_ini.strftime('%m-%d-%Y')

carga_inicial = 'S'


def world_covid(directory):

    #criando diretório para persistir os arquivos csv.
    if not os.path.exists(directory):
        os.makedirs(directory)

    #excluindo arquivos caso existam.
    for dates in Extract.gera_datas(dt):
        if os.path.exists(os.path.join(directory,f'{dates}.csv')):
            os.remove(os.path.join(directory,f'{dates}.csv'))

    time.sleep(1)

    #método responsável por criar requests do repositório John Hopkins
    Extract.extract_git(directory, dt)

    time.sleep(2)

    #verificando arquivos que estão em formatos diferentes e padronizando-os para um único formato.
    if os.path.exists(directory):
        for arq in os.listdir(directory):

            # Condição que verifica o formato dos arquivo e direciona para sua respectiva estrutura de dados.
            if re.search('csv', arq):

                if arq[:2] == '03' and arq[3:5] >= '22' and arq[6:10] == '2020':
                    format_dif.append(arq)
                elif arq[:2] >= '04' and arq[6:10] >= '2020':
                    format_dif.append(arq)

        #método para transformação das features
        Transform.trans_arquivos(directory, format_dif, directory)

    time.sleep(1)

    #método que irá criar a data das ocorrências dos datasets
    Transform.feature_date(dir_inicial)

    time.sleep(2)

    #criação dataset full

    if carga_inicial == 'S':
        Transform.load_dataset(dir_inicial, carga_inicial)

    elif carga_inicial == 'N':
        Transform.load_dataset(dir_inicial, carga_inicial, Extract.gera_datas(dt))

    time.sleep(2)

    Delete.del_arq(dir_inicial)

'''def main():

    world_covid(dir_initial)

    time.sleep(5)

    now = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    print(f'Task finalizada às {now} com sucesso.')

#schedule.every(1).day.at('00:00').do(main)
schedule.every(1).day.at('20:43').do(main)

while True:
    schedule.run_pending()
    time.sleep(30)

main()

exit()'''

world_covid(dir_inicial)
