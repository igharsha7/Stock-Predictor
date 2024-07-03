import streamlit as st

st.set_page_config(
    page_title="Stock Value Prediction",
    page_icon="money_with_wings",
)

st.title("🏠Home")

def home_page():
    """Displays an informative and engaging description of the stock predictor model on the Home page."""

    st.title("Welcome to Stock Value Prediction!")

    st.markdown(
        """
        **What is a Stock Predictor Model?**

        Imagine a tool that can analyze past stock market data and company information to make educated guesses about future stock prices. That's what a stock predictor model aims to do! It's like having a financial assistant who crunches numbers and considers various factors to provide insights into potential stock performance.

        **Think of it like this:**

        * A stock predictor model is like a weather forecast for the stock market. It can't predict with absolute certainty, but it can identify trends and patterns to give you an idea of what might happen next.
        * It's a powerful tool to help you make informed investment decisions, but it's important to remember that it's not a crystal ball.

        **Here's a simplified view of how it works:**

        1. **Data Collection:** The model gathers historical stock prices, company financials, economic indicators, and other relevant information.
        2. **Data Analysis:** It uses complex algorithms to identify patterns and relationships within the data.
        3. **Prediction:** Based on its analysis, the model makes an educated guess about the future direction of the stock price.

        **Things to note:**

        * The stock market is inherently unpredictable. News events, government policies, and unforeseen circumstances can all influence stock prices.
        * Models are only as good as the data they're trained on. High-quality data is crucial for accuracy.
        * Use stock predictor models as a guide, not a guarantee. Always conduct your own research and due diligence before making investment decisions.
        """
    )

# Call the home_page function to display the content
home_page()
