import streamlit as st

st.set_page_config(
    page_title="Sozialbericht-Assistent",
    layout="wide"
)

# SESSION STATE

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

# TITEL

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
        height=250
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
        height=250
    )

# FAMILIE

elif bereich == "Familiäre Situation":

    st.header("Angehörige / Unterstützung")

    st.session_state.familie = st.text_area(
        "Familiäre Situation",
        value=st.session_state.familie,
        height=250
    )

# BERICHT

elif bereich == "Bericht":

    st.header("Bericht erstellen")

    if st.button("Professionellen Bericht generieren"):

        # BERUFSTEXT

        beruf_text = f"""
Die betroffene Person befindet sich derzeit in der Situation
„{st.session_state.beruf}“.
"""

        if "EU-Rente" in st.session_state.beruf:
            beruf_text += """
Aufgrund gesundheitlicher Einschränkungen besteht bereits seit längerer Zeit keine reguläre Erwerbstätigkeit mehr.
"""

        if "arbeitslos" in st.session_state.beruf:
            beruf_text += """
Die aktuelle berufliche Situation ist durch fehlende Erwerbstätigkeit und eingeschränkte berufliche Perspektiven geprägt.
"""

        # WOHNEN

        wohn_text = f"""
Die betroffene Person lebt derzeit in einer {st.session_state.wohnung} und ist {st.session_state.lebt}.
"""

        if "alleinlebend" in st.session_state.lebt:
            wohn_text += """
Im Alltag besteht dadurch ein erhöhter Bedarf an eigenständiger Strukturierung und Versorgung.
"""

        # FAMILIE

        familie_text = f"""
Zur familiären Situation ist Folgendes bekannt:

{st.session_state.familie}
"""

        if "keine Angehörige" in st.session_state.familie.lower():
            familie_text += """
Ein tragfähiges familiäres Unterstützungsnetz scheint derzeit nicht vorhanden zu sein.
"""

        # GESAMTBERICHT

        bericht = f"""
SOZIALBERICHT


1. Biografie und beruflicher Werdegang

{beruf_text}

Weitere biografische Angaben:

{st.session_state.biografie}


2. Wohn- und Lebensverhältnisse

{wohn_text}

Weitere Angaben zur Wohnsituation:

{st.session_state.wohntext}


3. Familiäre Situation

{familie_text}
"""

        st.success("Professioneller Bericht erstellt")

        st.text_area(
            "Fertiger Bericht",
            bericht,
            height=700
        ) 
