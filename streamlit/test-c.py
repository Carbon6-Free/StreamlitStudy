#데이터 입력

import streamlit as st

label = "입력: "
value = "사용자 입력 예시"

# 텍스트
st.text_input(label, value)

#텍스트 데이터 암호 표시
st.text_input(label, value, type="password")

#여러 줄 텍스트 입력
st.text_area(label, value)

#날짜 입력
st.date_input(label)

#시간 입력
st.time_input(label)