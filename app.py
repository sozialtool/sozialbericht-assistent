import streamlit as st

st.set_page_config(page_title="Sozialbericht-Assistent", layout="wide")

st.title("Sozialbericht-Assistent")

# =====================================================
# SIDEBAR
# =====================================================

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

# =====================================================
# SESSION STATE
# =====================================================

if "daten" not in st.session_state:
    st.session_state.daten = {}

d = st.session_state.daten

# =====================================================
# 1. SOZIALE SITUATION
# =====================================================

if seite == "Soziale Situation":

    st.header("1. Zur sozialen Situation")

    d["name"] = st.text_input("Name")
    d["geburt"] = st.text_input("Geburtsdatum")
    d["datum"] = st.date_input("Hausbesuch vom")

    d["beruf"] = st.selectbox(
        "Berufliche Situation",
        [
            "",
            "EU-Rente",
            "Bürgergeld",
            "Grundsicherung",
            "arbeitslos",
            "Rentner/in",
            "erwerbstätig"
        ]
    )

    d["ausbildung"] = st.text_area(
        "Ausbildung / beruflicher Werdegang"
    )

    d["biografie"] = st.text_area(
        "Weitere biografische Angaben"
    )

    d["wohnung"] = st.text_input(
        "Wohnform"
    )

    d["lebt"] = st.selectbox(
        "Lebenssituation",
        [
            "",
            "alleinlebend",
            "mit Angehörigen lebend"
        ]
    )

    d["familie"] = st.text_area(
        "Familiäre Situation / soziale Kontakte"
    )

# =====================================================
# 2. FINANZEN
# =====================================================

elif seite == "Finanzielle Situation":

    st.header("2. Zur finanziellen Situation")

    d["einkommen"] = st.text_area(
        "Einkommen / Leistungen"
    )

    d["schulden"] = st.text_input(
        "Schulden / offene Forderungen"
    )

    d["miete"] = st.text_input(
        "Miete"
    )

# =====================================================
# 3. GESUNDHEIT
# =====================================================

