import streamlit as st
import pickle
import numpy as np

# Load the model
model = pickle.load(open("house_price_prediction_model.pkl", "rb"))

st.title("🏡 House Price Prediction")

# Create input fields for all features
bedrooms = st.number_input("Number of Bedrooms", min_value=0)
bathrooms = st.number_input("Number of Bathrooms", min_value=0.0, format="%.1f")
sqft_living = st.number_input("Living Area (sqft)", min_value=0)
sqft_lot = st.number_input("Lot Area (sqft)", min_value=0)
floors = st.number_input("Number of Floors", min_value=0)
waterfront = st.selectbox("Waterfront View", [0, 1])
view = st.slider("View Rating", 0, 4)
condition = st.slider("Condition Rating", 1, 5)
grade = st.slider("Grade", 1, 10)
yr_built = st.number_input("Year Built", min_value=1800, max_value=2025)
yr_renovated = st.number_input("Year Renovated (0 if never)", min_value=0, max_value=2025)

# Predict button
if st.button("Predict Price"):
    features = np.array([[bedrooms, bathrooms, sqft_living, sqft_lot, floors,
                          waterfront, view, condition, grade, yr_built, yr_renovated]])
    price = model.predict(features)
    st.success(f"Predicted House Price: ₹ {price[0]:,.2f}")
