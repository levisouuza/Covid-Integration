
from selenium import webdriver
import shutil
import gzip
import time
import os
import re


def extract(dir):
    driver = webdriver.Chrome()

    driver.get('https://data.brasil.io/dataset/covid19/_meta/list.html')

    time.sleep(3)

    download = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/table/tbody/tr[4]/td[1]/a')

    time.sleep(1)

    download.click()

    time.sleep(3)

    while True:
        pass
        if not re.search('gz.crdownload', str(os.listdir(dir))):
            driver.quit()
            break


def descompactar(dir):

    arq = os.path.join(dir,'caso_full.csv.gz')

    with gzip.open(arq, 'rb') as entrada:
        with open(os.path.join(dir,'caso_full.csv'), 'wb') as saida:
            shutil.copyfileobj(entrada, saida)

    os.remove(os.path.join(dir,'caso_full.csv.gz'))
