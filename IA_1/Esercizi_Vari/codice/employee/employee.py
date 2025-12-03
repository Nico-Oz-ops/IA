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
print()

# ESERCIZIO 13 – Merge semplice (left join)
# Obiettivo:
#   - Unire df con df_bonus tramite la colonna EmployeeId usando:
#   - LEFT JOIN: tieni tutti i dipendenti del df principale
#   - Se manca il bonus → NaN

# Prima di rispondere alla domanda bisogna creare un secondo dataset, perciò creo un secondo dataframe, df_bonus
df_bonus = pd.DataFrame({
    "EmployeeId": [101, 103, 105, 110, 115],
    "Bonus": [5000, 3000, 8000, 2000, 10000],
    "Performance": ["A", "B", "A", "C", "A"]
})

df_merge_left = df.merge(df_bonus, on="EmployeeId", how="left")
print(df_merge_left[["EmployeeId", "Name", "Performance", "Bonus"]])
print()

# ESERCIZIO 14 – Inner merge
# Obiettivo:
#   - Mantieni solo i dipendenti che appaiono in entrambi i DataFrame.

df_merge_inner = df.merge(df_bonus, on="EmployeeId", how="inner")
print(df_merge_inner[["EmployeeId", "Name", "Performance", "Bonus"]])
print()

# ESERCIZIO 15 – Outer merge
# Obiettivo:
#   - Unisce tutto, anche chi non appare da una parte o dall'altra.

df_merge_outer = df.merge(df_bonus, on="EmployeeId", how="outer")
print(df_merge_outer[["EmployeeId", "Name", "Performance", "Bonus"]])
print()

# ESERCIZIO 16 – Merge con nomi di colonne diversi
# Creo un piccolo DataFrame con un nome colonna diverso:

df_city = pd.DataFrame({
    "ID": [101, 103, 110],
    "CityCode": ["MIL", "ROM", "NAP"]
})

# Obiettivo:
#   - Unire df e df_city mappando:
#       - df.EmployeeId → df_city.ID
df_merge_city = df.merge(df_city, left_on="EmployeeId", right_on="ID", how="left" )
print(df_merge_city[["EmployeeId", "Name", "CityCode"]])
print()

# ESERCIZIO 17 – Merge + filtraggio
# Obiettivo:
# Dopo il merge con df_bonus, estrai solo:
#   - dipendenti con performance "A"
#   - bonus > 5000

df_perfA = df_merge_left[(df_merge_left["Performance"] == "A") & (df_merge_left["Bonus"] > 5000)]
print(df_merge_left[["EmployeeId", "Name", "Performance", "Bonus"]])
print()

# ESERCIZIO 18 – Merge multiplo
# Obiettivo:
# Fai:
#   - df → merge con df_bonus → merge con df_city.
df_all = df.merge(df_bonus, on="EmployeeId", how="left").merge(df_city, left_on="EmployeeId", right_on="ID", how="left")
print(df_all.head())
print()

#--------------------Nuovi esercizi   -    Merge----------------------

# ESERCIZIO 1

# Tema: Merge su colonne con lo stesso nome
# Obiettivo: Usare on e il parametro how
# Nome dell’esercizio: Unisci dipendenti e sedi di lavoro

# Traccia:
# Unisci il DataFrame principale df con df_offices usando la colonna EmployeeID come chiave comune.
# Utilizza un inner join per ottenere solo i dipendenti che hanno una sede associata.
# Ordina il risultato per EmployeeID.

# Creazione DataFrame "df_offices"
df_offices = pd.DataFrame({
    "EmployeeID": [1, 2, 4, 6, 8, 10],
    "Office": ["Rome", "Milan", "Rome", "Naples", "Turin", "Milan"]
})

print("Esercizio 1")
df_employees_offices = df.merge(df_offices, left_on="EmployeeId", right_on="EmployeeID", how="inner").sort_values("EmployeeID", ascending=False)
df_employees_offices = df_employees_offices.drop(columns="EmployeeID") # per pulizia, elimino la colonna "EmployeeID" perché ho già "EmployeeId"
print(df_employees_offices[["EmployeeId", "Name", "Office"]])
print()

# ESERCIZIO 2

# Tema: Left join tra DataFrame con dati mancanti
# Obiettivo: Capire l’uso di how="left"
# Nome dell’esercizio: Tutti i dipendenti con eventuale sede

# Traccia:
# Esegui una left join tra df e df_offices usando EmployeeID come chiave.
# Ottieni quindi tutti i dipendenti, anche quelli senza sede associata.
# Filtra e mostra solo le righe in cui la colonna Office è NaN.

print("Esercizio 2")
df_merge_employees_offices = df.merge(df_offices, left_on="EmployeeId", right_on="EmployeeID", how="left")

# filtro solo le righe in cui Office è NaN
df_missing_office = df_merge_employees_offices[df_merge_employees_offices["Office"].isna()]
df_missing_office = df_missing_office.drop(columns="EmployeeID")
print(df_missing_office[["EmployeeId", "Name", "Office"]])
print()

# opzione compatta - uso di lambda
df_missing_office = (
    df.merge(df_offices, left_on="EmployeeId", right_on="EmployeeID", how="left").loc[lambda x: x["Office"].isna()].drop(columns="EmployeeID"))

# ESERCIZIO 3

