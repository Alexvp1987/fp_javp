import streamlit as st

#Titulo a la aplicacion
st.title("Introducción a variables y tipos de datos en Python")

#Descripcion inicial
st.write("Python es un lenguaje de programacion dinamico donde ... ") 

#Seccion para variable de tipo entero
st.header("Ejemplo 1: Enteros ")
st.write("En python, un entero (integer) es un número sin decimales por ejemplo:")

#Definir una variable entera
int_variable = 42
st.code(f"int_variable = {int_variable} # Tipo: {type(int_variable)}")
