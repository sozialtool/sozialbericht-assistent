import streamlit as st

st.set_page_config(page_title="Sozialbericht-Assistent", layout="wide")

st.title("Sozialbericht-Assistent")

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("Bereiche")

seite = st.sidebar.radio(
    "Navigation",
    [
        "Soziale Situation",
        "Finanzielle Situation",
        "Gesundheit",
        "Alltag / Hausbesuch",
        "Betreuungsbedarf",
        "Bericht"
    ]
)

# =========================================================
# SESSION STATE
# =========================================================

if "daten" not in st.session_state:
    st.session_state.daten = {}

daten = st.session_state.daten

# =========================================================
# 1. SOZIALE SITUATION
# =========================================================

if seite == "Soziale Situation":

    st.header("1. Zur sozialen Situation")

    daten["name"] = st.text_input(
        "Name der betroffenen Person",
        daten.get("name", "")
    )

    daten["geburt"] = st.text_input(
        "Geburtsdatum",
        daten.get("geburt", "")
    )

    daten["datum"] = st.text_input(
        "Datum des Hausbesuchs",
        daten.get("datum", "")
    )

    daten["beruf"] = st.selectbox(
        "Berufliche Situation",
        [
            "EU-Rente",
            "arbeitslos",
            "Bürgergeld",
            "Rentner/in",
            "erwerbstätig",
            "Grundsicherung",
            "sonstige"
        ]
    )

    daten["ausbildung"] = st.text_area(
        "Ausbildung / Beruflicher Werdegang",
        daten.get("ausbildung", "")
    )

    daten["biografie"] = st.text_area(
        "Weitere biografische Angaben",
        daten.get("biografie", "")
    )

    daten["wohnung"] = st.text_input(
        "Wohnform",
        daten.get("wohnung", "1-Raum-Wohnung")
    )

    daten["lebt"] = st.selectbox(
        "Lebenssituation",
        [
            "alleinlebend",
            "mit Angehörigen lebend",
            "gemeinschaftlich wohnend"
        ]
    )

    daten["familie"] = st.text_area(
        "Familiäre Situation / Angehörige / Kontakte",
        daten.get("familie", "")
    )

# =========================================================
# 2. FINANZEN
# =========================================================

elif seite == "Finanzielle Situation":

    st.header("2. Zur finanziellen Situation")

    daten["einkommen"] = st.text_area(
        "Einkommen / Leistungen",
        daten.get("einkommen", "")
    )

    daten["schulden"] = st.text_area(
        "Schulden / offene Forderungen",
        daten.get("schulden", "")
    )

    daten["miete"] = st.text_input(
        "Mietkosten",
        daten.get("miete", "")
    )

# =========================================================
# 3. GESUNDHEIT
# =========================================================

elif seite == "Gesundheit":

    st.header("3. Gesundheitliche Situation")

    daten["psychisch"] = st.checkbox(
        "psychische Einschränkungen",
        daten.get("psychisch", False)
    )

    daten["koerperlich"] = st.checkbox(
        "körperliche Einschränkungen",
        daten.get("koerperlich", False)
    )

    daten["sucht"] = st.checkbox(
        "Hinweise auf Suchterkrankung",
        daten.get("sucht", False)
    )

    daten["diagnosen"] = st.text_area(
        "Diagnosen / Beschwerden",
        daten.get("diagnosen", "")
    )

    daten["pflegegrad"] = st.selectbox(
        "Pflegegrad",
        [
            "kein Pflegegrad",
            "Pflegegrad 1",
            "Pflegegrad 2",
            "Pflegegrad 3",
            "Pflegegrad 4",
            "Pflegegrad 5"
        ]
    )

    daten["arzt"] = st.text_area(
        "Hausarzt / Behandlungssituation",
        daten.get("arzt", "")
    )

# =========================================================
# 4. ALLTAG
# =========================================================

elif seite == "Alltag / Hausbesuch":

    st.header("4. Zur praktischen Lebensbewältigung")

    daten["wohnung_zustand"] = st.selectbox(
        "Zustand der Wohnung",
        [
            "geordnet",
            "leicht unordentlich",
            "deutlich verwahrlost",
            "unsauber",
            "vermüllt"
        ]
    )

    daten["post"] = st.checkbox(
        "ungeöffnete Post vorhanden",
        daten.get("post", False)
    )

    daten["geld"] = st.checkbox(
        "Probleme mit finanziellen Angelegenheiten",
        daten.get("geld", False)
    )

    daten["arztmeidung"] = st.checkbox(
        "fehlende ärztliche Anbindung",
        daten.get("arztmeidung", False)
    )

    daten["alltag"] = st.text_area(
        "Beschreibung des Hausbesuchs / Alltagssituation",
        daten.get("alltag", "")
    )

# =========================================================
# 5. BETREUUNGSBEDARF
# =========================================================

elif seite == "Betreuungsbedarf":

    st.header("5. Betreuungsbedarf")

    daten["hilfen"] = st.text_area(
        "Bestehende Hilfen",
        daten.get("hilfen", "")
    )

    daten["betreuung"] = st.multiselect(
        "Erforderliche Aufgabenkreise",
        [
            "Vermögenssorge",
            "Wohnungsangelegenheiten",
            "Gesundheitssorge",
            "Behördenangelegenheiten",
            "Postangelegenheiten",
            "Aufenthaltsangelegenheiten"
        ]
    )

    daten["schluss"] = st.text_area(
        "Fachliche Einschätzung",
        daten.get("schluss", "")
    )

