'''
Calcolare la probabilità che due persone vissute in luoghi ed epoche differenti:
siano nate lo stesso giorno del mese 
(considerando 30 giorni in un mese).
'''
from scipy.stats import binom
import scipy.special as sp

# Numero di giorni nel mese
num_giorni = 31

# Numero di persone
num_persone = 2

# Priobabilità che tutte e 2 le persone siano nate lo stesso giorno del mese

probabilita_stesso_giorno = (1 / num_giorni) ** (num_persone - 1)