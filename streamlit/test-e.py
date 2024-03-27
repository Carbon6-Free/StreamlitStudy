# Line Chart

import streamlit as st
import pandas as pd
import numpy as np

st.title("Line Chart")

chart_data = pd.DataFrame(
    np.random.randn(20,3), #20행 3열,가로 
    columns = ['a','b','c']) #열

st.line_chart(chart_data)

#np.random.randint 균일 분포의 정수 난수 1개 생성
#np.random.rand 0부터 1사이의 균일 분포에서 난수 matrix array 생성
#np.random.randn 가우시안 표준 정규 분포에서 난수 matrix array 생성
