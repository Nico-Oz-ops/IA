import pandas as pd

## Esercizio 1: Carica il CSV in un DataFrame
## Task: Leggi i dati del file CSV fornito in un Pandas DataFrame e visualizza le prime 3 righe  
## Soluzione:
print("***ESERCIZIO 1***")
df = pd.read_csv("../dati/SomeMusicAlbums.csv")
print(df.head(3))
print("*****************"+"\n")    
 
### Esercizio 2: Mostra informazioni di base sul DataFrame 
### Task: Mostra il numero di righe, colonne e tipi di dati per ogni colonna 
### Soluzione:
print("***ESERCIZIO 2***")
df = pd.read_csv("../dati/SomeMusicAlbums.csv")
print(df.info())

print("Un'altra opzione:")
print("Shape:", df.shape)
print("Tipo dato:", df.dtypes)
print("*****************"+"\n")
 
### Esercizio 3: Filtra gli album per genere
### Task: Crea un nuovo DataFrame contenente solo gli album con "rock" nella colonna 'Genre'
### Soluzione:
print("***ESERCIZIO 3***")
condition_rock = df['Genre'].str.contains('rock', case=False)
print(df.loc[condition_rock])
# Un'altra opzione
print(df[condition_rock])
print("*****************"+"\n")

## Esercizio 4: Trova gli album pubblicati dopo il 1980
## Task: Filtra gli album pubblicati dopo il 1980 e visualizza solo le colonne 'Artist', 'Album' e 'Released'
## Soluzione:
print("***ESERCIZIO 4***")
album_dopo_1980 = df['Released'] > 1980
print(df.loc[album_dopo_1980, ['Artist', 'Album', 'Released']])

#Un'altra opzione
recent_albums = df[df['Released'] > 1980][['Artist', 'Album', 'Released']]
print(recent_albums)
print("*****************"+"\n")

### Esercizio 5: Calcola la media delle valutazioni
### Task: Calcola la media della colonna 'Rating' per tutti gli album
### Soluzione:
print("***ESERCIZIO 5***")
media_rating = df['Rating'].mean()
print(f"Media Rating:", media_rating)
print("*****************"+"\n")

### Esercizio 6: Trova l'album più lungo e il più breve
### Task: Identifica l'album con la durata massima e minima nella colonna 'Length' e visualizza i suoi dettagli
### Soluzione:
print("***ESERCIZIO 6***")
album_piu_lungo = df.loc[df['Length'].idxmax()]
album_meno_lungo = df.loc[df['Length'].idxmin()]

print(f"Album con la durata massima:")
print(album_piu_lungo, "\n")

print(f"Album con la durata minima:")
print(album_meno_lungo)

# Questo metodo è affidabile solo se tutte le durate hanno lo stesso formato e ordinamento stringa coerente.
# Affidabilità: media. Funziona SOLO se il formato è coerente

print("\nUn'altra opzione da fare:\n")
df['Length_timedelta'] = pd.to_timedelta(df['Length'])
print(f"Album con la durata massima:")
longest_album = df.loc[df['Length_timedelta'].idxmax()]
print(f"Artist: {longest_album['Artist']}, Title: {longest_album['Album']}, Length: {longest_album['Length_timedelta']}")
print(f"\nAlbum con la durata minima:")
shortest_album = df.loc[df['Length_timedelta'].idxmin()]
print(f"Artist: {shortest_album['Artist']}, Title: {shortest_album['Album']}, Length: {shortest_album['Length_timedelta']}")
print("*****************"+"\n")

# Questo metodo è sempre corretto, perché le durate vengono convertite in un tipo numerico/temporale reale.
# Affidabilità: alta. Funziona SEMPRE.


