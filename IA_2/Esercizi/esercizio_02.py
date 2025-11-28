import math 
from scipy.stats import binom

# Alternativa 1 - calcolo di probabilità binomiale con la formula esplicita
def binom_manual(n: int, p: float, k: int):
    n_su_k = math.factorial(n)/(math.factorial(k)*math.factorial((n-k)))
    p_k = p**k
    insucesso = (1 - p)**(n-k)

    return n_su_k * p_k * insucesso

n = 5 # prove
p = 0.6 # probabilità di successo
k = 3 # numero di successi

prob = binom_manual(n, p, k)
print(prob)

# Alternativa 2 - usando scipy.stats.binom
def binom_scipy(n: int, p: float, k: int):
    # calcolo la probabilità binomiale P(X=k) usando scipy invece dei fattoriali
    return binom.pmf(k, n, p)

prob_2 = binom_scipy(n, p, k)
print(prob_2)