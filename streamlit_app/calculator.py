import streamlit as st

st.title("Calculator")

col1, col2 = st.columns(2)
a = col1.number_input("First number", value=12)
b = col2.number_input("Second number", value=5)
op = st.selectbox("Operation", ["+", "-", "*", "/"])

if st.button("Calculate"):
    if op == "/" and b == 0:
        st.error("You cannot divide by zero.")
    else:
        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        else:
            result = a / b
        st.success(f"{a} {op} {b} = {result}")