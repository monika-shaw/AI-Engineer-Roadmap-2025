import os
import streamlit as st
from data_processing import load_data

def main():
    st.title("Netflix Titles Dashboard")
    st.markdown("Exploratory dashboard of Netflix Movies & TV Shows")

    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, '..', 'data', 'netflix_titles.csv')

    df = load_data(data_path)

    st.subheader("Raw Data Sample")
    st.dataframe(df.head(10))

if __name__ == "__main__":
    main()
