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
    input_list = st.file_uploader('Choose input files',type=['xlsx'], accept_multiple_files=True)
elif datatype == 'xls':
    input_list = st.file_uploader('Choose input files',type=['xls'], accept_multiple_files=True)
elif datatype == 'csv':
    input_list = st.file_uploader('Choose input files',type=['csv'], accept_multiple_files=True)
  
n_input = len(input_list)
st.markdown('#### Input files')
st.sidebar.text('Number of uploaded files: '+str(n_input))


# Process ----------------------------------------
n_header = st.sidebar.selectbox('Number of header lines to skip',[0,1,2,3,4,5,6,7,8,9,10],0)

st.text(input_list[0].name)

'''



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

'''
