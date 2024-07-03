import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import yfinance as yf
from datetime import datetime
from keras.models import load_model
import streamlit as st
from streamlit_searchbox import st_searchbox

page_title = "Stock Prediction Model"
page_icon = ":money_with_wings:"
layout = "centered"
st.set_page_config(page_title=page_title, page_icon=page_icon, layout = layout)
st.title(page_title + " " + page_icon)

stock_tickers = [
    "AAPL", "GOOG", "AMZN", "TSLA", "MSFT", "META", "JPM", "BAC", "WMT", "UNH",
    "NVDA", "BRK.B", "HD", "KO", "CVX", "XOM", "LIN", "DIS", "COST", "VZ",
    "RELIANCE.NS", "TCS.NS", "INFY.NS", "HDFC.NS", "ITC.NS", "SBIN.NS", 
    "WIPRO.NS", "HINDUNILVR.NS", "BAJAJFINSV.NS", "MARUTI.NS",
    "NESTLE.NS", "BRITANIA.NS", "ULTRACEMCO.NS", "JSHAHNEL.NS", "ICICI.NS",
    "KOTAKBANK.NS", "AXISBANK.NS", "GRASIM.NS", "DRREDDY.NS", "HINDALCO.NS",
    "TATAPOWER.NS", "UPL.NS", "CIPLA.NS", "POWERGRID.NS", "NTPC.NS",
]

# Function to filter suggestions based on user input
def filter_suggestions(query, options):
    return [t for t in options if query.lower() in t.lower()]

selected_ticker = st.text_input("Enter Stock Ticker:")
filtered_tickers = filter_suggestions(selected_ticker, stock_tickers)
ticker = st.selectbox("Select Stock Ticker:", filtered_tickers, format_func=lambda x: x.upper())


yf.pdr_override()
startdate = datetime(2010,1,1)
enddate = datetime(2024,3,7)
df = pdr.get_data_yahoo(ticker, start = startdate, end = enddate)

#Describing Data
st.subheader("Data from 2010 - 2024")
st.write(df.describe())

#visualisations
st.subheader("Closing Price vs Time chart")
fig = plt.figure(figsize=(12,6))
plt.plot(df.Close)
st.pyplot(fig)


st.subheader("Closing Price vs Time chart")


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))


ma100 = df.Close.rolling(100).mean()
ax1.plot(ma100)
ax1.plot(df.Close)
ax1.set_title("100MA")


ma200 = df.Close.rolling(200).mean()
ax2.plot(ma100, 'r')
ax2.plot(ma200, 'g')
ax2.plot(df.Close, 'b')
ax2.set_title("100MA & 200MA")

plt.tight_layout()
st.pyplot(fig)



data_training = pd.DataFrame(df['Close'][0:int(len(df)*0.70)])
data_testing = pd.DataFrame(df['Close'][int(len(df)*0.70):int(len(df))])

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0,1))

data_training_array = scaler.fit_transform(data_training)

#loading the model
model_path = "C:/Users/chall/OneDrive/Desktop/Finance/Pages/keras_model.h5"
model = load_model(model_path)

#Testing
past_100_days = data_training.tail(100)
final_df = pd.concat([past_100_days, data_testing], ignore_index=True)
input_data = scaler.fit_transform(final_df)


x_test = []
y_test = []

for i in range(100, input_data.shape[0]):
    x_test.append(input_data[i-100: i].reshape(-1, 1))
    y_test.append(input_data[i, 0])

x_test, y_test = np.array(x_test), np.array(y_test)
y_predicted = model.predict(x_test)
scaler = scaler.scale_
scale_factor = 1/scaler[0]
y_predicted = y_predicted * scale_factor
y_test = y_test * scale_factor


#Final Graph

st.subheader("Prediction vs Original")
fig2 = plt.figure(figsize=(12,6))
plt.plot(y_test, 'b', label = 'Original Price')
plt.plot(y_predicted, 'r', label = 'Predicted Price')
plt.xlabel=('Time')
plt.ylabel('Price')
plt.legend()
st.pyplot(fig2)
