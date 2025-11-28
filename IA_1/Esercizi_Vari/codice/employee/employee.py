import pandas as pd

df = pd.read_json("../../dati/employee/employee_data_small.json")
print(df.head())

# ESERCIZIO 1 – Studio preliminare
# Stampa i tipi delle colonne (dtypes)
# Stampa le prime 10 e ultime 5 righe delle colonne: Age, Salary, Gender



# ESERCIZIO 2 – Pulizia valori mancanti
# Sostituisci "?" con np.nan



# ESERCIZIO 3 – Limitazione outliers
# Limita tutte le età sopra 80 a 80



# ESERCIZIO 4 – Sostituzione NaN con media
# Sostituisci i valori mancanti in Age e Salary con la media della colonna



# ESERCIZIO 5 – Correzione errori Gender
# Correggi "femael" → "female", "femlae" → "female", "mael" → "male"




# ESERCIZIO 6 – Conversione tipi
# Assicurati che:
#   Age → float
#   Salary → float
#   Gender → string




# ESERCIZIO 7 – Filtri
# Estrai tutti i dipendenti con Salary > 70000
# Estrai tutti i dipendenti dell’IT con Age < 35




# ESERCIZIO 8 – Aggregazioni
# Calcola lo stipendio medio per Department
# Calcola l’età media per Gender




# ESERCIZIO 9 – Ordinamenti
# Ordina i dipendenti per Salary decrescente
# Ordina per Department e poi Age crescente




# ESERCIZIO 10 – Creazione colonna
# Aggiungi una colonna Seniority:
#     "Junior" se Age < 30
#     "Mid" se 30 <= Age < 40
#     "Senior" se Age >= 40