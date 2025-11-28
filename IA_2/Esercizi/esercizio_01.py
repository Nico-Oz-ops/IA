"Simula il lancio di due dadi D6, e restituisci in output una lista con n=100 risultati della somma dei due dadi"
"Dopo aver lanciato n volte i dadi, verificare la frequenza"

import random
from collections import Counter

# def lancio_dadi(n = 100):
#     risultati = []

#     for _ in range(n):
#         dado_1 = random.randint(1, 6)
#         dado_2 = random.randint(1, 6)
#         somma = dado_1 + dado_2
#         risultati.append(somma)
#     return risultati


# print(lancio_dadi())
# print(f"Min: {min(lancio_dadi())}, Max: {max(lancio_dadi())}")


def lancio_dadi(n = 100):
    risultati = []

    for _ in range(n):
        dado_1 = random.randint(1, 6)
        dado_2 = random.randint(1, 6)
        somma = dado_1 + dado_2
        risultati.append(somma)
    
    conteggi = Counter(risultati)

    valore_piu_frequente = conteggi.most_common(1)
    return valore_piu_frequente

print("Valore più frequente:", lancio_dadi())






















