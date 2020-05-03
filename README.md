# Covid-Integration
#### Repositório criado com o intuito de conter scripts utilizados para extrair, transformar e carregar dados sobre a pandemia do Coronavírus - Covid-19.

1.[Scraper_Covid](https://github.com/levisouuza/Covid-Integration/blob/master/Scraper_Covid/main.py) realiza a extração e inclusão em um determinado banco de dados(utilizei o PostgreSQL) dos dados do Covid-19 do Brasil e do mundo em tempo real. A fonte de dados é o site do [WolrdMeters](https://www.worldometers.info/coronavirus/) amplamente utilizado como fonte principal em tempo real de informação da pandemia. 

2.[DataCovidWorld](https://github.com/levisouuza/Covid-Integration/blob/master/DataCovidWorld/covid_world.py) realiza a clonagem do repositório da [Johns Hopkins University](https://github.com/CSSEGISandData/COVID-19) da Covid-19. Neste repositório contém dados históricos dos países vítimas do vírus. Além disso, o script realiza o tratamento de alguns arquivos com formatos diferentes. 

3.[BrasilCovid](https://github.com/levisouuza/Covid-Integration/blob/master/BrasilCovid/main.py) cria um bot utilizando a biblioteca Selenium simulando o acesso de um usuário a um repositório do [Kaggle](https://www.kaggle.com/unanimad/corona-virus-brazil) para download da fonte dados que contempla os números da Covid-19 do Brasil.
