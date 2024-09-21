import streamlit as st
import requests

st.title('California Housing Price Predictor')

# Input fields
MedInc = st.number_input('Median Income', value=1.0, format="%.2f")
HouseAge = st.number_input('House Age', value=10.0, format="%.2f")
AveRooms = st.number_input('Average Rooms', value=5.0, format="%.2f")
AveOccup = st.number_input('Average Occupancy', value=3.0, format="%.2f")
Latitude = st.number_input('Latitude', value=34.0, format="%.2f")
Longitude = st.number_input('Longitude', value=-120.0, format="%.2f")

if st.button('Predict'):
    input_data = {
        'MedInc': MedInc,
        'HouseAge': HouseAge,
        'AveRooms': AveRooms,
        'AveOccup': AveOccup,
        'Latitude': Latitude,
        'Longitude': Longitude
    }
    response = requests.post('http://api:8000/predict', json=input_data)
    prediction = response.json()['prediction']
    st.write(f'Predicted House Value: ${prediction:,.2f}')
