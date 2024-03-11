# Import necessary modules
import streamlit as st

def app():
    """This function creates the home page"""

    # Create a container for hero section
    col1, col2 = st.columns(2)

    # Left column with header, paragraph, and project information
    with col1:
        st.header("Welcome to CreditCard Fraud Detector")
        st.write("""
        This web app is created to detect credit card fraud. It uses the credit card dataset to train the model and predict fraud. The dataset is processed to perform feature and target split. The model is trained using the Random Forest Classifier, and predictions are made on unseen data. The performance of the model is evaluated using precision, recall, and f1-score metrics.
        """)

        # Project information
        st.subheader("Project Information")
        st.markdown("""
        This project is realized by **El Bachir Outidrarine** and **Khaoula Baraka** as a school project in ML, big data, and cloud computing at ENSET Mohammedia.
        """)

    # Right column with image
    with col2:
        st.image("./images/home.png", caption='Fraud Detection', use_column_width=True)

    # Overview of each page
    st.subheader("Overview of Pages")
    st.markdown("""
    - **[Forest](#):** Visualize individual trees in the Random Forest.
    - **[Data Info](#):** Explore information about the dataset.
    - **[Prediction](#):** Make predictions using the pre-trained model.
    - **[Visualisation](#):** Visualize data and model performance.
    """)
