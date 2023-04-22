import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv('open_pubs_modified.csv')

st.set_page_config(page_title='Home', page_icon='🍻',layout='wide')
st.title('Cheers to Pour Decisions 🍸')
st.write('****Pubs Finder Application****')
st.subheader('Info:')
total_pubs= len(df['fsa_id'].unique())
total_local_authority= len(df['local_authority'].unique())
total_postal_codes= len(df['postcode'].unique())
st.subheader(f'Total Pubs Present in United Kingdom is {total_pubs}')
st.subheader(f'Total Local Authorities of Pubs is {total_local_authority}')
st.subheader(f'Total Postal Codes of Pubs Present in UK is {total_postal_codes}')

with st.expander(label='Seen Dataset',expanded=False):
    st.dataframe(df.head(11))

st.caption('Project By ****PRASAD JADHAV****')
