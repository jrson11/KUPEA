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
  st.markdown('#### You can upload your CSV file with 3 columns [Sample_ID, X, Y]')
  #
  csv_list = st.file_uploader('Choose input file',type=['csv'], accept_multiple_files=True)
  n_input = len(csv_list)
  #
  st.sidebar.markdown('#### Input files')
  st.sidebar.text('Number of uploaded files: '+str(n_input))
  

else:
  st.markdown('## Please join KUPEA')
  st.markdown('#### Only members can upload his own data to combine multiple CSV files')
  
