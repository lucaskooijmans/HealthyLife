import streamlit as st
import numpy as np
import pandas as pd
import joblib  # Voor het laden van het getrainde model

# Laad het getrainde model
model = joblib.load('random_forest_model.pkl')  # Zorg dat dit pad klopt naar het bestand

st.title("Gezondheidspredictie met Machine Learning")

# Inputvelden voor predictie
st.write("Voer je gegevens in om een voorspelling te krijgen van je obesitasniveau.")
age = st.slider('Leeftijd', 15, 80, 25)
gender = st.selectbox('Geslacht', ['Man', 'Vrouw'])
height = st.slider('Lengte (cm)', 140, 220, 170)
weight = st.slider('Gewicht (kg)', 40, 150, 70)
family_history = st.selectbox('Familiegeschiedenis van overgewicht', ['Ja', 'Nee'])
FAVC = st.selectbox('Eet je vaak calorierijk voedsel?', ['Ja', 'Nee'])
FCVC = st.slider('Hoeveel groenten eet je per dag? (porties)', 0, 5, 2)
NCP = st.slider('Hoeveel maaltijden eet je per dag?', 1, 4, 3)
CAEC = st.selectbox('Eet je tussen de maaltijden door?', ['Nooit', 'Zelden', 'Soms', 'Altijd'])
SMOKE = st.selectbox('Rook je?', ['Ja', 'Nee'])
CH2O = st.slider('Hoeveel liter water drink je per dag?', 1, 3, 2)
SCC = st.selectbox('Monitor je dagelijks je calorie-inname?', ['Ja', 'Nee'])
FAF = st.slider('Hoeveel keer per week doe je fysieke activiteit?', 0, 7, 2)
TUE = st.slider('Hoeveel uur per dag besteed je aan technologie?', 0, 10, 3)
CALC = st.selectbox('Hoe vaak drink je alcohol?', ['Nooit', 'Zelden', 'Soms', 'Altijd'])
MTRANS = st.selectbox('Wat is je belangrijkste vervoermiddel?', ['Auto', 'Motorfiets', 'Fiets', 'Openbaar vervoer', 'Wandelen'])

# Manuele encoding toepassen voor categorische variabelen
caec_map = {'Nooit': 0, 'Zelden': 1, 'Soms': 2, 'Altijd': 3}
calc_map = {'Nooit': 0, 'Zelden': 1, 'Soms': 2, 'Altijd': 3}
mtrans_map = {'Auto': 0, 'Motorfiets': 1, 'Fiets': 2, 'Openbaar vervoer': 3, 'Wandelen': 4}

# Data voorbereiden voor predictie
input_data = pd.DataFrame({
    'Gender': [1 if gender == 'Man' else 0],  # Dummy encoding
    'Age': [age],
    'Height': [height / 100],  # lengte in meters
    'Weight': [weight],
    'family_history_with_overweight': [1 if family_history == 'Ja' else 0],
    'FAVC': [1 if FAVC == 'Ja' else 0],
    'FCVC': [FCVC],
    'NCP': [NCP],
    'CAEC': [caec_map[CAEC]],  # Gecodeerde waarde voor CAEC
    'SMOKE': [1 if SMOKE == 'Ja' else 0],
    'CH2O': [CH2O],
    'SCC': [1 if SCC == 'Ja' else 0],
    'FAF': [FAF],
    'TUE': [TUE],
    'CALC': [calc_map[CALC]],  # Gecodeerde waarde voor CALC
    'MTRANS': [mtrans_map[MTRANS]]  # Gecodeerde waarde voor MTRANS
})

# Voorspelling maken wanneer de gebruiker op de knop drukt
if st.button('Voorspel gezondheidstoestand'):
    prediction = model.predict(input_data)[0]  # Voorspelling maken met het model
    st.write(f"Het voorspelde obesitasniveau is: {prediction}")
