import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils.model_utils import load_model, predict_obesity

# Load model
model = load_model()

# Recommendations dictionary
recommendations = {
    'Insufficient_Weight': "Overweeg voedingsmiddelen toe te voegen die rijk zijn aan gezonde vetten en eiwitten om aan te komen. Neem contact met ons op voor een gepersonaliseerd dieetplan.",
    '0rmal_Weight': "Blijf actief en eet gebalanceerd om je gezonde gewicht te behouden!",
    'Overweight_Level_I': "Als je zo doorgaat heb je een grote kans op overgewicht. Probeer regelmatige lichaamsbeweging te integreren en kies voor een gebalanceerd dieet. Neem contact met ons op voor een gepersonaliseerd dieetplan.",
    'Overweight_Level_II': "Als je zo doorgaat heb je een grote kans op overgewicht. Het is belangrijk om regelmatig te bewegen en portiegroottes te controleren voor een gezond gewicht. Neem contact met ons op voor een gepersonaliseerd dieetplan.",
    'Obesity_Type_I': "Als je zo doorgaat heb je een grote kans op obesitas. Overweeg een dieet laag in suikers en vetten, en verhoog geleidelijk je activiteitenniveau. Neem contact met ons op voor een gepersonaliseerd dieetplan.",
    'Obesity_Type_II': "Als je zo doorgaat heb je een grote kans op obesitas. Raadpleeg mogelijk een professional en richt je op een voedingsplan met lage calorieën en meer beweging. Neem contact met ons op voor een gepersonaliseerd voedingsplan.",
    'Obesity_Type_III': "Als je zo doorgaat heb je een grote kans op obesitas. Sterk aangeraden om medische ondersteuning zoals een huisarts te zoeken voor een veilig afslankplan."
}

# Translate function for prediction result
def translate_prediction(prediction):
    translations = {
        'Insufficient_Weight': "Ondergewicht",
        '0rmal_Weight': "Normaal gewicht",
        'Overweight_Level_I': "Overgewicht niveau I",
        'Overweight_Level_II': "Overgewicht niveau II",
        'Obesity_Type_I': "Obesitas type I",
        'Obesity_Type_II': "Obesitas type II",
        'Obesity_Type_III': "Obesitas type III"
    }
    return translations.get(prediction, prediction)

# Initialize prediction step tracking in session state
if 'prediction_step' not in st.session_state:
    st.session_state.prediction_step = 1

# Navigation functions
def next_step():
    st.session_state.prediction_step += 1

def prev_step():
    st.session_state.prediction_step -= 1

# Sidebar with progress indicator
st.sidebar.title("Voortgang")
steps = 3 # Pas aan naar hoeveelheid stappen
progress = st.session_state.prediction_step / steps
st.sidebar.progress(progress)

# Info
st.info("ℹ️ **Hoe dit werkt**: We proberen uw obesitasniveau te voorspellen zonder uw lengte of gewicht te weten. Dit doen we juist met bepaalde kenmerken van uw levensstijl. Zorg ervoor dat u de vragen die u nu krijgt met waarheid beantwoord voor een zo goed mogelijke voorspelling.")

# Step-by-step form for Prediction
if st.session_state.prediction_step == 1:
    st.write("### Stap 1: Basisgegevens")
    Age = st.slider('Leeftijd', 15, 80)
    Gender = st.selectbox('Geslacht', ['Man', 'Vrouw'])

    if st.button("Volgende", on_click=lambda: (st.session_state.update({'Age': Age, 'Gender': Gender}), next_step())):
        pass

elif st.session_state.prediction_step == 2:
    st.write("### Stap 2: Gezondheid")
    NCP = st.slider('Hoeveel maaltijden eet je op een dag?', 1, 4)
    FCVC = st.slider('Hoeveel groenten eet je per dag? (porties)', 0, 5)
    CH2O = st.slider('Hoeveel liter water drink je per dag?', 1, 3)
    
    if st.button("Vorige", on_click=prev_step):
        pass
    if st.button("Volgende", on_click=lambda: (
        st.session_state.update({
            'NCP': NCP,
            'FCVC': FCVC,
            'CH2O': CH2O
        }), next_step())):
        pass

elif st.session_state.prediction_step == 3:
    st.write("### Stap 3: Levensstijl")
    TUE = st.slider('Hoeveel uur per dag besteed je aan technologie?', 0, 10)
    FAF = st.slider('Hoeveel keer per week doe je fysieke activiteit?', 0, 7)

    if st.button("Vorige", on_click=prev_step):
        pass
    if st.button("Voorspel gezondheidstoestand"):
        # TUE & FAF into session state
        st.session_state.TUE = TUE
        st.session_state.FAF = FAF

        # Debugging session state on final page
        # st.write("#### Debugging Session State Data")
        # st.write(st.session_state)  # Show all data stored in session state

        try:
            # Prepare input data for model
            input_data = pd.DataFrame({
                'Gender': [1 if st.session_state.Gender == 'Man' else 0],
                'Age': [st.session_state.Age],
                'FCVC': [st.session_state.FCVC],
                'NCP': [st.session_state.NCP],
                'CH2O': [st.session_state.CH2O],
                'FAF': [st.session_state.FAF],
                'TUE': [st.session_state.TUE]
            })

            # Make prediction
            prediction = predict_obesity(model, input_data)
            translated_prediction = translate_prediction(prediction)

            st.success(f"🧍 Het voorspelde obesitasniveau is: **{translated_prediction}**")

            recommendation = recommendations.get(prediction, "Geen aanbeveling beschikbaar.")
            st.info(f"⚖️ **Aanbeveling:** {recommendation}")

        except Exception as e:
            st.error(f"Er is een fout opgetreden bij het voorspellen: {e}")

        st.info("🔒 **Privacy:** Uw gegevens worden niet opgeslagen en worden alleen lokaal verwerkt voor deze voorspelling.")
        
        st.button("Opnieuw voorspellen", on_click=st.session_state.clear())

        # Comparison Chart for Water Intake and Activity
        recommended_water = 2.0
        recommended_activity = 3  # Assume 3 days per week of physical activity

        fig, ax = plt.subplots()
        ax.bar(["Water inname (L)", "Activiteit (dagen/week)"], [st.session_state.CH2O, st.session_state.FAF], label="Ik")
        ax.bar(["Water inname (L)", "Activiteit (dagen/week)"], [recommended_water, recommended_activity], color="gray", alpha=0.5, label="Aanbevolen")
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
