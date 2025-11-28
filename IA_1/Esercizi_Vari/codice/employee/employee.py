import pandas as pd
import numpy as np

df = pd.read_json("../../dati/employee/employee_data_small.json")

# ESERCIZIO 1 – Studio preliminare
# Stampa i tipi delle colonne (dtypes)
# Stampa le prime 10 e ultime 5 righe delle colonne: Age, Salary, Gender

print(df.dtypes)
print()
a_s_g = df[["Age", "Salary", "Gender"]]
print(a_s_g.head(10))
print()
print(a_s_g.tail())
print("*" * 50)

# ESERCIZIO 2 – Pulizia valori mancanti
# Sostituisci "?" con np.nan

df = df.replace("?", np.nan)
print(df)
print("*" * 50)

# ESERCIZIO 3 – Limitazione outliers
# Limita tutte le età sopra 80 a 80

df["Age"] = df["Age"].clip(upper=80)
print(df[["EmployeeId", "Name", "Age"]])
print("*" * 50)

# ESERCIZIO 4 – Sostituzione NaN con media
# Sostituisci i valori mancanti in Age e Salary con la media della colonna

media_age = df["Age"].mean()
media_salary = df["Salary"].mean()
df["Age"] = df["Age"].replace(np.nan, media_age)
df["Salary"] = df["Salary"].replace(np.nan, media_salary)
print(df[["EmployeeId", "Name", "Age", "Salary"]])
print("*" * 50)

# ESERCIZIO 5 – Correzione errori Gender
# Correggi "femael" → "female", "femlae" → "female", "mael" → "male"

df["Gender"] = df["Gender"].replace({"femlae":"female", "femael":"female", "mael":"male"})
print(df[["EmployeeId", "Name", "Gender"]])
print("*" * 50)

# ESERCIZIO 6 – Conversione tipi
# Assicurati che:
#   Age → float
#   Salary → float
#   Gender → string

df["Age"] = df["Age"].astype("float")
df["Salary"] = df["Salary"].astype("float")
df["Gender"] = df["Gender"].astype("string")
df.info()
print("*" * 50)

# ESERCIZIO 7 – Filtri
# Estrai tutti i dipendenti con Salary > 70000
# Estrai tutti i dipendenti dell’IT con Age < 35
salary_70000 = df[df["Salary"] > 70000]
it_age_35 = df[(df["Department"] == "IT") & (df["Age"] < 35)]
print(salary_70000[["EmployeeId", "Name", "Salary"]])
print()
print(it_age_35[["EmployeeId", "Name", "Age"]])

# ESERCIZIO 8 – Aggregazioni
# Calcola lo stipendio medio per Department
# Calcola l’età media per Gender

stipendio_medio = df.groupby("Department")["Salary"].mean()
eta_media_gender = df.groupby("Gender")["Age"].mean()
print(stipendio_medio)
print(eta_media_gender)

# ESERCIZIO 9 – Ordinamenti
# Ordina i dipendenti per Salary decrescente
# Ordina per Department e poi Age crescente
dipendenti_stipendio_desc = df.sort_values(by="Salary", ascending=False)
print(dipendenti_stipendio_desc[["EmployeeId", "Name", "Salary"]])
print()
dep_age_cres = df.sort_values(by=["Department", "Age"], ascending=True)
print(dep_age_cres[["EmployeeId", "Name", "Department", "Age"]])


# ESERCIZIO 10 – Creazione colonna
# Aggiungi una colonna Seniority:
#     "Junior" se Age < 30
#     "Mid" se 30 <= Age < 40
#     "Senior" se Age >= 40

def seniority(age: int):
    if age < 30:
        return "Junior"
    elif 30 <= age <= 40:
        return "Mid"
    else:
        return "Senior"

df["Seniority"] = df["Age"].apply(seniority)
print(df[["EmployeeId", "Name", "Age", "Seniority"]])

# ESERCIZIO 11 – Flag HighSalary e JuniorIT
# Obiettivo:
#   Creare una colonna HighSalary → True se Salary > 70000, altrimenti False
#   Creare una colonna JuniorIT → True se Department == "IT" e Age < 30, altrimenti False

df["HighSalary"] = df["Salary"].apply(lambda x: True if x > 70000 else False)
df["JuniorIT"] = df.apply(lambda row: True if (row["Department"] == "IT" and row["Age"] < 30) else False, axis=1)
print(df[["EmployeeId", "Name", "HighSalary", "JuniorIT"]])

# ESERCIZIO 12 – Aggregazioni avanzate
# Obiettivo:
#   Calcolare stipendio medio, numero di dipendenti e età media per Department
#   Usare agg() per più funzioni contemporaneamente
aggregazioni_department = df.groupby("Department").agg(
    Stipendio_Medio=("Salary", "mean"),
    Stipendio_minimo=("Salary", "min"),
    Stipendio_massimo=("Salary", "max"),
    Numero_dipendenti=("EmployeeId", "count"),
    Età_media=("Age", "mean")
    )
print(aggregazioni_department)




'''
* Spiegazione uso di Groupby (ragruppamento):
groupby serve a raggruppare il DataFrame in base a una o più colonne e poi applicare 
funzioni di aggregazione (media, somma, conteggio, ecc.) su ciascun gruppo.

Sintassi:
df.groupby("colonna_di_gruppo")["colonna_su_cui_aggregare"].funzione()
    - "colonna_di_gruppo" → definisce i gruppi
    - "colonna_su_cui_aggregare" → colonna su cui calcolare l’aggregazione
    - .funzione() → tipo di aggregazione (mean(), sum(), count(), ecc.)


* Spiegazione uso di Sort-Values (ordinamento):
sort_values serve a ordinare le righe del DataFrame in base a una o più colonne.

Sintassi:
df.sort_values(by="colonna", ascending=True)
    - by → la colonna (o lista di colonne) su cui ordinare
    - ascending=True → ordine crescente (default), False → decrescente


* Spiegazione di .apply() su una Series:
Usata per applicare una funzione a righe, colonne o elementi di una Series.
Quando si applica su una singola colonna (Series):

df["colonna"].apply(funzione)

    - funzione → una funzione che prende un singolo valore e restituisce un nuovo valore
    - Pandas applica questa funzione a ogni elemento della colonna


.apply() su un DataFrame

Quando la applichi a un DataFrame intero:

df.apply(funzione, axis=0)  # per colonna
df.apply(funzione, axis=1)  # per riga

    - axis=0 → la funzione riceve ogni colonna come Series
    - axis=1 → la funzione riceve ogni riga come Series

    
Somma di due colonne riga per riga
df["Total"] = df.apply(lambda row: row["Salary"] + row["Bonus"], axis=1)

    - Qui row è una riga intera
    - Creo una nuova colonna Total sommando due colonne della stessa riga
'''