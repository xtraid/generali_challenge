import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math

# leggi il CSV
data = pd.read_csv("unico.csv")

# seleziona solo variabili numeriche
num_data = data.select_dtypes(include=['float64', 'int64'])

# calcola la matrice di correlazione
cor_matrix = num_data.corr()

# quante variabili per immagine (puoi cambiare il numero)
vars_per_plot = 10  

# numero totale di variabili
cols = cor_matrix.columns
n_vars = len(cols)

# quante immagini serviranno
n_plots = math.ceil(n_vars / vars_per_plot)

for i in range(n_plots):
    start = i * vars_per_plot
    end = min((i + 1) * vars_per_plot, n_vars)
    subset_cols = cols[start:end]
    
    # sotto-matrice di correlazione
    sub_matrix = cor_matrix.loc[subset_cols, subset_cols]
    
    # disegno
    plt.figure(figsize=(10, 8))
    sns.heatmap(sub_matrix, annot=True, cmap="coolwarm", fmt=".2f", 
                square=True, cbar=True)
    
    # salvo il PNG
    filename = f"correlation_plot_part{i+1}.png"
    plt.savefig(filename, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"Salvato {filename}")