# idxmax() e idxmin() restituisce l’indice dell’album con valore massimo e minimo nella colonna Length.
# loc[...] permette di estrarre l’intera riga corrispondente.
# df.loc[df['Length'].idxmax()]:
#   - una volta per guardare la colonna e calcolare l'indice
#   - una volta per recuperare la riga completa
# il dataframe è lo stesso


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
#  Calcolo la colonna differenza 
df['Sales_Difference'] = df['Claimed Sales (millions)'] - df['Music Recording Sales (millions)']
print(df[['Artist', 'Album', 'Claimed Sales (millions)', 'Music Recording Sales (millions)', 'Sales_Difference']])
print("*****************"+"\n")
  
### Esercizio 9: Trova gli album colonna sonora
### Task: Elenca tutti gli album contrassegnati come 'Soundtrack' (dove la colonna è "Y")
### Soluzione:
print("***ESERCIZIO 9***")
colonna_son = df[df['Soundtrack'] == "Y"]
print(colonna_son)
print()
print(colonna_son[['Artist', 'Album']])
print("*****************"+"\n")

# df['Soundtrack'] == "Y" --> non restituisce un DataFrame.
# Restituisce una Series booleana, cioè una colonna fatta di True e False (crea un filtro booleano)

# df[...] --> applica il filtro e restituisce solo le righe che soddisfano la condizione

### Esercizio 10: Salva i dati filtrati in un file CSV
### Task: Salva tutti gli album con una valutazione (Rating) ≥ 9 in un nuovo file CSV
### Soluzione:
print("***ESERCIZIO 10***")
valutazione_maggiore_uguale_9 = df[df['Rating'] >= 9]
valutazione_maggiore_uguale_9.to_csv("album_rating_9.csv", index=False)
print("File 'album_rating_9.csv' salvato correttamente")
print("******************"+"\n")

# index=True --> per default salva anche l’indice come colonna nel CSV
# index=False --> Non salva l’indice, solo i dati reali

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
# Trovo l'indice dell'album con la differenza massima
idxmax_diff = df['Sales_Difference'].idxmax()

# Recupero i dettagli dell'album (loc per recuperare i dettagli dell’album)
album_maggiore_dif = df.loc[idxmax_diff]
print(album_maggiore_dif)
print()
max_diff_album = df.loc[df['Sales_Difference'].idxmax()]
print(f"Artist: {max_diff_album['Artist']}, Album: {max_diff_album['Album']}, Sales Difference: {max_diff_album['Sales_Difference']}")

print("******************"+"\n")
  
### Esercizio 13: Filtra gli album per generi multipli
### Task: Crea un nuovo DataFrame contenente gli album che includono entrambi "rock" e "pop" nella colonna 'Genre'
### Soluzione:**  
print("***ESERCIZIO 13***")
album_rock_pop = df[df['Genre'].str.contains('rock', case=False) & df['Genre'].str.contains('pop', case=False)]
print(album_rock_pop)
print()
print(f"Artist: {album_rock_pop['Artist']}, Album: {album_rock_pop['Album']}")
print("******************"+"\n")

# df['Genre'].str.contains('rock', case=False) → crea una Series booleana con True per tutte le righe che 
# contengono "rock". Stessa cosa per "pop"
# L’operatore "&" serve a prendere solo le righe dove entrambe le condizioni sono True.
# df[...] applica il filtro e restituisce il DataFrame finale.

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
# Filtro gli album che NON sono colonna sonora
non_soundtrack = df[df['Soundtrack'] != "Y"]
print(non_soundtrack)

# Trovo l'indice con l'album cn le maggiori "Music Recording Sales"
idx_max_sales = non_soundtrack['Music Recording Sales (millions)'].idxmax()

# Recupero i dettagli dell'album
album_piu_venduto = df.loc[idx_max_sales]
print(album_piu_venduto)
print(df.dtypes)
print("******************"+"\n")

# df['Soundtrack'] != "Y" --> prende solo album non colonna sonora
# idxmax() sulla colonna Music Recording Sales (millions) --> trova l’indice dell’album con più vendite (idxmax())
# loc[...] --> recupera i dettagli completi dell’album