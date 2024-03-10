import warnings
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Import necessary functions from web_functions
from web_functions import train_model

def app(df, X, y):
    """This function creates the visualisation page"""

    # Set the page title
    st.title("Visualise Some Demographics")

    # Create an expander for the correlation heatmap
    with st.expander("Show the correlation heatmap"):
        # Create a checkbox to conditionally execute code
        if st.checkbox("Load Correlation Heatmap"):
            st.subheader("Correlation Heatmap")

            fig = plt.figure(figsize=(25, 25))
            ax = sns.heatmap(df.iloc[:, 1:].corr(), annot=True)
            bottom, top = ax.get_ylim()
            ax.set_ylim(bottom + 0.5, top - 0.5)
            st.pyplot(fig)

    # Create an expander for boxplots
    with st.expander("Show Boxplots for Each Feature (Grouped by Class)"):
        # Create a checkbox to conditionally execute code
        if st.checkbox("Load Boxplots Details"):
            for col in df.columns:
                if col != 'Class':
                    plt.figure(figsize=(10, 4))
                    sns.boxplot(data=df, x='Class', y=col)
                    st.pyplot()

    # Create an expander for individual variable distributions
    with st.expander("Show Individual Variable Distribution"):
        # Create a checkbox to conditionally execute code
        if st.checkbox("Load Individual Variable Distribution Details"):
            numerical_features = [feature for feature in df.columns if df[feature].dtype != 'O']
            for feature in numerical_features:
                # Create a new figure for each feature
                plt.figure(figsize=(10, 4))

                try:
                    sns.distplot(df[feature])

                    # Show the distribution plot using Streamlit's pyplot function
                    st.pyplot()
                except Exception as e:
                    # Handle exceptions (e.g., if the feature contains non-numeric values)
                    st.warning(f"Unable to plot distribution for {feature}: {str(e)}")
