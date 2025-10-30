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

    st.subheader("Raw Data Sample")
    st.dataframe(df.head(10))

    st.subheader("Distribution: Movies vs TV Shows")
    fig1 = plot_type_distribution(df)
    st.pyplot(fig1)

    st.subheader("Trend: Titles Added Over Years")
    if 'year_added' in df.columns:
        fig2 = plot_year_added_trend(df)
        st.pyplot(fig2)
    else:
        st.write("No `year_added` column found.")

if __name__ == "__main__":
    main()
