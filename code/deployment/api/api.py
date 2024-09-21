from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

# Load model
with open('models/model.pkl', 'rb') as f:
    model = pickle.load(f)

app = FastAPI()

class InputData(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveOccup: float
    Latitude: float
    Longitude: float

@app.post('/predict')
def predict(data: InputData):
    # Prepare data for prediction
    input_data = np.array([[data.MedInc, data.HouseAge, data.AveRooms, data.AveOccup, data.Latitude, data.Longitude]])
    # Make prediction
    prediction = model.predict(input_data)[0]
    return {'prediction': prediction}

@app.get("/")
def read_root():
    return {"message": "Welcome to the California Housing Price Predictor API"}
