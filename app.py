import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Bienvenidos a mi primera aplicación web")       
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
st.header("Histograma datos de anuncios") 
hist_button = st.button('Construir histograma') # crear un botón

if hist_button: # al hacer clic en el botón
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True) 

st.header("Histograma de millas") 
odo_button= st.button("Visualizar recorrido en millas")    

if odo_button:
    st.write("Creación de un histograma para el conteo de millas recorridas de los coches en venta")
    fig = px.scatter(car_data, x="odometer", y="price")# crear un histograma
    st.plotly_chart(fig, use_container_width=True) 

st.header("Carros") 
car_button= st.button("Cantidad de carros por marca") 
if car_button:
    st.write("Creación de una gráfica de barras por marca")
    fig = px.bar(car_data, x="type")
    st.plotly_chart(fig, use_container_width=True) 

like= st.checkbox("¿Te ha gustado esta app?")
button2= st.button("Submit")
if button2:
    if like:
        st.write("¡Muchas gracias!")
    else:
        st.write(":(")

    
