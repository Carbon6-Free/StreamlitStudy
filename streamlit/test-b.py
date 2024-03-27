# 선택박스, 다중 선택박스, 슬라이더
import streamlit as st

option = st.selectbox('Please select in selectbox!',
                        ('doreen', 'yuna', 'lisa'))

st.write("You selected", option)

multi_select = st.multiselect('Please select somethings!',
                             ['A','B','C','D'])

st.write('You selected:', multi_select)

values = st.slider('Select a range of values',
                   0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)
