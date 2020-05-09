import os
import re
import shutil
import git
from datetime import datetime
import time
from Scripts.DataCovidWorld.Transform import Transform

format_one = list()
format_two = list()

old_format = list()

dh_integracao = datetime.now().strftime('%d%m%Y%H%M%S')

class Worldcovid():

    def gitt(directory, rep_git, url_git, hist):
        '''
        Função que Realiza a clonagem de um repositório do github para um repositório local.

        :param directory: Diretório que terá os arquivos em que será armazenado o repositório local do github que será clonado.
        :param rep_git: Repositório local que será armazenado o github clonado.
        :param url_git: Url repositório github.
        :param hist: folder que será armazenado os históricos dos arquivos baixados.
        '''
        try:
            #Caso o repositório não exista no host local
            if not os.path.exists(rep_git):
                git.Git(directory).clone(url_git)
                return print('Repositório clonado com sucesso.')

            #Caso o repositório já exista, é transferido para uma pasta de histórico e, posteriormente, é clonado o novo.
            else:
                new_path = rep_git + f' - {dh_integracao}'
                os.rename(rep_git, new_path)
                shutil.move(new_path, hist)
                time.sleep(2)
                git.Git(directory).clone(url_git)

                return print('Repositório clonado com sucesso.')
        except:
            return print('Erro na clonagem do repositório.')


    def delete(type, directory):
        '''
        Função que tem objetivo de excluir diretórios ou arquivos.

        :param type: Tipo de exclusão: d -> Diretórios ou a -> arquivos.
        :param directory: Diretório que será excluído ou terá arquivos excluídos.
        '''
        if type == 'd':
            if os.path.exists(directory):
                shutil.rmtree(directory)
                return print('Diretório excluído com sucesso!')
            else:
                return print('Erro na exclusão do diretório.')

        elif type == 'a':
            if os.path.exists(directory):
                for arq in os.listdir(directory):
                    arq = os.path.join(directory, arq)
                    os.remove(arq)

                return print('Arquivo(s) excluídos com sucesso')
            else:
                return print('Erro na exclusão dos arquivos.')

    def extract(dir_initial, dir_final):
        '''
        Função que irá extrair os dados do diretório local e enviará para seus diretórios destino.

        :param dir_initial: Diretório que terá os arquivos em que será armazenado o repositório local do github que será clonado.
        :param dir_final: Diretório que irá receber os novos arquivos.
        '''
        if os.path.exists(dir_initial):
            for arq in os.listdir(dir_initial):

                #Condição que verifica o formato dos arquivo e direciona para sua respectiva estrutura de dados.
                if re.search('csv', arq):

                    if arq[:2] == '03' and arq[3:5] >= '22' and arq[6:10] == '2020':
                        format_two.append(arq)
                    elif arq[:2] >= '04' and arq[6:10] >= '2020':
                        format_two.append(arq)
                    else:
                        format_one.append(arq)

            #inclusão dos arquivos com formato padrão no diretório master.
            for one in format_one:
                old_path = os.path.join(dir_initial,one)
                old_format.append(old_path)

            for i in old_format:
                shutil.copy(i,dir_final)

            #transformação e carga no diretório master dos arquivos com formato distinto.
            Transform.trans_arquivos(dir_initial, format_two,dir_final)
            return print('Arquivos extraídos e transformados com sucesso')

        else:
            print('Diretório não encontrado.')








