# Esercizio sull'aggiornamento Bayesiano sequenziale

import matplotlib.pyplot as plt

def teorema_bayes(p_a_dato_b, p_b, p_a):
    """
    Calcola P(B|A)=P(A|B)*P(B) / P(A)
    
    Arg
    p_a_dato_b : P(A|B) - verosimiglianza
    p_b : P(B) - probabilità a priori
    p_a : P(A) - evidenza

    Returns
    P(B|A) - probabilità a posteriori
    """
    return(p_a_dato_b*p_b) / p_a


def teorema_bayes_completo(p_a_dato_b, p_b, p_a_dato_non_b):
    """
    Calcola P(B|A) usando la legge di probabilità totale per P(A)
    """
    p_non_b = 1-p_b
    p_a = p_a_dato_b*p_b + p_a_dato_non_b*p_non_b
    return teorema_bayes(p_a_dato_b, p_b, p_a)


# Aggiornamento Bayesiano sequenziale
# Stima della probabilità di una moneta truccata
# Prior: P(Truccata)= 0.5
# Osserviamo una sequenza di lanci ed aggiorniamo la probabilità

# scenario: moneta truccata (70% testa) vs equa (50% testa)
p_testa_truccata = 0.70
p_testa_equa = 0.50

# sequenza lanci osservati
lanci = ['T', 'T', 'T', 'C', 'T', 'T', 'T', 'T', 'T', 'C', 'T', 'T', 'T', 'T', 'T']

# Prior iniziale 
p_truccata = 0.5
storia_probabilita = [p_truccata]

for i, lancio in enumerate(lanci,1):
    if lancio == 'T':

        p_evidenza_truccata = p_testa_truccata
        p_evidenza_equa = p_testa_equa
    else:
        p_evidenza_truccata = 1-p_testa_truccata
        p_evidenza_equa = 1-p_testa_equa

    p_truccata = teorema_bayes_completo(p_evidenza_truccata, p_truccata, p_evidenza_equa)
    storia_probabilita.append(p_truccata) 

    print(f"Lancio{i}: {lancio} -> P(Truccata) = {p_truccata:.4f}")

print(f"\nProbabilità finale: {p_truccata:.4f}= {p_truccata:.2%}")


x = range(len(storia_probabilita))
y = storia_probabilita

plt.figure(figsize=(12,5))

markerline, stemlines, baseline = plt.stem(x, y)
plt.setp(stemlines, 'linewidth', 1.5)
etichette = ["Prior"] + lanci
plt.xticks(x, etichette, rotation=45)
plt.xlabel("Lanci osservati")
plt.ylabel("P(Truccata)")
plt.title("Aggiornamento Bayesiano sequenziale")
plt.ylim(0,1)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

