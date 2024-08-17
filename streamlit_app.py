import streamlit as st
import numpy as np
import pandas as pd

st.title('🎈 Training Become Jedi')

st.write('Welcome Anakin')

listofdata = {
  'A' : [1, 2, 3, 4, 5, 6, 7],
  'B' : [2, 1, 3, 2, 4, 3, 5]
}

st.table(data=listofdata.head())

st.line_chart(data=listofdata, x='A', y='B', color='#18919B')

