import warnings
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import os

def app(df, X, y):
    """This function creates the visualisation page"""
    # Remove the warnings
    warnings.filterwarnings('ignore')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    
    # Set the page title
    st.title("Visualise Some Demographics")

    # Create an expander for the correlation heatmap
    with st.expander("Show the correlation heatmap"):
    # Use st.image to display the saved heatmap image
        st.image("heatmap/heatmap.png")
    # Create an expander for boxplots
    # Path to the directory containing the box plot images
    boxplot_dir = "boxplot"

    # Create an expander to show the box plots
    with st.expander("Show Boxplots for Each Feature (Grouped by Class)"):
        # Create a checkbox to conditionally execute code
        if st.checkbox("Load Boxplots Details"):
            # Use st.spinner to indicate ongoing calculations
            with st.spinner("Calculating..."):
                # Iterate over each file in the boxplot directory
                for filename in os.listdir(boxplot_dir):
                    # Check if the file is a PNG image
                    if filename.endswith(".png"):
                        # Display the image using st.image
                        st.image(os.path.join(boxplot_dir, filename))

    distribution_dir = "distribution"

    # Create an expander for individual variable distributions
    with st.expander("Show Individual Variable Distribution"):
        # Create a checkbox to conditionally execute code
        if st.checkbox("Load Individual Variable Distribution Details"):
            # Use st.spinner to indicate ongoing calculations
            with st.spinner("Calculating..."):
                # Iterate over each file in the distribution directory
                for filename in os.listdir(distribution_dir):
                    # Check if the file is a PNG image
                    if filename.endswith(".png"):
                        # Display the image using st.image
                        st.image(os.path.join(distribution_dir, filename))
