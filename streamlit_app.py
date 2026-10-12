import streamlit as st

import pandas as pd

st.title('🕹 Machine Learning App')

st.info('This app is build on machine learning mode! ')

with st.expander('Data'):
  st.write('**Raw Data**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv')
  df

  st.write('**X**')
  x = df.drop('species', axis = 1)
  x

  st.write('**Y**')
  Y = df.species
  Y

with st.expander('Data Visualization'):
  #"bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g","sex"
  st.scatter_chart(data=df, x='bill_length_mm', y='body_mass_g', color='species')

# Data Preparation
with st.sidebar:
  st.header('Input Features')
