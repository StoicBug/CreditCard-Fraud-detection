# Import necessary modules
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import streamlit as st
import gdown
import os
import joblib
import warnings

warnings.filterwarnings('ignore')
st.set_option('deprecation.showPyplotGlobalUse', False)

@st.cache_data()
def load_data():
    """This function returns the preprocessed data"""
    # Load the Diabetes dataset into DataFrame.
    file_id = '1DiDDLCJE3DkD7Q7SolFMsAG4hladL5SU'
    url = f'https://drive.google.com/uc?id={file_id}'
    output = 'creditcard1.csv'
    # Check if the file already exists locally
    if not os.path.exists(output):
        # Download the file only if it doesn't exist locally
        gdown.download(url, output, quiet=False)
    df = pd.read_csv(output)

    # Perform feature and target split
    # Feature selection
    X = df.drop('Class', axis=1)

    # Target selection
    y = df['Class']

    return df, X, y

@st.cache_data()
def load_pretrained_model():
    """This function loads the pre-trained model"""
    # Specify the path to your pre-trained model
    model_path = 'random_forest_model.joblib'

    # Load the pre-trained model
    model = joblib.load(model_path)

    return model


def predict(features):
    """This function makes predictions using the pre-trained model"""
    # Predict the value
    prediction = load_pretrained_model().predict(np.array(features).reshape(1, -1))

    return prediction
