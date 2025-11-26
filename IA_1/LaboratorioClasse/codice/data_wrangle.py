import pandas as pd
import numpy as np

# Preparazione
data_path = "../dati/autos/auto_mini.csv"
clean_data_path = "../dati/autos/auto_clean.csv"

# Leggi un file locale
df = pd.read_csv(data_path)
print("\nLetto da file locale")
# print("\n")
# print(df)
# print("\n")
# print(df.dtypes) # normalized-loss: average loss per car per year
# print("\n")

# "numpy NaNs" al posto di valori mancanti
df.replace("?", np.nan, inplace=True)
# df = df.replace("?", np.nan)
# print(df)
# print("\n")

# # Quanti NaNs per colonna
# missing_data = df.isnull()
# for column in missing_data.columns.values.tolist():
#     # print(column)
#     print (missing_data[column].value_counts())

# Media al posto di NaNs    
avg = df["normalized-losses"].astype("float").mean(axis = 0)
# df["normalized-losses"].replace(np.nan, avg, inplace = True)
df["normalized-losses"] = df["normalized-losses"].replace(np.nan, avg)

# Max frequenza al posto di NaNs
print(df['num-of-doors'].value_counts())
df["num-of-doors"].replace(np.nan, df['num-of-doors'].value_counts().idxmax(), inplace = True)

# Eliminazione righe dove NaNs
df.dropna(subset=["price"], axis=0, inplace = True)
df.reset_index(drop = True, inplace = True)
print(df)
print("\n")

# print(df.dtypes)
   
# # Conversione tipi di dato  
# df = df.convert_dtypes()
# print(df.dtypes)
# print("\n")
# df[["normalized-losses"]] = df[["normalized-losses"]].astype("int")
# df[["price"]] = df[["price"]].astype("float")
# print(df.dtypes)

# Normalizzazione dei dati
df['length'] = (df['length']-df['length'].min())/(df['length'].max() - df['length'].min())
# print(df)
# print("\n")

# Correzione "typos"
df['make'] = df['make'].replace({'alfa-romero': 'alfa-romeo'})

# # Limita gli outliers
df['price'] = df['price'].clip(lower=15000, upper=20000)
# Limita (“tagliare”) i valori di una serie o colonna entro un intervallo minimo e/o massimo.
# Tutti i valori inferiori a 15000 diventano 15000
# I valori già compresi tra 15000 e 20000 rimangono invariati
# In altre parole, impone un “range” ai valori della colonna price. 
# È molto utile per gestire outlier o valori estremi che non vuoi superino certi limiti.

print(df)
print("\n")

print(df.sort_values('price', ascending=True))
# Ordina le righe del DataFrame df in base alla colonna price, dal valore più basso al più alto (ascending = True)
# Se mettessi ascending=False, ottengo l’ordine decrescente (dal più alto al più basso)

# # Scrivi il dataset pulito su file CSV
# df.to_csv(clean_data_path)
# print("\nAuto DataFrame ""pulito"" salvato come file CSV (../dati/autos/auto_clean.csv)")
