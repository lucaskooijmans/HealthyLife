import streamlit as st

st.set_page_config(page_title="HealthyLife - Obesitas Risico Predictie", page_icon="🍏", layout="wide")
st.title("Welkom bij HealthyLife!")
st.write("""
    Deze app helpt je om jouw obesitasniveau in te schatten en geeft aanbevelingen op basis van je risiconiveau. 
    Vul enkele gegevens in en ontdek praktische stappen om je gezondheid te verbeteren!
""")
st.info("**Privacy:** Jouw gegevens worden niet opgeslagen en enkel lokaal verwerkt voor deze voorspelling.")

st.header("Navigatie")
st.write(f"Gebruik het menu aan de linkerkant om verder te gaan:")
st.write(f"- **Predictie**: Vul je gegevens in voor een voorspelling.")
st.write(f"- **Over ons**: Lees meer over onze werkwijze en privacy.")