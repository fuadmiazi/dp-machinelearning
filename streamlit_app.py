import streamlit as st

import pandas as pd

st.title('🕹 Machine Learning App')

st.info('This app is build on machine learning mode! ')

with st.expander('Data'):
  st.write('**Raw Data**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv')
  df
