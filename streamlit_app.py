import streamlit as st

st.title('🎈 App Name')

st.write('Hello world!')

listofdata = {
  'A' : [1, 2, 3, 4, 5],
  'B' : [2, 4, 6, 8, 10]
}

st.table(data=listofdata)
