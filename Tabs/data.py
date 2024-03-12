import streamlit as st
import pandas as pd
import os

def app(df):
    """This function creates the Data Info page"""

    # Add title to the page
    st.title("Data Info page")

    # Define the directory containing the stats files
    stats_dir = "stats"

    # Read and display the content of each CSV file in the stats directory
    for filename in os.listdir(stats_dir):
        file_path = os.path.join(stats_dir, filename)
        
        # Check if the file is a CSV file
        if filename.endswith(".csv"):
            # Remove the file extension from the filename
            filename_without_extension = os.path.splitext(filename)[0]
            # Display the data from CSV files
            with st.expander(filename_without_extension):
                data = pd.read_csv(file_path)
                st.dataframe(data)
