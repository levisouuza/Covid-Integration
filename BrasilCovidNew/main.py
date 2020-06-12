
from Scripts.BrasilCovidNew import Extract
import time

zipp = r'C:\Users\26497\Downloads\caso_full.csv.gz'

Extract.extracao()

time.sleep(2)

Extract.descompactar(zipp)



