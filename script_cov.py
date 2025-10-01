import pandas as pd

# leggi il CSV
data = pd.read_csv("unico.csv")

# seleziona solo variabili numeriche
num_data = data.select_dtypes(include=['float64', 'int64'])

# matrice di correlazione
cor_matrix = num_data.corr()

# soglia per considerare "forte" una correlazione
threshold = 0.7

# lista per salvare i risultati
strong_corrs = []

for col1 in cor_matrix.columns:
    for col2 in cor_matrix.columns:
        if col1 < col2:  # evita duplicati e auto-correlazioni
            value = cor_matrix.loc[col1, col2]
            if abs(value) >= threshold:
                strong_corrs.append((col1, col2, value))

# ordina per valore assoluto della correlazione (dalla più forte)
strong_corrs = sorted(strong_corrs, key=lambda x: abs(x[2]), reverse=True)

# salva report in CSV
report = pd.DataFrame(strong_corrs, columns=["Variabile 1", "Variabile 2", "Correlazione"])
report.to_csv("strong_correlations_report.csv", index=False)

print("Report salvato in 'strong_correlations_report.csv'")
print(report)
