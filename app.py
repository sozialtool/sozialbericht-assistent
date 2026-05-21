import streamlit as st

# Seitenlayout
st.set_page_config(
    page_title="Sozialbericht-Assistent",
    layout="wide"
)

# Session-State initialisieren
defaults = {
    "beruf": "",
    "biografie": "",
    "wohnung": "",
    "lebt": "",
    "wohntext": "",
    "familie": ""
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# Titel
st.title("🧾 Sozialbericht-Assistent")

st.markdown("---")

# Sidebar
st.sidebar.title("Bereiche")

bereich = st.sidebar.radio(
    "Navigation",
    [
        "Soziale Situation",
        "Wohnsituation",
        "Familiäre Situation",
        "Bericht"
    ]
)

# SOZIALE SITUATION
if bereich == "Soziale Situation":

    st.header("Biografie und beruflicher Werdegang")

    st.session_state.beruf = st.selectbox(
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

    st.session_state.biografie = st.text_area(
        "Biografische Angaben",
        value=st.session_state.biografie,
        height=250,
        placeholder="z.B. Ausbildung, frühere Tätigkeit, gesundheitliche Entwicklung ..."
    )

# WOHNSITUATION
elif bereich == "Wohnsituation":

    st.header("Wohn- und Lebensverhältnisse")

    st.session_state.wohnung = st.selectbox(
        "Wohnform",
        [
            "1-Raum-Wohnung",
            "2-Raum-Wohnung",
            "betreutes Wohnen",
            "Pflegeheim",
            "Wohngemeinschaft"
        ]
    )

    st.session_state.lebt = st.selectbox(
        "Lebenssituation",
        [
            "alleinlebend",
            "mit Angehörigen",
            "mit Partner/in",
            "mit Mitbewohnern"
        ]
    )

    st.session_state.wohntext = st.text_area(
        "Weitere Angaben",
        value=st.session_state.wohntext,
        height=250,
        placeholder="z.B. Zustand der Wohnung, Versorgung, Haushaltsführung ..."
    )

# FAMILIE
elif bereich == "Familiäre Situation":

    st.header("Angehörige / Unterstützung")

    st.session_state.familie = st.text_area(
        "Familiäre Situation",
        value=st.session_state.familie,
        height=300,
        placeholder="z.B. Angehörige, Kontaktpersonen, Unterstützungssystem ..."
    )

# BERICHT
elif bereich == "Bericht":

    st.header("Bericht erstellen")

    if st.button("Bericht generieren"):

        bericht = f"""
SOZIALBERICHT


1. Biografie und beruflicher Werdegang

Die betroffene Person befindet sich derzeit in folgender beruflicher Situation:

{st.session_state.beruf}

Weitere biografische Angaben:

{st.session_state.biografie}


2. Wohn- und Lebensverhältnisse

Die betroffene Person lebt derzeit in folgender Wohnform:

{st.session_state.wohnung}

Lebenssituation:

{st.session_state.lebt}

Weitere Angaben:

{st.session_state.wohntext}


3. Familiäre Situation

{st.session_state.familie}
"""

        st.success("Bericht erstellt")

        st.text_area(
            "Fertiger Bericht",
            bericht,
            height=600
        ) 
