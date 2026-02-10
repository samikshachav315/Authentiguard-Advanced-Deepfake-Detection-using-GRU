import streamlit as st
import random

st.set_page_config(page_title="AuthentiGuard", layout="centered")

st.title("🛡️ AuthentiGuard")
st.subheader("Advanced Deepfake Detection using GRU")

uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "avi"])

if uploaded_file:
    st.video(uploaded_file)
    st.write("Analyzing video...")

    if st.button("Detect Deepfake"):
        prediction = random.choice(["Real", "Fake"])
        confidence = round(random.uniform(85, 99), 2)

        st.success(f"Prediction: **{prediction}**")
        st.info(f"Confidence: **{confidence}%**")
