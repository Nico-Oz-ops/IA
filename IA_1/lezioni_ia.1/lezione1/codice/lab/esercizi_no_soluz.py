import pandas as pd

## Esercizio 1: Carica il CSV in un DataFrame
## Task: Leggi i dati del file CSV fornito in un Pandas DataFrame e visualizza le prime 3 righe  
## Soluzione:
print("***ESERCIZIO 1***")
csv_path: str = "../../dati/lab/some_music_albums.csv"
df = pd.read_csv(csv_path)
print(df.head(3))
print("*****************"+"\n")    
 
### Esercizio 2: Mostra informazioni di base sul DataFrame 
### Task: Mostra il numero di righe, colonne e tipi di dati per ogni colonna 
### Soluzione:
print("***ESERCIZIO 2***")
df.info()
print("*****************"+"\n")
 
### Esercizio 3: Filtra gli album per genere
### Task: Crea un nuovo DataFrame contenente solo gli album con "rock" nella colonna 'Genre'
### Soluzione:
print("***ESERCIZIO 3***")
df_rock = df[df['Genre'].str.contains('rock', case=False, na=False)]
print(df_rock)
print(df_rock[["Artist", "Album", "Genre"]])
print("*****************"+"\n")

## Esercizio 4: Trova gli album pubblicati dopo il 1980
## Task: Filtra gli album pubblicati dopo il 1980 e visualizza solo le colonne 'Artist', 'Album' e 'Released'
## Soluzione:
print("***ESERCIZIO 4***")
album_dopo_1980 = df[df["Released"] > 1980]
print(album_dopo_1980[["Artist", "Album", "Released"]])
print("*****************"+"\n")

### Esercizio 5: Calcola la media delle valutazioni
### Task: Calcola la media della colonna 'Rating' per tutti gli album
### Soluzione:
print("***ESERCIZIO 5***")
media_valutazioni = df["Rating"].mean()
print(f"La media delle valutazioni per tutti gli album: {media_valutazioni}")
print("*****************"+"\n")

### Esercizio 6: Trova l'album più lungo e il più breve
### Task: Identifica l'album con la durata massima e minima nella colonna 'Length' e visualizza i suoi dettagli
### Soluzione:
print("***ESERCIZIO 6***")
df["Length_timedelta"] = pd.to_timedelta(df["Length"]) # converte i valori in un oggetto di tipo timedelta (durata temporale) e permette di fare operazioni di tempo 
indice_massimo = df["Length_timedelta"].idxmax()
album_piu_lungo = df.loc[indice_massimo, ["Artist", "Album", "Released", "Length_timedelta"]]
print(album_piu_lungo)
print()
indice_minimo = df["Length_timedelta"].idxmin()
album_piu_corto = df.loc[indice_minimo, ["Artist", "Album", "Released", "Length_timedelta"]]
print(album_piu_corto)
print("*****************"+"\n")
 
### NON FARE
### Esercizio 7: Elenco generi unici
### Task: Estrai e stampa tutti i generi unici nel dataset (dividendo i generi combinati come "pop, rock")
### Soluzione:
print("***ESERCIZIO 7***")

print("*****************"+"\n")

### Esercizio 8: Confronta le vendite con vendite dichiarate
### Task: Aggiungi una nuova colonna 'Sales_Difference' che mostri la differenza tra 'Claimed Sales' e 'Music Recording Sales'
### Soluzione:
print("***ESERCIZIO 8***")
df["Sales_Difference"] = df["Claimed Sales (millions)"].fillna(0) - df["Music Recording Sales (millions)"].fillna(0)
print(df[["Artist", "Album", "Claimed Sales (millions)", "Music Recording Sales (millions)", "Sales_Difference"]])
print("*****************"+"\n")
  
### Esercizio 9: Trova gli album colonna sonora
### Task: Elenca tutti gli album contrassegnati come 'Soundtrack' (dove la colonna è "Y")
### Soluzione:
print("***ESERCIZIO 9***")
soundtrack_album = df[df["Soundtrack"] == "Y"]
print(soundtrack_album[["Artist", "Album"]])

print("*****************"+"\n")

### Esercizio 10: Salva i dati filtrati in un file CSV
### Task: Salva tutti gli album con una valutazione (Rating) ≥ 9 in un nuovo file CSV
### Soluzione:
print("***ESERCIZIO 10***")
album_migliori = df[df["Rating"] >= 9]
album_migliori.to_csv("../../dati/lab/album_migliori.csv", index=False) # index=False, evita di salvare l'indice del DataFrame nel csv (in file puliti di solito non serve)
print("Il file 'album_migliori.csv' è stato salvato correttamente")
print("******************"+"\n")

### NON FARE  
### Esercizio 11: Conta gli album per genere
### Task:Conta quanti album appartengono a ogni genere unico (dividendo generi combinati come "pop, rock")
### Soluzione:  
print("***ESERCIZIO 11***")

print("******************"+"\n")

### Esercizio 12: Trova l'album con la maggior differenza tra vendite e vendite dichiarate
### Task: Identifica l'album con la maggiore differenza tra 'Claimed Sales' e 'Music Recording Sales' e visualizza i suoi dettagli
### Soluzione:  
print("***ESERCIZIO 12***")
df["Sales_Difference"] = df["Claimed Sales (millions)"].fillna(0) - df["Music Recording Sales (millions)"].fillna(0)
indice_max_differenza = df["Sales_Difference"].idxmax()
print(df.loc[indice_max_differenza, ["Artist", "Album", "Claimed Sales (millions)", "Music Recording Sales (millions)", "Sales_Difference"]])
print("******************"+"\n")
  
### Esercizio 13: Filtra gli album per generi multipli
### Task: Crea un nuovo DataFrame contenente gli album che includono entrambi "rock" e "pop" nella colonna 'Genre'
### Soluzione:**  
print("***ESERCIZIO 13***")
df["Genre"] = df["Genre"].astype(str) # mi assicuro che tutte le righe di Genre siano stringhe
df_rock_pop = df[df["Genre"].str.contains("rock", case=False, na=False) & df["Genre"].str.contains("pop", case=False, na=False)]
print(df_rock_pop[["Artist", "Album", "Genre"]])
print("******************"+"\n")

### NON FARE    
### Esercizio 14: Calcola la durata media per genere
### Task: Calcola la media della durata (in minuti) degli album per ogni genere (dividendo generi combinati)
### Soluzione:  
print("***ESERCIZIO 14***")

print("******************"+"\n")

### Esercizio 15: Trova l'album più venduto che non è una colonna sonora
### Task: Identifica l'album con le maggiori 'Music Recording Sales' che non è una colonna sonora
### Soluzione:  
print("***ESERCIZIO 15***")
album_non_soundtrack = df[df["Soundtrack"] != "Y"] # creo un nuovo dataframe, in cui vado a filtrare gli album che non sono colonne sonore
index_max_recording_sales = album_non_soundtrack["Music Recording Sales (millions)"].idxmax() # restituisce l'indice della riga con le maggiori vendite musicali
print(album_non_soundtrack.loc[index_max_recording_sales, ["Artist", "Album", "Music Recording Sales (millions)"]]) # uso .loc per selezionare la riga corrispondente all'indice trovato
print("******************"+"\n")