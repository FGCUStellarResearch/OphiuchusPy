import os
import time
import datetime

numbs = ['1','2','3','4','5','6','7','8','9','10',
         '11','12','13','14','15','16','17','18','19','20',
         '21','22','23','24','25','26','27','28','29','30',
         '31','32','33','34','35','36','37','38','39','40',
         '41','42','43','44','45','46','47','48']

starte = time.time()

for s in numbs:
    start = time.time()
    shellcommand = "sh " + s + ".txt"
    removcommand = "rm " + s + ".txt"

    os.system(shellcommand)
    print s
    elapse = time.time() - start
    print elapse
    os.system(removcommand)
    
    timesec = time.time()
    timestamp = datetime.datetime.fromtimestamp(timesec).strftime('%Y-%m-%d %H:%M:%S')
    print timestamp

totale = time.time() - starte
print totale
