import streamlit as st

#st.title("Title")
#st.header("Header")
#st.subheader("Sub Header")

#st.write("Hello, World!!")

checkbox_btn = st.checkbox('체크박스')

if checkbox_btn:
    st.write('선택!')

selected_item = st.radio("Radio Part", ("A","B","C"))
if selected_item == "A":
    st.write("A!!")
elif selected_item == "B":
    st.write("B!")

elif selected_item == "C":
    st.write("C")        