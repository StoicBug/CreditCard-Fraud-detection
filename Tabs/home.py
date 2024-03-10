"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("CreditCard Fraud Detector")

    # Add image to the home page
    st.image("./images/home.png", caption='Fraud Detection', use_column_width=True)

    # Add brief describtion of your web app
    st.write("This web app is created to detect credit card fraud. It uses the credit card dataset to train the model and predict the fraud. The dataset is highly imbalanced, so the model is trained using the SMOTE technique to balance the dataset. The model is trained using the Random Forest Classifier and the model is evaluated using the precision, recall, and f1-score. The model is also evaluated using the ROC-AUC curve. The model is deployed using the Streamlit web app.")