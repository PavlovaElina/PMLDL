import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Fetch California Housing dataset
housing = fetch_california_housing(as_frame=True)
data = housing.frame

# Save the dataset as CSV
data.to_csv('code/datasets/california_housing.csv', index=False)

# Define feature and target variables
X = data[['MedInc', 'HouseAge', 'AveRooms', 'AveOccup', 'Latitude', 'Longitude']]
y = data['MedHouseVal']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the trained model
with open('models/model.pkl', 'wb') as f:
    pickle.dump(model, f)
