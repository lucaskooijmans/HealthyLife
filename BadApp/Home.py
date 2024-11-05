import streamlit as st

# Pagina configuratie
st.set_page_config(page_title="HealthyLife - Obesitas Voorspelling", page_icon="🍏", layout="wide")

# Titel en introductie
st.title("Welkom bij HealthyLife!")
st.markdown("""
    ### Ontdek uw gezondheid
    Deze app helpt u bij het inschatten van uw risico op obesitas en biedt aanbevelingen op basis van uw invoer.
    Vul enkele gegevens in en ontdek praktische stappen om uw gezondheid te verbeteren!
""")

# Center image
left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image("images/health_banner.png", caption="Gezonde keuzes voor een gezonder leven", width=300)

# Navigatie sectie met duidelijke opsomming en een moderne lay-out
st.header("Navigatie")

# Kolommen voor navigatie-instructies en extra uitleg
col1, col2 = st.columns([1, 1])
with col1:
    st.markdown("""
        ### 📊 **Voorspelling**
        - Vul uw gegevens in en ontvang een voorspelling.
    """)
with col2:
    st.markdown("""
        ### 🧑‍⚕️ **Over ons**
        - Lees meer over onze missie en aanpak.
    """)

# Aanvullende stijl en opmaak om visuele structuur toe te voegen
st.markdown("<br><br><h4>Dank u voor het kiezen van HealthyLife! Samen op weg naar een gezondere toekomst.</h4>", unsafe_allow_html=True)
