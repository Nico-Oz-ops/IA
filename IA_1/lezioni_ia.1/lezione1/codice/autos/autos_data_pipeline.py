import pandas as pd
import numpy as np
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

class DataSourceConfig: # classe che permette la configurazione delle sorgenti e destinazione output
    """Configurazione sorgenti dati e destinazione output"""
    remote_url: str = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
    db_uri: str = "postgresql+psycopg://postgres:postgres@postgresql:5432/auto_db"
    csv_path: str = "../../dati/autos/auto.csv" # creo il percorso di salvataggio del file csv con i dati grezzi
    csv_clean_path: str = "../../dati/autos/auto_clean.csv" # percorso di salvataggio del file csv con i dati puliti
    output_plot: str = "../../visual/autos/plot.png" # percorso di salvataggio dei plot dei dati puliti

class DataPipeline: # classe inizializzata con istanza di DSC, permette di caricare, salvare, pulire e visualizzare i dati 
    def __init__(self, config: DataSourceConfig):
        self.config = config
        self.data = None
        
    def load_from_csv(self) -> pd.DataFrame: # carica i dati CSV tramite il suo percorso definito in DSC
        """Carica dati da un file CSV"""
        return pd.read_csv(self.config.csv_path)       

    def load_from_remote(self) -> pd.DataFrame:
        """Carica dati da un file remoto identificato da un URL aggiungendo intestazioni"""
        headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
                  "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
                  "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
                  "peak-rpm","city-mpg","highway-mpg","price"]
        return pd.read_csv(self.config.remote_url, names = headers)
    
    def save_on_csv(self, df: pd.DataFrame) -> None: # metodo che serve a salvare i dati grezzi in un file CSV
        """Salva dati in un file CSV"""
        df.to_csv(self.config.csv_path)    
        
    def save_clean_on_csv(self, df: pd.DataFrame) -> None: # metodo che serve a salvare i dati puliti in un file CSV
        """Salva dati puliti in un file CSV"""
        df.to_csv(self.config.csv_clean_path)    
    
    def store_on_database(self, df: pd.DataFrame) -> None: # serve per scrivere dati in un database PostgreSQL
        """Scrive dati in un database PostgreSQL"""      
        table_name = "auto_info"
        engine = create_engine(self.config.db_uri) # apre la connessione
        try:
            with engine.begin() as conn:  # begin() per gestione automatica di commit/rollback
                df.to_sql(table_name, con=conn, if_exists='replace', index=False)
        except SQLAlchemyError as e: # SQLAlchemy serve a fare da ponte tra Python e PostgreSQL
            print(f"Error di scrittura in database: {e}")
        finally:
            engine.dispose()  # Chiusura pulita e rilascio risorse
        
    def load_from_database(self) -> pd.DataFrame: # si importano o si caricano dati dal database PostgreSQL
        """Carica dati da un database PostgreSQL"""
        query_def = "SELECT * FROM public.auto_info"        
        engine = create_engine(self.config.db_uri)
        try:
            with engine.connect() as conn:
                df = pd.read_sql_query(text(query_def), con=conn)
        except SQLAlchemyError as e:
            print(f"Errore di lettura da database: {e}")
            df = pd.DataFrame() 
        finally:
            engine.dispose()  # Chiusura pulita e rilascio risorse
        return df

    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame: # metodo di pulizia dei dati
        """Operazioni varie di pulizia dati"""
        df.replace("?", np.nan, inplace=True)
        avg = df["normalized-losses"].astype("float").mean(axis = 0) # df["normalized-losses"].astype("float"): stabilisce il tipo di dato per la colonna stabilita
        df["normalized-losses"] = df["normalized-losses"].replace(np.nan, avg) # df["normalized-losses"].replace(np.nan, avg, inplace=True)
        df["num-of-doors"] = df["num-of-doors"].replace(np.nan, df['num-of-doors'].value_counts().idxmax()) # sostituire i valori mancanti NaN nella colonna num-of-doors per il valore più frequente della colonna
        # num_porte = df['num-of-doors'].value_counts().idxmax() ---> un'altra maniera di sostituire NAN
        # df["num-of-doors"] = df["num-of-doors"].replace(np.nan, num_porte)
        # value_counts() → conta
        # idxmax() → sceglie il valore più frequente
        # replace() → riempie i buchi (NaN) con quel valore
        
        df.dropna(subset=["price"], axis=0, inplace = True) #dropna, cancella tutte le righe della colonna "price", con valori NAN
        # df.dropna(axis=0, inplace=True) # serve a cancellare tutte le righe del DF che hanno valori NaN
        df.reset_index(drop = True, inplace = True) # resetta gli indici del dataframe a partire delle modifiche fatte
        df = df.convert_dtypes() # converte in automatico i tipi di dato del DF (completo)
        df[["normalized-losses"]] = df[["normalized-losses"]].astype("int")
        df[["price"]] = df[["price"]].astype("float")
        df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")
        df['make'] = df['make'].replace({'alfa-romero': 'alfa-romeo', 'peugot': 'peugeot'}) #.replace({"chiave":"valore"})---> chiave = valore da sostituire. valore: valore che sostituisce (quello corretto)
        self.save_clean_on_csv(df) # richiamo il metodo di salvataggio per i dati puliti in formato CSV pasando il dataframe
        return df 

    def visualize(self, df: pd.DataFrame) -> None:
        """Crea e salva visualizzazioni"""        
        
    def run_pipeline(self) -> pd.DataFrame:
        """Esegue la pipeline completa"""

        # Carica dati da remoto
        remote_df = self.load_from_remote()
        # print("   -Letto file remoto")
        # print(remote_df.shape)
        # print(remote_df.head(15))
        # print(remote_df.dtypes)
        # print(remote_df.info())
        # return pd.DataFrame()
        
        # Salva dati in locale
        self.save_on_csv(remote_df)
        print("   -Salvato file remoto in locale")

        # Scrive dati in database
        self.store_on_database(remote_df)
        print("   -Scritto file remoto in una tabella su db")

        # Legge dati da database
        db_df = self.load_from_database()
        print("   -Letti dati da una tabella su db")
        # print(db_df.dtypes)
        # return pd.DataFrame()

        # Pulizia dati
        clean_df = self.clean_data(db_df)
        print("   -Pulizia dati completata e file pulito salvato")

        # Visualizza risultati
        self.visualize(clean_df)
        print("   -Analisi e visualizzazione dati terminate")          
        self.data = clean_df
        return clean_df
        
if __name__ == "__main__":
    config = DataSourceConfig()
    pipeline = DataPipeline(config)
    print("Pipeline avviata...")  
    final_df = pipeline.run_pipeline()
    print("Pipeline completata con successo!")
    print(final_df.head())