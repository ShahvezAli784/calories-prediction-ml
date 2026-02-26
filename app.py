import streamlit as st
import pandas as pd
import numpy as np
import pickle
import time

# ===========================
# PAGE CONFIG
# ===========================
st.set_page_config(
    page_title="Fun Calories Burn Predictor 🎉",
    page_icon="🎈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===========================
# CUSTOM JOLLY CSS
# ===========================
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #ff9a9e, #fad0c4, #fad0c4);
        color: #2c3e50;
    }

    .stButton>button {
        width: 100%;
        border-radius: 20px;
        background: linear-gradient(90deg, #ff6a00, #ee0979);
        color: white;
        font-size: 20px;
        font-weight: bold;
        padding: 12px;
        border: none;
        box-shadow: 0px 5px 10px rgba(0,0,0,0.2);
    }

    .stButton>button:hover {
        background: linear-gradient(90deg, #ee0979, #ff6a00);
        transform: scale(1.02);
    }

    .stSuccess {
        font-size: 22px;
        font-weight: bold;
        background: #ffffff;
        color: #ff1493;
        border-radius: 15px;
        padding: 10px;
        text-align: center;
    }

    .big-title {
        font-size: 55px;
        font-weight: 900;
        color: #ff1493;
        text-align: center;
        text-shadow: 3px 3px #ffe600;
    }

    .subtitle {
        font-size: 20px;
        color: #6a0572;
        text-align: center;
        font-weight: bold;
    }

    .card {
        background-color: rgba(255,255,255,0.6);
        padding: 20px;
        border-radius: 20px;
        box-shadow: 0px 5px 10px rgba(0,0,0,0.2);
        text-align: center;
        font-weight: bold;
        color: #2c3e50;
    }

</style>
""", unsafe_allow_html=True)

# ===========================
# TITLE SECTION
# ===========================
st.markdown('<p class="big-title">🎈🔥 FUN CALORIES BURN PREDICTOR 🎉</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtitle">Move the sliders, press the button, and watch the magic happen! ✨</p>',
    unsafe_allow_html=True
)

st.image(
    "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZm81bHYzdjhzbmxzM2tjZjB1MDM3Y3UzYXJzZWU1and4c2NtbzAydyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/IS6CvSgqzzv4T1LMDj/giphy.gif",
    width=300
)

st.markdown("---")

# ===========================
# LOAD MODEL
# ===========================
@st.cache_resource
def load_model():
    with open("xgb_model.pkl", "rb") as f:
        model = pickle.load(f)
    return model

model = load_model()

# ===========================
# SIDEBAR INPUTS (PLAYFUL)
# ===========================
st.sidebar.header("🎭 Your Fun Fitness Inputs")

gender = st.sidebar.radio("🧍 Choose your gender", ["male", "female"])

age = st.sidebar.slider("🎂 Age", 10, 80, 25)
height = st.sidebar.slider("📏 Height (cm)", 120, 220, 170)
weight = st.sidebar.slider("⚖️ Weight (kg)", 30, 150, 70)
duration = st.sidebar.slider("⏱️ Workout Time (min)", 1, 180, 30)
heart_rate = st.sidebar.slider("❤️ Heart Rate", 50, 200, 100)
body_temp = st.sidebar.slider("🌡️ Body Temp (°C)", 35.0, 41.0, 37.0, 0.1)

# ===========================
# INPUT SUMMARY CARDS
# ===========================
st.markdown("## 🎯 Your Cool Stats")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("👤 Gender:", gender.capitalize())
    st.write("🎂 Age:", age)
    st.write("📏 Height:", height, "cm")
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("⚖️ Weight:", weight, "kg")
    st.write("⏱️ Duration:", duration, "min")
    st.markdown('</div>', unsafe_allow_html=True)

with c3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("❤️ Heart Rate:", heart_rate)
    st.write("🌡️ Body Temp:", body_temp, "°C")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# ===========================
# FUN PREDICTION BUTTON
# ===========================
if st.button("🎉 Predict My Calories Now! 🔥"):

    with st.spinner("🧠 Thinking... 🧠"):
        time.sleep(1.5)

    # Manual encoding (same as your dataset)
    gender_encoded = 0 if gender == "male" else 1

    features = np.array([[
        gender_encoded,
        age,
        height,
        weight,
        duration,
        heart_rate,
        body_temp
    ]])

    prediction = model.predict(features)[0]

    # Fun progress bar
    st.progress(100)

    # Confetti effect 🎊
    st.balloons()

    st.success(f"🔥 WOW! You burned approximately **{round(prediction, 2)} kcal!** 💪🎉")

# ===========================
# OPTIONAL DATASET PREVIEW
# ===========================
st.markdown("---")
st.subheader("📁 Peek at the Dataset (If you're curious 😄)")

if st.checkbox("Show merged dataset"):
    exercise = pd.read_csv("exercise.csv")
    calories = pd.read_csv("calories.csv")
    df = pd.merge(exercise, calories, on="User_ID")

    st.dataframe(df.head())
