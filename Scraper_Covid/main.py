
from Scripts.Scraper_Covid.Covid_Real_Time import Coronavirus
from datetime import  datetime
import time
import schedule

web = 'https://www.worldometers.info/coronavirus/'

def main():

    Coronavirus.getdata(web, datetime.now())

    time.sleep(5)

    now = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    print(f'Task finalizada às {now} com sucesso.')

#agendamento do job
schedule.every(1).day.at('00:00').do(main)
schedule.every(1).day.at('07:00').do(main)

while True:
    schedule.run_pending()
    time.sleep(30)

#teste.Coronavirus.getdata()

main()

exit()

