import streamlit as st

st.title("Hello Google")


age = st.slider("how old are you", 0, 130, 25)
st.write("I am ",age,"years old")

brother_age = st.slider("How old is your Brother",0, 130, 25)
st.write("my Brother ", brother_age ,"years old")

c = age + brother_age
st.write("Total age is ", c)
