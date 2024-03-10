# Importing the necessary Python modules.
import streamlit as st

# Import necessary functions from web_functions
from web_functions import load_data

# Import pages
from Tabs import home, data, predict, visualise, about

# Configure the app
st.set_page_config(
    page_title='CreditCard Fraud Detector',
    layout='wide',
    initial_sidebar_state='auto'
)

# Dictionary for pages
Tabs = {
    "Home": home,
    "About": about,
    "Data Info": data,
    "Prediction": predict,
    "Visualisation": visualise
}

# Create a sidebar
# Add title to sidebar
st.sidebar.title("Navigation")

# Create buttons to select the page
selected_page_home = st.sidebar.button(label="Home", key="home_button", on_click=lambda: set_page("Home"), use_container_width=True)
selected_page_about = st.sidebar.button(label="About", key="about_button", on_click=lambda: set_page("About"), use_container_width=True)
selected_page_data_info = st.sidebar.button(label="Data Info", key="data_info_button", on_click=lambda: set_page("Data Info"), use_container_width=True)
selected_page_prediction = st.sidebar.button(label="Prediction", key="prediction_button", on_click=lambda: set_page("Prediction"), use_container_width=True)
selected_page_visualisation = st.sidebar.button(label="Visualisation", key="visualisation_button", on_click=lambda: set_page("Visualisation"), use_container_width=True)

# Initialize the page variable with a default value
page = st.session_state.page if "page" in st.session_state else "Home"

# Set the page based on the clicked button
def set_page(selected_page):
    st.session_state.page = selected_page

# Loading the dataset.
df, X, y = load_data()

# Call the app function of the selected page to run
if page == "Visualisation":
    Tabs[page].app(df, X, y)
elif page == "Prediction":
    Tabs[page].app(df)
elif page == "Data Info":
    Tabs[page].app(df)
else:
    Tabs[page].app()
