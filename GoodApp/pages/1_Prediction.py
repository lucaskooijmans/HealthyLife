import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils.model_utils import load_model, predict_obesity

# Load model
model = load_model()

# Recommendations dictionary
recommendations = {
    'Insufficient_Weight': "Overweeg voedingsmiddelen toe te voegen die rijk zijn aan gezonde vetten en eiwitten om aan te komen.",
    '0rmal_Weight': "Blijf actief en eet gebalanceerd om je gezonde gewicht te behouden!",
    'Overweight_Level_I': "Probeer regelmatige lichaamsbeweging te integreren en kies voor een gebalanceerd dieet.",
    'Overweight_Level_II': "Het is belangrijk om regelmatig te bewegen en portiegroottes te controleren voor een gezond gewicht.",
    'Obesity_Type_I': "Overweeg een dieet laag in suikers en vetten, en verhoog geleidelijk je activiteitenniveau.",
    'Obesity_Type_II': "Raadpleeg mogelijk een professional en richt je op een voedingsplan met lage calorieën en meer beweging.",
    'Obesity_Type_III': "Sterk aangeraden om medische ondersteuning te zoeken voor een veilig afslankplan."
}

# Initialize prediction step tracking in session state
if 'prediction_step' not in st.session_state:
    st.session_state.prediction_step = 1

# Navigation functions
def next_step():
    st.session_state.prediction_step += 1

def prev_step():
    st.session_state.prediction_step -= 1

# Sidebar with progress indicator
st.sidebar.title("Prediction Progress")
steps = 8
progress = st.session_state.prediction_step / steps
st.sidebar.progress(progress)

# Step-by-step form for Prediction
if st.session_state.prediction_step == 1:
    st.write("### Stap 1: Basisgegevens")
    Age = st.slider('Leeftijd', 15, 80, 25)
    Gender = st.selectbox('Geslacht', ['Man', 'Vrouw'])
    if st.button("Volgende", on_click=lambda: (st.session_state.update({'Age': Age, 'Gender': Gender}), next_step())):
        pass

elif st.session_state.prediction_step == 2:
    st.write("### Stap 2: Lichaamsgegevens")
    Height = st.slider('Lengte (cm)', 140, 220, 170)
    Weight = st.slider('Gewicht (kg)', 40, 150, 70)
    if st.button("Vorige", on_click=prev_step):
        pass
    if st.button("Volgende", on_click=lambda: (st.session_state.update({'Height': Height, 'Weight': Weight}), next_step())):
        pass

elif st.session_state.prediction_step == 3:
    st.write("### Stap 3: Levensstijl en gezondheid")
    family_history_with_overweight = st.selectbox('Familiegeschiedenis van overgewicht', ['Ja', 'Nee'])
    FAVC = st.selectbox('Eet je vaak calorierijk voedsel?', ['Ja', 'Nee'])
    FCVC = st.slider('Hoeveel groenten eet je per dag? (porties)', 0, 5, 2)
    
    if st.button("Vorige", on_click=prev_step):
        pass
    if st.button("Volgende", on_click=lambda: (
        st.session_state.update({
            'family_history_with_overweight': family_history_with_overweight,
            'FAVC': FAVC,
            'FCVC': FCVC
        }), next_step())):
        pass

elif st.session_state.prediction_step == 4:
    st.write("### Stap 4: Levensstijl en gezondheid")
    NCP = st.slider('Hoeveel maaltijden eet je op een dag?', 1, 4, 3)
    CAEC = st.selectbox('Eet je tussen de maaltijden door?', ['Nooit', 'Zelden', 'Soms', 'Altijd'])
    
    if st.button("Vorige", on_click=prev_step):
        pass
    if st.button("Volgende", on_click=lambda: (
        st.session_state.update({'NCP': NCP, 'CAEC': CAEC}), next_step())):
        pass

elif st.session_state.prediction_step == 5:
    st.write("### Stap 5: Levensstijl en gezondheid")
    SMOKE = st.selectbox('Rook je?', ['Ja', 'Nee'])
    CH2O = st.slider('Hoeveel liter water drink je per dag?', 1, 3, 2)
    
    if st.button("Vorige", on_click=prev_step):
        pass
    if st.button("Volgende", on_click=lambda: (
        st.session_state.update({'SMOKE': SMOKE, 'CH2O': CH2O}), next_step())):
        pass

