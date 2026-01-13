import pandas as pd
from typing import Tuple
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
        
class MLPipeline:
    def __init__(self):
        self.data_path = "../dati/RomeHousingPlus-History.csv"
        self.output_plot_scatter_regline: str = "../visual/plot_scatter_regline.png"
        
    def load_data(self) -> pd.DataFrame:
        """Carica dati da un file Excel"""
        return pd.read_csv(self.data_path)    
         
    def process_data(self, df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """Operazioni varie di processamento dati"""
        # predictors = df[["Rooms", "Surface", "Floor_number", "Outdoor_surface"]] # Usare per test di Regressione Lineare Multipla 
        #                                                                          # (NB. Studiabile e valutabile con RMSE e r2, ma non visualizzabile)
        predictors = df[["Outdoor_surface"]] # Predittore maggiormente correlato con target "Rent" (studio effettuato con workflow KNIME) 
        target = df[["Rent"]]
        return predictors, target      

    def build_evaluate_visualise_ml_model(self, X: pd.DataFrame, y: pd.DataFrame) -> None:
        """Crea, valuta e visualizza un modello di Machine Learning (i.e., Regressione Lineare)""" 
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)
        deg = 1
        poly_features = PolynomialFeatures(degree=deg, include_bias=False)
        X_train_poly = poly_features.fit_transform(X_train)  
        X_test_poly = poly_features.transform(X_test)
        model = LinearRegression()
        model.fit(X_train_poly, y_train)        
        # Stampa grado, intercetta e coefficienti
        print(f"      Degree: {deg}")
        print(f"      Intercept: {model.intercept_}")
        print(f"      Coefficients: {model.coef_}")
        # Recupera i nomi delle features (predittori)
        feature_names = poly_features.get_feature_names_out([X_test.columns[0]])
        # feature_names = poly_features.get_feature_names_out([X_test.columns[0], X_test.columns[1]])
        print("      Feature names in order:")
        for i, name in enumerate(feature_names):
            print(f"        Coefficient {i}: {name}")        
        y_hat = model.predict(X_test_poly) 
        # Stampa le metriche di performance
        rmse = root_mean_squared_error(y_test, y_hat)
        r2 = r2_score(y_test, y_hat)
        print(f"      RMSE: {rmse}")
        print(f"      R-squared: {r2}")
        # Visualizza dati (scatter plot) e curva di regressione
        plt.figure(figsize=(10, 6))
        # Plot dei punti associati ai dati
        plt.scatter(X_test, y_test, color='blue', label='Actual', alpha=0.7)
        # Crea un DataFrame con X_test e y_hat per ordinamento volto a consentire un corretto plottaggio di matplotlib
        results_df = X_test.copy()
        results_df['y_hat'] = y_hat       
        # Ordina per la colonna X column (assumendo un solo predittore)
        # Se X ha più colonne (Rgressione Lineare Multipla), specifica il nome della colonna (predittore)
        x_column = X_test.columns[0]  # Prendi il nome della prima colonna 
        results_df_sorted = results_df.sort_values(by=x_column)       
        # Estrai i valori ordinati
        X_test_sorted = results_df_sorted[x_column]
        y_hat_sorted = results_df_sorted['y_hat']
        # print(X_test.head(50))
        # print(X_test_sorted.head(50))
        # Plot della curva di regressione con valori ordinati (per evitare zig-zag nel caso di deg > 1)  
        plt.plot(X_test_sorted, y_hat_sorted, color='red', linewidth=3, label='Regression Line')
        # Aggiungi titolo ed etichette degli assi
        X_name = X_test.columns.tolist()[0]
        y_name =y_test.columns.tolist()[0]
        title = str(y_name) + " vs. " + str(X_name) + " (Regression Line's Degree = " + str(deg) + ")"       
        ylabel = y_name
        plt.title(title) 
        plt.xlabel(X_name)
        plt.ylabel(ylabel)
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.savefig(self.output_plot_scatter_regline)
        plt.show()
        plt.close()  
              
    def run_pipeline(self) -> None:
        """Esegue la pipeline completa"""
        # Caricamento dati
        raw_df = self.load_data()
        print("   -Letti dati da un file sorgente")
        # Processamento dati
        X, y = self.process_data(raw_df)
        print("   -Processamento dati completato")       
        # Costruisce, valuta e visualizza un modello di Machine Learning
        self.build_evaluate_visualise_ml_model(X, y)
        print("   -Modello di Machine Learning creato, valutato e visualizzato")        
    
if __name__ == "__main__":
    pipeline = MLPipeline() 
    print("Pipeline avviata...")
    pipeline.run_pipeline() # Esegui la pipeline
    print("Pipeline completata con successo!")    

