import os
import streamlit as st
from data_processing import load_data, clean_data, feature_engineering
from visualizations import plot_type_distribution, plot_year_added_trend

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

if __name__ == "__main__":
    main()
