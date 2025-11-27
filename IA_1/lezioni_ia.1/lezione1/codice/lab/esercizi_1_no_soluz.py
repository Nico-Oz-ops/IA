import pandas as pd
import numpy as np
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

csv_clean_path: str = "../../dati/autos/auto_clean.csv"
df = pd.read_csv(csv_clean_path)
print(df.head())

# Esercizio 1: Connessione con SQLAlchemy
# Task: Write code to store the df DataFrame on a SQLite table named cars using SQLAlchemy. 
# Handle errors gracefully (print a message if it fails).
# Soluzione:
print("***ESERCIZIO 1***")
engine = create_engine("sqlite:///cars.db") # si crea un motore SQLAlchemy collegato a un database SQLite (cars.db)
# engine è l'oggetto che permette di connettersi al database e eseguire query

try: #si inizia il blocco di gestione degli errori, se qualcosa va storto l'eccezione viene catturata
    with engine.begin() as conn: # si apre una connessione al database usando il contesto with.
        # engine.begin() (metodo dell'oggetto Engine di SQLAlchemy) avvia automaticamente una transazione, 
        # cioè tutte le operazioni dentro il blocco saranno committate se tutto va bene, altrimenti rollback in caso di errore.
        # "conn" è l'oggetto connessione che si userà per scrivere sul database
        df.to_sql("cars", conn, if_exists="replace", index=False)
        # si salva il DataFrame "df" in una tabella "cars"
        # conn, è la connessione usata per scrivere sul database
        # if_exists="replace", se la tabella "cars" esiste già, viene sostituita
        # index=False, non salva l'indice del DataFrame come colonna nella tabella

except Exception as e: # cattura qualsiasi errore che accade nel blocco "try", e l'errore viene salvato in "e"
    print(f"Error: {e}") # stampa messaggio di errore

finally: # viene eseguito sempre, indipendentemente dal successo o fallimento del "try"
    engine.dispose() # chiude tutte le connessioni aperte e libera le risorse del motore. 
                     # è buona pratica farlo quando ho finito di usare il database
print("*****************"+"\n")
 
### Esercizio 2: Reading SQL Data 
### Task:  Query the cars table to load rows where fuel-type is "gas" into a new DataFrame df_gas 
### Soluzione:
print("***ESERCIZIO 2***")
query_def = """SELECT * FROM cars WHERE "fuel-type" = 'gas'"""
with engine.begin() as conn: # with engine.connect() as conn ?? 
    df_gas = pd.read_sql_query(text(query_def), conn)

# with engine.begin() as conn:
#     df_gas = pd.read_sql(text(query_def), conn) ----> questo contesto with va anche bene, fa lo stesso del precedente
print("*****************"+"\n")
 
### Esercizio 3: Replacing Missing Values
### Task: Replace missing values (NaN) in the price column with the column’s median
### Soluzione:
print("***ESERCIZIO 3***")
mediana_prezzo = df["price"].median()
df["price"] = df["price"].replace(np.nan, mediana_prezzo) #replace è più generico, viene usato anche per sostituire valorir arbitrari, non solo NaN
print(df[["price"]])

print(f"\nOppure (opzione più pythonica):")
df["price"] = df["price"].fillna(mediana_prezzo) #fillna è pensato appositamente per valori mancanti (NaN). Serve a riempire i valori mancanti (missing value)
print(df[["price"]])
print("*****************"+"\n")

## Esercizio 4: Most Frequent Value
## Task: Replace NaN values in num-of-doors with the most frequent door count
## Soluzione:
print("***ESERCIZIO 4***")
numero_porte_più_frequente = df["num-of-doors"].value_counts().idxmax()
# ".value_counts()" applicato a una colonna (df["num-of-doors"].....una Series) conta quante volte appare ciascun valore
# e restitusice una Series ordinata decrescente
# ".idxmax()" restituisce l'indice del valore massimo nella serie

# ".value_counts().idxmax()" calcola automaticamente il numero di porte più frequente
df["num-of-doors"] = df["num-of-doors"].fillna(numero_porte_più_frequente)
print(df[["num-of-doors"]])
print("*****************"+"\n")
 
