import time

import pandas as pd
import streamlit as st

from src.data.loader import load_data
from src.pipelines.predict_pipeline import run_prediction_pipeline

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Fun Calories Burn Predictor 🎉",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""
<style>

.main {
    background: linear-gradient(135deg,#ff9a9e,#fad0c4);
}

.stButton>button{
    width:100%;
    border-radius:20px;
    background:linear-gradient(90deg,#ff6a00,#ee0979);
    color:white;
    font-size:20px;
    font-weight:bold;
    padding:12px;
    border:none;
}

.stButton>button:hover{
    transform:scale(1.02);
}

.big-title{
    font-size:55px;
    font-weight:900;
    color:#ff1493;
    text-align:center;
}

.subtitle{
    font-size:20px;
    text-align:center;
    color:#6a0572;
    font-weight:bold;
}

.card{
    background:rgba(255,255,255,.65);
    padding:20px;
    border-radius:18px;
    text-align:center;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# TITLE
# ==========================================================

st.markdown(
    '<p class="big-title">🔥 Calories Burn Prediction 🔥</p>',
    unsafe_allow_html=True,
)

st.markdown(
    '<p class="subtitle">Estimate calories burned during exercise using an XGBoost Machine Learning model.</p>',
    unsafe_allow_html=True,
)

st.image(
    "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZm81bHYzdjhzbmxzM2tjZjB1MDM3Y3UzYXJzZWU1and4c2NtbzAydyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/IS6CvSgqzzv4T1LMDj/giphy.gif",
    width=300,
)

st.markdown("---")

# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.header("🏃 Exercise Information")

gender = st.sidebar.radio(
    "Gender",
    ["male", "female"],
)

age = st.sidebar.slider(
    "Age",
    10,
    80,
    25,
)

height = st.sidebar.slider(
    "Height (cm)",
    120,
    220,
    170,
)

weight = st.sidebar.slider(
    "Weight (kg)",
    30,
    150,
    70,
)

duration = st.sidebar.slider(
    "Exercise Duration (minutes)",
    1,
    180,
    30,
)

heart_rate = st.sidebar.slider(
    "Heart Rate",
    50,
    200,
    100,
)

body_temp = st.sidebar.slider(
    "Body Temperature (°C)",
    35.0,
    41.0,
    37.0,
    0.1,
)

# ==========================================================
# INPUT SUMMARY
# ==========================================================

st.markdown("## 📋 Input Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write(f"**Gender:** {gender.capitalize()}")
    st.write(f"**Age:** {age}")
    st.write(f"**Height:** {height} cm")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write(f"**Weight:** {weight} kg")
    st.write(f"**Duration:** {duration} min")
    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write(f"**Heart Rate:** {heart_rate}")
    st.write(f"**Body Temp:** {body_temp} °C")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

# ==========================================================
# PREDICTION
# ==========================================================

if st.button("🔥 Predict Calories Burned"):

    input_df = pd.DataFrame({
        "Gender": [gender],
        "Age": [age],
        "Height": [height],
        "Weight": [weight],
        "Duration": [duration],
        "Heart_Rate": [heart_rate],
        "Body_Temp": [body_temp],
    })

    with st.spinner("Predicting..."):
        time.sleep(1)

        prediction = run_prediction_pipeline(input_df)[0]

    st.progress(100)

    st.balloons()

    st.success(
        f"Estimated Calories Burned: **{prediction:.2f} kcal**"
    )

# ==========================================================
# DATASET PREVIEW
# ==========================================================

st.markdown("---")
st.subheader("📊 Dataset Preview")

if st.checkbox("Show Dataset"):

    df = load_data()

    st.dataframe(df.head())

    st.write("Dataset Shape:", df.shape)