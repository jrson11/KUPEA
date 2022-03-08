# Purspose: To combine multiple Excel files, which have the same format
# Name: Excel-Combine_multiple_files.py
# Author: glocivilngneer at gmail dot com
# All right reserved

import pandas as pd
import streamlit as st


# Initialization ----------------------------------------
st.markdown('## To Combine Multiple Excel files')
password = st.sidebar.text_input('Password to Continue', 'password')
#
st.sidebar.markdown('## Input')
datatype = st.sidebar.selectbox('Type of input data file',['xlsx','xls','csv'])


# Importing ----------------------------------------
if datatype == 'xlsx':
    input_files = st.file_uploader('Choose input files',type=['xlsx'], accept_multiple_files=True)
elif datatype == 'xls':
    input_files = st.file_uploader('Choose input files',type=['xls'], accept_multiple_files=True)
elif datatype == 'csv':
    input_files = st.file_uploader('Choose input files',type=['csv'], accept_multiple_files=True)
  
n_input = len(input_files)
st.sidebar.text('Number of uploaded files: '+str(n_input))


# Process ----------------------------------------
i_sheet = st.sidebar.text_input('Name of sheet to import', 'Sheet1')
n_header = st.sidebar.selectbox('Number of header lines to skip',[0,1,2,3,4,5,6,7,8,9,10],3)

df_XLSX = pd.DataFrame()
#
for input_file in input_files:
    #df = pd.read_excel(input_file, sheet_name=i_sheet, skiprows=n_header)
    #st.dataframe(df)
    
    if datatype == 'xlsx' or 'xls':
        df = pd.read_excel(input_file, sheet_name=i_sheet, skiprows=n_header)
    elif datatype == 'csv':
        df = pd.read_csv(input_file, skiprows=n_header)

    df.insert(0,'File',input_file.name)
    df_XLSX = pd.concat([df_XLSX,df])    
    
st.dataframe(df_XLSX)


# Export ----------------------------------------
def convert_df(df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
     return df.to_csv(index=False).encode('utf-8')
csv_result = convert_df(df_XLSX)


# Membership --------------------------------------------
if password == st.secrets['db_password']:
    st.markdown('## Welcome to KUPEA')
    st.markdown('#### Please click the button in sidebar to download the result table]')
    #
    st.sidebar.markdown('## Output result')
  
    st.sidebar.download_button(
        label="Download result table",
        data=csv_result,
        file_name='all_data.csv',
        mime='text/csv',
        )

else:
  st.markdown('## Please join KUPEA')
  st.markdown('#### Only members can download the result table')

