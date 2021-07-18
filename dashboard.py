import streamlit as st
from datetime import datetime, date, timedelta
import pandas as pd

st.title("Stock Tracking Dashboard")

option = st.sidebar.selectbox("Which Dashboard?", ('FANG', 'INDEX', 'IBD', 'Master', 'SPDR', 'CP'))

timing = st.sidebar.selectbox("What Timeframe?", ('Daily', 'Weekly', 'Both'))

st.header(option)

if option == "FANG":
    symbols=['QQQ', 'AAPL', 'AMZN', 'MSFT', 'GOOGL', 'FB', 'NFLX', 'NVDA', 'TSLA', 'ADBE', 'PYPL', 'SQ', 'SE', 'ROKU', 'SHOP', 'TWLO', 'DOCU', 'ZM', 'ZS', 'NOW',
             'CRWD', 'NET', 'FTNT', 'TTD', 'CRM', 'TEAM', 'ASML', 'LRCX', 'AMAT', 'AMD', 'TSM', 'CMG', 'COST', 'TGT', 'NKE', 'SBUX', 'HD', 'IDXX', 'INTU', 'ISRG', 'SNPS', 'UNH',
             'DPZ', 'VEEV', 'WST', 'ACN' ]

    if timing == "Daily":
        for stock in symbols:
            st.image(f"https://finviz.com/chart.ashx?t={stock}")

    if timing == "Weekly":
        for stock in symbols:
            st.image(f"https://finviz.com/chart.ashx?t={stock}&ta=0&ty=c&p=w&s=l", width=None)

    if timing == "Both":
        for stock in symbols:
            st.image(f"https://finviz.com/chart.ashx?t={stock}")
            st.image(f"https://finviz.com/chart.ashx?t={stock}&ta=0&ty=c&p=w&s=l", width=None)

if option == "INDEX":
    symbols=['SPY', 'QQQ', 'DIA', 'IWM', 'VTI', 'VIXY', 'SQQQ', 'TQQQ', 'SSO', 'UPRO', 'SPXL', 'XLK','SMH', 'IGV', 'TAN', 'ARKK', 'ARKG', 'ARKF', 'ARKQ', 'ARKX',
             'AAPL', 'AMZN', 'MSFT', 'FB', 'GOOGL', 'NFLX', 'NVDA', 'TSLA', 
             'ADBE', 'PYPL', 'SQ', 'SE', 'SHOP', 'ROKU', 'DOCU', 'TWLO', 'ZM', 'ZS',
             'LRCX', 'ASML', 'AMAT', 'AMD', 'TSM','SNAP', 'CRWD', 'NET', 'PINS', 'PTON', 'TWTR', 'NIO']

    if timing == "Daily":
        for stock in symbols:
            st.image(f"https://finviz.com/chart.ashx?t={stock}")

    if timing == "Weekly":
        for stock in symbols:
            st.image(f"https://finviz.com/chart.ashx?t={stock}&ta=0&ty=c&p=w&s=l", width=None)

    if timing == "Both":
        for stock in symbols:
            st.image(f"https://finviz.com/chart.ashx?t={stock}")
            st.image(f"https://finviz.com/chart.ashx?t={stock}&ta=0&ty=c&p=w&s=l", width=None)


if option == "SPDR":
    symbols=['XLK', 'XLY', 'XLP', 'XLRE', 'XLE', 'XLV', 'XLB', 'XLI', 'XLF', 'XLU', 'XLC', 'XHB']

    if timing == "Daily":
        for stock in symbols:
            st.image(f"https://finviz.com/chart.ashx?t={stock}")

    if timing == "Weekly":
        for stock in symbols:
            st.image(f"https://finviz.com/chart.ashx?t={stock}&ta=0&ty=c&p=w&s=l", width=None)

    if timing == "Both":
        for stock in symbols:
            st.image(f"https://finviz.com/chart.ashx?t={stock}")
            st.image(f"https://finviz.com/chart.ashx?t={stock}&ta=0&ty=c&p=w&s=l", width=None)

if option == "IBD":
    with open('ibd') as f:
        symbols=[i.strip() for i in f.readlines()]

    if timing == "Daily":
        for stock in symbols:
            st.image(f"https://finviz.com/chart.ashx?t={stock}")

    if timing == "Weekly":
        for stock in symbols:
            st.image(f"https://finviz.com/chart.ashx?t={stock}&ta=0&ty=c&p=w&s=l", width=None)

    if timing == "Both":
        for stock in symbols:
            st.image(f"https://finviz.com/chart.ashx?t={stock}")
            st.image(f"https://finviz.com/chart.ashx?t={stock}&ta=0&ty=c&p=w&s=l", width=None)

if option == "Master":
    with open('master') as f:
        symbols=[i.strip() for i in f.readlines()]

    if timing == "Daily":
        for stock in symbols:
            st.image(f"https://finviz.com/chart.ashx?t={stock}")

    if timing == "Weekly":
        for stock in symbols:
            st.image(f"https://finviz.com/chart.ashx?t={stock}&ta=0&ty=c&p=w&s=l", width=None)

    if timing == "Both":
        for stock in symbols:
            st.image(f"https://finviz.com/chart.ashx?t={stock}")
            st.image(f"https://finviz.com/chart.ashx?t={stock}&ta=0&ty=c&p=w&s=l", width=None)


if option == "CP":

    d2 = st.date_input('start date', date.today())
    #d2 = d2.strftime("%Y-%m-%d")
    year = d2.strftime("%Y")
    month = d2.strftime("%m")
    day = d2.strftime("%d")
    print(month, day)

    tckr = st.text_input("Enter the symbol: ")    
    #symbols=['XLK', 'XLY', 'XLP', 'XLRE', 'XLE', 'XLV', 'XLB', 'XLI', 'XLF', 'XLU', 'XLC', 'XHB']
    #for stock in symbols:
    st.image(f"http://www.chartpattern.com/charts/{tckr}-{month}-{day}-21.gif")

