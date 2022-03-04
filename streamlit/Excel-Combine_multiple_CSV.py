# Purspose: To combine multiple CSV files, which have the same format
# Name: Excel-Combine_multiple_CSV.py
# Author: glocivilngneer at gmail dot com
# All right reserved

import numpy as np
import pandas as pd
import streamlit as st

# Initialization ----------------------------------------
st.markdown('## Combine multiple CSV files')
password = st.sidebar.text_input('Password to Continue', 'password')
st.sidebar.markdown('## Input')
t_data = st.sidebar.selectbox('Type of input data file',['xlsx','xls','csv'])

# Importing --------------------------------------------
if t_data == 'xlsx':
    input_list = st.sidebar.file_uploader('Choose input files',type=['xlsx'], accept_multiple_files=True)
elif t_data == 'xls':
    input_list = st.sidebar.file_uploader('Choose input files',type=['xls'], accept_multiple_files=True)
elif t_data == 'csv':
    input_list = st.sidebar.file_uploader('Choose input files',type=['csv'], accept_multiple_files=True)

n_input = len(input_list)
st.sidebar.text('Number of uploaded files: '+str(n_input))

# Processing --------------------------------------------
n_header = st.sidebar.selectbox('Number of header lines to skip',[0,1,2,3,4,5,6,7,8,9,10],1)

df_XLSX = pd.DataFrame()
for input_file in input_list:
    st.text(input_file.name)
    if t_data == 'xlsx':
        df_xlsx = pd.read_excel(input_file, header=n_header)
    elif t_data == 'xlsx':
        df_xlsx = pd.read_csv(input_file, header=n_header)
    df_xlsx.insert(0,'File',input_file.name)
    df_XLSX = pd.concat([df_XLSX,df_xlsx.loc[1:,:]])    

st.markdown('#### Output result')
st.dataframe(df_XLSX)


# Membership --------------------------------------------
st.sidebar.markdown('## Output result')

def convert_df(df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
     return df.to_csv(index=False).encode('utf-8')
csv_result = convert_df(df_XLSX)

if password == st.secrets['db_password']:
  st.markdown('## Welcome to KUPEA')
  st.markdown('#### You can download your results, which have values in same format')
  #
  st.sidebar.download_button(
     label="Download result table",
     data=csv_result,
     file_name='all_data.csv',
     mime='text/csv',
 )

else:
  st.markdown('## Please join KUPEA')
  st.markdown('#### Only members can upload his own data to combine multiple CSV files')

