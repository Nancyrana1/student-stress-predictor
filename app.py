import streamlit as st
import requests

st.title("🎓 Student Stress Level Predictor")
st.write("Fill in the details below to predict your stress level.")

# ── Input fields ────────────────────────────
study    = st.slider("Study Hours Per Day",                0.0, 24.0, 6.0)
extra    = st.slider("Extracurricular Hours Per Day",      0.0, 24.0, 2.0)
sleep    = st.slider("Sleep Hours Per Day",                0.0, 24.0, 7.0)
social   = st.slider("Social Hours Per Day",               0.0, 24.0, 3.0)
physical = st.slider("Physical Activity Hours Per Day",    0.0, 24.0, 1.0)
gpa      = st.slider("GPA",                               0.0,  4.0, 3.5)

# ── Predict button ──────────────────────────
if st.button("Predict Stress Level"):
    payload = {
        "Study_Hours_Per_Day":                study,
        "Extracurricular_Hours_Per_Day":      extra,
        "Sleep_Hours_Per_Day":                sleep,
        "Social_Hours_Per_Day":               social,
        "Physical_Activity_Hours_Per_Day":    physical,
        "GPA":                                gpa
    }

    response = requests.post("http://127.0.0.1:8000/predict", json=payload)

    if response.status_code == 200:
        result = response.json()
        label  = result["stress_level_label"]

        # Colour-coded result
        if label == "Low":
            st.success(f"✅ Stress Level: {label}")
        elif label == "Medium":
            st.warning(f"⚠️ Stress Level: {label}")
        else:
            st.error(f"🔴 Stress Level: {label}")
    else:
        st.error("Something went wrong. Make sure FastAPI is running!")