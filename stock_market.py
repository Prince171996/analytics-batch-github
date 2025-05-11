import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import datetime

st.title('Stock Market Analysis')
st.write('This is my 1st App')
inputer = st.text_input("Name Of stock", "TSLA",key='placeholder')
ticker_symbol = inputer
tickler_data = yf.Ticker(ticker_symbol)
col1,col2 = st.columns(2)
with col1:
    sd=st.date_input("Enter start date", datetime.date(2019, 7, 6))
with col2:
    ed=st.date_input("Enter end date", datetime.date(2020, 1, 1))


ticker_df = tickler_data.history(period='1d',start=f'{sd

}',end=f'{ed}')

st.write(f'your are visiting info {ticker_symbol}')
st.write(ticker_df)
col1, col2= st.columns(2)

with col1:
    st.header('Volume')
    st.line_chart(ticker_df['Volume'])

with col2:
    st.header("Closing Price")
    st.line_chart(ticker_df['Close'])