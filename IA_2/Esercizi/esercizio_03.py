'''
3 persone si danno appuntamento in un bar nella piazza della città.
Poco pratici della città non sanno che in quella piazza ci sono 4 bar.
Quale è la probabilità che tutti e 3 scelgano lo stesso bar? 
'''
from scipy.stats import binom
import scipy.special as sp
# Numero di bar
num_bar = 4

# Numero di persone
num_persone = 3

# Priobabilità che tutte e 3 le persone scelgano lo stesso bar

probabilita_stesso_bar = num_bar * (1 / num_bar) ** num_persone
