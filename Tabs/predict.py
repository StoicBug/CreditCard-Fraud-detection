# Import necessary modules
import streamlit as st

# Import necessary functions from web_functions
from web_functions import predict

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
    time = st.number_input("Time", value=float(df["Time"].min()))
    v1 = st.number_input("V1", value=float(df["V1"].min()))
    v2 = st.number_input("V2", value=float(df["V2"].min()))
    v3 = st.number_input("V3", value=float(df["V3"].min()))
    v4 = st.number_input("V4", value=float(df["V4"].min()))
    v5 = st.number_input("V5", value=float(df["V5"].min()))
    v6 = st.number_input("V6", value=float(df["V6"].min()))
    v7 = st.number_input("V7", value=float(df["V7"].min()))
    v8 = st.number_input("V8", value=float(df["V8"].min()))
    v9 = st.number_input("V9", value=float(df["V9"].min()))
    v10 = st.number_input("V10", value=float(df["V10"].min()))
    v11 = st.number_input("V11", value=float(df["V11"].min()))
    v12 = st.number_input("V12", value=float(df["V12"].min()))
    v13 = st.number_input("V13", value=float(df["V13"].min()))
    v14 = st.number_input("V14", value=float(df["V14"].min()))
    v15 = st.number_input("V15", value=float(df["V15"].min()))
    v16 = st.number_input("V16", value=float(df["V16"].min()))
    v17 = st.number_input("V17", value=float(df["V17"].min()))
    v18 = st.number_input("V18", value=float(df["V18"].min()))
    v19 = st.number_input("V19", value=float(df["V19"].min()))
    v20 = st.number_input("V20", value=float(df["V20"].min()))
    v21 = st.number_input("V21", value=float(df["V21"].min()))
    v22 = st.number_input("V22", value=float(df["V22"].min()))
    v23 = st.number_input("V23", value=float(df["V23"].min()))
    v24 = st.number_input("V24", value=float(df["V24"].min()))
    v25 = st.number_input("V25", value=float(df["V25"].min()))
    v26 = st.number_input("V26", value=float(df["V26"].min()))
    v27 = st.number_input("V27", value=float(df["V27"].min()))
    v28 = st.number_input("V28", value=float(df["V28"].min()))
    amount = st.number_input("Amount", value=float(df["Amount"].min()))

    # Create a list to store all the features
    features = [time, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20, v21, v22, v23, v24, v25, v26, v27, v28, amount]

    # Create a button to predict
    if st.button("Detect Fraud"):
        # Get prediction and model score
        prediction, score = predict(features)
        score = score
        st.info("Detection Successful...")

        # Print the output according to the prediction
        if prediction == 1:
            st.warning("The transaction is likely fraudulent!")
        else:
            st.success("The transaction appears to be safe.")

        # Print the score of the model 
        st.write("The model has an accuracy of ", round((score * 100)), "%")
