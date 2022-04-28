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


# Example Data -------------------------------------------
loca = 'DCPT-103A'
SCPT_DPTH=[0,0.02,0.04,0.06,0.08,0.1,0.12,0.14,0.16,0.18,0.2,0.22,0.24,0.26,0.28,0.3,0.32,0.34,0.36,0.38,0.4,0.42,0.44,0.46,0.48,0.5,0.52,0.54,0.56,0.58,0.6,0.62,0.64,0.66,0.68,0.7,0.72,0.74,0.76,0.78,0.8,0.82,0.84,0.86,0.88,0.9,0.92,0.94,0.96,0.98,1,1.02,1.04,1.06,1.08,1.1,1.12,1.14,1.16,1.18,1.2,1.22,1.24,1.26,1.28,1.3,1.32,1.34,1.36,1.38,1.4,1.42,1.44,1.46,1.48,1.5,1.52,1.54,1.56,1.58,1.6,1.62,1.64,1.66,1.68,1.7,1.72,1.74,1.76,1.78,1.8,1.82,1.84,1.86,1.88,1.9,1.92,1.94,1.96,1.98,2,2.02,2.04,2.06,2.08,2.1,2.12,2.14,2.16,2.18,2.2,2.22,2.24,2.26,2.28,2.3,2.32,2.34,2.36,2.38,2.4,2.42,2.44,2.46,2.48,2.5,2.52,2.54,2.56,2.58,2.6,2.62,2.64,2.66,2.68,2.7,2.72,2.74,2.76,2.78,2.8,2.82,2.84,2.86,2.88,2.9,2.92,2.94,2.96,2.98,3,3.02,3.04,3.06,3.08,3.1,3.12,3.14,3.16,3.18,3.2,3.22,3.24,3.26,3.28,3.3,3.32,3.34,3.36,3.38,3.4,3.42,3.44,3.46,3.48,3.5,3.52,3.54,3.56,3.58,3.6,3.62,3.64,3.66,3.68,3.7,3.72,3.74,3.76,3.78,3.8,3.82,3.84,3.86,3.88,3.9,3.92,3.94,3.96,3.98,4,4.02,4.04,4.06,4.08,4.1,4.12,4.14,4.16,4.18,4.2,4.22,4.24,4.26,4.28,4.3,4.32,4.34,4.36,4.38,4.4,4.42,4.44,4.46,4.48,4.5,4.52,4.54,4.56,4.58,4.6,4.62,4.64,4.66,4.68,4.7,4.72,4.74,4.76,4.78,4.8,4.82,4.84,4.86,4.88,4.9,4.92,4.94,4.96,4.98,5,5.02,5.04,5.06,5.08,5.1,5.12,5.14,5.16,5.18,5.2,5.22,5.24,5.26,5.28,5.3,5.32,5.34,5.36,5.38,5.4,5.42,5.44,5.46,5.48,5.5,5.52,5.54,5.56,5.58,5.6,5.62,5.64,5.66,5.68,5.7,5.72,5.74,5.76,5.78,5.8,5.82,5.84,5.86,5.88,5.9,5.92,5.94,5.96,5.98,6,6.02,6.04,6.06,6.08,6.1,6.12,6.14,6.16,6.18,6.2,6.22,6.24,6.26,6.28,6.3,6.32,6.34,6.36,6.38,6.4,6.42,6.44,6.46,6.48,6.5,6.52,6.54,6.56,6.58,6.6,6.62,6.64,6.66,6.68,6.7,6.72,6.74,6.76,6.78,6.8,6.82,6.84,6.86,6.88,6.9,6.92,6.94,6.96,6.98,7,7.02,7.04,7.06,7.08,7.1,7.12,7.14,7.16,7.18,7.2,7.22,7.24,7.26,7.28,7.3,7.32,7.34,7.36,7.38,7.4,7.42,7.44,7.46,7.48,7.5,7.52,7.54,7.56,7.58,7.6,7.62,7.64,7.66,7.68,7.7,7.72,7.74,7.76,7.78,7.8,7.82,7.84,7.86,7.88,7.9,7.92,7.94,7.96,7.98,8,8.02,8.04,8.06,8.08,8.1,8.12,8.14,8.16,8.18,8.2,8.22,8.24,8.26,8.28,8.3,8.32,8.34,8.36,8.38,8.4,8.42,8.44,8.46,8.48,8.5,8.52,8.54,8.56,8.58,8.6,8.62,8.64,8.66,8.68,8.7,8.72,8.74,8.76,8.78,8.8,8.82,8.84,8.86,8.88,8.9,8.92,8.94,8.96,8.98,9,9.02,9.04,9.06,9.08,9.1,9.12,9.14,9.16,9.18,9.2,9.22,9.24,9.26,9.28,9.3,9.32,9.34,9.36,9.38,9.4,9.42,9.44,9.46,9.48,9.5,9.52,9.54,9.56,9.58,9.6,9.62,9.64,9.66,9.68,9.7,9.72,9.74,9.76,9.78,9.8,9.82,9.84,9.86,9.88,9.9,9.92,9.94,9.96,9.98,10,10.02,10.04,10.06,10.08,10.1,10.12,10.14,10.16,10.18,10.2,10.22,10.24,10.26,10.28,10.3,10.32,10.34,10.36,10.38,10.4,10.42,10.44,10.46,10.48,10.5,10.52,10.54,10.56,10.58,10.6,10.62,10.64,10.66,10.68,10.7,10.72,10.74,10.76,10.78,10.8,10.82,10.84,10.86,10.88,10.9,10.92,10.94,10.96,10.98,11,11.02,11.04,11.06,11.08,11.1,11.12,11.14,11.16,11.18,11.2,11.22,11.24,11.26,11.28,11.3,11.32,11.34,11.36,11.38,11.4,11.42,11.44,11.46,11.48,11.5,11.52,11.54,11.56,11.58,11.6,11.62,11.64,11.66,11.68,11.7,11.72,11.74,11.76,11.78,11.8,11.82,11.84,11.86,11.88,11.9,11.92,11.94,11.96,11.98,12,12.02,12.04,12.06,12.08,12.1,12.12,12.14,12.16,12.18,12.2,12.22,12.24,12.26,12.28,12.3,12.32,12.34,12.36,12.38,12.4,12.42,12.44,12.46,12.48,12.5,12.52,12.54,12.56,12.58,12.6,12.62,12.64,12.66,12.68,12.7,12.72,12.74,12.76,12.78,12.8,12.82,12.84,12.86,12.88,12.9,12.92,12.94,12.96,12.98,13,13.02,13.04,13.06,13.08,13.1,13.12,13.14,13.16,13.18,13.2,13.22,13.24,13.26,13.28,13.3,13.32,13.34,13.36,13.38,13.4,13.42,13.44,13.46,13.48,13.5,13.52,13.54,13.56,13.58,13.6,13.62,13.64,13.66,13.68,13.7,13.72,13.74,13.76,13.78,13.8,13.82,13.84,13.86,13.88,13.9,13.92,13.94,13.96,13.98,14,14.02,14.04,14.06,14.08,14.1,14.12,14.14,14.16,14.18,14.2,14.22,14.24,14.26,14.28,14.3,14.32,14.34,14.36,14.38,14.4,14.42,14.44,14.46,14.48,14.5,14.52,14.54,14.56,14.58,14.6,14.62,14.64,14.66,14.68,14.7,14.72,14.74,14.76,14.78,14.8,14.82,14.84,14.86,14.88,14.9,14.92,14.94,14.96,14.98,15,15.02,15.04,15.06,15.08,15.1,15.12,15.14,15.16,15.18,15.2,15.22,15.24,15.26,15.28,15.3,15.32,15.34,15.36,15.38,15.4,15.42,15.44,15.46,15.48,15.5,15.52,15.54,15.56,15.58,15.6,15.62,15.64,15.66,15.68,15.7,15.72,15.74,15.76,15.78,15.8,15.82,15.84,15.86,15.88,15.9,15.92,15.94,15.96,15.98,16,16.02,16.04,16.06,16.08,16.1,16.12,16.14,16.16,16.18,16.2,16.22,16.24,16.26,16.28,16.3,16.32,16.34,16.36,16.38,16.4,16.42,16.44,16.46,16.48,16.5,16.52,16.54,16.56,16.58,16.6,16.62,16.64,16.66,16.68,16.7,16.72,16.74,16.76,16.78,16.8,16.82,16.84,16.86,16.88,16.9,16.92,16.94,16.96,16.98,17,17.02,17.04,17.06,17.08,17.1,17.12,17.14,17.16,17.18,17.2,17.22,17.24,17.26,17.28,17.3,17.32,17.34,17.36,17.38,17.4,17.42,17.44,17.46,17.48,17.5,17.52,17.54,17.56,17.58,17.6,17.62,17.64,17.66,17.68,17.7,17.72,17.74,17.76,17.78,17.8,17.82,17.84,17.86,17.88,17.9,17.92,17.94,17.96,17.98,18,18.02,18.04,18.06,18.08,18.1,18.12,18.14,18.16,18.18,18.2,18.22,18.24,18.26,18.28,18.3,18.32,18.34,18.36,18.38,18.4,18.42,18.44,18.46,18.48,18.5,18.52,18.54,18.56,18.58,18.6,18.62,18.64,18.66,18.68,18.7,18.72,18.74,18.76,18.78,18.8,18.82,18.84,18.86,18.88,18.9,18.92,18.94,18.96,18.98,19,19.02,19.04,19.06,19.08,19.1,19.12,19.14,19.16,19.18,19.2,19.22,19.24,19.26,19.28,19.3,19.32,19.34,19.36,19.38,19.4,19.42,19.44,19.46,19.48,19.5,19.52,19.54,19.56,19.58,19.6,19.62,19.64,19.66,19.68,19.7,19.72,19.74,19.76,19.78,19.8,19.82,19.84,19.86,19.88,19.9,19.92,19.94,19.96,19.98,20,20.02,20.04,20.06,20.08,20.1,20.12,20.14,20.16,20.18,20.2,20.22,20.24,20.26,20.28,20.3,20.32,20.34,20.36,20.38,20.4,20.42,20.44,20.46,20.48,20.5,20.52,20.54,20.56,20.58,20.6,20.62,20.64,20.66,20.68,20.7,20.72,20.74,20.76,20.78,20.8,20.82,20.84,20.86,20.88,20.9,20.92,20.94,20.96,20.98,21,21.02,21.04,21.06,21.08,21.1,21.12,21.14,21.16,21.18,21.2,21.22,21.24,21.26]
SCPT_RES=[0.15,0.214,0.274,0.333,0.374,0.426,0.506,0.687,0.795,1.02,1.206,1.362,1.524,1.598,1.82,2.123,2.23,2.349,2.44,2.578,2.694,2.73,2.964,3.291,3.995,4.632,4.823,5.083,5.132,5.042,4.806,4.478,4.024,3.912,4.847,7.261,9.062,10.018,10.483,10.703,10.881,11.132,11.387,11.798,12.351,12.991,13.388,13.511,13.502,13.584,14.035,14.787,15.253,15.265,15.135,15.004,15.009,14.98,14.9,14.786,14.686,14.577,14.366,14.051,13.661,13.309,13.171,13.29,13.241,13.371,13.599,13.581,12.945,12.355,11.78,11.71,11.915,11.326,10.178,8.713,7.607,6.319,5.148,4.347,3.835,3.097,4.914,9.235,12.315,13.018,12.277,11.15,9.898,8.314,7.138,6.373,5.242,4.912,5.377,6.213,7.378,8.119,8.365,8.16,8.081,8.14,8.015,7.4,6.473,7.162,9.452,10.863,9.791,8.049,6.389,5.223,4.45,3.897,3.45,3.325,3.944,4.771,5.972,7.258,6.839,5.245,2.974,2.983,2.869,2.837,2.699,2.566,2.556,2.694,2.759,2.952,3.198,3.203,2.934,2.995,3.2,3.424,3.4,3.043,2.686,2.448,2.351,2.364,2.424,2.521,2.625,2.671,2.716,2.727,2.737,2.771,2.918,3.041,3.057,3.219,3.461,3.676,3.943,5.261,7.604,10.454,11.812,12.413,12.458,12.135,11.762,11.453,11.095,10.544,9.772,8.951,8.147,7.528,7.189,7.164,7.33,8.116,8.62,8.827,8.764,8.573,8.296,7.95,7.623,7.419,7.342,7.237,7.032,6.904,6.935,7.098,7.259,7.37,7.401,7.354,7.287,7.255,7.308,7.481,7.645,7.766,7.778,7.631,7.277,6.832,6.382,6.053,5.696,5.451,5.368,5.292,5.297,5.247,5.161,5.187,5.397,5.924,6.556,6.772,6.835,6.96,7.169,7.501,7.878,8.051,8.07,7.51,6.696,5.747,4.854,4.266,3.935,3.804,3.767,3.68,3.411,3.345,3.316,3.451,3.65,3.647,3.623,3.553,3.326,3.229,3.235,3.224,3.151,2.881,2.731,2.892,3.283,3.978,5.077,5.477,4.922,4.272,3.625,2.996,2.482,2.248,2.347,2.972,4.067,4.923,5.072,4.236,3.252,2.538,2.09,1.951,2.537,3.717,4.147,3.718,3.489,3.754,3.942,4.467,5.999,7.292,6.881,5.657,4.393,3.382,2.642,2.191,1.769,1.52,1.546,2.097,2.748,3.153,2.707,2.259,2.032,2.513,3.357,3.782,3.564,3.406,4.387,5.991,7.7,8.285,7.89,7.251,6.674,6.032,5.259,4.324,3.898,4.185,5.11,6.213,6.846,7.012,7.114,7.15,7.129,7.12,7.081,7.052,7.024,7.068,7.187,7.263,7.142,6.814,6.235,5.703,5.205,5.093,5.333,5.712,5.813,5.914,6.212,6.575,6.811,7.019,7.011,6.938,6.834,6.792,6.853,7.045,7.068,6.882,6.505,5.996,5.513,5.071,4.748,4.405,4.242,4.29,4.273,4.344,4.301,4.456,4.745,5.017,5.244,5.35,5.413,5.818,6.594,7.508,8.411,8.689,8.676,9.157,9.885,10.872,11.404,11.137,10.61,10.159,10.086,10.549,11.212,11.61,11.849,11.922,11.812,11.612,11.294,10.992,10.522,10.154,9.982,10.054,10.109,9.788,8.86,7.615,6.201,5.291,4.299,4.394,4.528,4.205,3.583,2.958,2.412,2.378,2.578,3.111,4.948,6.732,6.501,5.327,4.172,3.213,2.502,2.279,2.256,2.209,1.987,1.968,2.187,2.504,2.659,2.506,2.403,2.794,3.163,2.898,2.387,1.929,1.798,1.896,2.343,2.834,2.633,2.312,2.346,2.607,2.868,3.21,3.62,4.095,4.391,4.625,5.011,5.885,6.92,7.665,8.152,8.324,7.912,6.926,6.026,5.06,4.358,4.027,4.294,5.103,5.842,5.724,5.23,5.138,6.324,7.722,9.589,11.481,13.174,14.548,15.645,16.329,16.59,16.488,16.529,16.747,17.169,17.673,18.347,19.531,21.33,24.022,27.412,30.447,33.312,35.611,37.578,39.178,40.95,42.716,43.881,44.787,45.53,46.475,47.763,48.925,50.036,51.074,52.072,52.841,53.667,54.913,55.422,55.163,54.804,54.479,53.979,53.207,51.336,51.292,50.742,50.117,49.288,48.144,46.688,44.913,42.553,39.722,36.893,32.908,27.854,23.081,19.351,17.402,16.356,15.363,17.231,22.047,28.075,33.011,35.548,37.135,38.497,40.185,41.106,40.633,39.151,36.427,32.732,28.972,25.302,22.004,19.891,18.386,17.588,18.69,19.593,19.12,17.746,15.643,13.888,12.792,12.451,12.706,12.28,10.774,9.105,8.203,7.986,8.155,7.199,6.079,4.936,4.438,4.558,4.596,4.392,5.292,6.172,7.023,6.734,5.592,4.692,3.846,3.614,3.867,4.38,5.658,7.201,7.326,6.387,5.236,4.367,3.564,2.948,2.714,2.6,2.601,2.555,2.502,2.481,2.439,2.507,2.62,2.645,2.688,2.764,2.808,2.825,2.819,2.746,2.725,2.72,2.801,2.829,2.83,2.856,2.793,2.708,2.697,2.731,2.867,2.918,2.895,2.905,2.911,2.892,2.76,2.637,2.615,2.63,2.764,2.856,2.885,2.84,2.778,2.715,2.677,2.683,2.677,2.687,2.648,2.592,2.586,2.634,2.652,2.629,2.641,2.66,2.655,2.624,2.552,2.473,2.44,2.379,2.326,2.282,2.285,2.275,2.29,2.341,2.436,2.709,3.016,3.09,2.943,2.84,2.715,2.591,2.531,2.462,2.435,2.434,2.471,2.519,2.62,2.931,3.051,2.753,2.547,2.402,2.398,2.417,2.449,2.471,2.483,2.465,2.464,2.466,2.494,2.531,2.514,2.496,2.456,2.422,2.413,2.434,2.467,2.494,2.503,2.503,2.532,2.522,2.561,2.56,2.598,2.691,2.665,2.651,2.585,2.568,2.583,2.62,2.689,2.703,2.707,2.666,2.612,2.603,2.613,2.711,2.795,2.929,3.033,3.115,3.014,2.855,2.835,2.832,2.876,2.834,2.484,2.603,3.158,3.532,3.338,3.09,3.038,3.094,3.43,3.68,3.537,2.945,2.671,2.605,3.317,4.972,7.131,7.516,7.249,7.131,7.15,7.222,8.482,11.096,14.447,16.581,18.449,20.11,21.685,23.13,24.139,25.025,26.15,27.474,28.949,29.943,30.474,30.516,30.161,29.909,29.38,29.245,29.192,29.072,29.449,30.091,30.64,31.085,31.128,31.022,30.577,30.075,29.717,29.313,29.253,29.716,30.117,29.758,29.624,29.66,29.992,30.717,31.603,32.225,32.451,32.264,31.892,31.299,30.544,29.782,29.056,28.283,27.646,26.807,26.261,26.166,26.495,27.424,28.81,30.306,32.495,35.213,38.245,40.851,42.433,43.073,43.391,43.117,42.589,41.893,40.915,38.636,36.005,33.75,32.288,30.874,30.376,30.752,32.376,34.627,36.432,37.484,37.896,38.218,38.134,37.893,37.348,36.561,35.703,34.887,33.776,32.096,30.111,27.823,25.648,24.131,23.944,24.941,26.994,29.421,29.744,29.416,28.999,28.666,28.619,28.609,28.725,29.478,30.461,31.659,33.034,34.568,36.113,37.284,38.22,38.344,39.24,40.012,40.735,40.989,41.026,41.038,41.205,41.598,42.164,42.975,43.515,43.759,43.808,43.891,43.877,43.954,44.294,44.629,44.991,45.355,45.51,45.45,45.178,44.683,43.929,43.005,41.932,40.588,38.834,36.986,35.328,33.587,31.666,29.577,27.37,24.779,22.406,20.693,18.928,17.439,16.622,17.837,19.4,21.94,26.701,31.837,37.083,41.25,44.89,47.74,49.651,50.231,50.999,50.591,50.444,51.422,52.062,53.944,56.422,59.303,61.134,60.707,58.532,55.96,54.556,54.201,54.192,54.584,54.825,53.687,51.702,50.041,49.595,51.213,53.69,55.611,56.689,57.123,57.489,57.357,56.291,55.81,55.948,56.086,56.224,52.865,52.314,53.072,53.409,52.039,49.808,47.619,45.396,43.217,42.122,42.095,43.017,45.525,50.798,58.037,63.457,66.808,68.758,72.387,75.387,76.689,74.537,73.893,72.88,71.667,68.385,66.792,65.2,63.185,61.067,60.021,60.057,61.346,63.126,62.893,64.201,66.19,67.552,67.912,66.552,65.894,64.615,64.043,63.717,64.115,66.465,69.357,69.959,70.45,68.565,67.679,68.481,70.127,71.208,69.097,67.035,65.301,63.189,62.633,63.032,62.867,62.735,61.94,60.969,59.878,58.611,57.071,55.884,54.722,53.474,51.641,50.579,49.869,49.313,48.946,48.091,46.647,45.985,45.74,46.032,46.112,45.585,45.089,44.89,45.135,46.024,47.123,47.62,47.444,47.278,46.832,46.378,46.568,47.168,47.991,47.939,47.626,47.835,48.484,48.758,49.328,49.117,48.472,47.455,46.991,46.515,46.16,46.114,46.597,47.398,48.685,50.717,53.852,57.33,61.516,65.998,70.162,74.2]
SCPT_FRES=[np.nan,np.nan,np.nan,0.0002,0.0006,0.0016,0.0014,0.0018,0.0021,0.0028,0.004,0.0052,0.0077,0.0088,0.0124,0.0125,0.014,0.0171,0.0199,0.0218,0.0194,0.0186,0.0218,0.0248,0.0271,0.0236,0.0211,0.0261,0.0399,0.0505,0.0375,0.0391,0.0395,0.0411,0.0413,0.0427,0.0436,0.0437,0.0451,0.0473,0.0506,0.0505,0.051,0.0532,0.0554,0.0565,0.0563,0.0548,0.0543,0.0549,0.0576,0.0615,0.0661,0.071,0.0743,0.0763,0.0771,0.0758,0.0766,0.0796,0.0825,0.0852,0.0861,0.0779,0.0731,0.0692,0.066,0.064,0.0612,0.0578,0.0509,0.047,0.0421,0.0409,0.0354,0.03,0.0279,0.0279,0.0325,0.0442,0.0694,0.0993,0.0998,0.0848,0.0681,0.0612,0.0574,0.0545,0.0472,0.0445,0.0529,0.0819,0.0844,0.0831,0.0896,0.0944,0.0939,0.0994,0.0962,0.0866,0.0801,0.0785,0.0694,0.0737,0.0967,0.0973,0.0831,0.0831,0.08,0.0759,0.0739,0.079,0.0866,0.1007,0.1068,0.097,0.0899,0.0878,0.0714,0.0571,0.0605,0.0884,0.0889,0.0963,0.103,0.1059,0.113,0.1108,0.0776,0.0709,0.0683,0.0701,0.0743,0.0769,0.0828,0.0883,0.0943,0.0917,0.091,0.0961,0.1024,0.1,0.0968,0.0924,0.0896,0.0842,0.0769,0.0735,0.0751,0.0776,0.0807,0.0805,0.0865,0.091,0.091,0.0933,0.0989,0.1072,0.1211,0.123,0.1165,0.1242,0.1242,0.1128,0.1016,0.0897,0.0789,0.0672,0.0724,0.078,0.0849,0.0915,0.0944,0.0982,0.1043,0.1133,0.1139,0.1137,0.1103,0.1007,0.0897,0.0741,0.0535,0.0413,0.0456,0.0526,0.0603,0.0668,0.0742,0.08,0.0824,0.0839,0.0881,0.0899,0.0807,0.0715,0.0665,0.0637,0.0632,0.0658,0.0737,0.0832,0.0786,0.0679,0.064,0.0592,0.0616,0.0707,0.0818,0.076,0.0822,0.0933,0.1055,0.1134,0.1061,0.0965,0.0974,0.1059,0.1127,0.1108,0.0992,0.0957,0.1054,0.1152,0.1206,0.1075,0.0953,0.0767,0.0922,0.0856,0.1022,0.1157,0.1253,0.1305,0.1256,0.1264,0.1289,0.1209,0.1162,0.1178,0.1207,0.123,0.1233,0.1236,0.1236,0.1222,0.1256,0.1333,0.1393,0.134,0.1224,0.1155,0.1136,0.1096,0.1176,0.0976,0.0917,0.0953,0.1022,0.098,0.0956,0.089,0.0822,0.0755,0.0681,0.0619,0.0592,0.0619,0.0655,0.0693,0.0694,0.0684,0.068,0.0665,0.0668,0.0744,0.0779,0.0758,0.0871,0.0888,0.0894,0.1004,0.0999,0.0916,0.0958,0.1012,0.1,0.1003,0.0971,0.0967,0.0924,0.0829,0.0664,0.0641,0.0665,0.0651,0.068,0.0655,0.067,0.0758,0.0936,0.0874,0.0811,0.0756,0.0789,0.0772,0.076,0.073,0.0671,0.0705,0.0776,0.0956,0.1003,0.1028,0.0998,0.0997,0.0982,0.0892,0.0785,0.0657,0.0601,0.0559,0.0591,0.0625,0.0646,0.0695,0.0727,0.0746,0.0741,0.0744,0.0783,0.0834,0.0876,0.0944,0.0962,0.0931,0.0902,0.085,0.0784,0.0743,0.0682,0.06,0.063,0.0698,0.0748,0.0782,0.0812,0.0813,0.0806,0.0739,0.0735,0.0753,0.0779,0.0795,0.0822,0.0895,0.0953,0.0949,0.094,0.093,0.0976,0.0988,0.1018,0.0984,0.0856,0.0756,0.0787,0.0825,0.0823,0.0752,0.0724,0.0707,0.0749,0.0734,0.0814,0.09,0.0982,0.0991,0.1048,0.1138,0.1195,0.1146,0.1125,0.1133,0.1085,0.1093,0.109,0.1077,0.1074,0.1075,0.1115,0.1088,0.0964,0.0867,0.0836,0.0762,0.0796,0.0867,0.1176,0.139,0.1419,0.1332,0.1237,0.124,0.1325,0.1293,0.115,0.0984,0.1022,0.0986,0.0866,0.0753,0.0704,0.0738,0.095,0.1144,0.109,0.1057,0.1021,0.1013,0.095,0.0852,0.0699,0.0585,0.0631,0.0767,0.0808,0.0717,0.0681,0.0841,0.1016,0.1013,0.0926,0.0811,0.0751,0.0707,0.0638,0.0611,0.0594,0.0648,0.0739,0.0914,0.0941,0.0906,0.09,0.1034,0.1078,0.1025,0.1028,0.1119,0.1179,0.1148,0.1042,0.1001,0.1007,0.0919,0.096,0.1076,0.1221,0.1189,0.1196,0.1332,0.1327,0.1251,0.1196,0.1196,0.1238,0.1307,0.1228,0.1068,0.1018,0.0909,0.0765,0.073,0.0778,0.0855,0.094,0.1003,0.0925,0.0842,0.078,0.0737,0.0832,0.0846,0.0916,0.1055,0.1245,0.1491,0.1782,0.2062,0.2347,0.2624,0.2903,0.3097,0.333,0.3507,0.3703,0.3788,0.3866,0.3934,0.4009,0.4034,0.4118,0.4314,0.4452,0.4562,0.4755,0.4874,0.4979,0.5066,0.509,0.5043,0.5034,0.496,0.4863,0.4799,0.4876,0.4939,0.4878,0.476,0.4574,0.4397,0.446,0.4717,0.4953,0.4836,0.4732,0.4202,0.3863,0.3817,0.377,0.362,0.333,0.2901,0.253,0.2388,0.2554,0.2807,0.3075,0.3275,0.3335,0.3283,0.342,0.3501,0.3343,0.3412,0.3327,0.3158,0.2878,0.2699,0.2557,0.238,0.1916,0.1711,0.1626,0.1732,0.195,0.1952,0.1747,0.1641,0.1623,0.1737,0.1657,0.1565,0.1459,0.1457,0.1383,0.1281,0.1161,0.1013,0.1039,0.1089,0.119,0.1256,0.1202,0.115,0.1143,0.1111,0.1088,0.1052,0.0957,0.102,0.1198,0.1248,0.1175,0.1163,0.1152,0.1117,0.105,0.0923,0.0795,0.0794,0.0806,0.084,0.089,0.0894,0.0899,0.0903,0.0913,0.0934,0.0947,0.0947,0.0961,0.0999,0.0987,0.0947,0.0939,0.0951,0.0965,0.096,0.094,0.0946,0.0979,0.1014,0.1032,0.1012,0.1027,0.1055,0.108,0.108,0.1055,0.1043,0.1055,0.1059,0.105,0.1044,0.1063,0.1098,0.1103,0.1104,0.1113,0.11,0.1064,0.1036,0.1009,0.0998,0.0999,0.1015,0.1006,0.0993,0.1003,0.1009,0.1013,0.1016,0.1003,0.1008,0.0993,0.0969,0.0937,0.0891,0.0849,0.0785,0.0742,0.0751,0.0762,0.0783,0.0846,0.09,0.0931,0.0973,0.1006,0.1062,0.1019,0.0959,0.0903,0.0856,0.0847,0.0866,0.0856,0.091,0.0931,0.0933,0.0928,0.0952,0.0943,0.0822,0.0688,0.068,0.0693,0.0705,0.0727,0.0732,0.0748,0.0757,0.0747,0.0733,0.0726,0.073,0.0721,0.0687,0.0668,0.0679,0.0669,0.0681,0.0687,0.068,0.0679,0.0715,0.0756,0.0774,0.0782,0.0774,0.077,0.0769,0.0757,0.0756,0.0766,0.0769,0.0761,0.075,0.0767,0.0797,0.0801,0.0781,0.0792,0.0804,0.0824,0.0867,0.0873,0.0839,0.0859,0.0894,0.0863,0.0856,0.0857,0.09,0.0923,0.0959,0.0934,0.0907,0.0945,0.1035,0.0989,0.1004,0.1024,0.1017,0.0925,0.0948,0.0977,0.0997,0.1099,0.1224,0.1463,0.1548,0.1482,0.1339,0.1229,0.1096,0.0958,0.0886,0.085,0.079,0.0794,0.0837,0.0913,0.0913,0.0925,0.0915,0.092,0.0933,0.0948,0.0998,0.1089,0.1116,0.1162,0.1189,0.12,0.1189,0.1202,0.1206,0.1202,0.1228,0.1261,0.1352,0.1449,0.1477,0.1478,0.1518,0.1552,0.1582,0.1583,0.1599,0.1574,0.1555,0.1507,0.1484,0.1464,0.1417,0.1415,0.146,0.1492,0.1501,0.1461,0.1418,0.1417,0.1423,0.1474,0.1502,0.1493,0.1475,0.1489,0.1435,0.1352,0.1234,0.1175,0.1151,0.1265,0.1434,0.1605,0.1759,0.188,0.2019,0.2149,0.2229,0.225,0.2243,0.2239,0.2185,0.2137,0.1925,0.1737,0.1519,0.1385,0.137,0.138,0.1421,0.1547,0.1705,0.1809,0.1899,0.1987,0.2071,0.2185,0.2274,0.2311,0.2374,0.2558,0.2824,0.2969,0.2888,0.2815,0.2638,0.2488,0.2341,0.2236,0.1912,0.1617,0.1599,0.1608,0.1618,0.1648,0.1661,0.1689,0.1732,0.1839,0.1925,0.2033,0.2119,0.2204,0.231,0.2421,0.2537,0.2631,0.2687,0.2705,0.2718,0.2714,0.274,0.278,0.2833,0.2886,0.2975,0.3052,0.3179,0.3244,0.33,0.3335,0.3391,0.3453,0.3502,0.3515,0.3516,0.3533,0.3521,0.3519,0.349,0.3414,0.332,0.3236,0.3158,0.3048,0.2851,0.2635,0.2441,0.2234,0.2084,0.2061,0.2017,0.2093,0.2278,0.227,0.2078,0.1819,0.1667,0.178,0.1822,0.1734,0.1802,0.1872,0.2307,0.2465,0.2533,0.2815,0.3087,0.307,0.3143,0.3219,0.3158,0.3295,0.3281,0.3573,0.3714,0.3629,0.3615,0.3645,0.3509,0.3305,0.3242,0.3348,0.3164,0.303,0.2875,0.2697,0.2614,0.2544,0.2455,0.2458,0.24,0.2342,0.2284,0.2382,0.2564,0.2705,0.276,0.2753,0.2673,0.2545,0.2472,0.2415,0.2484,0.2517,0.2491,0.2429,0.2255,0.2117,0.2086,0.1939,0.1853,0.1836,0.2108,0.2241,0.2312,0.2312,0.2336,0.2634,0.2779,0.2906,0.3178,0.34,0.3663,0.3984,0.3691,0.3565,0.3391,0.33,0.3441,0.3194,0.3063,0.3067,0.2951,0.2944,0.2849,0.311,0.3077,0.3418,0.338,0.3858,0.3743,0.3737,0.3489,0.3233,0.3054,0.2971,0.2987,0.2862,0.2722,0.2693,0.2709,0.2952,0.3089,0.3208,0.3354,0.3355,0.3424,0.3476,0.3208,0.3293,0.3108,0.3147,0.2992,0.3106,0.3291,0.3202,0.3103,0.3202,0.3084,0.3121,0.3002,0.2939,0.2883,0.2877,0.2785,0.2742,0.2755,0.2778,0.2727,0.2668,0.2681,0.2691,0.2678,0.2712,0.2671,0.2688,0.2766,0.2788,0.268,0.2745,0.2711,0.2729,0.2721,0.2637,0.2644,0.2598,0.2626,0.2549,0.2568,0.2616,0.2669,0.274,0.2818,0.2858,0.2887,0.2895,0.2889,0.2802,0.2688,0.2593,0.2637,0.277,np.nan,np.nan,np.nan,np.nan,np.nan]
SCPT_PWP2=[0.0108,0.0112,0.0117,0.0121,0.0122,0.0122,0.0122,0.0123,0.0124,0.0127,0.0128,0.0129,0.0128,0.0132,0.0135,0.0137,0.0145,0.0153,0.0156,0.0158,0.0159,0.0159,0.0161,0.016,0.0132,0.0105,0.0137,0.0147,0.0141,0.0075,0.0172,0.0181,0.0203,0.0153,0.0348,-0.0022,-0.0146,0,0.0306,0.0298,0.0158,0.0152,0.0181,0.0205,0.0199,0.0195,0.0183,0.0182,0.0172,0.0186,0.0231,0.0284,0.0217,0.0184,0.0186,0.0225,0.0209,0.0205,0.022,0.0226,0.0232,0.0229,0.0234,0.0243,0.0237,0.0238,0.0243,0.0241,0.0246,0.0243,0.0201,0.0198,0.0207,0.0277,0.0206,0.0248,0.0229,0.0209,0.0195,0.019,0.0087,0.0293,0.0284,0.0297,0.021,0.0328,0.0658,0.0635,-0.0022,0.0129,0.0209,0.0238,0.0278,0.0275,0.0266,0.0353,0.044,0.0842,0.0126,-0.0227,-0.0927,-0.0636,-0.0789,-0.0687,-0.0291,0.0254,0.0564,-0.0148,0.0118,0.0838,0.1611,-0.0098,-0.0495,-0.0486,-0.0437,-0.0284,0.0038,0.0395,0.0451,0.1311,0.2104,0.0741,-0.0211,-0.0476,-0.0196,-0.1039,-0.1128,-0.0461,0.0501,0.1182,0.2426,0.4334,0.517,0.4343,0.4378,0.4393,0.4381,0.3493,0.376,0.4155,0.4599,0.4725,0.2836,0.22,0.2835,0.4305,0.5118,0.5394,0.5567,0.5874,0.623,0.6228,0.6198,0.656,0.6483,0.684,0.6357,0.6952,0.6686,0.5913,0.599,0.61,0.6262,0.7908,0.7134,0.1934,0.1301,0.0909,0.0463,0.0372,0.038,0.039,0.0396,0.0384,0.0344,0.0277,0.0048,-0.0058,0.0002,0.0022,-0.0211,-0.049,-0.0555,-0.063,-0.0613,-0.0577,-0.0501,-0.0414,-0.0304,-0.017,-0.0128,-0.0157,-0.0389,-0.0725,-0.1041,-0.1245,-0.1442,-0.1622,-0.1831,-0.1928,-0.1975,-0.1973,-0.1933,-0.1891,-0.1842,-0.1892,-0.1998,-0.213,-0.2128,-0.2023,-0.1936,-0.1868,-0.1807,-0.1832,-0.184,-0.1847,-0.1911,-0.1991,-0.1991,-0.1948,-0.1946,-0.1977,-0.2023,-0.2114,-0.2126,-0.212,-0.2141,-0.2189,-0.2206,-0.2222,-0.2231,-0.2256,-0.2245,-0.2168,-0.2106,-0.1947,-0.1629,-0.1359,-0.0967,-0.0842,-0.0795,-0.0477,0.0019,0.0403,0.076,0.1157,0.1417,0.1771,0.2446,0.2427,0.2035,0.1883,0.1921,0.2533,0.2813,0.2506,0.2135,0.152,0.0562,0.0435,-0.0321,-0.0363,-0.0298,-0.0246,-0.0026,0.0229,0.0905,0.1707,0.1101,0.0049,-0.0406,-0.051,-0.057,-0.0525,-0.0247,0.0074,0.0442,0.0347,-0.0031,-0.032,-0.0171,0.0341,0.0322,0.0283,0.061,-0.0265,-0.0713,-0.0798,-0.0767,-0.0623,-0.0411,-0.0158,0.0334,0.0998,0.1572,0.2065,0.193,0.0835,0.0376,0.074,0.1172,0.1515,0.136,0.0671,0.0159,0.0377,0.109,0.068,0.0031,-0.0227,-0.0335,-0.0566,-0.0542,-0.0499,-0.0396,-0.0294,-0.0024,0.1022,0.125,0.0728,0.0166,-0.0011,-0.0084,-0.0111,-0.0088,-0.0084,-0.0044,-0.0046,-0.0184,-0.0147,-0.0072,-0.0141,-0.022,-0.0332,-0.0306,-0.0213,-0.0043,0.0212,0.0271,0.0199,-0.0263,-0.0503,-0.041,-0.0284,-0.0178,-0.0134,-0.0029,0.0052,0.0147,0.0213,0.0294,0.0081,-0.0539,-0.0707,-0.0508,-0.023,-0.0018,0.0134,0.0122,-0.009,-0.0028,-0.0268,-0.0362,-0.0608,-0.0732,-0.0841,-0.111,-0.1274,-0.1341,-0.1298,-0.1255,-0.126,-0.1316,-0.1387,-0.1537,-0.1487,-0.1353,-0.1284,-0.1063,-0.0742,-0.088,-0.0828,-0.0728,-0.061,-0.0507,-0.037,-0.0254,-0.0451,-0.0845,-0.0664,-0.0439,-0.0261,-0.0113,0.0034,0.0066,0.0162,0.0329,0.0536,0.0808,0.0868,0.0917,0.0684,0.126,0.1369,0.2679,0.3704,0.2208,0.1239,0.1819,0.3075,0.5052,0.6583,0.6925,0.7377,0.6921,0.3727,0.1372,0.1374,0.1819,0.2584,0.3682,0.5436,0.6747,0.6298,0.7354,0.8569,0.8982,0.7667,0.5723,0.5271,0.669,0.8754,0.7069,0.3229,0.382,0.6524,0.7598,0.8347,0.9142,0.7589,0.364,0.3801,0.5556,0.5659,0.4522,0.4367,0.4393,0.3652,0.3564,0.2413,0.2888,0.3849,0.1589,0.1335,0.0379,-0.0605,-0.1005,-0.1161,-0.1044,-0.0733,-0.0164,0.0626,0.1915,0.3197,0.3086,0.095,0.138,0.3074,0.3528,0.1699,0.0843,-0.0232,-0.0303,-0.0207,-0.0336,-0.042,-0.0648,-0.0376,-0.0048,0.0176,0.0057,-0.0557,-0.1226,-0.1372,-0.1022,-0.0886,-0.1251,-0.1367,-0.1232,-0.0637,-0.0124,0.0412,0.083,0.1045,0.1072,0.1091,0.0993,0.0766,0.0655,0.0826,0.0979,0.1328,0.1271,0.1289,0.1215,0.1174,0.1224,0.1307,0.1386,0.1177,0.1046,0.124,0.1116,0.1095,0.1223,0.1049,0.1252,0.0998,0.0929,0.0748,0.0677,0.0676,0.0554,0.0311,0.0084,-0.003,0.006,0.0694,0.5646,0.5153,0.6409,0.5541,0.4344,0.0708,0.0254,0.0214,0.0133,0.0434,-0.0173,-0.0638,-0.078,-0.0857,-0.0716,-0.055,-0.0448,-0.042,-0.0377,0.0184,0.0834,0.0906,0.0899,0.0413,-0.0399,-0.0714,-0.0922,-0.0955,-0.0844,-0.0859,-0.0974,-0.113,-0.1157,-0.0841,-0.0715,-0.0383,-0.0535,-0.0451,-0.035,0.0074,0.043,0.0718,0.1806,0.2529,0.1727,0.0946,0.0339,0,0.0119,0.0699,0.169,0.2235,0.2682,0.2676,0.2139,0.0835,0.0497,0.0475,0.0749,0.1206,0.2131,0.3322,0.6288,0.7688,0.8672,0.9305,0.9384,1.0066,1.0541,1.1254,1.1792,1.2628,1.2625,1.2877,1.2989,1.3445,1.4088,1.4234,1.3987,1.3851,1.4369,1.3715,1.2765,1.2468,1.3151,1.3883,1.4341,1.4102,1.3771,1.3829,1.4062,1.436,1.4302,1.4241,1.4055,1.4485,1.4945,1.5071,1.494,1.4219,1.3669,1.3845,1.4399,1.5032,1.4896,1.5072,1.5217,1.4933,1.4953,1.5222,1.5277,1.5763,1.5807,1.6145,1.638,1.6345,1.6372,1.6625,1.6621,1.6247,1.6126,1.5856,1.5979,1.6543,1.7111,1.7458,1.7572,1.8032,1.8211,1.8799,1.796,1.6437,1.5369,1.5896,1.6583,1.6746,1.729,1.7612,1.8028,1.8103,1.8082,1.7302,1.6111,1.5358,1.2683,1.2857,1.451,1.4899,1.5173,1.5745,1.6353,1.6798,1.7161,1.7541,1.8143,1.8358,1.8313,1.8164,1.8052,1.8686,1.8926,1.9021,1.8925,1.8702,1.9206,1.943,1.9646,1.9523,1.9357,1.9079,1.9265,1.894,1.8648,1.8059,1.823,1.8895,1.9341,1.9583,1.9563,1.878,1.8161,1.7607,1.7806,1.8691,1.9071,1.8774,1.8998,1.9176,1.9905,2.0406,1.8792,1.7441,1.7228,1.7433,1.7831,1.6187,1.4316,1.4892,1.6191,1.5864,1.2768,1.2169,1.4865,1.5347,1.5637,1.6019,1.5175,1.3417,1.1248,1.3841,1.5804,1.6771,1.5424,0.5978,0.2754,0.2456,0.2396,0.2325,0.4898,0.5715,0.2749,0.1291,0.098,0.1076,0.0919,-0.0068,0.0038,-0.0052,0.0081,0.0787,0.1142,0.0553,-0.0059,-0.0151,-0.0109,0.0272,0.0509,0.0612,0.0831,0.1049,0.1018,0.0995,0.0613,0.0331,-0.0044,-0.0084,0.0246,0.0547,0.0975,0.1131,0.1274,0.1382,0.1217,0.117,0.1296,0.1296,0.1368,0.1389,0.1291,0.114,0.1036,0.103,0.0961,0.0996,0.111,0.1163,0.1285,0.1218,0.1223,0.0845,0.1137,0.1231,0.1126,0.1041,0.07,-0.0422,-0.0706,-0.0838,-0.1013,-0.1077,-0.1068,-0.0993,-0.0986,-0.0828,-0.0618,-0.0407,-0.0259,-0.0126,0.011,0.042,0.0549,0.068,0.0821,0.0881,0.0967,0.1138,0.1149,0.1192,0.1248,0.1051,0.1079,0.1254,0.1214,0.145,0.1501,0.1413,0.1375,0.1472,0.1446,0.1596,0.1443,0.1271,0.1352,0.2044,0.351,0.3912,0.1049,0.0583,0.0381,0.0426,0.061,0.0749,0.0883,0.1161,0.1236,0.1467,0.1506,0.1468,0.1469,0.1462,0.1571,0.1737,0.1636,0.1568,0.1658,0.1647,0.1774,0.1683,0.1709,0.1798,0.1672,0.1635,0.1691,0.1685,0.1817,0.1908,0.186,0.1787,0.1722,0.1696,0.179,0.1791,0.1739,0.1677,0.1746,0.1731,0.1618,0.153,0.1488,0.161,0.162,0.1626,0.1592,0.1548,0.1514,0.1465,0.1492,0.1437,0.1262,0.1253,0.1193,0.1349,0.1485,0.1558,0.194,0.3184,0.2338,0.1026,0.1039,0.0701,0.0421,0.0879,0.0313,0.0863,0.0438,0.0986,0.2017,0.2856,0.2385,0.182,0.2886,0.1874,0.2014,0.1578,0.1516,0.1585,0.0736,0.146,0.29,0.2487,0.1761,0.1353,0.1757,0.2313,0.1875,0.1895,0.1687,0.1577,0.1795,0.1704,0.1882,0.2405,0.189,0.1378,0.1206,0.0696,0.0187,0.0014,0.026,0.0648,0.0935,0.138,0.141,0.1455,0.1495,0.1642,0.1917,0.2052,0.1813,0.2011,0.1988,0.201,0.2059,0.1984,0.1876,0.0841,0.1283,0.1138,0.2075,0.1983,0.1427,0.1086,0.1559,0.1335,0.1239,0.1344,0.2461,0.2373,0.265,0.2194,0.2071,0.178,0.299,0.1614,0.1569,0.1901,0.1454,0.1588,0.1497,0.2929,0.2987,0.3081,0.1429,0.1556,0.2117,0.1879,0.2198,0.1696,0.1203,0.1042,0.1419,0.1917,0.2607,0.1486,0.175,0.1432,0.2136,0.2034,0.2123,0.3125,0.2126,0.1686,0.1571,0.1859,0.18,0.1819,0.1701,0.1793,0.2176,0.1871,0.2137,0.1978,0.1883,0.1897,0.1975,0.2228,0.2115,0.1999,0.2067,0.2083,0.2222,0.2308,0.2032,0.2058,0.2172,0.1902,0.2124,0.2074,0.1865,0.2,0.2116,0.2155,0.1986,0.1982,0.2035,0.2054,0.2056,0.1972,0.2223,0.2104,0.1829,0.1565,0.1792,0.2077,0.2069,0.2132,0.2078,0.1837,0.1973,0.2101,0.2026,0.2067,0.2042,0.2118,0.2361,0.2127]
SCPT_QT=[0.1542,0.2186,0.2792,0.3379,0.3792,0.4308,0.5107,0.692,0.7998,1.025,1.2117,1.3675,1.5297,1.6039,1.8252,2.1291,2.2361,2.3553,2.4469,2.5845,2.7004,2.7368,2.9706,3.2974,4.0009,4.636,4.8283,5.0888,5.1375,5.0455,4.8135,4.4855,4.033,3.9181,4.862,7.2603,9.0557,10.0178,10.4959,10.7153,10.8879,11.1387,11.395,11.8063,12.3597,12.9993,13.3957,13.5185,13.5092,13.5915,14.0447,14.7987,15.2625,15.2731,15.1428,15.0134,15.0174,14.9888,14.9097,14.7956,14.6956,14.5871,14.3758,14.0611,13.6711,13.3194,13.1809,13.3003,13.2513,13.3817,13.6075,13.5892,12.9534,12.3669,11.7883,11.7208,11.9247,11.3344,10.1867,8.7212,7.6107,6.3314,5.1597,4.3595,3.8442,3.1107,4.9419,9.262,12.3141,13.0237,12.2862,11.1597,9.91,8.3256,7.1495,6.3878,5.2606,4.9477,5.3823,6.2032,7.3393,8.0924,8.3323,8.1309,8.0684,8.1509,8.0385,7.3938,6.4781,7.1976,9.5198,10.8585,9.7706,8.0289,6.3702,5.2115,4.452,3.9136,3.4691,3.3803,4.0321,4.8023,5.9631,7.2381,6.8308,5.2009,2.9263,2.9641,2.8899,2.887,2.8004,2.7481,2.773,2.8768,2.9427,3.1363,3.3821,3.3494,3.0915,3.1692,3.3928,3.6225,3.5191,3.1353,2.8053,2.629,2.5657,2.5903,2.6578,2.7681,2.8862,2.9327,2.976,3.0021,3.009,3.0586,3.185,3.333,3.3373,3.4669,3.7124,3.9317,4.2064,5.5934,7.9034,10.5347,11.8662,12.4515,12.4773,12.1504,11.7781,11.4696,11.1114,10.5605,9.7868,8.9631,8.1489,7.5254,7.1892,7.1652,7.3208,8.0955,8.5962,8.8003,8.7386,8.5488,8.2747,7.9327,7.6103,7.4115,7.3365,7.2308,7.0154,6.874,6.8916,7.0459,7.1986,7.3023,7.324,7.2731,7.2036,7.1718,7.2265,7.4018,7.5673,7.6867,7.6938,7.5411,7.1879,6.7471,6.3005,5.9749,5.6201,5.3738,5.2906,5.2147,5.2166,5.1629,5.0771,5.1055,5.3156,5.8409,6.4706,6.6828,6.7457,6.8706,7.0787,7.4088,7.7855,7.9579,7.9761,7.4157,6.6019,5.6557,4.7657,4.1841,3.867,3.7474,3.7267,3.6447,3.3776,3.3245,3.3164,3.4675,3.6815,3.6958,3.6826,3.6274,3.4285,3.331,3.3206,3.3028,3.232,2.9871,2.8493,2.9976,3.373,4.0414,5.1001,5.4956,4.9081,4.2566,3.6121,2.9861,2.4812,2.2575,2.3852,3.0435,4.1133,4.9253,5.0552,4.2148,3.228,2.5159,2.0797,1.9543,2.5555,3.7315,4.1456,3.7046,3.4818,3.7682,3.9552,4.4785,6.0244,7.2805,6.8512,5.6235,4.361,3.3557,2.6244,2.1842,1.7828,1.5615,1.6121,2.1841,2.8288,3.1879,2.7229,2.2899,2.0812,2.5768,3.4141,3.8097,3.5709,3.4215,4.4326,6.0194,7.7016,8.2754,7.8762,7.2268,6.6515,6.0109,5.242,4.3112,3.8969,4.2275,5.163,6.2435,6.8528,7.0113,7.1101,7.1457,7.1256,7.1161,7.0789,7.0505,7.0168,7.0617,7.1836,7.2569,7.1326,6.7996,6.2223,5.6941,5.2032,5.1023,5.3439,5.7204,5.8022,5.8926,6.1944,6.563,6.8034,7.0131,7.0096,6.9407,6.8404,6.8005,6.8649,7.0484,7.0457,6.8521,6.4835,5.986,5.5121,5.0767,4.7533,4.4009,4.2409,4.2786,4.2576,4.3184,4.2704,4.421,4.6981,4.9634,5.188,5.2957,5.3604,5.7654,6.5388,7.4502,8.3466,8.6264,8.6188,9.1028,9.8408,10.8406,11.3673,11.1025,10.5792,10.1337,10.0648,10.533,11.2013,11.591,11.8131,11.8945,11.7931,11.6009,11.289,10.9938,10.5252,10.1604,9.9955,10.0762,10.1432,9.8241,8.898,7.6438,6.2538,5.3484,4.411,4.5491,4.6203,4.2572,3.6592,3.0872,2.6246,2.6548,2.8691,3.4205,5.239,6.8889,6.559,5.3848,4.2489,3.3219,2.6563,2.5078,2.5395,2.4731,2.2958,2.3284,2.5644,2.8263,2.8996,2.7274,2.6843,3.1619,3.4598,3.0338,2.547,2.2029,2.1171,2.2463,2.7273,3.1524,2.7854,2.4713,2.5797,2.8447,3.0583,3.3932,3.8042,4.248,4.5409,4.7267,5.1328,6.047,6.9869,7.7213,8.1682,8.2985,7.8696,6.8776,5.9825,5.029,4.3516,4.0532,4.374,5.2369,5.9715,5.764,5.288,5.2676,6.4719,7.793,9.6246,11.4708,13.1615,14.5389,15.6311,16.3117,16.5632,16.4724,16.5266,16.754,17.1713,17.6497,18.2951,19.4733,21.2875,23.9847,27.3594,30.3899,33.2598,35.5838,37.5727,39.195,40.9849,42.7596,43.9257,44.8324,45.5721,46.507,47.7904,48.9593,50.0769,51.1293,52.1253,52.8948,53.7175,54.9624,55.4738,55.2181,54.8619,54.5286,54.0227,53.2592,51.3824,51.3379,50.7937,50.1612,49.3406,48.1858,46.7267,44.9447,42.581,39.7502,36.9163,32.9211,27.8574,23.0802,19.3539,17.4315,16.5928,15.5794,17.4998,22.2794,28.2577,33.0411,35.5588,37.1442,38.503,40.2033,41.0985,40.6057,39.1183,36.391,32.702,28.9492,25.2828,21.9861,19.8748,18.3939,17.6235,18.7282,19.6313,19.1378,17.7288,15.6134,13.8488,12.752,12.416,12.6697,12.2392,10.7263,9.0561,8.1673,7.9565,8.1387,7.177,6.0602,4.9214,4.4415,4.5764,4.6257,4.4675,5.3984,6.2442,7.0631,6.748,5.5917,4.6967,3.8751,3.6849,3.9612,4.4923,5.7701,7.2913,7.3608,6.4076,5.2561,4.3987,3.6148,3.0371,2.8537,2.8644,2.9238,2.9194,2.893,2.8751,2.8621,2.9495,3.0929,3.1402,3.2181,3.2944,3.3491,3.3701,3.384,3.3373,3.3229,3.3077,3.3824,3.4325,3.4064,3.3922,3.3172,3.2605,3.2801,3.3338,3.4589,3.4967,3.4753,3.4957,3.5137,3.4925,3.3581,3.2275,3.2238,3.2581,3.3973,3.4833,3.482,3.4138,3.3593,3.3194,3.3083,3.3091,3.3102,3.3259,3.2752,3.2203,3.225,3.2753,3.3138,3.2932,3.3186,3.3481,3.3414,3.3114,3.2503,3.171,3.1227,3.0564,2.9921,2.9534,2.9794,2.9932,3.0233,3.0786,3.1931,3.4738,3.8053,3.8447,3.633,3.4856,3.383,3.2875,3.2343,3.1885,3.1744,3.1915,3.2314,3.2785,3.3469,3.6078,3.6961,3.2858,3.0869,3.0115,3.0242,3.0539,3.1106,3.158,3.1887,3.186,3.2004,3.2279,3.2646,3.2997,3.277,3.2547,3.2413,3.2172,3.2118,3.229,3.2526,3.3003,3.3191,3.3285,3.3524,3.3352,3.3626,3.3689,3.3936,3.474,3.4233,3.4163,3.3788,3.3802,3.4052,3.4412,3.4774,3.4654,3.4465,3.4139,3.3973,3.4044,3.4016,3.5086,3.6007,3.7652,3.8903,3.9048,3.7465,3.5788,3.5671,3.5809,3.5559,3.4352,3.1099,3.2835,3.8243,4.0682,3.8495,3.7146,3.6823,3.7508,4.1025,4.3169,4.1008,3.4175,3.2522,3.2691,4.0214,5.6201,7.382,7.6318,7.352,7.2312,7.2481,7.4281,8.7224,11.2114,14.5009,16.6217,18.4939,20.1488,21.6825,23.1318,24.1372,25.028,26.183,27.5216,28.9724,29.9409,30.4674,30.5117,30.1726,29.9306,29.4055,29.2798,29.2359,29.115,29.491,30.1164,30.6535,31.0827,31.1248,31.0322,30.5996,30.116,29.7645,29.3667,29.3112,29.7674,30.1661,29.8127,29.6786,29.7178,30.0506,30.7714,31.6509,32.2688,32.4946,32.3047,31.9337,31.3454,30.5929,29.8356,29.107,28.3342,27.6819,26.8544,26.3127,26.2131,26.5388,27.4539,28.792,30.2763,32.4599,35.1709,38.1995,40.806,42.391,43.0317,43.3563,43.0906,42.5719,41.8821,40.9095,38.6408,36.0222,33.7733,32.317,30.9083,30.4129,30.793,32.4242,34.6748,36.482,37.5367,37.9406,38.2636,38.1863,37.9444,37.4087,36.6243,35.7627,34.9447,33.8381,32.1567,30.1777,27.8831,25.701,24.1874,24.0301,25.0885,27.1581,29.4654,29.7685,29.4319,29.0174,28.6918,28.6502,28.6458,28.7735,29.5296,30.5222,31.7225,33.096,34.6298,36.1744,37.3503,38.2932,38.4132,39.3062,40.0814,40.8042,41.0639,41.0964,41.1101,41.2806,41.6683,42.2325,43.046,43.5859,43.8357,43.8884,43.9696,43.9517,44.0267,44.3652,44.7037,45.0661,45.4278,45.5809,45.5231,45.251,44.7513,43.9928,43.0671,41.9998,40.6556,38.902,37.0532,35.3927,33.6502,31.7277,29.64,27.4305,24.8321,22.4584,20.7433,18.9845,17.5012,16.6876,17.9189,19.5333,22.0377,26.7436,31.8807,37.112,41.2677,44.9274,47.7534,49.6872,50.2498,51.0404,50.6758,50.5642,51.5221,52.1384,54.0655,56.501,59.3881,61.2004,60.7707,58.5982,55.991,54.6174,54.3223,54.2965,54.6583,54.8819,53.7607,51.7996,50.12,49.6744,51.2841,53.7565,55.6862,56.7608,57.2023,57.5902,57.4365,56.3491,55.8625,55.9832,56.1039,56.2246,52.8762,52.3414,53.1113,53.4666,52.0985,49.8691,47.6814,45.4651,43.2974,42.2085,42.1713,43.1017,45.6089,50.8821,58.1237,63.5406,66.8864,68.7933,72.441,75.4348,76.7757,74.6201,73.953,72.9253,71.7327,68.4411,66.8439,65.2565,63.2881,61.1666,60.1325,60.1495,61.4326,63.2005,63.0187,64.2687,66.2558,67.6314,67.9729,66.6192,65.9566,64.7379,64.1682,63.846,64.1753,66.5302,69.4455,70.0381,70.5423,68.6366,67.7295,68.5243,70.1863,71.2884,69.207,67.0971,65.3745,63.2491,62.7226,63.1172,62.9558,62.8659,62.029,61.0398,59.9443,58.6895,57.1468,55.9602,54.7936,53.5494,51.7328,50.6572,49.9589,49.3965,49.0247,48.1709,46.7295,46.079,45.8293,46.1163,46.1988,45.6723,45.1824,44.9871,45.2204,46.1107,47.214,47.7,47.5329,47.3648,46.9106,46.462,46.657,47.2581,48.074,48.022,47.7112,47.921,48.57,48.8404,49.4211,49.2057,48.549,47.5208,47.0667,46.602,46.247,46.2039,46.6838,47.4749,48.7677,50.805,53.9371,57.4164,61.6017,66.087,70.2612,74.2897]
#
df = pd.DataFrame()
df['SCPT_DPTH'] = SCPT_DPTH
df['SCPT_RES'] = SCPT_RES
df['SCPT_FRES'] = SCPT_FRES
df['SCPT_PWP2'] = SCPT_PWP2
df['SCPT_QT'] = SCPT_QT
df.insert(0,'LOCA_ID',loca)
#
st.markdown('#### Importing Data')
st.dataframe(df)

