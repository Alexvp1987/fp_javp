import streamlit as st

#Ejercicio 5: Generar e imprimir los números pares entre 0 y 100
st.title("Ejercicios de números pares")

st.subheader("Ejercicio 5: Números pares entre 0 y 100 ")
pares_0_100 = [i for i in range(0,101) if i % 2 ==0]
st.write("Numeros pares entre 0 y 100:")
st.write(pares_0_100)

#Ejercicio 5 con boton
st.markdown("""
    <style>
    div.stButton > button{
        background-color: #8B0000;
        color: white;
        font-size:16px;
        padding: 10x;
        border-radius:10px;
        border:none;
    }
    </style>
""", unsafe_allow_html=True)

if st.button("Mostrar números pares entre 0 y 100"):
    pares0a100 = [i for i in range(0,101) if i%2 == 0]
    st.write("Numeros pares entre 0 y 100:")
    st.write(pares0a100)