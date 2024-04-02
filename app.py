import streamlit as st
import pandas as pd 
import seaborn as sns
from st_aggrid import AgGrid

st.set_page_config(
    page_title="Data Visualization App", 
    page_icon="🖼", 
    page_icon=":bar_chart:", 
    layout="centered"
)

st.title("Data Visualization App")
df = pd.read_csv('IRIS.csv')
AgGrid(df)
