from scipy.stats import binom
import scipy.special as sp

'''
Un dado viene lanciato 7 volte. Un lancio è un successo se esce il numero 1.
- Calcolare la probabilità di avere 3 successi
'''
n = 7
p = 1/6
k = 3
prob = binom.pmf(k, n, p)
print(f'La probabilità di ottenere esattamente {k} successi in {n} lanci è: {prob:.4f}')


# Esempio: Calcolare 5 su 2 (5! / (2! * 3!))
n = 7
k = 3

# Calcolo del coefficiente binomiale
risultato = sp.comb(n, k)
print(risultato)

'''
- Calcolare la probabilità di avere 0 successi.
'''
k = 0
n = 7
prob = binom.pmf(k, n, p)
print(f'La probabilità di ottenere esattamente {k} successi in {n} lanci è: {prob:.4f}')