import streamlit as st

st.title("❗About")

def about_page():
    """Displays information about the project owner and development process on the About page."""

    st.title("About the project")

    st.markdown(
        """
        **Project Owner:** C.Harshavardhan Reddy 
        **B.TECH CSE With AI & ML**

        **Development Process:**

        This stock value prediction model was created using Streamlit, a Python library for building user interfaces for data science applications. It involved several steps:

        1. **Data Collection:** I used pandas-datareader package and yfinance (yahoo finance) package to retrieve stock data from the past to till today.
        2. **Data Preprocessing:** I loaded the data into pandas DataFrame and removed uneccessary values, left only "Close" time values and then loaded them into an numpy array.
        3. **Model Selection:** I chose the Keras model from Tensorflow, to train it i feeded it the arrays data into the model and compiled it using the adam optimiser.
        4. **Visualisation:** I used streamlit package to create the front end of my project and used Matplotlib to display the graphs of stock value data.
        5. **Additional Features:** Using streamlit i added autocomplete suggestion feature while searching for the stock ticker.
        """
    )
    st.title("THANK YOU!")
about_page()
