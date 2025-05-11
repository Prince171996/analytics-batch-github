import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.title('Car Prediction Application')
col1, col2 = st.columns(2)

with col1:
    Fuel_Type = st.radio(
        'Select Fuel Type',
        ['Diesel','Petrol','LPG','CNG','Electrical'],

    )
with (col2):
    Transmission =st.selectbox(
    "Select Transmission Type",
    ('Manual','Automatic'),
)
col1, col2 = st.columns(2)

with col1:
    Engine = st.slider(
        'Select The Engine Power',
        500,5000,step=100

    )
with (col2):
    Seats =st.selectbox(
    "Select Number Of seats",
    (2,3,4,5,6,7,8,9,10),
)

encoded_dic = {'Fuel_Type':{'Diesel':1,'Petrol':2,'LPG':3,'CNG':4,'Electrical':5},
               'Transmission':{'Manual':1,'Automatic':2},}
def model_predict(Fuel_type,Transmission,Engine,Seats):
    with open('car_pred','rb') as file:
        reg_model = pickle.load(file)

        x_test = [[2018.0, 1, 40000, Fuel_type, Transmission, 18.00, Engine, 85, Seats]]
        return reg_model.predict(x_test)

if st.button("Predict"):
    Fuel_type = encoded_dic['Fuel_Type'][Fuel_Type]
    Transmission = encoded_dic['Transmission'][Transmission]
    Price = model_predict(Fuel_type,Transmission,Engine,Seats)
    st.write(f'Predicted Price: {Price}')


else:
    st.write("Select Predict Button")

