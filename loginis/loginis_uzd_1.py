# ; 1 užduotis
# ; Sukurti funkcijas, kurios:

# ; Gražintų visų paduotų skaičių sumą (su *args argumentu)
# ; Gražintų paduoto skaičiaus šaknį (panaudoti math.sqrt())
# ; Gražintų paduoto sakinio simbolių kiekį (su len())
# ; Gražintų rezultatą, skaičių x padalinus iš y
# ; Nustatyti standartinį logerį (logging) taip, kad jis:

# ; Saugotų pranešimus į norimą failą
# ; Saugotų INFO lygio žinutes
# ; Pranešimai turi būti tokiu formatu: data/laikas, lygis, žinutė
# ; Kiekviena funkcija turi sukurti INFO lygio log pranešimą apie tai, ką atliko, pvz.:

# ; logging.info(f"Skaiciu {args} suma lygi: {sum(args)}")
# ; Paleisti kiekvieną funkciją su norimais argumentais


import math

import logging
logging.basicConfig(filename="uzduotis1_23_9.log", level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

def skaiciu_suma(*args):
    logging.info(f"Skaiciu {args} suma lygi: {sum(args)}")
    return sum(args)

def saknis(skaicius):
    logging.info(f"Skaiciaus {skaicius} saknis lygi {math.sqrt(skaicius)}")
    return math.sqrt(skaicius)

def simboliu_kiekis(tekstas):
    logging.info(f"Sakinio {tekstas} ilgis lygus {len(tekstas)} simboliu")
    return len(tekstas)

def dalyba(a,b):
    logging.info(f"{a} padalinta is {b} lygu {a / b}")
    return a/b


print(skaiciu_suma(4,54,2,3,6))
print(saknis(9))
print(simboliu_kiekis("Hello, how are you?"))
print(dalyba(20,5))
