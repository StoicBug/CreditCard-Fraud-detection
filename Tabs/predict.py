# Import necessary modules
import streamlit as st
import pandas as pd

# Import necessary functions from web_functions
from web_functions import predict

def preprocess_time(raw_time):
    """Function to preprocess the 'time' feature."""
    return ((raw_time / 3600) % 24)

def app(df):
    """This function creates the prediction page"""

    # Add title to the page
    st.title("Credit Card Fraud Detection Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app utilizes machine learning for Credit Card Fraud Detection.
            </p>
        """, unsafe_allow_html=True)

    st.write("You can get csv data from this data set to test with: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud")
    
    # Option to upload a CSV file
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file is not None:
        # Read the CSV file
        uploaded_df = pd.read_csv(uploaded_file)
        uploaded_df = uploaded_df.drop(columns=['Class'])   
        # Display the uploaded dataframe
        st.subheader("Uploaded DataFrame:")
        st.write(uploaded_df)

        # Preprocess the 'time' column
        uploaded_df['Time'] = uploaded_df['Time'].apply(preprocess_time)

        # Get predictions for each row using the pre-trained model
        predictions = []
        for index, row in uploaded_df.iterrows():
            row_features = row.tolist()
            prediction = predict(row_features)
            predictions.append(prediction)

        # Add a new column to the dataframe with the predictions
        uploaded_df['Prediction'] = predictions

        # Display the dataframe with predictions
        st.subheader("DataFrame with Predictions:")
        # Define a function to apply color to the entire row based on the Prediction column
        def highlight_fraud(row):
            color = 'red' if row['Prediction'] == 1 else 'green'
            return [f'background-color: {color}' for _ in row]

        # Apply the styling function to the entire DataFrame
        styled_df = uploaded_df.style.apply(highlight_fraud, axis=1)

        # Display the styled DataFrame
        st.dataframe(styled_df)
    else:
        st.info("Upload a CSV file to get predictions.")