### Esercizio 5: Normalisation
### Task: Normalise the horsepower column (convert to numeric first) to a 0-1 range
### Soluzione:
print("***ESERCIZIO 5***")
df["horsepower"] = pd.to_numeric(df["horsepower"], errors="coerce")
# ".to_numeric(...)", converte una Series o colonna in valori numerici (interi o float)
# "errors="coerce"", gestisce cosa fare se ci sono valori che non possono essere convertiti in numeri. 
# Possibili opzioni:
    # raise = genera un errore se c'è qualcosa che non si può convertire (default)
    # coerce = sostituisce i valori non convertibili con NaN
    # ignore = lascia i valori così come sono senza modifiche

# normalizzazione 0-1
df["horsepower"] = (df["horsepower"] - df["horsepower"].min()) / (df["horsepower"].max() - df["horsepower"].min())
print(df[["horsepower"]])
print("*****************"+"\n")

### Esercizio 6: Clipping Outliers
### Task:  Clip values in city-mpg to the 10th and 90th percentiles
### Soluzione:
print("***ESERCIZIO 6***")
# Calcolo i percentili 10° e 90°
p10 = df["city-mpg"].quantile(0.1)
p90 = df["city-mpg"].quantile(0.9)

# Limito i valori di city_mpg tra p10 e p90
df["city-mpg"] = df["city-mpg"].clip(lower=p10, upper=p90) 
# .clip(lower=p10, upper=p90): 
#   - tutti i valori inferiori a p10 diventano uguali a p10
#   - tutti i valori superiori a p90 diventano uguali a p90
#   - i valori tra p10 e p90 rimangono invariati

# Metodo molto usato per ridurre l’effetto degli outlier senza eliminare i dati.
print(df[["city-mpg"]])
print("*****************"+"\n")
 
### Esercizio 7: Dropping Rows
### Task:  Drop all rows where both price and horsepower are NaN
### Soluzione:
print("***ESERCIZIO 7***")
df.dropna(subset=["price", "horsepower"], how="all", inplace=True)
# ".dropna(...)" elimina la riga solo se entrambe price e horsepower sono NaN.
# invece se volessi eliminare le righe se almeno uno dei due è NaN, allora dovrei usare "how=any"
# print(df[["price", "horsepower"]])

print("Oppure:")
print(df.loc[:, "horsepower":"price"]) # questo funziona solo se nel DataFrame le colonne sono nel ordine giusto, se fosse stato [:, "price":"horsepower", allora avrebbe stampato un DataFrame vuoto]
print(df.columns.tolist()) # serve a mostrare la lista completa delle colonne del DataFrame
print("*****************"+"\n")
  
### Esercizio 8: Merging DataFrames
### Task: Merge df with a new DataFrame df_extra (columns: make, safety-rating) on the make column. 
# Keep only matching rows
### Soluzione:
print("***ESERCIZIO 8***")
df = df.convert_dtypes()
print(df.dtypes)
print(df[["make"]])
# creo il dataframe extra usando la colonna esistente "make" e creando "safety-rating"
df_extra = pd.DataFrame({"make":["alfa-romeo", "audi", "volvo"], "safety-rating":[4, 5, 3]})
print(df_extra)
print()
# bisogna usare inner join, perché tiene solo le righe corrispondenti. "make" è la colonna presente in entrambi DF
# ora faccio il merge tenendo solo corrispondenze
df_merged = df.merge(df_extra, on="make", how="inner")
# df_merged_2 = pd.merge(df, df_extra, on="make", how="inner") ---> un'altra maniera di fare merge
print(df_merged[["make", "price", "safety-rating"]])
print()
# print(df_merged_2[["make", "price", "safety-rating"]])

print("*****************"+"\n")

### Esercizio 9: Complex Cleaning
### Task: For normalized-losses:
###       Replace missing values (? or NaN) with np.nan.
###       Fill remaining NaN with the mean.
###       Convert to float64.
### Soluzione:
print("***ESERCIZIO 9***")
# sostituisco "?" con NaN
df["normalized-losses"] = df["normalized-losses"].replace("?", np.nan)
# converto in numerico
df["normalized-losses"] = pd.to_numeric(df["normalized-losses"], errors="coerce")
# riempio i NaN con la media
df["normalized-losses"] = df["normalized-losses"].fillna(df["normalized-losses"].mean())
# mi assicuro che sia tipo float64
df["normalized-losses"] = df["normalized-losses"].astype("float64")
print(df[["normalized-losses"]])
print("******************"+"\n")

