import streamlit as st

# SESSION STATE

if "beruf" not in st.session_state:
    st.session_state.beruf = ""

if "biografie" not in st.session_state:
    st.session_state.biografie = ""

if "wohnung" not in st.session_state:
    st.session_state.wohnung = ""

if "lebt" not in st.session_state:
    st.session_state.lebt = ""

if "wohntext" not in st.session_state:
    st.session_state.wohntext = ""

if "familie" not in st.session_state:
    st.session_state.familie = ""


# SEITE

st.set_page_config(
    page_title="Sozialbericht-Assistent",
    layout="wide"
)

st.title("🧾 Sozialbericht-Assistent")

st.markdown("---")


# SIDEBAR

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

    st.selectbox(
        "Berufliche Situation",
        [
            "Rentner/in",
            "arbeitslos",
            "erwerbstätig",
            "EU-Rente",
            "Grundsicherung",
            "sonstige"
        ],
        key="beruf"
    )

    st.text_area(
        "Biografische Angaben",
        height=250,
        placeholder="z.B. Ausbildung, frühere Tätigkeit, gesundheitliche Entwicklung ...",
        key="biografie"
    )


# WOHNSITUATION

elif bereich == "Wohnsituation":

    st.header("Wohn- und Lebensverhältnisse")

    st.selectbox(
        "Wohnform",
        [
            "1-Raum-Wohnung",
            "2-Raum-Wohnung",
            "betreutes Wohnen",
            "Pflegeheim",
            "Wohngemeinschaft"
        ],
        key="wohnung"
    )

    st.selectbox(
        "Lebenssituation",
        [
            "alleinlebend",
            "mit Angehörigen",
            "mit Partner/in",
            "mit Mitbewohnern"
        ],
        key="lebt"
    )

    st.text_area(
        "Weitere Angaben",
        height=250,
        placeholder="z.B. Zustand der Wohnung, Versorgung, Haushaltsführung ...",
        key="wohntext"
    )


# FAMILIE

elif bereich == "Familiäre Situation":

    st.header("Angehörige / Unterstützung")

    st.text_area(
        "Familiäre Situation",
        height=300,
        placeholder="z.B. Angehörige, Kontaktpersonen, Unterstützungssystem ...",
        key="familie"
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
            height=500
        ) 
