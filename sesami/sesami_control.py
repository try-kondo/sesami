# Sesami WebAPi

from io import open
from pysesame2 import get_sesames

import dir_path


def get_webapi():
    path = dir_path.api_path()
    with open(path) as f:
	    s = f.read()

    return s.rstrip()


def sesami_status():
    webapi = get_webapi()
    sesames = get_sesames(webapi)
    sesame = sesames[0]

    if sesame.get_status()['locked'] == True:
        lock = "Lock"
    elif sesame.get_status()['locked'] == False:
        lock = "Unlock"

    print 'Battery    : ', sesame.get_status()['battery']
    print 'Locked     : ', lock
    print 'Responsive : ', sesame.get_status()['responsive']


def sesami_lock():
    webapi = get_webapi()
    sesames = get_sesames(webapi)
    sesame = sesames[0]

    if sesame.get_status()['responsive'] == True:
        if sesame.get_status()['locked'] == False:
            sesame.lock()
            print("Sesami Lock Complete!!")


def sesami_unlock():
    webapi = get_webapi()
    sesames = get_sesames(webapi)
    sesame = sesames[0]

    if sesame.get_status()['responsive'] == True:
        if sesame.get_status()['locked'] == True:
            sesame.unlock()
            print("Sesami Unlock Complete!!")

