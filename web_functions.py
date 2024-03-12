# Import necessary modules
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import streamlit as st
import gdown
import os
import joblib
import warnings
from sklearn.tree import DecisionTreeClassifier, plot_tree

warnings.filterwarnings('ignore')
st.set_option('deprecation.showPyplotGlobalUse', False)

@st.cache_data
def load_data():
    """This function returns the preprocessed data"""
    # Load the Diabetes dataset into DataFrame.
    #file_id = '1DiDDLCJE3DkD7Q7SolFMsAG4hladL5SU'
    #url = f'https://drive.google.com/uc?id={file_id}'
    #output = 'creditcard1.csv'
    # Check if the file already exists locally
    #if not os.path.exists(output):
        # Download the file only if it doesn't exist locally
        #gdown.download(url, output, quiet=False)
    #df = pd.read_csv(output)
    df =''

    # Perform feature and target split
    # Feature selection
    X = ''

    # Target selection
    y = ''

    return df, X, y

@st.cache_resource
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

# Load column names from stats/columns.csv
columns = pd.read_csv("stats/columns.csv").squeeze()

def visualize_trees(current_tree_index):
    model = load_pretrained_model()
    
    # Get the individual trees in the random forest
    trees = model.estimators_
    
    st.subheader(f"Tree {current_tree_index + 1}")
    st.write(f"The total number of trees in the forest is {len(trees)}")
    plot_tree(trees[current_tree_index], filled=True, feature_names=columns, class_names=["Normal", "Fraud"])
    st.pyplot()

def get_number_of_trees():
    return len(load_pretrained_model().estimators_)