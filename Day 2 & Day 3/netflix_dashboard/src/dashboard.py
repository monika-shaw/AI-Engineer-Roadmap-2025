import os
import streamlit as st
from data_processing import load_data, clean_data, feature_engineering
from visualizations import plot_type_distribution, plot_year_added_trend
import matplotlib.pyplot as plt
import seaborn as sns
def main():
    st.title("Netflix Titles Dashboard")
    st.markdown("Exploratory dashboard of Netflix Movies & TV Shows")

    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, '..', 'data', 'netflix_titles.csv')

    df = load_data(data_path)
    df = clean_data(df)
    df = feature_engineering(df)

    st.sidebar.header("🔍 Filter Options")
    type_filter = st.sidebar.multiselect("Select Type:", options=df["type"].unique(), default=df["type"].unique())
    country_filter = st.sidebar.multiselect("Select Country:", options=sorted(df["country"].unique()), default=["United States"])
    year_filter = st.sidebar.slider("Select Year Range (Release):", int(df["release_year"].min()), int(df["release_year"].max()), (2010, 2020))

    filtered_df = df[
        (df["type"].isin(type_filter)) &
        (df["country"].isin(country_filter)) &
        (df["release_year"].between(year_filter[0], year_filter[1]))
    ]

    st.subheader("📋 Filtered Dataset")
    st.write(f"Showing {len(filtered_df)} records after applying filters.")
    st.dataframe(filtered_df.head(10))
    
    st.subheader("🍿 Movies vs TV Shows")
    fig1 = plot_type_distribution(filtered_df)
    st.pyplot(fig1)

    st.subheader("📆 Titles Added Over the Years")
    fig2 = plot_year_added_trend(filtered_df)
    st.pyplot(fig2)

    st.subheader("🌎 Top 10 Countries by Number of Titles")
    top_countries = filtered_df["country"].value_counts().head(10)
    fig3, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=top_countries.values, y=top_countries.index, palette="coolwarm", ax=ax)
    ax.set_xlabel("Number of Titles")
    ax.set_ylabel("Country")
    ax.set_title("Top 10 Countries by Netflix Titles")
    st.pyplot(fig3)

    st.subheader("⭐ Rating Distribution")
    fig4, ax = plt.subplots(figsize=(8, 6))
    sns.countplot(y="rating", data=filtered_df, order=filtered_df["rating"].value_counts().index, palette="muted", ax=ax)
    ax.set_title("Distribution of Ratings")
    st.pyplot(fig4)

if __name__ == "__main__":
    main()
