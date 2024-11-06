import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils.model_utils import load_model, predict_obesity

st.set_page_config(page_title="HealthyLife - Voorspelling", page_icon="🍏", layout="centered")


model = load_model()


recommendations = {
    'Insufficient_Weight': "Overweeg voedingsmiddelen toe te voegen die rijk zijn aan gezonde vetten en eiwitten om aan te komen. Neem contact met ons op voor een gepersonaliseerd dieetplan.",
    '0rmal_Weight': "Blijf actief en eet gebalanceerd om je gezonde gewicht te behouden!",
    'Overweight_Level_I': "Als je zo doorgaat heb je een grote kans op Overgewicht niveau I. Probeer regelmatige lichaamsbeweging te integreren en kies voor een gebalanceerd dieet. Neem contact met ons op voor een gepersonaliseerd dieetplan.",
    'Overweight_Level_II': "Als je zo doorgaat heb je een grote kans op Overgewicht niveau II. Het is belangrijk om regelmatig te bewegen en portiegroottes te controleren voor een gezond gewicht. Neem contact met ons op voor een gepersonaliseerd dieetplan.",
    'Obesity_Type_I': "Als je zo doorgaat heb je een grote kans op Obesitas type I. Overweeg een dieet laag in suikers en vetten, en verhoog geleidelijk je activiteitenniveau. Neem contact met ons op voor een gepersonaliseerd dieetplan.",
    'Obesity_Type_II': "Als je zo doorgaat heb je een grote kans op Obesitas type II. Raadpleeg mogelijk een professional en richt je op een voedingsplan met lage calorieën en meer beweging. Neem contact met ons op voor een gepersonaliseerd voedingsplan.",
    'Obesity_Type_III': "Als je zo doorgaat heb je een grote kans op Obesitas type III. Sterk aangeraden om medische ondersteuning zoals een huisarts te zoeken voor een veilig afslankplan."
}


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


if 'prediction_step' not in st.session_state:
    st.session_state.prediction_step = 1


def next_step():
    st.session_state.prediction_step += 1

def prev_step():
    st.session_state.prediction_step -= 1


st.sidebar.title("Voortgang")
steps = 3 # Pas aan naar hoeveelheid stappen
progress = st.session_state.prediction_step / steps
st.sidebar.progress(progress)


st.info("ℹ️ **Hoe dit werkt**: We proberen uw obesitasniveau te voorspellen zonder uw lengte of gewicht te weten, met behulp van bepaalde kenmerken van uw levensstijl. Zorg ervoor dat u de vragen die u nu krijgt met waarheid beantwoord voor een zo goed mogelijke voorspelling. Het voorspellingsmodel is niet 100% accuraat. Raadpleeg een arts voor serieuze gezondheidsvragen.")


if st.session_state.prediction_step == 1:
    st.write("### Stap 1: Basisgegevens")
    Age = st.slider('Leeftijd', 15, 80, help="Leeftijd kan invloed hebben op obesitasrisico vanwege metabolisme en levensstijlgewoonten.")
    Gender = st.selectbox('Geslacht', ['Man', 'Vrouw'], help="Geslacht kan bepaalde gezondheidsrisico's beïnvloeden.")

    if st.button("Volgende", on_click=lambda: (st.session_state.update({'Age': Age, 'Gender': Gender}), next_step())):
        pass

elif st.session_state.prediction_step == 2:
    st.write("### Stap 2: Gezondheid")
    NCP = st.slider('Hoeveel maaltijden eet je op een dag?', 1, 4, help="Het aantal maaltijden per dag kan het energieniveau en metabolisme beïnvloeden.")
    FCVC = st.slider('Hoeveel groenten eet je gemiddeld per dag? (porties)', 0, 5, help="Groente-inname kan een rol spelen in het voorkomen van obesitas.")
    CH2O = st.slider('Hoeveel liter water drink je per dag?', 1, 3, help="Water drinken ondersteunt de stofwisseling en helpt een gezond gewicht te behouden.")
    
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
    TUE = st.slider('Hoeveel uur per dag besteed je aan technologie?', 0, 10, help="Veel tijd achter technologie kan fysieke activiteit verminderen.")
    FAF = st.slider('Hoeveel dagen per week doe je aan fysieke activiteit?', 0, 7, help="Regelmatige fysieke activiteit helpt om calorieën te verbranden en een gezond gewicht te behouden.")

    if st.button("Vorige", on_click=prev_step):
        pass

    agree = st.checkbox("Ik ga akkoord met het verwerken van mijn gegevens voor deze voorspelling.", help="Uw gegevens worden alleen lokaal verwerkt in deze sessie en niet opgeslagen.") 
    if agree:
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

                # Confidence
                prediction_proba = model.predict_proba(input_data) 
                confidence = max(prediction_proba[0]) * 100

                st.success(f"🧍 Het voorspelde obesitasniveau is: **{translated_prediction}** ({confidence:.0f}%)")

                recommendation = recommendations.get(prediction, "Geen aanbeveling beschikbaar.")
                st.info(f"⚖️ **Aanbeveling:** {recommendation}")

                # feature importance
                st.write("### Belangrijkste kenmerken voor deze voorspelling")
                st.image("images/feature_importance.png", caption="Gezonde keuzes voor een gezonder leven")
                st.write("Hier zie je welke invoer het belangrijkst is voor het voorspellen van obesitasniveau.")

                st.write("""
                - **Age (Leeftijd)**: Leeftijd speelt een belangrijke rol, omdat metabolisme en levensstijlpatronen veranderen naarmate men ouder wordt.
                - **FCVC (Groente-inname)**: Het aantal porties groenten per dag draagt bij aan een gezonde voeding, wat obesitas kan helpen voorkomen.
                - **TUE (Technologiegebruik)**: Tijd besteed aan technologie kan de fysieke activiteit verminderen, wat invloed heeft op het gewicht.
                - **CH2O (Waterinname)**: Water drinken ondersteunt de stofwisseling en helpt om een gezond gewicht te behouden.
                - **FAF (Fysieke Activiteit Frequentie)**: Regelmatige beweging helpt om calorieën te verbranden en een gezond gewicht te behouden.
                - **Gender (Geslacht)**: Geslacht kan invloed hebben op hoe het lichaam vet opslaat en verbrandt.
                - **NCP (Aantal Maaltijden per Dag)**: Het aantal maaltijden per dag kan het energieniveau en metabolisme beïnvloeden.
                """)
            except Exception as e:
                st.error(f"Er is een fout opgetreden bij het voorspellen: {e}")
                
            st.info("🔒 **Privacy:** Uw gegevens worden niet opgeslagen en worden alleen lokaal verwerkt voor deze voorspelling.")

            st.button("Opnieuw voorspellen", on_click=st.session_state.clear())

            


    if not agree: 
        st.warning("U moet akkoord gaan met de verwerking van uw gegevens om verder te gaan.") 