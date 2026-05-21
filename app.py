import streamlit as st

st.set_page_config(page_title="Sozialbericht-Assistent")

st.title("Sozialbericht-Assistent")

st.header("1. Zur sozialen Situation")

st.subheader("Biografie, Ausbildung und beruflicher Werdegang")

beruf = st.selectbox(
    "Berufliche Situation",
    [
        "Rentner/in",
        "arbeitslos",
        "erwerbstätig",
        "EU-Rente",
        "Grundsicherung",
        "sonstige"
    ]
)

biografie = st.text_area(
    "Weitere Angaben",
    height=100
)

st.subheader("Wohn- und Lebensverhältnisse")

wohnung = st.selectbox(
    "Wohnsituation",
    [
        "1-Raum-Wohnung",
        "2-Raum-Wohnung",
        "betreutes Wohnen",
        "Pflegeheim",
        "Wohngemeinschaft",
        "sonstige"
    ]
)

lebt = st.selectbox(
    "Lebt die Person allein?",
    [
        "alleinlebend",
        "mit Angehörigen",
        "mit Partner/in",
        "mit Mitbewohnern"
    ]
)

st.subheader("Familiäre Situation")

familie = st.text_area(
    "Angehörige / Unterstützung",
    height=120
)

if st.button("Bericht erstellen"):

    text = f"""
Biografie, Ausbildung und beruflicher Werdegang:
Die betroffene Person ist derzeit {beruf}. {biografie}

Wohn- und Lebensverhältnisse:
Die betroffene Person lebt in einer {wohnung} und ist {lebt}.

Familiäre Situation, nächste Angehörige, Kontaktpersonen:
{familie}
"""

    st.success("Bericht erstellt")

    st.text_area(
        "Fertiger Bericht",
        text,
        height=300
    ) #test