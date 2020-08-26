# Covid-Integration-Brazil
#### Repositório criado com o intuito de conter scripts utilizados para extrair e carregar dados sobre a pandemia do Coronavírus - Covid-19 do Brasil.
##### Sobre os scripts:

1.[Scraper_Covid](https://github.com/levisouuza/Covid-Integration-Brazil/blob/master/Scraper_Covid/main_real_time.py) realiza a extração e inclusão em um determinado banco de dados(utilizei o PostgreSQL) dos dados do Covid-19 do Brasil e do mundo em tempo real. A fonte de dados é o site do [WolrdMeters](https://www.worldometers.info/coronavirus/), amplamente utilizado para informações em tempo real sobre a pandemia.

2.[brasil-integration-covid](https://github.com/levisouuza/Covid-Integration-Brazil/blob/master/brasil-integration-covid/main.py) cria um bot utilizando a biblioteca Selenium simulando o acesso de um usuário a um repositório do [Brasil.IO](https://brasil.io/home/) para download da fonte dados que contempla os números da Covid-19 do Brasil.
