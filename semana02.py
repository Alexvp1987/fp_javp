import streamlit as st

#Titulo a la aplicacion
st.title("Introducción a variables y tipos de datos en Python")

#Descripcion inicial
st.write("Python es un lenguaje de programacion dinamico donde ... ") 

#Seccion para variable de tipo entero
st.header("Ejemplo 1: Enteros ")
st.write("En python, un entero (integer) es un número sin decimales por ejemplo:")

#Input para que el usuario ingrese un dato (de preferencia un numero entero)
int_variable = st.number_input("Ingrese un número entero:", value=42, step=1)

#Mostrando el valor
st.code(f"int_variable = {int_variable} # Tipo: {type(int_variable)}")
