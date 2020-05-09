
import time
import os
from datetime import datetime
from Scripts.CovidWorldHist.support import Worldcovid
import schedule

dir_initial = r'C:\Repositories\GitPython\COVID-19\csse_covid_19_data\csse_covid_19_daily_reports'
dir_final = r'C:\Users\levis\Documents\BaseCovid\COVID-19-master\csse_covid_19_data\csse_covid_19_daily_reports'
rep_master = r"C:\Repositories\GitPython"
rep_git = r"C:\Repositories\GitPython\COVID-19"
url_git = "https://github.com/CSSEGISandData/COVID-19.git"
hist = r'C:\Repositories\GitPython\Historico'

dh_integracao = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

def world_covid():
    #Clonagem repositório github John Hopkins
    Worldcovid.git(rep_master, rep_git, url_git, hist)

    time.sleep(2)

    #verificação de existência dos diretórios destinos.
    if not os.path.exists(dir_final):
        os.makedirs(dir_final)

    time.sleep(2)

    #Excluíndo arquivos antigos para recebimento dos arquivos novos dos diretórios destino, caso existam.
    Worldcovid.delete('a', dir_final)

    time.sleep(2)

    #Copiando arquivos do repositório local para diretórios destino.
    Worldcovid.extract(dir_initial, dir_final)

    time.sleep(2)

#Realizando o agendamento do script
'''schedule.every(1).day.at('14:08').do(world_covid)

while True:
    schedule.run_pending()
    time.sleep(30)


exit()
'''
world_covid()







