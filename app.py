import streamlit as st

st.title("Mi primera App con Python")

st.sidebar.title("Parametros")

nombre = st.sidebar.text_input("Introduce tu nombre")

st.sidebar.success("Usuario identificado")

st.write("¡Hola ", nombre, "!")