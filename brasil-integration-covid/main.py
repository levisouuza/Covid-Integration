
from extract.extract import extract, descompactar
from datetime import datetime
from transform.transform import transform
import schedule
import time

directory = '/home/levis/Downloads'

dh_inicio = datetime.now()

extract(directory)

time.sleep(1)

descompactar(directory)

time.sleep(1)

transform(directory)

dh_final = datetime.now()

print(f'O ETL iniciou às {dh_inicio} e finalizou às {dh_final}.')
