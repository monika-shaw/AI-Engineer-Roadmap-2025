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

def plot_year_added_trend(df):
    if 'year_added' in df.columns:
        plt.figure(figsize=(10,6))
        df_year = df['year_added'].value_counts().sort_index()
        sns.lineplot(x=df_year.index, y=df_year.values)
        plt.title('Content Added Over Years')
        plt.xlabel('Year Added')
        plt.ylabel('Number of Titles')
        plt.tight_layout()
        return plt
