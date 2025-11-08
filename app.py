import streamlit as st

st.title("Hello Streamlit-er 👋")
st.write("This is my first Streamlit app!")

name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=1, max_value=100)

if st.button("Greet Me"):
    st.success(f"Hello {name}! You are {age} years old 🎉")
