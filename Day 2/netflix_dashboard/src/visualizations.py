import matplotlib.pyplot as plt
import seaborn as sns

def plot_type_distribution(df):
    plt.figure(figsize=(8,6))
    sns.countplot(data=df, x='type', palette='pastel')
    plt.title('Distribution of Movies vs TV Shows')
    plt.xlabel('Type')
    plt.ylabel('Count')
    plt.tight_layout()
    return plt
