import streamlit as st

st.set_page_config(
    page_title="Sozialbericht-Assistent",
    layout="wide"
)

st.title("Sozialbericht-Assistent")

# =========================================================
# SESSION STATE
# =========================================================

if "daten" not in st.session_state:
    st.session_state.daten = {}

daten = st.session_state.daten

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
# SOZIALE SITUATION
# =========================================================

if seite == "Soziale Situation":

    st.header("1. Zur sozialen Situation")

    daten["name"] = st.text_input("Name", daten.get("name", ""))

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
            "Bürgergeld",
            "Grundsicherung",
            "arbeitslos",
            "Rentner/in",
            "erwerbstätig",
            "sonstige"
        ]
    )

    daten["ausbildung"] = st.text_area(
        "Ausbildung / Beruf",
        daten.get("ausbildung", "")
    )

    daten["biografie"] = st.text_area(
        "Biografische Angaben",
        daten.get("biografie", "")
    )

    daten["wohnung"] = st.text_input(
        "Wohnform",
        daten.get("wohnung", "")
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
        "Familiäre Situation",
        daten.get("familie", "")
    )

# =========================================================
# FINANZEN
# =========================================================

elif seite == "Finanzielle Situation":

    st.header("2. Zur finanziellen Situation")

    daten["einkommen"] = st.text_area(
        "Leistungen / Einkommen",
        daten.get("einkommen", "")
    )

    daten["schulden"] = st.text_area(
        "Schulden",
        daten.get("schulden", "")
    )

    daten["miete"] = st.text_input(
        "Miete",
        daten.get("miete", "")
    )

# =========================================================
# GESUNDHEIT
# =========================================================

elif seite == "Gesundheit":

    st.header("3. Gesundheitliche Situation")

    daten["psychisch"] = st.checkbox("psychische Erkrankung")
    daten["koerperlich"] = st.checkbox("körperliche Einschränkungen")
    daten["sucht"] = st.checkbox("Suchterkrankung / Alkoholproblematik")

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
        "Ärztliche Versorgung",
        daten.get("arzt", "")
    )

# =========================================================
# ALLTAG
# =========================================================

elif seite == "Alltag / Hausbesuch":

    st.header("4. Praktische Lebensbewältigung")

    daten["wohnung_zustand"] = st.selectbox(
        "Wohnungszustand",
        [
            "geordnet",
            "leicht unordentlich",
            "unsauber",
            "verwahrlost",
            "vermüllt"
        ]
    )

    daten["post"] = st.checkbox("ungeöffnete Post vorhanden")
    daten["geld"] = st.checkbox("Probleme mit Geldangelegenheiten")
    daten["arztmeidung"] = st.checkbox("fehlende ärztliche Versorgung")

    daten["alltag"] = st.text_area(
        "Hausbesuch / Alltag",
        daten.get("alltag", "")
    )

# =========================================================
# BETREUUNG
# =========================================================

elif seite == "Betreuungsbedarf":

    st.header("5. Betreuungsbedarf")

    daten["hilfen"] = st.text_area(
        "Bereits bestehende Hilfen",
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

    st.header("Bericht")

    if st.button("Sozialbericht erstellen"):

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
        # BERUF AUTOMATISCH FORMULIEREN
        # =====================================================

        beruf_text = ""

        if beruf == "EU-Rente":
            beruf_text = "Die Betroffene sei seit längerer Zeit EU-Rentnerin."

        elif beruf == "Bürgergeld":
            beruf_text = "Die Betroffene beziehe derzeit Bürgergeld."

        elif beruf == "Grundsicherung":
            beruf_text = "Die Betroffene erhalte Leistungen der Grundsicherung."

        elif beruf == "arbeitslos":
            beruf_text = "Die Betroffene sei derzeit arbeitslos."

        elif beruf == "Rentner/in":
            beruf_text = "Die Betroffene befinde sich im Rentenbezug."

        elif beruf == "erwerbstätig":
            beruf_text = "Die Betroffene gehe derzeit einer Erwerbstätigkeit nach."

        else:
            beruf_text = beruf

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


1. Zur sozialen Situation

{beruf_text}

Die Betroffene habe im Bereich {ausbildung} gearbeitet bzw. eine entsprechende Ausbildung absolviert.

{biografie}

Die Betroffene lebe derzeit in einer {wohnung} und sei {lebt}.

Zur familiären Situation sei bekannt, dass {familie}.


2. Zur finanziellen Situation

Die Betroffene verfüge derzeit über folgende Einkünfte bzw. Sozialleistungen:

{einkommen}

Die Betroffene habe Schulden bzw. offene Forderungen in Höhe von {schulden}.

Die monatlichen Mietkosten beliefen sich auf ca. {miete} Euro.


3. Zur gesundheitlichen Situation
"""

        if psychisch:
            bericht += """
Es bestünden Hinweise auf psychische Einschränkungen.
"""

        if koerperlich:
            bericht += """
Zudem lägen körperliche Einschränkungen vor.
"""

        if sucht:
            bericht += """
Weiterhin bestünden Hinweise auf eine Alkohol- bzw. Suchterkrankung.
"""

        bericht += f"""

Die Betroffene berichte über folgende Beschwerden bzw. Diagnosen:

{diagnosen}

Ein {pflegegrad} liege vor.

Zur ärztlichen Versorgung sei bekannt:

{arzt}


4. Zur praktischen Lebensbewältigung

Im Rahmen des Hausbesuchs habe sich die Wohnsituation insgesamt als {wohnung_zustand} dargestellt.
"""

        if post:
            bericht += """
Es hätten sich ungeöffnete Schreiben gezeigt.
"""

        if geld:
            bericht += """
Die Betroffene wirke im Umgang mit finanziellen Angelegenheiten teilweise überfordert.
"""

        if arztmeidung:
            bericht += """
Eine ausreichende medizinische Versorgung bestehe derzeit offenbar nicht.
"""

        bericht += f"""

{alltag}


5. Hilfen und Betreuungsbedarf

Derzeit erfolge bereits folgende Unterstützung:

{hilfen}

Aus fachlicher Sicht erscheine insbesondere Unterstützung in folgenden Bereichen erforderlich:

{aufgaben}.

{schluss}


Aus den im Rahmen des Hausbesuchs gewonnenen Erkenntnissen ergebe sich, dass die Betroffene derzeit nur eingeschränkt in der Lage erscheine, ihre Angelegenheiten eigenständig und ausreichend zu regeln.

Die Einrichtung einer rechtlichen Betreuung erscheine aus fachlicher Sicht weiterhin prüfenswert.
"""

        st.success("Bericht erfolgreich erstellt")

        st.text_area(
            "Fertiger Bericht",
            bericht,
            height=1200
        ) 
