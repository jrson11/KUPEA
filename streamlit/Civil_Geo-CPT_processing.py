# Purspose: To derive engineering parameters from CPT in-situ data
# Name: Civil_Geo-CPT_processing.py
# Author: glocivilngneer at gmail dot com
# All right reserved

import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Initialization ----------------------------------------
st.markdown('## Deriving ENG parmeters from CPT')
password = st.sidebar.text_input('Password to Continue', 'password')