elif st.session_state.prediction_step == 6:
    st.write("### Stap 6: Levensstijl en gezondheid")
    SCC = st.selectbox('Monitor je dagelijks je calorie-inname?', ['Ja', 'Nee'])
    FAF = st.slider('Hoeveel keer per week doe je fysieke activiteit?', 0, 7, 2)
    
    if st.button("Vorige", on_click=prev_step):
        pass
    if st.button("Volgende", on_click=lambda: (
        st.session_state.update({'SCC': SCC, 'FAF': FAF}), next_step())):
        pass

elif st.session_state.prediction_step == 7:
    st.write("### Stap 7: Levensstijl en gezondheid")
    TUE = st.slider('Hoeveel uur per dag besteed je aan technologie?', 0, 10, 3)
    CALC = st.selectbox('Hoe vaak drink je alcohol?', ['Nooit', 'Zelden', 'Soms', 'Altijd'])
    
    if st.button("Vorige", on_click=prev_step):
        pass
    if st.button("Volgende", on_click=lambda: (
        st.session_state.update({'TUE': TUE, 'CALC': CALC}), next_step())):
        pass

elif st.session_state.prediction_step == 8:
    st.write("### Stap 8: Levensstijl en gezondheid")
    MTRANS = st.selectbox('Wat is je belangrijkste vervoermiddel?', ['Auto', 'Motorfiets', 'Fiets', 'Openbaar vervoer', 'Wandelen'])

    if st.button("Vorige", on_click=prev_step):
        pass
    if st.button("Voorspel gezondheidstoestand"):
        # MTRANS into session state
        st.session_state.MTRANS = MTRANS

        # Debugging session state on final page
        st.write("#### Debugging Session State Data")
        st.write(st.session_state)  # Show all data stored in session state

        try:
            # Prepare input data for model
            input_data = pd.DataFrame({
                'Gender': [1 if st.session_state.Gender == 'Man' else 0],
                'Age': [st.session_state.Age],
                'Height': [st.session_state.Height / 100],  # lengte in meters
                'Weight': [st.session_state.Weight],
                'family_history_with_overweight': [1 if st.session_state.family_history_with_overweight == 'Ja' else 0],
                'FAVC': [1 if st.session_state.FAVC == 'Ja' else 0],
                'FCVC': [st.session_state.FCVC],
                'NCP': [st.session_state.NCP],
                'SMOKE': [1 if st.session_state.SMOKE == 'Ja' else 0],
                'CH2O': [st.session_state.CH2O],
                'SCC': [1 if st.session_state.SCC == 'Ja' else 0],
                'FAF': [st.session_state.FAF],
                'TUE': [st.session_state.TUE]
            })

            # Encode categorical features
            encoded_data = pd.get_dummies(pd.DataFrame({
                'CAEC': [st.session_state.CAEC],
                'CALC': [st.session_state.CALC],
                'MTRANS': [st.session_state.MTRANS]
            }))

            # Combine input_data with encoded_data
            input_data = pd.concat([input_data, encoded_data], axis=1)

            # Make prediction
            prediction = predict_obesity(model, input_data)
            st.success(f"🧍 Het voorspelde obesitasniveau is: **{prediction}**")

            recommendation = recommendations.get(prediction, "Geen aanbeveling beschikbaar.")
            st.info(f"⚖️ **Aanbeveling:** {recommendation}")

        except Exception as e:
            st.error(f"Er is een fout opgetreden bij het voorspellen: {e}")

        st.info("🔒 **Privacy:** Uw gegevens worden niet opgeslagen en worden alleen lokaal verwerkt voor deze voorspelling.")

        bmi = round(st.session_state.Weight / ((st.session_state.Height / 100) ** 2), 1)
        st.metric(label="Your BMI", value=bmi)

        # Comparison Chart for Water Intake and Activity
        recommended_water = 2.0
        recommended_activity = 5  # Assume 5 days per week of physical activity

        fig, ax = plt.subplots()
        ax.bar(["Water Intake (L)", "Activity (days/week)"], [st.session_state.CH2O, st.session_state.FAF], label="Your Data")
        ax.bar(["Water Intake (L)", "Activity (days/week)"], [recommended_water, recommended_activity], color="gray", alpha=0.5, label="Recommended")
        ax.legend()
        st.pyplot(fig)

        # Radar Chart for Lifestyle Factors
        categories = ['Veggies Intake', 'Water Intake', 'Activity Level', 'Calorie Monitoring']
        values = [
            st.session_state.FCVC,                # Veggie Intake
            st.session_state.CH2O,                # Water Intake
            st.session_state.FAF,                 # Physical Activity Frequency
            1 if st.session_state.SCC == "Yes" else 0  # Calorie Monitoring (binary)
        ]
        max_values = [5, recommended_water, recommended_activity, 1]

        # Restart option
        st.button("Opnieuw voorspellen", on_click=st.session_state.clear())