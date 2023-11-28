import datetime
import time
#
# Variables globales pour stocker l'heure réglée et l'alarme
heure_reglee = None
alarme = None

def afficher_heure(heure_tuple):
    global heure_reglee
    now = datetime.datetime.now()
    heure_reglee = now.replace(hour=heure_tuple[0], minute=heure_tuple[1], second=heure_tuple[2])

def regler_alarme(heure_tuple):
    global alarme
    alarme = datetime.time(heure_tuple[0], heure_tuple[1], heure_tuple[2])

def verifier_alarme():
    global alarme
    now = datetime.datetime.now().time()
    if alarme and now >= alarme:
        print("\nAlarme ! Il est", alarme)
        # Désactiver l'alarme après déclenchement
        alarme = None

regler_alarme((10, 35, 0))

while True:
    if heure_reglee:
        delta = datetime.datetime.now() - heure_reglee
        now = heure_reglee + delta
    else:
        now = datetime.datetime.now()

    formatted_time = now.strftime("%H:%M:%S")
    print("\rHeure actuelle:", formatted_time, end="")

    verifier_alarme()

    time.sleep(1)
#