import streamlit as st
from datetime import datetime, date, timedelta
import pandas as pd

st.title("Stock Tracking Dashboard")

option = st.sidebar.selectbox("Which Dashboard?", ('FANG', 'INDEX', 'IBD', 'Master', 'SPDR'))

timing = st.sidebar.selectbox("What Timeframe?", ('Daily', 'Weekly', 'Both'))

st.header(option)

if option == "FANG":
    symbols=['QQQ', 'AAPL', 'AMZN', 'MSFT', 'GOOGL', 'FB', 'NFLX', 'NVDA', 'TSLA', 'ADBE', 'PYPL', 'SQ', 'SE', 'ROKU', 'SHOP', 'MELI', 'TWLO', 'DOCU', 'ZM', 'ZS', 'NOW', 'TWLO', 'COUP', 'MTCH', 'SNAP',
             'CRWD', 'NET', 'FTNT', 'TTD', 'CRM', 'TEAM', 'ASML', 'LRCX', 'AMAT', 'AMD', 'TSM', 'TXN', 'CMG', 'COST', 'TGT', 'NKE', 'LULU', 'CROX', 'SBUX', 'HD', 'IDXX', 'INTU', 'ISRG', 'SNPS', 'UNH',
             'DPZ', 'DXCM', 'VEEV', 'WST', 'GNRC', 'AMT', 'ADI', 'TMO', 'ACN', 'HUBS', 'WDAY', 'ABNB', 'DASH', 'UBER', 'PLTR', 'SNOW', 'DDOG', 'DT']

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
    symbols=['SPY', 'QQQ', 'DIA', 'IWM', 'VTI', 'VIXY', 'SQQQ', 'TQQQ', 'SSO', 'UPRO', 'SPXL', 'XLK','SMH', 'IGV', 'TAN', 'ARKK', 'ARKG', 'ARKF', 'ARKQ', 'ARKX', 'CIBR',
             'AAPL', 'AMZN', 'MSFT', 'FB', 'GOOGL', 'NFLX', 'NVDA', 'TSLA', 
             'ADBE', 'NOW', 'PYPL', 'SQ', 'SE', 'SHOP', 'MELI', 'ROKU', 'DOCU', 'TWLO', 'ZM', 'ZS',
             'LRCX', 'ASML', 'AMAT', 'AMD', 'TSM','SNAP', 'CRWD', 'NET', 'PINS', 'ABNB', 'DASH', 'PLTR', 'SNOW', 'DDOG', 'UPST', 'CELH']

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
    symbols=['XLK', 'XLY', 'XLP', 'XLRE', 'XLE', 'XLV', 'XLB', 'XLI', 'XLF', 'XLU', 'XLC', 'XHB', 'XSW', 'XSD', 'KRE', 'XME', 'XRT','XOP', 'GLD', 'KBE', ]

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