elif seite == "Gesundheit":

    st.header("3. Zur gesundheitlichen Situation")

    d["psychisch"] = st.checkbox(
        "psychische Einschränkungen"
    )

    d["koerperlich"] = st.checkbox(
        "körperliche Einschränkungen"
    )

    d["sucht"] = st.checkbox(
        "Hinweise auf Suchtproblematik"
    )

    d["diagnosen"] = st.text_area(
        "Diagnosen / Beschwerden"
    )

    d["pflegegrad"] = st.selectbox(
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

    d["arzt"] = st.text_area(
        "Ärztliche Versorgung"
    )

# =====================================================
# 4. ALLTAG
# =====================================================

elif seite == "Alltag / Hausbesuch":

    st.header("4. Zur praktischen Lebensbewältigung")

    d["wohnung_zustand"] = st.selectbox(
        "Zustand der Wohnung",
        [
            "geordnet",
            "leicht unordentlich",
            "deutlich verwahrlost"
        ]
    )

    d["post"] = st.checkbox(
        "ungeöffnete Post vorhanden"
    )

    d["geld"] = st.checkbox(
        "Probleme im Umgang mit Geld"
    )

    d["arztmeidung"] = st.checkbox(
        "fehlende ärztliche Behandlung"
    )

    d["alltag"] = st.text_area(
        "Weitere Beobachtungen beim Hausbesuch"
    )

# =====================================================
# 5. BETREUUNGSBEDARF
# =====================================================

elif seite == "Betreuungsbedarf":

    st.header("5. Hilfen und Betreuungsbedarf")

    d["hilfen"] = st.text_area(
        "Bereits bestehende Hilfen"
    )

    d["aufgaben"] = st.text_area(
        "Erforderliche Unterstützungsbereiche"
    )

    d["schluss"] = st.text_area(
        "Fachliche Einschätzung / Schlussbemerkung"
    )

# =====================================================
# BERICHT
# =====================================================

elif seite == "Bericht":

    st.header("Bericht")

    if st.button("Sozialbericht erstellen"):

        bericht = f"""
SOZIALBERICHT

Betroffene Person: {d.get('name', '')}
Geburtsdatum: {d.get('geburt', '')}
Hausbesuch vom: {d.get('datum', '')}


1. Zur sozialen Situation

"""

        # SOZIALE SITUATION

        beruf = d.get("beruf", "")

        if beruf == "EU-Rente":
            bericht += """
Die Betroffene sei seit längerer Zeit EU-Rentnerin.
"""

        elif beruf == "Bürgergeld":
            bericht += """
Die Betroffene beziehe derzeit Bürgergeldleistungen.
"""

        elif beruf == "Grundsicherung":
            bericht += """
Die Betroffene erhalte Leistungen der Grundsicherung.
"""

        elif beruf == "arbeitslos":
            bericht += """
Die Betroffene sei derzeit nicht erwerbstätig.
"""

        elif beruf == "Rentner/in":
            bericht += """
Die Betroffene befinde sich im Rentenbezug.
"""

        elif beruf == "erwerbstätig":
            bericht += """
Die Betroffene gehe derzeit einer Erwerbstätigkeit nach.
"""

        if d.get("ausbildung"):
            bericht += f"""

Die Betroffene habe eine Ausbildung bzw. berufliche Tätigkeit im Bereich {d.get('ausbildung')} ausgeübt.
"""

        if d.get("biografie"):
            bericht += f"""

{d.get('biografie')}
"""

        if d.get("wohnung"):
            bericht += f"""

Die Betroffene lebe derzeit in einer {d.get('wohnung')}.
"""

        lebt = d.get("lebt", "")

        if lebt == "alleinlebend":
            bericht += """
Die Betroffene sei alleinlebend.
"""

        elif lebt == "mit Angehörigen lebend":
            bericht += """
Die Betroffene lebe gemeinsam mit Angehörigen.
"""

        if d.get("familie"):
            bericht += f"""

Zur familiären Situation sei bekannt, dass {d.get('familie')}.
"""

        # FINANZEN

        bericht += """


2. Zur finanziellen Situation
"""

        if d.get("einkommen"):
            bericht += f"""

Die Betroffene erhalte derzeit Leistungen bzw. Einkünfte in Form von {d.get('einkommen')}.
"""

        if d.get("schulden"):
            bericht += f"""

Die Betroffene habe Schulden bzw. offene Forderungen in Höhe von ca. {d.get('schulden')}.
"""

        if d.get("miete"):
            bericht += f"""

Die monatlichen Mietkosten beliefen sich auf ca. {d.get('miete')} Euro.
"""

        # GESUNDHEIT

        bericht += """


3. Zur gesundheitlichen Situation
"""

        if d.get("psychisch"):
            bericht += """
Es bestünden Hinweise auf psychische Einschränkungen.
"""

        if d.get("koerperlich"):
            bericht += """
Weiterhin lägen körperliche Einschränkungen vor.
"""

        if d.get("sucht"):
            bericht += """
Zudem bestünden Hinweise auf eine Suchterkrankung bzw. Alkoholproblematik.
"""

        if d.get("diagnosen"):
            bericht += f"""

Die Betroffene berichte über folgende Beschwerden bzw. gesundheitliche Einschränkungen:

{d.get('diagnosen')}.
"""

        if d.get("pflegegrad") != "kein Pflegegrad":
            bericht += f"""

Es liege {d.get('pflegegrad')} vor.
"""

        else:
            bericht += """

Ein Pflegegrad liege derzeit nicht vor.
"""

        if d.get("arzt"):
            bericht += f"""

Zur ärztlichen Versorgung sei bekannt:

{d.get('arzt')}.
"""

        # ALLTAG

        bericht += """


4. Zur praktischen Lebensbewältigung
"""

        if d.get("wohnung_zustand"):
            bericht += f"""

Im Rahmen des Hausbesuchs habe sich die Wohnsituation insgesamt als {d.get('wohnung_zustand')} dargestellt.
"""

        if d.get("post"):
            bericht += """
Es hätten sich ungeöffnete Schreiben bzw. Postrückstände gezeigt.
"""

        if d.get("geld"):
            bericht += """
Im Umgang mit finanziellen Angelegenheiten wirke die Betroffene teilweise überfordert.
"""

        if d.get("arztmeidung"):
            bericht += """
Eine regelmäßige ärztliche Versorgung bestehe derzeit offenbar nicht.
"""

        if d.get("alltag"):
            bericht += f"""

{d.get('alltag')}
"""

        # BETREUUNGSBEDARF

        bericht += """


5. Hilfen und Betreuungsbedarf
"""

        if d.get("hilfen"):
            bericht += f"""

Derzeit erfolge bereits folgende Unterstützung:

{d.get('hilfen')}.
"""

        if d.get("aufgaben"):
            bericht += f"""

Aus fachlicher Sicht erscheine insbesondere Unterstützung in folgenden Bereichen erforderlich:

{d.get('aufgaben')}.
"""

        if d.get("schluss"):
            bericht += f"""

{d.get('schluss')}
"""

        bericht += """

Aus den im Rahmen des Hausbesuchs gewonnenen Erkenntnissen ergebe sich, dass die Betroffene derzeit nur eingeschränkt in der Lage erscheine, ihre Angelegenheiten eigenständig und ausreichend zu regeln.

Die Einrichtung einer rechtlichen Betreuung erscheine aus fachlicher Sicht weiterhin prüfenswert.
"""

        st.success("Bericht erfolgreich erstellt")

        st.text_area(
            "Fertiger Bericht",
            bericht,
            height=900
        ) 
