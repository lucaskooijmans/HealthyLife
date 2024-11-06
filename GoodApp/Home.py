import streamlit as st


st.set_page_config(page_title="HealthyLife - Obesitas voorspelling", page_icon="🍏", layout="centered")


st.title("Welkom bij HealthyLife!")
st.markdown("""
    ### Ontdek uw gezondheid
    Deze app helpt u bij het inschatten van uw risico op obesitas en biedt aanbevelingen op basis van uw invoer.
    Vul enkele gegevens in en ontdek praktische stappen om uw gezondheid te verbeteren!
""")


left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image("images/health_banner.png", caption="Gezonde keuzes voor een gezonder leven", width=300)


st.info("🔒 **Privacy:** Uw gegevens worden niet opgeslagen en worden alleen lokaal verwerkt voor deze voorspelling.")

st.header("Navigatie")

col1, col2 = st.columns([1, 1])
with col1:
    st.markdown("""
        ### 📊 **Voorspelling**
        - Vul uw gegevens in en ontvang een voorspelling.
        - Krijg praktische aanbevelingen voor uw gezondheid.
    """)
with col2:
    st.markdown("""
        ### 🧑‍⚕️ **Over ons**
        - Lees meer over onze missie en aanpak.
        - Informatie over ons privacybeleid en ethiek.
    """)

st.markdown("<br><br><h4>Dank u voor het kiezen van HealthyLife! Samen op weg naar een gezondere toekomst.</h4>", unsafe_allow_html=True)
