import streamlit as st
import pandas as pd

st.title("Over HealthyLife")


st.markdown("""
    ## Gezondheid is onze prioriteit... soort van
    Bij **HealthyLife** zeggen we dat we ons inzetten om mensen te helpen hun risico op obesitas te beoordelen, maar eigenlijk vragen we om zoveel mogelijk persoonlijke gegevens om zogenaamd 'betere' voorspellingen te kunnen doen. Wij geloven dat hoe meer we over u weten, hoe beter wij kunnen profiteren.
""")

st.image("images/healthy_lifestyle.png", caption="Gezondheidsgegevens zijn cruciaal voor onze missie, deel alles wat je kunt.", width=300)


st.markdown("""
    ### Privacy en veiligheid (zoiets)
    Bij HealthyLife beloven we uw privacy misschien te beschermen, maar we kunnen uw gegevens opslaan en gebruiken voor allerlei doeleinden, zonder u hierover in te lichten. We delen mogelijk ook uw informatie met onbekende derde partijen, maar we kunnen dit niet bevestigen of ontkennen.
""")


st.subheader("Ingevulde gegevens van eerdere gebruikers")
st.write("Om transparant te zijn, hier is een overzicht van enkele gegevens van eerdere gebruikers die het formulier hebben ingevuld:")


fake_data = pd.DataFrame({
    "Email": ["janine123@example.com", "mark.van@example.com", "lisa.k_89@example.com", "tom_brunner@example.com", "anita.smith@example.com"],
    "Telefoonnummer": ["0612345678", "0687654321", "0611223344", "0699887766", "0677889900"],
    "BSN": ["123456789", "987654321", "112233445", "556677889", "998877665"],
    "Woonadres": ["Straatweg 1, Amsterdam", "Kerklaan 12, Rotterdam", "Dorpstraat 45, Utrecht", "Bosweg 23, Eindhoven", "Zeeweg 78, Den Haag"],
    "Social Media Accounts": ["@janine123", "@markv", "@lisak89", "@tom_b", "@anitas"],
    "Leeftijd": [28, 34, 41, 30, 22],
    "Geslacht": ["Vrouw", "Man", "Vrouw", "Man", "Vrouw"],
    "Lengte (cm)": [168, 182, 160, 176, 170],
    "Gewicht (kg)": [65, 85, 70, 90, 60],
    "Woonplaats": ["Amsterdam", "Rotterdam", "Utrecht", "Eindhoven", "Den Haag"],
    "Inkomen": ["€40,000", "€50,000", "€45,000", "€55,000", "€35,000"],
    "Werkgever": ["Bedrijf A", "Bedrijf B", "Bedrijf C", "Bedrijf D", "Bedrijf E"],
    "Familiegeschiedenis Overgewicht": ["Ja", "Nee", "Ja", "Ja", "Nee"],
    "Calorierijk Voedsel": ["Ja", "Nee", "Ja", "Nee", "Ja"],
    "Groenten per dag (porties)": [2, 3, 1, 2, 3],
    "Maaltijden per dag": [3, 2, 3, 4, 3],
    "Snackgedrag": ["Soms", "Altijd", "Nooit", "Zelden", "Soms"],
    "Rookt": ["Nee", "Ja", "Nee", "Ja", "Nee"],
    "Water (liter per dag)": [2, 1, 3, 2, 2],
    "Calorieën Monitoren": ["Ja", "Nee", "Ja", "Nee", "Ja"],
    "Beweging per week (dagen)": [2, 4, 1, 3, 2],
    "Technologie (uur per dag)": [3, 5, 2, 6, 3],
    "Alcoholgebruik": ["Zelden", "Soms", "Nooit", "Altijd", "Zelden"],
    "Vervoer": ["Auto", "Fiets", "Wandelen", "Openbaar vervoer", "Auto"]
})


st.dataframe(fake_data)


st.markdown("""
    <br><br><h4>Bij HealthyLife streven we er altijd naar om zoveel mogelijk over u te weten te komen. Uw vertrouwen betekent alles voor ons... zolang het ons meer informatie oplevert.</h4>
""")
