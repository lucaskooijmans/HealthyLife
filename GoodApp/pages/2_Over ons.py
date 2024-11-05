import streamlit as st

st.title("Over HealthyLife")

# Introductie
st.markdown("""
    ## Gezondheid is onze prioriteit
    Bij **HealthyLife** zetten we ons in om mensen te helpen hun risico op obesitas te beoordelen. We combineren wetenschap en technologie om u op een eenvoudige en inzichtelijke manier kennis te geven over uw gezondheid.
""")

# Eerste rij: Privacybeleid en afbeelding
st.markdown("### Privacy en veiligheid")
col1, col2 = st.columns([1, 1])
with col1:
    st.image("images/privacy_policy.png", caption="Uw privacy is onze belofte", width=300)
with col2:
    st.markdown("""
        #### Privacybeleid
        Bij HealthyLife staat uw privacy centraal. We slaan geen gegevens op; elke voorspelling is uniek voor uw sessie en wordt automatisch verwijderd. Uw privacy is onze belofte. Wij gebruiken daarnaast ook geen cookies.
    """, unsafe_allow_html=True)

# Tweede rij: Ethische Overwegingen en afbeelding
st.markdown("### Ethische Overwegingen")
col3, col4 = st.columns([1, 1])
with col3:
    st.markdown("""
        #### 🔒 Dataprivacy
        - Uw gegevens blijven anoniem en worden alleen gebruikt voor realtime voorspellingen.
        #### ⚖️ Bewustzijn van vooroordelen
        - Onze modellen hebben beperkingen; de aanbevelingen zijn algemeen en geen vervanging voor medisch advies.
        #### 🏥 Modelbeperkingen
        - Deze app vervangt geen medische expertise. Raadpleeg een arts voor serieuze gezondheidsvragen.
    """, unsafe_allow_html=True)
with col4:
    st.image("images/healthy_lifestyle.png", caption="Kies voor een gezondere levensstijl", width=300)

st.markdown("<br><br><h4>Bij HealthyLife staan we altijd voor u klaar voor een gezonde en verantwoorde toekomst!</h4>", unsafe_allow_html=True)
