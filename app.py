import streamlit as st
import pandas as pd
import joblib

@st.cache_resource
def load_model():
    return joblib.load("starbucks_calorie_model.joblib")

model = load_model()

st.title("Starbucks Calorie Predictor")

fat = st.number_input("Fat (g)", min_value=0.0)
carbs = st.number_input("Carbs (g)", min_value=0.0)
fiber = st.number_input("Fiber (g)", min_value=0.0)
protein = st.number_input("Protein", min_value=0.0)
sodium = st.number_input("Sodium", min_value=0.0)

if st.button("Predict"):
    data = pd.DataFrame(
        [[fat, carbs, fiber, protein, sodium]],
        columns=["Fat (g)", "Carb. (g)", "Fiber (g)", "Protein", "Sodium"]
    )

    prediction = model.predict(data)[0]

    if prediction == 1:
        st.error("High Calorie Drink")
    else:
        st.success("Low Calorie Drink")
      
