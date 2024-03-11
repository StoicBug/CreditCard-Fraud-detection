# Import necessary modules
import streamlit as st
import joblib

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
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.
    time = st.number_input("Time", key="time_input", value=float(df["Time"].min()))
    v1 = st.number_input("V1", key="v1_input", value=float(df["V1"].min()))
    v2 = st.number_input("V2", key="v2_input", value=float(df["V2"].min()))
    v3 = st.number_input("V3", key="v3_input", value=float(df["V3"].min()))
    v4 = st.number_input("V4", key="v4_input", value=float(df["V4"].min()))
    v5 = st.number_input("V5", key="v5_input", value=float(df["V5"].min()))
    v6 = st.number_input("V6", key="v6_input", value=float(df["V6"].min()))
    v7 = st.number_input("V7", key="v7_input", value=float(df["V7"].min()))
    v8 = st.number_input("V8", key="v8_input", value=float(df["V8"].min()))
    v9 = st.number_input("V9", key="v9_input", value=float(df["V9"].min()))
    v10 = st.number_input("V10", key="v10_input", value=float(df["V10"].min()))
    v11 = st.number_input("V11", key="v11_input", value=float(df["V11"].min()))
    v12 = st.number_input("V12", key="v12_input", value=float(df["V12"].min()))
    v13 = st.number_input("V13", key="v13_input", value=float(df["V13"].min()))
    v14 = st.number_input("V14", key="v14_input", value=float(df["V14"].min()))
    v15 = st.number_input("V15", key="v15_input", value=float(df["V15"].min()))
    v16 = st.number_input("V16", key="v16_input", value=float(df["V16"].min()))
    v17 = st.number_input("V17", key="v17_input", value=float(df["V17"].min()))
    v18 = st.number_input("V18", key="v18_input", value=float(df["V18"].min()))
    v19 = st.number_input("V19", key="v19_input", value=float(df["V19"].min()))
    v20 = st.number_input("V20", key="v20_input", value=float(df["V20"].min()))
    v21 = st.number_input("V21", key="v21_input", value=float(df["V21"].min()))
    v22 = st.number_input("V22", key="v22_input", value=float(df["V22"].min()))
    v23 = st.number_input("V23", key="v23_input", value=float(df["V23"].min()))
    v24 = st.number_input("V24", key="v24_input", value=float(df["V24"].min()))
    v25 = st.number_input("V25", key="v25_input", value=float(df["V25"].min()))
    v26 = st.number_input("V26", key="v26_input", value=float(df["V26"].min()))
    v27 = st.number_input("V27", key="v27_input", value=float(df["V27"].min()))
    v28 = st.number_input("V28", key="v28_input", value=float(df["V28"].min()))
    amount = st.number_input("Amount", key="amount_input", value=float(df["Amount"].min()))

    # Preprocess the 'time' feature
    time = preprocess_time(time)
    # ... (similar input code for other features)

    # Create a list to store all the features
    features = [time, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20, v21, v22, v23, v24, v25, v26, v27, v28, amount]


    if st.button("Detect Fraud", type="primary"):
        # Get prediction using the pre-trained model
        prediction = predict(features)
        st.info("Detection Successful...")

        # Print the output according to the prediction
        if prediction == 1:
            st.warning("The transaction is likely fraudulent!", icon="🚨")
        else:
            st.success("The transaction appears to be safe.", icon="✅")
