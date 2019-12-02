# Sesami WebAPi
# Lock

from io import open
from pysesame2 import get_sesames

import dir_path

path = dir_path.api_path()
with open(path) as f:
	s = f.read()
	sesames = get_sesames(s.rstrip())

sesame = sesames[0]
if sesame.get_status()['responsive'] == True:
	if sesame.get_status()['locked'] == False:
		sesame.lock()
		print("Sesami Lock Complete!!")

