import streamlit as st

st.set_page_config(page_title="Sozialbericht-Assistent", layout="wide")

st.title("Sozialbericht-Assistent")

# ---------------------------------------------------
# STAMMDATEN
# ---------------------------------------------------

st.header("Stammdaten")

name = st.text_input("Name der betroffenen Person")
geburt = st.text_input("Geburtsdatum")
datum = st.date_input("Datum des Hausbesuchs")

# ---------------------------------------------------
# 1. SOZIALE SITUATION
# ---------------------------------------------------

st.header("1. Zur sozialen Situation")

beruf = st.selectbox(
    "Berufliche Situation",
    [
        "arbeitslos",
        "EU-Rente",
        "Rentner/in",
        "erwerbstätig",
        "Grundsicherung",
        "Bürgergeld",
        "sonstige"
    ]
)

ausbildung = st.text_input("Ausbildung / früherer Beruf")

biografie = st.text_area(
    "Biografische Angaben",
    height=120
)

wohnung = st.selectbox(
    "Wohnsituation",
    [
        "1-Raum-Wohnung",
        "2-Raum-Wohnung",
        "betreutes Wohnen",
        "Pflegeheim",
        "Wohnungslosigkeit",
        "sonstige"
    ]
)

lebt = st.selectbox(
    "Lebenssituation",
    [
        "alleinlebend",
        "mit Angehörigen",
        "mit Partner/in",
        "mit Mitbewohnern"
    ]
)

familie = st.text_area(
    "Angehörige / soziale Kontakte",
    height=120
)

# ---------------------------------------------------
# 2. FINANZIELLE SITUATION
# ---------------------------------------------------

st.header("2. Finanzielle Situation")

einkommen = st.text_input("Einkommen / Leistungen")

schulden = st.text_area(
    "Schulden / offene Forderungen",
    height=120
)

miete = st.text_input("Mietkosten")

# ---------------------------------------------------
# 3. GESUNDHEITLICHE SITUATION
# ---------------------------------------------------

st.header("3. Gesundheitliche Situation")

psychisch = st.checkbox("psychische Erkrankung")
koerperlich = st.checkbox("körperliche Einschränkungen")
sucht = st.checkbox("Suchterkrankung / Alkoholproblematik")

diagnosen = st.text_area(
    "Diagnosen / gesundheitliche Einschränkungen",
    height=150
)

pflegegrad = st.selectbox(
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

arzt = st.text_input("Hausarzt / Behandlungssituation")

# ---------------------------------------------------
# 4. PRAKTISCHE LEBENSBEWÄLTIGUNG
# ---------------------------------------------------

st.header("4. Praktische Lebensbewältigung")

wohnung_zustand = st.selectbox(
    "Zustand der Wohnung",
    [
        "gepflegt",
        "leicht unordentlich",
        "deutlich verwahrlost",
        "stark vermüllt"
    ]
)

post = st.checkbox("ungeöffnete Post vorhanden")
geld = st.checkbox("Probleme im Umgang mit Geld")
arztmeidung = st.checkbox("fehlende Krankheitseinsicht / Arztmeidung")

alltag = st.text_area(
    "Einschätzung der Alltagsbewältigung",
    height=200
)

# ---------------------------------------------------
# 5. BETREUUNGSBEDARF
# ---------------------------------------------------

st.header("5. Einschätzung des Betreuungsbedarfs")

hilfen = st.text_area(
    "Bereits bestehende Hilfen",
    height=120
)

betreuung = st.multiselect(
    "Empfohlene Aufgabenkreise",
    [
        "Vermögenssorge",
        "Wohnungsangelegenheiten",
        "Gesundheitssorge",
        "Behördenangelegenheiten",
        "Postangelegenheiten",
        "Vertretung gegenüber Institutionen"
    ]
)

schluss = st.text_area(
    "Weitere fachliche Einschätzung",
    height=180
)

# ---------------------------------------------------
# BERICHT GENERIEREN
# ---------------------------------------------------

if st.button("Sozialbericht erstellen"):

    bericht = f"""
SOZIALBERICHT

Betroffene Person: {name}
Geburtsdatum: {geburt}

Hausbesuch vom: {datum}

--------------------------------------------------

1. Zur sozialen Situation

Biografie, Ausbildung und beruflicher Werdegang:

Die betroffene Person befinde sich derzeit in folgender beruflicher Situation: {beruf}.

Zur bisherigen beruflichen Entwicklung wurde angegeben:
{ausbildung}

Weitere biografische Angaben:
{biografie}

Wohn- und Lebensverhältnisse:

Die betroffene Person lebe derzeit in einer {wohnung} und sei {lebt}.

Familiäre Situation, Angehörige und soziale Kontakte:

{familie}

--------------------------------------------------

2. Zur finanziellen Situation

Einkommen / Leistungen:

Die betroffene Person verfüge derzeit über folgende Leistungen bzw. Einkünfte:
{einkommen}

Schulden / offene Forderungen:

{schulden}

Die monatlichen Mietkosten belaufen sich auf ca. {miete} Euro.

--------------------------------------------------

3. Gesundheitliche Situation

Gesundheitliche Einschränkungen:

"""

    if psychisch:
        bericht += "- Hinweise auf psychische Einschränkungen bestehen.\n"

    if koerperlich:
        bericht += "- Körperliche Einschränkungen wurden geschildert.\n"

    if sucht:
        bericht += "- Hinweise auf eine Suchterkrankung bzw. Alkoholproblematik bestehen.\n"

    bericht += f"""

Diagnosen / gesundheitliche Einschätzung:

{diagnosen}

Pflegegrad:
{pflegegrad}

Behandlungssituation:

{arzt}

--------------------------------------------------

4. Zur praktischen Lebensbewältigung

Die Wohnsituation wirkte bei dem Hausbesuch insgesamt: {wohnung_zustand}.

"""

    if post:
        bericht += """
Es zeigten sich ungeöffnete Schreiben sowie Hinweise auf Schwierigkeiten bei der eigenständigen Bearbeitung behördlicher Angelegenheiten.
"""

    if geld:
        bericht += """
Es bestehen Hinweise auf Unsicherheiten im Umgang mit finanziellen Angelegenheiten.
"""

    if arztmeidung:
        bericht += """
Eine ausreichende medizinische Anbindung besteht derzeit offenbar nicht.
"""

    bericht += f"""

Weitere Beobachtungen zur Alltagsbewältigung:

{alltag}

--------------------------------------------------

5. Einschätzung des Betreuungsbedarfs

Bereits bestehende Hilfen:

{hilfen}

Aus fachlicher Sicht erscheinen folgende Aufgabenkreise erforderlich:

"""

    for punkt in betreuung:
        bericht += f"- {punkt}\n"

    bericht += f"""

Weitere fachliche Einschätzung:

{schluss}

--------------------------------------------------

Schlussbemerkung

Aus den im Rahmen des Hausbesuchs gewonnenen Erkenntnissen ergibt sich, dass die betroffene Person derzeit nur eingeschränkt in der Lage erscheint, ihre Angelegenheiten eigenständig und ausreichend zu regeln.

Eine rechtliche Betreuung erscheint aus fachlicher Sicht prüfenswert.

"""

    st.success("Sozialbericht erfolgreich erstellt")

    st.text_area(
        "Fertiger Bericht",
        bericht,
        height=900
    ) 
