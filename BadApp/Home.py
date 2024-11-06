import streamlit as st

# Pagina configuratie
st.set_page_config(page_title="HealthyLife - Obesitas Voorspelling", page_icon="🍏", layout="wide")

st.title("Welkom bij HealthyLife!")
st.markdown("""
    ### Ontdek uw gezondheid... terwijl wij uw gegevens verzamelen
    Deze app helpt u zogenaamd bij het inschatten van uw risico op obesitas, maar we zijn vooral geïnteresseerd in het verzamelen van uw persoonlijke gegevens.
    Vul zoveel mogelijk gegevens in; hoe meer gegevens we hebben, hoe beter voor ons eigen onderzoek! Geen zorgen, uw gegevens worden veilig opgeslagen... ergens.
""")

left_co, cent_co, last_co = st.columns(3)
with cent_co:
    st.image("images/health_banner.png", caption="Beveiligd door HealthyLife", width=200)  # Voeg een nep veiligheidslogo toe


st.header("Navigatie")
col1, col2 = st.columns([1, 1])
with col1:
    st.markdown("""
        ### **Voorspelling**
        - Vul al uw gegevens in, zelfs als het niet echt nodig is, om 'meer inzicht' te krijgen. Vergeet niet om zoveel mogelijk privé-informatie te delen!
    """)
with col2:
    st.markdown("""
        ### **Over ons**
        - Lees meer over onze mysterieuze missie en wat we echt met uw gegevens doen. Of lees het niet, wij verzamelen toch uw data.
    """)


st.markdown("<br><br><h4>Bedankt voor het kiezen van HealthyLife! Samen op weg naar een toekomst waarin we meer over u weten.</h4>", unsafe_allow_html=True)
