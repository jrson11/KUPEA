import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Initialization ----------------------------------------
st.markdown('## Cc, Cr, Cs Lines from log(x)-y plot')
password = st.sidebar.text_input('Password to Continue', 'password')

## Data
x = [1.03,1.04,1.03,1.26,1.27,1.38,1.47,1.52,1.63,1.76,1.84,1.94,2.08,2.21,2.37,2.52,2.68,2.83,2.99,3.18,3.37,3.55,3.76,3.97,4.21,4.45,4.71,4.99,5.27,5.57,5.89,6.21,6.56,6.92,7.27,7.66,8.05,8.45,8.51,8.55,8.85,8.84,8.86,8.85,8.85,8.23,6.9,5.97,5.86,5.17,4.6,4.1,3.68,3.32,2.99,2.7,2.45,2.22,2.02,1.83,1.68,1.53,1.36,1.24,1.13,1.06,1.05,1.01,0.91,0.9,0.91,0.91,0.9,1.05,2.45,3.93,5.75,8.07,10.77,13.73,17.01,20.7,24.93,29.63,34.81,40.47,46.57,53.26,60.29,67.92,76.12,84.7,93.88,103.61,113.79,123.96,135.05,146.99,159.17,171.9,184.73,198.36,211.99,226.66,241.11,241.11,241.32,242.07,242.15,242.18,242.17,242.17,241.55,218.32,195.99,175.45,156.14,139.13,123.41,109.2,95.84,84.67,73.69,64.01,55.35,47.73,41.08,35.26,30.45,25.99,22.08,18.79,15.92,15.08]
y = [0.749,0.75,0.75,0.751,0.75,0.748,0.747,0.746,0.743,0.741,0.741,0.74,0.737,0.734,0.733,0.731,0.73,0.728,0.725,0.724,0.723,0.72,0.718,0.716,0.714,0.711,0.71,0.708,0.705,0.704,0.703,0.7,0.699,0.696,0.694,0.693,0.691,0.689,0.688,0.688,0.685,0.685,0.684,0.684,0.684,0.684,0.685,0.687,0.687,0.689,0.691,0.693,0.695,0.698,0.699,0.702,0.704,0.705,0.706,0.709,0.712,0.713,0.717,0.719,0.721,0.723,0.723,0.724,0.727,0.727,0.727,0.728,0.728,0.728,0.719,0.708,0.698,0.687,0.679,0.669,0.659,0.65,0.64,0.632,0.622,0.612,0.602,0.594,0.585,0.575,0.567,0.557,0.549,0.54,0.531,0.524,0.516,0.508,0.5,0.493,0.484,0.478,0.469,0.464,0.456,0.455,0.456,0.454,0.454,0.453,0.453,0.452,0.452,0.451,0.453,0.453,0.456,0.459,0.462,0.465,0.469,0.473,0.476,0.482,0.487,0.493,0.499,0.505,0.511,0.517,0.524,0.531,0.539,0.542]
nx = len(x)

# Membership --------------------------------------------
if password == st.secrets['db_password']:
  st.markdown('## Welcome to KUPEA')
  st.markdown('#### You can upload your CSV file with 3 columns [Name, X, Y]')
  #
  st.file_uploader('Choose input file',type=['csv'], accept_multiple_files=False)
  
else:
  st.markdown('## Please join KUPEA')
  st.markdown('#### Only members can upload his own data to analyze engineering parameters')
  

# Main -----------------------------------------------
st.sidebar.markdown('#### Seclect Points')
Px = st.sidebar.selectbox('Index of max curvature point', np.arange(nx), 20) 
Pc = st.sidebar.selectbox('Index of max Cc starting point', np.arange(nx), 105) 
Pr = st.sidebar.selectbox('Index of max Cr starting point', np.arange(nx), 70) 
st.sidebar.markdown('#### Seclect Index')
Cc1000 = st.sidebar.slider('Cc: Compression Index * 1000', 0, 400, 120) 
Cr1000 = st.sidebar.slider('Cr: Recompression Index* 1000', 0, 400, 20) 
Cs1000 = st.sidebar.slider('Cs: Swelling Index* 1000', 0, 400, 20) 
Cc = Cc1000 / 1000
Cr = Cr1000 / 1000
Cs = Cs1000 / 1000

def find_y2(x1,y1,C,x2):
  # y1 = a x1 + b
  # b = y1 - a x1
  # y2 = a x2 + b = a x2 -a x1 + y1
  a = C*-1
  y2 = a*x2 - a*x1 + y1
  return y2

## Plot
xmin = min(x)
xmax = max(x)
ymin = min(y)
ymax = max(y)

fig = plt.figure(figsize = (5,5), dpi=100)
plt.rcParams['font.size'] = '8'
plt.plot(np.log(x),y, '.-')
plt.scatter(np.log(x[Px]),y[Px], c='k', marker='x')
plt.scatter(np.log(x[Pc]),y[Pc], c='r', marker='x')
plt.scatter(np.log(x[Pr]),y[Pr], c='m', marker='x')
#
plt.plot([np.log(x[Pc]),np.log(xmin)],[y[Pc],find_y2(np.log(x[Pc]),y[Pc],Cc,np.log(xmin))], 'r--')
plt.plot([np.log(x[Pr]),np.log(xmax)],[y[Pr],find_y2(np.log(x[Pr]),y[Pr],Cr,np.log(xmax))], 'm--')
plt.plot([np.log(x[Pr]),np.log(xmax)],[y[Pr],find_y2(np.log(x[Pr]),y[Pr],Cs,np.log(xmax))], 'y--')
#
plt.xlabel('log(x)')
plt.ylabel('y')
plt.xlim([np.log(xmin)-0.5,np.log(xmax)+0.5])
plt.ylim([ymin-0.05,ymax+0.05])
#plt.xscale('log')
plt.grid(linestyle='-', alpha=0.5)
plt.grid(which='minor', color='grey', linestyle='-', alpha=0.2)
#
st.pyplot(fig)




  
