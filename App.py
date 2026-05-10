import streamlit as st
import yfinance as yf
import pandas as pd

# Page Configuration
st.set_page_config(layout="wide", page_title="My Chartmaze Clone")

# Custom CSS for Dark Theme Look
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .sidebar .sidebar-content { background-image: linear-gradient(#2e313a,#2e313a); color: white; }
    </style>
    """, unsafe_allow_html=True)

# Sidebar Menu
st.sidebar.title("💎 Pro Screeners")
menu = st.sidebar.radio("Screener List:", [
    "🏠 Dashboard", 
    "📈 Relative Strength (RS)", 
    "🔍 VCP Setup (Volatility)", 
    "📊 Volume Shockers"
])

# Dashboard Logic
if menu == "🏠 Dashboard":
    st.title("🚀 Market Analytics Dashboard")
    ticker = st.sidebar.text_input("Stock Symbol (e.g. RELIANCE.NS)", "BTC-USD")
    
    st.subheader(f"Analyzing: {ticker}")
    data = yf.download(ticker, period="3mo", interval="1d")
    
    if not data.empty:
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Current Price", f"{data['Close'].iloc[-1]:.2f}")
        with col2:
            st.metric("Volume", f"{data['Volume'].iloc[-1]:,}")
            
        st.line_chart(data['Close'])
    else:
        st.error("Invalid Ticker! Please enter a valid symbol.")

# Placeholders for other features
elif menu == "📈 Relative Strength (RS)":
    st.title("Relative Strength (RS) Scanner")
    st.info("Comparing stocks against Nifty 50... Logic coming soon.")

elif menu == "🔍 VCP Setup (Volatility)":
    st.title("VCP (Volatility Contraction) Scanner")
    st.warning("Identifying tight setups... Logic coming soon.")

elif menu == "📊 Volume Shockers":
    st.title("High Volume Breakouts")
    st.success("Scanning for unusual volume... Logic coming soon.")
  
