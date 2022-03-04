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

# Membership --------------------------------------------
if password == st.secrets['db_password']:
  st.markdown('## Welcome to KUPEA')
  st.markdown('#### You can upload your multiple CSV files, which have values in same format')
  #
  csv_list = st.file_uploader('Choose input file',type=['csv'], accept_multiple_files=True)
  n_input = len(csv_list)
  #
  st.sidebar.markdown('#### Input files')
  st.sidebar.text('Number of uploaded files: '+str(n_input))
  
else:
  st.markdown('## Please join KUPEA')
  st.markdown('#### Only members can upload his own data to combine multiple CSV files')

  
# Processing
n_header = st.sidebar.selectbox('Number of header lines to skip',[0,1,2,3,4,5,6,7,8,9,10])

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


# Export
def convert_df(df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
     return df.to_csv(index=False).encode('utf-8')


csv_result = convert_df(df_XLSX)

st.sidebar.markdown('## Output result')

st.sidebar.download_button(
     label="Download result table",
     data=csv_result,
     file_name='all_data.csv',
     mime='text/csv',
 )
