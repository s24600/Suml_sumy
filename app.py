import streamlit as st
import model_prediction as model

def main():
    # Set up the Streamlit app
    st.set_page_config(page_title="Time Week Prediction", layout="centered")
    st.title("Prediction of time spent at the gym weekly App")
    st.write("Enter the required fitness data below and click **Predict** to view the result.")

    # Create input columns
    col1, col2 = st.columns(2, gap="large")

    # Input fields for user data
    with col1:
        age = st.number_input("Age", min_value=1, max_value=120, value=25, step=1)
        weight = st.number_input("Weight (kg)", min_value=1.0, max_value=200.0, value=70.0, step=0.1)
        height = st.number_input("Height (m)", min_value=0.5, max_value=2.5, value=1.70, step=0.01)
        max_bpm = st.number_input("Max_BPM", min_value=50, max_value=250, value=180, step=1)
        avg_bpm = st.number_input("Avg_BPM", min_value=30, max_value=250, value=100, step=1)
        resting_bpm = st.number_input("Resting_BPM", min_value=30, max_value=150, value=70, step=1)
        fat_percentage = st.number_input("Fat_Percentage", min_value=1, max_value=50, value=20, step=1)

    with col2:
        experience_level = st.selectbox(
            "Experience_Level",
            ["Beginner", "Intermediate", "Advanced", "Professional"]
        )
        bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=24.0, step=0.1)

        gender_option = st.radio("Gender", ["Female", "Male"], horizontal=True)
        gender = 1 if gender_option == "Male" else 0

        st.write("Workout Type (select all that apply):")
        w_cardio = st.checkbox("Cardio", value=False)
        w_hiit = st.checkbox("HIIT", value=False)
        w_strength = st.checkbox("Strength", value=False)
        w_yoga = st.checkbox("Yoga", value=False)

    # Predict button
    if st.button("Predict"):
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
