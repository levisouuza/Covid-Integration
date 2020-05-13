
from Scripts.CovidWorld import Extract, Transform
import os
import time
import re
from datetime import datetime, timedelta

dir_initial = r'C:\Users\levis\Documents\Covid'
format_dif = list()

dt_ini = datetime.now().date() - timedelta(days=5)
dt_ini.strftime('%m-%d-%Y')


for dates in Extract.gera_datas(dt):
    if os.path.exists(os.path.join(dir_initial,f'{dates}.csv')):
        os.remove(os.path.join(dir_initial,f'{dates}.csv'))

time.sleep(1)

Extract.extract_git(dir_initial,dt)

time.sleep(2)

if os.path.exists(dir_initial):
    for arq in os.listdir(dir_initial):

        # Condição que verifica o formato dos arquivo e direciona para sua respectiva estrutura de dados.
        if re.search('csv', arq):

            if arq[:2] == '03' and arq[3:5] >= '22' and arq[6:10] == '2020':
                format_dif.append(arq)
            elif arq[:2] >= '04' and arq[6:10] >= '2020':
                format_dif.append(arq)

    # transformação e carga no diretório master dos arquivos com formato distinto.
    Transform.trans_arquivos(dir_initial, format_dif, dir_initial)

