
from selenium.webdriver import Chrome
import time
import gzip
import shutil
import os

def extracao():

    driver = Chrome()
    driver.get('https://data.brasil.io/dataset/covid19/caso_full.csv.gz')
    time.sleep(2)
    driver.quit()

def descompactar(arq):

    if os.path.exists(arq):
        with gzip.open(arq, 'rb') as entrada:
            with open('caso_full.csv', 'wb') as saida:
                shutil.copyfileobj(entrada, saida)

    shutil.move(r'C:\Users\26497\PycharmProjects\Analytics\venv\Scripts\caso_full.csv',
                r'C:\Users\26497\Downloads')

    os.remove(arq)
