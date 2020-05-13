
from Scripts.DataCovidWorld import Extract, Transform
import os
import time
import re
from datetime import datetime, timedelta
import schedule

dir_initial = r'C:\Users\levis\Documents\Covid'
format_dif = list()

dt_ini = datetime.now().date() - timedelta(days=5)
dt = dt_ini.strftime('%m-%d-%Y')



def world_covid(directory):

    if not os.path.exists(directory):
        os.makedirs(directory)

    for dates in Extract.gera_datas(dt):
        if os.path.exists(os.path.join(directory,f'{dates}.csv')):
            os.remove(os.path.join(directory,f'{dates}.csv'))

    time.sleep(1)

    Extract.extract_git(directory,dt)

    time.sleep(2)

    if os.path.exists(directory):
        for arq in os.listdir(directory):

            # Condição que verifica o formato dos arquivo e direciona para sua respectiva estrutura de dados.
            if re.search('csv', arq):

                if arq[:2] == '03' and arq[3:5] >= '22' and arq[6:10] == '2020':
                    format_dif.append(arq)
                elif arq[:2] >= '04' and arq[6:10] >= '2020':
                    format_dif.append(arq)

        # transformação e carga no diretório master dos arquivos com formato distinto.
        Transform.trans_arquivos(directory, format_dif, directory)


def main():

    world_covid(dir_initial)

    time.sleep(5)

    now = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    print(f'Task finalizada às {now} com sucesso.')

#schedule.every(1).day.at('00:00').do(main)
schedule.every(1).day.at('17:45').do(main)

while True:
    schedule.run_pending()
    time.sleep(30)

main()

exit()
