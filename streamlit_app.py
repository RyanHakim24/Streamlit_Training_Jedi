import streamlit as st
import numpy as np
import pandas as pd

st.title('🎈 Training Become Jedi')

st.write('Welcome Anakin')

listofdata = {
  'A' : [1, 2, 3, 4, 5],
  'B' : [2, 4, 6, 8, 10]
}

st.table(data=listofdata)

st.bar_chart(listofdata['B'])
