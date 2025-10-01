import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# leggi il CSV
data = pd.read_csv("unico.csv")

# seleziona solo le colonne numeriche
num_data = data.select_dtypes(include=['float64', 'int64'])

# calcola la matrice di correlazione
cor_matrix = num_data.corr()

# crea la heatmap delle correlazioni
plt.figure(figsize=(12, 10))
sns.heatmap(cor_matrix, annot=True, cmap="coolwarm", fmt=".2f", 
            square=True, cbar=True)

# salva il grafico in PNG
plt.savefig("correlation_plot.png", dpi=300, bbox_inches="tight")
plt.close()
