# Import necessary modules
import streamlit as st


def app(df):
    """This function creates the Data Info page"""

    # Add title to the page
    st.title("Data Info page")

    # Add subheader for the section
    st.subheader("View Data")

    # Create an expansion option to check the data
    with st.expander("View data"):
        st.dataframe(df)

    # Create a section to columns values
    # Give subheader
    st.subheader("Columns Description:")

    # Create a checkbox to get the summary.
    with st.expander("View Summary"):
        st.dataframe(df.describe())

    # Create multiple check boxes in a row
    col_name, col_dtype, col_data = st.columns(3)

    # Show name of all dataframe
    with col_name:
        with st.expander("Column Names"):
            st.dataframe(df.columns, width=300)

    # Show datatype of all columns
    with col_dtype:
        with st.expander("Columns data types"):
            dtypes = df.dtypes.apply(lambda x: x.name)
            st.dataframe(dtypes, width=300)

    # Show data for each column
    with col_data:
        with st.expander("Columns Data"):
            col = st.selectbox("Column Name", list(df.columns))
            st.dataframe(df[col], width=300)

    # Section to describe the data
    st.subheader("Data Description:")
    with st.expander("Data Statistics"):
        st.write("Number of Rows:", df.shape[0])
        st.write("Number of Columns:", df.shape[1])
        st.write("Data Types:", df.dtypes.unique())

    # Section to check for null values
    st.subheader("Null Values:")
    with st.expander("Check for Null Values"):
        null_counts = df.isnull().sum()
        st.write("Number of Null Values in Each Column:")
        st.dataframe(null_counts)

        st.write("Columns with Null Values:")
        st.write(null_counts[null_counts > 0].index.tolist())
