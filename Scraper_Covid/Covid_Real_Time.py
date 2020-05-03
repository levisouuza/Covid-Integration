#COVID REAL TIME BRASIL E MUNDO

from selenium import webdriver
from datetime import datetime
from time import sleep
import psycopg2

conexao = psycopg2.connect(
    host= host,
    database= database,
    user= user,
    password= password
)

cursor = conexao.cursor()

class Coronavirus():

    # função que realiza a abertura e retorno de dados do site worldmeters
    def getdata(site, hora):
        '''
        Função scraper que realiza o download do arquivo selecionado.
        :param site: Site em que o scraper vai funcionar.
        :param hora:  Data e hora do início do processo que será incluída no banco de dados.
        '''
        driver = webdriver.Chrome()

        # get para abrir o site
        driver.get(site)

        sleep(2)

        # objeto que encontra a tabela principal de dados
        table = driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]')

        #keys = ["//td[contains(.,'Brazil')]"]
        keys = ["//td[contains(.,'Brazil')]", "//td[contains(.,'World')]"]

        dados = list()
        #objeto que guardar caminho dos dados na pagina html
        sleep(1)

        inserts = 0

        while inserts < 2:

            for var in keys:
                country_element = table.find_element_by_xpath(var)
                row = country_element.find_element_by_xpath("./..")
                data = row.text.split(" ")
                #print(type(data))

                #objetos e tratamentos de dados
                pais = data[0]

                total_cases = data[1].replace(',','')
                total_cases = int(total_cases)

                new_cases = data[2].replace(',','.')

                total_deaths = data[3].replace(',','')
                total_deaths = int(total_deaths)

                new_deaths = data[4].replace(',','.')

                total_recovered = data[5].replace(',','')
                total_recovered = int(total_recovered)

                actives_cases = data[6].replace(',','')
                actives_cases = int(actives_cases)

                serius_critical = data[7].replace(',','')
                serius_critical = int(serius_critical)

                # data/hora da integração scraper
                feature_date = hora.strftime('%d/%m/%Y %H:%M:%S')
                dh_integracao = feature_date

                #print(pais,total_cases,new_cases,total_deaths,new_deaths,total_recovered,actives_cases,serius_critical,dh_integracao)

                sleep(1)

                cursor.execute("delete from public.covid_real_time where pais = %s", (pais,))

                conexao.commit()

                #sleep(1)

                cursor.execute(
                   "insert into public.covid_real_time(pais, total_cases, new_cases, total_deaths, new_deaths, total_recovered,actives_cases, serius_critical,dh_integracao) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                  (pais, total_cases, new_cases, total_deaths, new_deaths, total_recovered, actives_cases, serius_critical,dh_integracao))

                sleep(1)

                conexao.commit()

                sleep(1)

                inserts += 1

            driver.quit()