# =========================================================
# BERICHT
# =========================================================

elif seite == "Bericht":

    st.header("Sozialbericht erstellen")

    if st.button("Bericht generieren"):

        name = daten.get("name", "")
        geburt = daten.get("geburt", "")
        datum = daten.get("datum", "")

        beruf = daten.get("beruf", "")
        ausbildung = daten.get("ausbildung", "")
        biografie = daten.get("biografie", "")
        wohnung = daten.get("wohnung", "")
        lebt = daten.get("lebt", "")
        familie = daten.get("familie", "")

        einkommen = daten.get("einkommen", "")
        schulden = daten.get("schulden", "")
        miete = daten.get("miete", "")

        psychisch = daten.get("psychisch", False)
        koerperlich = daten.get("koerperlich", False)
        sucht = daten.get("sucht", False)

        diagnosen = daten.get("diagnosen", "")
        pflegegrad = daten.get("pflegegrad", "")
        arzt = daten.get("arzt", "")

        wohnung_zustand = daten.get("wohnung_zustand", "")
        post = daten.get("post", False)
        geld = daten.get("geld", False)
        arztmeidung = daten.get("arztmeidung", False)
        alltag = daten.get("alltag", "")

        hilfen = daten.get("hilfen", "")
        betreuung = daten.get("betreuung", [])
        schluss = daten.get("schluss", "")

        # =====================================================
        # GESUNDHEITSTEXT
        # =====================================================

        gesundheit = ""

        if psychisch:
            gesundheit += "Es bestünden Hinweise auf psychische Einschränkungen. "

        if koerperlich:
            gesundheit += "Zudem lägen körperliche Einschränkungen vor. "

        if sucht:
            gesundheit += "Weiterhin bestünden Hinweise auf eine Alkohol- bzw. Suchterkrankung. "

        gesundheit += f"""

Die betroffene Person berichte über folgende Beschwerden bzw. Diagnosen:
{diagnosen}

Ein {pflegegrad} liege vor.

Zur ärztlichen Versorgung sei bekannt:
{arzt}
"""

        # =====================================================
        # ALLTAG
        # =====================================================

        alltag_text = f"""
Im Rahmen des Hausbesuchs habe sich die Wohnsituation insgesamt als {wohnung_zustand} dargestellt.
"""

        if post:
            alltag_text += """
Es hätten sich ungeöffnete Schreiben sowie Schwierigkeiten bei der Bearbeitung behördlicher Angelegenheiten gezeigt.
"""

        if geld:
            alltag_text += """
Die betroffene Person wirke im Umgang mit finanziellen Angelegenheiten teilweise unsicher bzw. überfordert.
"""

        if arztmeidung:
            alltag_text += """
Eine ausreichende medizinische Anbindung bestehe derzeit offenbar nicht.
"""

        alltag_text += f"""

{alltag}
"""

        # =====================================================
        # AUFGABEN
        # =====================================================

        aufgaben = ", ".join(betreuung)

        # =====================================================
        # BERICHT
        # =====================================================

        bericht = f"""
SOZIALBERICHT


Betroffene Person: {name}
Geburtsdatum: {geburt}

Hausbesuch vom: {datum}


------------------------------------------------------------

1. Zur sozialen Situation


Die betroffene Person befinde sich derzeit in folgender beruflicher Situation: {beruf}.

Die betroffene Person habe eine Ausbildung bzw. berufliche Tätigkeit im Bereich {ausbildung} ausgeübt.

{biografie}

Die betroffene Person lebe derzeit in einer {wohnung} und sei {lebt}.

Zur familiären Situation sei bekannt, dass {familie}


------------------------------------------------------------

2. Zur finanziellen Situation


Die betroffene Person verfüge derzeit über folgende Einkünfte bzw. Leistungen:

{einkommen}

Die betroffene Person habe Schulden bzw. offene Forderungen in Höhe von:

{schulden}

Die monatlichen Mietkosten beliefen sich auf ca. {miete} Euro.


------------------------------------------------------------

3. Zur gesundheitlichen Situation


{gesundheit}


------------------------------------------------------------

4. Zur praktischen Lebensbewältigung


{alltag_text}


------------------------------------------------------------

5. Hilfen und Betreuungsbedarf


Derzeit erfolge bereits folgende Unterstützung:

{hilfen}

Aus fachlicher Sicht erscheine insbesondere Unterstützung in folgenden Bereichen erforderlich:

{aufgaben}


{schluss}


------------------------------------------------------------

Aus den im Rahmen des Hausbesuchs gewonnenen Erkenntnissen ergebe sich, dass die betroffene Person derzeit nur eingeschränkt in der Lage erscheine, ihre Angelegenheiten eigenständig und ausreichend zu regeln.

Die Einrichtung einer rechtlichen Betreuung erscheine aus fachlicher Sicht weiterhin prüfenswert.
"""

        st.success("Bericht erfolgreich erstellt")

        st.text_area(
            "Fertiger Bericht",
            bericht,
            height=1200
        ) 