# Tema: Merge con colonne di nome diverso
# Obiettivo: Usare left_on e right_on
# Nome dell’esercizio: Aggiungi il livello di salario
# Traccia:
# Unisci df con df_salary_info, sapendo che le chiavi sono:

#   - df.EmployeeID
#   - df_salary_info.EmpID
#   Usa un left join.
#   Mostra solo i dipendenti che hanno un SalaryLevel non nullo.

# Creazione dataframe "df_salary_info"
df_salary_info = pd.DataFrame({
    "EmpID":[1, 2, 3, 5, 7, 10],
    "SalaryLevel":["High", "Medium", "Low", "Medium", "High", "Low"]
})

print("Esercizio 3")
df_merge_salary_level = df.merge(df_salary_info, left_on="EmployeeId", right_on="EmpID", how="left")
df_employee_salary_not_null = df_merge_salary_level[df_merge_salary_level["SalaryLevel"].notnull()]
print(df_employee_salary_not_null[["EmployeeId", "Name", "SalaryLevel"]])

#oppure
df_merge_salary = df.merge(df_salary_info, left_on="EmployeeId", right_on="EmpID", how="left").loc[lambda x: x["SalaryLevel"].notnull()]
# .loc[lambda x: ...] filtra direttamente senza creare variabile intermedia
print()

# ESERCIZIO 4

# Tema: Right join
# Obiettivo: Capire cosa accade quando preserviamo il DataFrame di destra
# Nome dell’esercizio: Sedi presenti, dipendenti mancanti

# Traccia:
# Esegui un right join tra:

#   - df (sinistra)
#   - df_offices (destra)

#   Unisci su EmployeeID.
#   Mostra le righe in cui il dipendente non è presente nel DataFrame principale (Name == NaN).
print("Esercizio 4")
df_missing_employees_offices = df.merge(df_offices, left_on="EmployeeId", right_on="EmployeeID", how="right").drop(columns="EmployeeID")
df_missing_employee = df_missing_employees_offices[df_missing_employees_offices["Name"].isnull()]
print(df_missing_employee[["EmployeeId", "Name", "Office"]])

#oppure
df_missing_employee_office = df.merge(
    df_offices, left_on="EmployeeId", right_on="EmployeeID", how="right").loc[lambda x: x["Name"].isnull()].drop(columns="EmployeeID")

print()

# ESERCIZIO 5

# Tema: Merge One-to-Many
# Obiettivo: Capire cosa accade quando una chiave del DataFrame destro ha più occorrenze
# Nome dell’esercizio: Progetti assegnati a ogni dipendente

# Traccia:
# Unisci df a df_projects usando:

#   - df.EmployeeID
#   - df_projects.Emp_ID

#   Usa un left join.
#   Ottieni così, per ogni dipendente, tutti i progetti a cui partecipa.
#   Ordina per EmployeeID e Project.

# creo dataframe df_projects
df_projects = pd.DataFrame({
    "EmpID": [1, 1, 2, 3, 5, 7, 7],
    "Project": ["Alpha", "Beta", "Alpha", "Gamma", "Delta", "Alpha", "Omega"]
})
print("Esercizio 5")
df_prog_dip = df.merge(df_projects, left_on="EmployeeId", right_on="EmpID", how="left", validate="one_to_many").drop(columns="EmpID")
df_prog_dip_ord = df_prog_dip.sort_values(["EmployeeId", "Project"])
print(df_prog_dip_ord[["EmployeeId", "Name", "Project"]])

print()

# ESERCIZIO 6

# Tema: Merge per confrontare DataFrame
# Obiettivo: Usare how="outer" e indicator=True

# Nome dell’esercizio: Confronto tra dipendenti con sede e dipendenti con livello di salario
# Traccia:
# Confronta df_offices e df_salary_info unendoli con:

#   - left_on = "EmployeeID"
#   - right_on = "EmpID"

#   Usa un outer join e indicator=True.
#   Mostra quali EmployeeID compaiono:
#       - solo nelle sedi
#       - solo nel file salary_info
#       - in entrambi.

df_merge_offices_salary = pd.merge(df_offices, df_salary_info, left_on="EmployeeID", right_on="EmpID", how="outer", indicator=True).drop(columns="EmpID")
print(df_merge_offices_salary[["_merge", "EmployeeID", "Office", "SalaryLevel"]])



# ESERCIZIO 7

# Tema: Merge su più colonne
# Obiettivo: Unire DataFrame con chiavi multiple
# Nome dell’esercizio: Confronto valutazioni 2023 e 2024

# Traccia:
# Hai due DataFrame:
#   - df_reviews2023 con colonne EmployeeID, Year, Score
#   - df_reviews2024 con colonne EmpID, YearVal, Score

# Rinomina le colonne di df_reviews2024 in modo da ottenere stessa struttura di df_reviews2023:

#   - EmpID → EmployeeID
#   - YearVal → Year

# Poi esegui un merge inner su:

#   - EmployeeID
#   - Year

# Mostra solo le righe in cui lo Score del 2024 è maggiore di quello del 2023.



# ESERCIZIO 8

# Tema: Merge con indici
# Obiettivo: Usare left_index e right_index
# Nome dell’esercizio: Unisci valutazioni 2023 e anagrafica tramite indice

# Traccia:
# Imposta EmployeeID come indice in df e in df_reviews2023.

# Esegui un merge usando:

#   - left_index=True
#   - right_index=True

# Mostra per ogni dipendente la sua Name, Age e Score del 2023.
# Ordina per Score decrescente.


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