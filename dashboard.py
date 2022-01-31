import streamlit as st
from datetime import datetime, date, timedelta
import pandas as pd

st.title("Stock Tracking Dashboard")

option = st.sidebar.selectbox("Which Dashboard?", ('FANG', 'INDEX', 'IBD', 'Master', 'DOW'))

timing = st.sidebar.selectbox("What Timeframe?", ('Daily', 'Weekly', 'Both'))

st.header(option)

if option == "FANG":
    symbols=['SPY', 'QQQ', 'DIA', 'IWM', 'VTI', 'VIXY', 'XLK','SMH', 'IGV', 'TAN', 'TLT', 'ARKK', 'FFTY', 'SQQQ', 'TQQQ', 'SSO', 'UPRO', 'QLD', 'SPXL', 'SOXL',
             'TECL', 'TNA', 'UDOW', 'ERX', 'FAS', 'LABU', 'NUGT', 'JNUG', 'GUSH',
             'XLK', 'XLY', 'XLP', 'XLRE', 'XLE', 'XLV', 'XLB', 'XLI', 'XLF', 'XLU', 'XLC', 'XHB', 'XSW', 'XSD', 'KRE', 'XME', 'XRT','XOP', 'GLD', 'KBE',
             'AAPL', 'AMZN', 'MSFT', 'GOOGL', 'FB', 'NFLX', 'NVDA', 'TSLA', 'ADBE', 'NOW', 'CRM', 'TEAM', 'ASML', 'LRCX', 'AMAT', 'AMD', 'TSM', 'MU',
             'FTNT', 'TTD',  'COST', 'HD', 'INTU', 'ISRG', 'SNPS', 'ACN', 'ABNB','SNOW', 'DDOG', 'RBLX', 'MDB', 'CRWD', 'NET', 'APPS', 'SHOP', 'ETSY',
             'OKTA', 'ZS', 'PANW', 'ANET', 'JNPR', 'TWLO', 'ROKU', 'U', 'DOCU', 'ZM', 'UBER']

    if timing == "Daily":
        for stock in symbols:
            st.image(f"https://charts2.finviz.com/chart.ashx?t={stock}&ty=c&ta=1&p=d&tas=0")

    if timing == "Weekly":
        for stock in symbols:
            st.image(f"https://finviz.com/chart.ashx?t={stock}&ta=0&ty=c&p=w&s=l", width=None)

    if timing == "Both":
        for stock in symbols:
            st.image(f"https://charts2.finviz.com/chart.ashx?t={stock}&ty=c&ta=1&p=d&tas=0")
            st.image(f"https://finviz.com/chart.ashx?t={stock}&ta=0&ty=c&p=w&s=l", width=None)

if option == "INDEX":
    symbols=['SPY', 'QQQ', 'DIA', 'IWM', 'VTI', 'VIXY', 'SQQQ', 'TQQQ', 'XLK','SMH', 'IGV', 'TAN', 'ARKK', 'FFTY', 'SSO', 'UPRO', 'QLD', 'SPXL', 'SOXL',
             'TECL', 'TNA', 'UDOW', 'ERX', 'FAS', 'LABU', 'NUGT',  'AAPL', 'AMZN', 'MSFT', 'GOOGL', 'FB', 
             'NFLX', 'NVDA', 'TSLA', 'AMD', 'COST', 'HD', 'LOW', 'SHOP', 'ADBE', 'INTU', 'ACN', 'ZS','LRCX', 'ASML', 'AMAT', 'TSM', 'QCOM', 'AVGO', 'MU', 'KLAC', 'TXN',
             'NOW', 'CRM', 'TEAM', 'TTD', 'PYPL', 'SQ', 'SE', 'MELI', 'ROKU', 'DOCU', 'TWLO', 'ZM', 'SPOT', 'OKTA', 'CRWD', 'NET', 'FTNT', 'PANW', 'ANET',
             'ABNB', 'DASH', 'PLTR', 'SNOW', 'DDOG', 'MDB', 'UPST', 'CELH', 'AFRM', 'ASAN', 'RBLX', 'SOFI', 'COIN', 'U', 'ASO', 'ZI', 'ZIM', 'ON', 'MRVL',
             'RIVN', 'LCID', 'HD', 'LOW', 'CROX', 'NKE', 'TGT', 'DPZ', 'LULU', 'ENPH', 'DHI', 'JPM', 'BRK.B', 'GS', 'SCHW', 'BAC', 'CAT', 'DE', 'F', 'GM',
             'XOM', 'CVN', 'DOCN', 'GLBE', 'INMD' 'APPS', 'HOOD', 'GLBE',
              'GBTC', 'BITO', 'ETHE', 'CIBR', 'BUG', 'HACK']

    if timing == "Daily":
        for stock in symbols:
            st.image(f"https://charts2.finviz.com/chart.ashx?t={stock}&ty=c&ta=1&p=d&tas=0")

    if timing == "Weekly":
        for stock in symbols:
            st.image(f"https://finviz.com/chart.ashx?t={stock}&ta=0&ty=c&p=w&s=l", width=None)

    if timing == "Both":
        for stock in symbols:
            st.image(f"https://finviz.com/chart.ashx?t={stock}")
            st.image(f"https://finviz.com/chart.ashx?t={stock}&ta=0&ty=c&p=w&s=l", width=None)


if option == "DOW":
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


