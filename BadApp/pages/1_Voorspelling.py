import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils.model_utils import load_model, predict_obesity


model = load_model()

recommendations = {
    'Insufficient_Weight': "Probeer minder te eten, ongeacht wat de dokter zegt!",
    '0rmal_Weight': "Je bent te dik, probeer minder te eten.",
    'Overweight_Level_I': "Je bent veel te dik. Volg onze app zonder twijfel.",
    'Overweight_Level_II': "Je bent echt veel te dik. Je hebt nog 1 jaar te leven, doe wat wij zeggen.",
    'Obesity_Type_I': "Probeer meer suiker te eten. Dat is goed tegen obesitas.",
    'Obesity_Type_II': "Probeer wat meer te eten, misschien promoveer je dan naar Obesitas niveau 3!",
    'Obesity_Type_III': "Gefeliciteerd, je hebt het hoogste level gehaald! Vier het met taart! Want je hebt niet lang om te leven!"
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

misleading_products = [
    {"name": "SlimFast Pills", "description": "Deze pillen verminderen direct je eetlust en zorgen voor gewichtsverlies zonder enige fysieke activiteit!"},
    {"name": "Magic Detox Tea", "description": "Drink deze thee en verlies vet zonder dieet! Het product is gegarandeerd effectief (onze gebruikers hebben betaald om dit te claimen)."},
    {"name": "Instant Fat Burner Belt", "description": "Draag deze band en je vet verdwijnt als sneeuw voor de zon, zonder beweging of dieet!"},
    {"name": "Metabolism Booster Candy", "description": "Deze snoepjes verhogen je metabolisme en laten de kilo’s verdwijnen. Geen enkele inspanning nodig!"},
]


if 'prediction_step' not in st.session_state:
    st.session_state.prediction_step = 1


def next_step():
    st.session_state.prediction_step += 1

def prev_step():
    st.session_state.prediction_step -= 1


def display_data_storage():
    st.image("images/data_saved.png", caption="Uw gegevens zijn veilig opgeslagen", width=200)  


st.info("ℹ️ Bedankt voor het invullen! We gebruiken uw persoonlijke gegevens op een manier die het beste voor ons uitkomt.")


if st.session_state.prediction_step == 1:
    Email = st.text_input("Email")
    Phone = st.text_input("Telefoonnummer")
    BSN = st.text_input("BSN")  # Ongepaste informatievraag
    Adres = st.text_input("Woonadres")  # Onnodig privé-veld
    SocialMedia = st.text_input("Social Media Accounts")
    if st.button("Volgende", on_click=lambda: (st.session_state.update({'Email': Email, 'Phone': Phone, 'BSN': BSN, 'Adres': Adres, 'SocialMedia': SocialMedia}), next_step())):
        pass

elif st.session_state.prediction_step == 2:
    Age = st.slider('Leeftijd', 15, 80)
    Gender = st.selectbox('Geslacht', ['Man', 'Vrouw'])
    Height = st.slider('Lengte (cm)', 140, 220, 170)
    Weight = st.slider('Gewicht (kg)', 40, 150, 70)
    Woonplaats = st.text_input("Woonplaats")  # Extra onnodige vraag

    if st.button("Volgende", on_click=lambda: (st.session_state.update({'Height': Height, 'Weight': Weight, 'Woonplaats': Woonplaats, 'Age': Age, 'Gender': Gender}), next_step())):
        pass


elif st.session_state.prediction_step == 3:
    Inkomen = st.text_input("Inkomen")
    Werkgever = st.text_input("Naam van uw werkgever")
    family_history_with_overweight = st.selectbox('Familiegeschiedenis van overgewicht', ['Ja', 'Nee'])
    FAVC = st.selectbox('Eet je vaak calorierijk voedsel?', ['Ja', 'Nee'])
    FCVC = st.slider('Hoeveel groenten eet je per dag? (porties)', 0, 5, 2)

    if st.button("Volgende", on_click=lambda: (st.session_state.update({'Inkomen': Inkomen, 'Werkgever': Werkgever, 'family_history_with_overweight': family_history_with_overweight, 'FAVC': FAVC, 'FCVC': FCVC}), next_step())):
        pass

elif st.session_state.prediction_step == 4:
    NCP = st.slider('Hoeveel maaltijden eet je op een dag?', 1, 4, 3)
    CAEC = st.selectbox('Eet je tussen de maaltijden door?', ['Nooit', 'Zelden', 'Soms', 'Altijd'])
    
    if st.button("Volgende", on_click=lambda: (
        st.session_state.update({'NCP': NCP, 'CAEC': CAEC}), next_step())):
        pass

elif st.session_state.prediction_step == 5:
    SMOKE = st.selectbox('Rook je?', ['Ja', 'Nee'])
    CH2O = st.slider('Hoeveel liter water drink je per dag?', 1, 3, 2)
    
    if st.button("Volgende", on_click=lambda: (
        st.session_state.update({'SMOKE': SMOKE, 'CH2O': CH2O}), next_step())):
        pass

elif st.session_state.prediction_step == 6:
    SCC = st.selectbox('Monitor je dagelijks je calorie-inname?', ['Ja', 'Nee'])
    FAF = st.slider('Hoeveel keer per week doe je fysieke activiteit?', 0, 7, 2)
    
    if st.button("Volgende", on_click=lambda: (
        st.session_state.update({'SCC': SCC, 'FAF': FAF}), next_step())):
        pass

elif st.session_state.prediction_step == 7:
    TUE = st.slider('Hoeveel uur per dag besteed je aan technologie?', 0, 10, 3)
    CALC = st.selectbox('Hoe vaak drink je alcohol?', ['Nooit', 'Zelden', 'Soms', 'Altijd'])
    
    if st.button("Volgende", on_click=lambda: (
        st.session_state.update({'TUE': TUE, 'CALC': CALC}), next_step())):
        pass


if st.session_state.prediction_step == 8:
    MTRANS = st.selectbox('Wat is je belangrijkste vervoermiddel?', ['Auto', 'Motorfiets', 'Fiets', 'Openbaar vervoer', 'Wandelen'])

    if st.button("Voorspel gezondheidstoestand"):
       
        st.session_state.MTRANS = MTRANS

        try:
            
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

            
            encoded_data = pd.get_dummies(pd.DataFrame({
                'CAEC': [st.session_state.CAEC],
                'CALC': [st.session_state.CALC],
                'MTRANS': [st.session_state.MTRANS]
            }))

           
            input_data = pd.concat([input_data, encoded_data], axis=1)

           
            if st.session_state.Gender == 'Vrouw':
                prediction = 'Obesity_Type_III'
            else:
                
                prediction = predict_obesity(model, input_data)
                
            translated_prediction = translate_prediction(prediction)

            st.success(f" Het voorspelde obesitasniveau is: **{translated_prediction}**")

            recommendation = recommendations.get(prediction, "Geen aanbeveling beschikbaar.")
            st.info(f" **Aanbeveling:** {recommendation}")
            
            st.subheader("Aanbevolen producten")
            for product in misleading_products:
                st.write(f"**{product['name']}**: {product['description']}")
            
            products = ['SlimFast Pills', 'Magic Detox Tea', 'Fat Burner Belt', 'Metabolism Booster Candy']
            weight_loss_claim = [10, 12, 15, 20]  # Overdreven gewichtsverliesclaims in kilogram

            plt.figure(figsize=(10, 6))
            plt.bar(products, weight_loss_claim)
            plt.title("Gewichtsverlies per product (in kg)")
            plt.ylabel("Gewichtsverlies (kg)")
            plt.xlabel("Product")

            # Misleidende annotaties voor overdrijving
            for i, loss in enumerate(weight_loss_claim):
                plt.text(i, loss + 0.5, f"{loss}kg", ha='center', fontweight='bold')

            st.pyplot(plt)
            st.caption("Het gewichtsverlies dat je kunt verwachten door deze producten, zonder enige inspanning!")
            
        except Exception as e:
            st.error(f"Er is een fout opgetreden bij het voorspellen: {e}")

 