# Import necessary modules
import streamlit as st
from PIL import Image
from web_functions import visualize_trees, get_number_of_trees

def app():
    st.balloons()
    # Add title to the page with a tree icon
    st.title('Random Forest Trees Visualization 🌲🌳')

    # Session state to keep track of the current tree index
    session_state = st.session_state
    if 'current_tree_index' not in session_state:
        session_state.current_tree_index = 0

    # Add a button to go to the next tree
    if st.button("Next Tree ➡️"):
        session_state.current_tree_index = (session_state.current_tree_index + 1) % get_number_of_trees()
        
        # Use st.spinner to indicate ongoing calculations
        with st.spinner("Calculating..."):
            visualize_trees(session_state.current_tree_index)
        
    # Add a button to trigger the tree visualization
    if st.button("Visualize Random Forest Trees (Click Here)", type="primary"):
        # Use st.spinner to indicate ongoing calculations
        with st.spinner("Calculating..."):
            visualize_trees(session_state.current_tree_index)
