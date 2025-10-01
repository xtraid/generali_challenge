import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import umap
import densitypeakclustering

def test():
    data = pd.read_csv("./data/unico.csv")
    
    # Set the style for the plots
    sns.set(style="whitegrid")

    numeric_data = data.select_dtypes(include=['number'])
    filtered_data = numeric_data[numeric_data["premio"] >= 0]

    filtered_data.reset_index(drop=True, inplace=True)

    print(filtered_data.head())
    print(filtered_data["premio"].min(), filtered_data["premio"].max())

    # Loop through each column in the DataFrame
    for idx, column in enumerate(filtered_data.columns):
        plt.figure(figsize=(10, 6))  # Set the figure size
        sns.histplot(filtered_data[column], bins=50, kde=True)  # Create histogram with KDE
        plt.title(f'Histogram of {column}')  # Title for the histogram
        plt.xlabel(column)  # X-axis label
        plt.ylabel('Frequency')  # Y-axis label
        plt.grid(True)  # Add grid
        plt.savefig(f'plots/{column}.png')  # Display the plot
        plt.close()

if __name__ == "__main__":
    test()