from selenium import webdriver
from time import sleep
import os
import shutil
import zipfile

class Brazilcovid():
    # função que realiza a abertura e retorno de dados do site worldmeters
    def getdata(user, passw):
        '''
        Função scraper que realiza o download do arquivo selecionado.
        :param user: Nome do usuário do site.
        :param password:  Senha do usuário do site.
        '''
        driver = webdriver.Chrome()

        # get para abrir o site
        driver.get('https://www.kaggle.com/account/login?phase=emailSignIn&returnUrl=https%3A%2F%2Fwww.kaggle.com%2Funanimad%2Fcorona-virus-brazil')

        sleep(2)

        #input username
        username = driver.find_element_by_xpath('/html/body/main/div/div[1]/div[1]/form/div[2]/div[1]/div[1]/div[1]/input')
        sleep(1)
        username.send_keys(user)

        sleep(2)

        # input password
        password = driver.find_element_by_xpath('/html/body/main/div/div[1]/div[1]/form/div[2]/div[2]/div[1]/div[1]/input')
        sleep(1)
        password.send_keys(passw)

        sleep(2)

        # sign page
        sign = driver.find_element_by_class_name('mdc-button__label')
        sleep(1)
        sign.click()

        sleep(2)

        # download archive
        download = driver.find_element_by_class_name('button__anchor-wrapper')
        sleep(1)
        download.click()

        sleep(5)
        driver.quit()

    def descompactar(zipp):
        '''
        Função que descompacta o arquivo zip.
        :param zip: Arquivo zip que será descompactado.
        '''
        if os.path.exists(zipp):

            zip = zipfile.ZipFile(zipp)
            dir = os.path.dirname(zipp)

            for name in zip.namelist():
                if not name.endswith('/'):
                    outfile = open(os.path.join(dir, name), 'wb')
                    outfile.write(zip.read(name))
                    outfile.close()

    def move_archive(arquivo_inicial, arquivo_final):
        '''
        Função que move o arquivo principal para o diretório final

        :param arquivo_inicial: Arquivo principal em seu diretório inicial que contém os dados do brasil sobre a covid-19.
        :param arquivo_final: Arquivo principal em seu diretório final que contém os dados do brasil sobre a covid-19.

        '''
        #Verifica se o arquivo já existe no diretório final  e realiza a sua exclusão, caso for verdadeiro.
        if os.path.exists(arquivo_final):
            os.remove(arquivo_final)

        sleep(1)
        # Verifica se o arquivo já existe no diretório inicial  e realiza a sua tranferência para o seu destino, caso for verdadeiro.
        if os.path.exists(arquivo_inicial):
            shutil.move(arquivo_inicial,
                       arquivo_final)

