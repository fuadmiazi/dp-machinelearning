import streamlit as st

import pandas as pd

st.title('🕹 Machine Learning App')

st.info('This app is build on machine learning mode! ')

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv')
df