# Sidebar -----------------------------------
st.sidebar.markdown('#### Seclect Index')

# Processing --------------------------------------------
# 1. Isct
Pa_kPa = 101.3
qc_kPa = df.SCPT_RES*1000
fs_kPa = df.SCPT_FRES*1000
Rf = fs_kPa/qc_kPa*100
Isbt = np.array([np.sqrt((3.47-np.log10(x))**2 + (np.log10(y)+1.22)**2) for x,y in zip(qc_kPa/Pa_kPa,Rf)])
df['Isbt'] = Isbt
#
# 2. Ic before iteration
#qt_kPa = df.SCPT_QT*1000
#sv0_kPa = df['s,v0']
#sv0e_kPa = df['s,v0e']
#Qt1 = (qt_kPa-sv0_kPa)/sv0e_kPa
#Fr = fs_kPa/(qc_kPa-sv0_kPa)*100
#Ic1 = np.array([np.sqrt((3.47-np.log10(x))**2 + (np.log10(y)+1.22)**2) for x,y in zip(Qt1,Rf)])
#df['Ic1'] = Ic1

#st.dataframe(qc_kPa)


# Plot ---------------------------------------------------
zmax = np.nanmax(df.SCPT_DPTH)
fig,ax = plt.subplots(1,3, figsize=(7,7))
ax[0].plot(df.SCPT_RES,df.SCPT_DPTH,'.')
ax[1].plot(df.SCPT_FRES,df.SCPT_DPTH,'.')
ax[2].plot(df.SCPT_PWP2,df.SCPT_DPTH,'.')
#
ax[0].set_ylabel('Depth [m BSF]')
ax[0].set_xlabel('qc [MPa]')        
ax[1].set_xlabel('fs [MPa]')        
ax[2].set_xlabel('u2 [MPa]')        
#
for k in range(3):
  ax[k].set(ylim=(zmax,0))
  ax[k].grid(linestyle='dotted')
  ax[k].minorticks_on()
  ax[k].xaxis.set_ticks_position('top')
  ax[k].xaxis.set_label_position('top')
#
fig.tight_layout()
fig.suptitle(loca, y=1.02, fontsize=12)
#
st.markdown('#### Plotting Data')
st.pyplot(fig)


