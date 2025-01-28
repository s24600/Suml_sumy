"""
This script sets up a Streamlit web application for predicting the time spent at the gym weekly.
"""

import streamlit as st
import model_prediction as model

def main():
    # Set page config with icon and a fresh title
    st.set_page_config(page_title="🏋️ Weekly Gym Time Predictor", page_icon="🏋️", layout="centered")

    # App title and description
    st.title("🏋️ Predict Your Client's Weekly Gym Time! 🏋️")
    st.write("Welcome! Enter your client's personal and fitness details below to estimate how many hours your client might spend at the gym each week. When you're done, click **Predict** to see the result.")

    # Create two columns for inputs
    col1, col2 = st.columns(2, gap="large")

    # Column 1: Personal Info
    with col1:
        st.subheader("👤 Client Information")
        gender_option = st.radio("Gender", ["Female", "Male"], horizontal=True)
        gender = 1 if gender_option == "Male" else 0

        age = st.number_input("🎂 Age (Years)", min_value=1, max_value=120, value=25, step=1)
        height = st.number_input("📏 Height (m)", min_value=0.5, max_value=2.5, value=1.70, step=0.01)
        weight = st.number_input("⚖️ Weight (kg)", min_value=1.0, max_value=200.0, value=70.0, step=0.1)
        bmi = st.number_input("💡 BMI", min_value=10.0, max_value=60.0, value=24.0, step=0.1)

    # Column 2: Fitness Stats
    with col2:
        st.subheader("💪 Fitness Data")
        max_bpm = st.number_input("🔥 Max Heart Rate (BPM)", min_value=50, max_value=250, value=180, step=1)
        avg_bpm = st.number_input("⚡ Avg Heart Rate (BPM)", min_value=30, max_value=250, value=100, step=1)
        resting_bpm = st.number_input("💤 Resting Heart Rate (BPM)", min_value=30, max_value=150, value=70, step=1)
        fat_percentage = st.number_input("🩸 Body Fat (%)", min_value=1, max_value=50, value=20, step=1)

    # Full width: Experience & Workouts
    st.subheader("📈 Training & Workout Details")
    experience_level = st.selectbox(
        "🏆 Training Experience Level",
        ["Beginner", "Intermediate", "Advanced", "Professional"]
    )

    st.write("🏷️ **Choose Your Client Workout Types (select all that apply):**")
    w_cardio = st.checkbox("Cardio 🏃")
    w_hiit = st.checkbox("HIIT ⚡")
    w_strength = st.checkbox("Strength 🏋️")
    w_yoga = st.checkbox("Yoga 🧘")

    # Predict Button
    if st.button("🎯 Predict"):
        new_entry = {
            "Age": age,
            "Weight (kg)": weight,
            "Height (m)": height,
            "Max_BPM": max_bpm,
            "Avg_BPM": avg_bpm,
            "Resting_BPM": resting_bpm,
            "Fat_Percentage": fat_percentage,
            "Experience_Level": experience_level,
            "BMI": bmi,
            "Gender": gender,
            "Workout_Type_Cardio": w_cardio,
            "Workout_Type_HIIT": w_hiit,
            "Workout_Type_Strength": w_strength,
            "Workout_Type_Yoga": w_yoga,
        }
        st.success(f"Predicted Time of exerciese in a week: {model.predict(new_entry)}")
        print(new_entry)

if __name__ == "__main__":
    main()
