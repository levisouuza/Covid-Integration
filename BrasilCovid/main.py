#funcao que realiza o agendamento e execução do bot
from Scripts.BrasilCovid.Extract.bot_covid_brasil import Brazilcovid
from time import sleep
from datetime import datetime
import schedule
import os
import sys

arq_inicial = r'C:\Users\usuario\Downloads\brazil_covid19.csv'
arq_final = r'C:\Users\usuario\Documents\brazil_covid19.csv'
zip = r'C:\Users\usuario\Downloads\corona-virus-brazil.zip'

def main():

    #funcao que cria o scraper e realiza o download do arquivo em questão.
    Brazilcovid.getdata(user,password)

    sleep(15)

    Brazilcovid.descompactar(zip)

    sleep(5)

    # excluindo o arquivo .zip que fizemos o download e o arquivo extra que também foi extraído.
    if os.path.exists(r'C:\Users\usuario\Downloads\corona-virus-brazil.zip'):
        os.remove(r'C:\Users\usuario\Downloads\corona-virus-brazil.zip')

    if os.path.exists(r'C:\Users\usuario\Downloads\brazil_covid19_cities.csv'):
        os.remove(r'C:\Users\usuario\Downloads\brazil_covid19_cities.csv')

    if os.path.exists(r'C:\Users\usuario\Downloads\brazil_covid19_macro.csv'):
	os.remove(r'C:\Users\usuario\Downloads\brazil_covid19_macro.csv')

    sleep(1)

    Brazilcovid.move_archive(arq_inicial, arq_final)

    sleep(1)

    now = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    print(f'Task realizada às {now} com sucesso.')

#agendando o job para determinado horário, uma vez por dia.
schedule.every(1).days.at('13:56').do(main)
schedule.every(1).days.at('14:00').do(main)

while True:
    schedule.run_pending()
    sleep(30)

exit()

