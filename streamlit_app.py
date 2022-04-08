# Import base streamlit dependency
import streamlit as st
# Import pandas to load the analytics data
import pandas as pd
# Import subprocess to run tiktok script from command line
from subprocess import call
# Import plotly for viz
import plotly.express as px
from TikTokApi import TikTokApi as tiktok
import time as time 
import datetime
# Set page width to wide
st.set_page_config(layout='wide')

# Create sidebar
st.sidebar.markdown("<div><img src='https://png2png.com/wp-content/uploads/2021/08/Tiktok-logo-png.png' width=100 /><h1 style='display:inline-block'>Tiktok Analytics</h1></div>", unsafe_allow_html=True)
st.sidebar.markdown("This is my test-2 results for PundiX.")
st.sidebar.markdown("To initiate <ol><li>Enter a input<i>#hashtag</i> you wish to analyse</li> <li>Hit <i>Search</i>.</li> <li>You are good to go</li></ol>",unsafe_allow_html=True)

# Input 
hashtag = st.text_input('Search for a hashtag here', value="")

# Button
if st.button('Search'):
    # Run get data function here

    call(['python', 'Data_Scrapping.py', hashtag])
    # Load in existing data to test it out
    df = pd.read_csv('Export_Data.csv')
    
    
    # Plotly viz here
    fig = px.histogram(df, x='createTime', hover_data=['desc'], y='stats_diggCount', height=300) 
    st.plotly_chart(fig, use_container_width=True)
    # Show tabular dataframe in streamlit
    df