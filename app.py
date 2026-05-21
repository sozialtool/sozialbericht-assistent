import streamlit as st

st.set_page_config(page_title="Sozialbericht", layout="wide")

# =====================================================
# DATENSPEICHER
# =====================================================

if "daten" not in st.session_state:
    st.session_state.daten = {}

d = st.session_state.daten

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("Bereiche")

seite = st.sidebar.radio(
    "Navigation",
    [
        "Gespräch / Hausbesuch",
        "Soziale Situation",
        "Wohn- und Lebensverhältnisse",
        "Familiäre Situation",
        "Finanzielle Situation",
        "Gesundheitliche Situation",
        "Beobachtungen beim Hausbesuch",
        "Defizite / Betreuungsbedarf",
        "Hilfen",
        "Bericht"
    ]
)

# =====================================================
# GESPRÄCH
# =====================================================

if seite == "Gespräch / Hausbesuch":

    st.header("Gespräch / Hausbesuch")

    d["datum"] = st.date_input("Datum")

    d["ort"] = st.selectbox(
        "Art des Gesprächs",
        [
            "Hausbesuch",
            "Behördengespräch",
            "Klinik",
            "Pflegeheim",
            "telefonisch"
        ]
    )

    d["teilnehmer"] = st.text_area(
        "Weitere Gesprächsteilnehmer / Kontaktdaten",
        d.get("teilnehmer", "")
    )

# =====================================================
# SOZIALE SITUATION
# =====================================================

elif seite == "Soziale Situation":

    st.header("Soziale Situation")

    d["beruf"] = st.selectbox(
        "Berufliche Situation",
        [
            "",
            "EU-Rente",
            "Rente",
            "Bürgergeld",
            "ergänzende Grundsicherung",
            "Grundsicherung",
            "arbeitslos",
            "erwerbstätig"
        ]
    )

    d["ausbildung"] = st.text_input(
        "Ausbildung / Beruf",
        d.get("ausbildung", "")
    )

    d["biografie"] = st.text_area(
        "Weitere biografische Angaben",
        d.get("biografie", "")
    )

# =====================================================
# WOHNEN
# =====================================================

elif seite == "Wohn- und Lebensverhältnisse":

    st.header("Wohn- und Lebensverhältnisse")

    d["wohnform"] = st.selectbox(
        "Wohnform",
        [
            "",
            "1-Raum-Wohnung",
            "2-Raum-Wohnung",
            "3-Raum-Wohnung",
            "Haus",
            "Pflegeeinrichtung",
            "wohnungslos",
            "obdachlos"
        ]
    )

    d["wohnstatus"] = st.selectbox(
        "Wohnstatus",
        [
            "",
            "zur Miete",
            "Eigentum",
            "betreutes Wohnen",
            "Notunterkunft"
        ]
    )

    d["allein"] = st.checkbox("alleinlebend")

    d["wohnen_text"] = st.text_area(
        "Weitere Angaben",
        d.get("wohnen_text", "")
    )

# =====================================================
# FAMILIE
# =====================================================

elif seite == "Familiäre Situation":

    st.header("Familiäre und soziale Situation")

    d["familienstand"] = st.selectbox(
        "Familienstand",
        [
            "",
            "ledig",
            "verheiratet",
            "geschieden",
            "verwitwet",
            "getrennt lebend"
        ]
    )

    d["kinder"] = st.checkbox("Kinder vorhanden")

    d["angehoerige"] = st.checkbox(
        "Angehörige vorhanden"
    )

    d["unterstuetzung"] = st.checkbox(
        "Angehörige unterstützen"
    )

    d["kein_kontakt"] = st.checkbox(
        "kein Kontakt zu Angehörigen"
    )

    d["isolation"] = st.checkbox(
        "soziale Isolation"
    )

    d["familie_text"] = st.text_area(
        "Weitere Angaben",
        d.get("familie_text", "")
    )

# =====================================================
# FINANZEN
# =====================================================

elif seite == "Finanzielle Situation":

    st.header("Finanzielle Situation")

    d["einkommen"] = st.selectbox(
        "Leistungen / Einkommen",
        [
            "",
            "Rente",
            "EU-Rente",
            "Bürgergeld",
            "ergänzende Grundsicherung",
            "Grundsicherung",
            "Lohn / Gehalt"
        ]
    )

    d["einkommen_hoehe"] = st.text_input(
        "monatliche Höhe",
        d.get("einkommen_hoehe", "")
    )

    d["vermoegen"] = st.selectbox(
        "Vermögen",
        [
            "",
            "kein Vermögen",
            "unter 10.000 Euro",
            "über 10.000 Euro"
        ]
    )

    d["schulden"] = st.text_input(
        "Schulden / offene Forderungen",
        d.get("schulden", "")
    )

    d["miete"] = st.text_input(
        "monatliche Mietkosten",
        d.get("miete", "")
    )

# =====================================================
# GESUNDHEIT
# =====================================================

elif seite == "Gesundheitliche Situation":

    st.header("Gesundheitliche Situation")

    d["psychisch"] = st.checkbox(
        "psychische Erkrankung"
    )

    d["demenz"] = st.checkbox(
        "dementielle Veränderung"
    )

    d["koerperlich"] = st.checkbox(
        "körperliche Einschränkungen"
    )

    d["sucht"] = st.checkbox(
        "Suchterkrankung / Alkoholproblematik"
    )

    d["krankheitseinsicht"] = st.checkbox(
        "fehlende Krankheitseinsicht"
    )

    d["diagnosen"] = st.text_area(
        "Diagnosen / Beschwerden",
        d.get("diagnosen", "")
    )

    d["pflegegrad"] = st.selectbox(
        "Pflegegrad",
        [
            "",
            "kein Pflegegrad",
            "Pflegegrad 1",
            "Pflegegrad 2",
            "Pflegegrad 3",
            "Pflegegrad 4",
            "Pflegegrad 5"
        ]
    )

# =====================================================
# HAUSBESUCH
# =====================================================

elif seite == "Beobachtungen beim Hausbesuch":

    st.header("Beobachtungen beim Hausbesuch")

    d["wohnung_unordentlich"] = st.checkbox(
        "Wohnung unordentlich"
    )

    d["verwahrlosung"] = st.checkbox(
        "Verwahrlosungstendenzen"
    )

    d["post"] = st.checkbox(
        "ungeöffnete Post vorhanden"
    )

    d["hausbesuch_text"] = st.text_area(
        "Weitere Beobachtungen",
        d.get("hausbesuch_text", "")
    )

# =====================================================
# BETREUUNGSBEDARF
# =====================================================

elif seite == "Defizite / Betreuungsbedarf":

    st.header("Defizite / Betreuungsbedarf")

    d["finanzen_problem"] = st.checkbox(
        "Probleme bei finanziellen Angelegenheiten"
    )

    d["post_problem"] = st.checkbox(
        "Probleme mit Behördenangelegenheiten / Post"
    )

    d["gesundheit_problem"] = st.checkbox(
        "fehlende Gesundheitsfürsorge"
    )

    d["betreuung"] = st.checkbox(
        "rechtliche Betreuung erforderlich"
    )

    d["bedarf_text"] = st.text_area(
        "Weitere Angaben",
        d.get("bedarf_text", "")
    )

# =====================================================
# HILFEN
# =====================================================

elif seite == "Hilfen":

    st.header("Bereits vorhandene Hilfen")

    d["hilfen"] = st.text_area(
        "Hilfen / Unterstützungsangebote",
        d.get("hilfen", "")
    )

    d["hilfen_reichen_nicht"] = st.text_area(
        "Warum reichen die Hilfen nicht aus?",
        d.get("hilfen_reichen_nicht", "")
    )

# =====================================================
# BERICHT
# =====================================================

elif seite == "Bericht":

    st.header("Sozialbericht")

    if st.button("Bericht generieren"):

        bericht = ""

        # =================================================
        # GESPRÄCH
        # =================================================

        bericht += f"""
Das Gespräch fand im Rahmen eines {d.get('ort')}s statt.
"""

        if d.get("teilnehmer"):
            bericht += f"""

An dem Gespräch nahmen zusätzlich folgende Personen teil:

{d.get('teilnehmer')}
"""

        # =================================================
        # SOZIALE SITUATION
        # =================================================

        bericht += """



1. Zur sozialen Situation
"""

        beruf = d.get("beruf", "")

        if beruf == "EU-Rente":
            bericht += """
Die Betroffene sei EU-Rentnerin.
"""

        elif beruf == "Rente":
            bericht += """
Die Betroffene befinde sich im Rentenbezug.
"""

        elif beruf == "Bürgergeld":
            bericht += """
Die Betroffene erhalte Leistungen nach dem SGB II.
"""

        elif beruf == "ergänzende Grundsicherung":
            bericht += """
Die Betroffene erhalte ergänzende Grundsicherungsleistungen.
"""

        elif beruf == "Grundsicherung":
            bericht += """
Die Betroffene erhalte Grundsicherungsleistungen.
"""

        elif beruf == "arbeitslos":
            bericht += """
Die Betroffene sei derzeit arbeitslos.
"""

        elif beruf == "erwerbstätig":
            bericht += """
Die Betroffene gehe derzeit einer Erwerbstätigkeit nach.
"""

        if d.get("ausbildung"):
            bericht += f"""

Die Betroffene habe im Bereich {d.get('ausbildung')} gearbeitet bzw. eine entsprechende Ausbildung absolviert.
"""

        if d.get("biografie"):
            bericht += f"""

{d.get('biografie')}
"""

        # =================================================
        # WOHNEN
        # =================================================

        bericht += """



2. Wohn- und Lebensverhältnisse
"""

        wohnsatz = "Die Betroffene lebe "

        if d.get("allein"):
            wohnsatz += "allein "

        if d.get("wohnstatus") == "zur Miete":
            wohnsatz += "zur Miete "

        elif d.get("wohnstatus") == "Eigentum":
            wohnsatz += "in eigenem Wohnraum "

        elif d.get("wohnstatus") == "betreutes Wohnen":
            wohnsatz += "im betreuten Wohnen "

        elif d.get("wohnstatus") == "Notunterkunft":
            wohnsatz += "in einer Notunterkunft "

        if d.get("wohnform"):
            wohnsatz += f"in einer {d.get('wohnform')}."

        bericht += wohnsatz

        if d.get("wohnen_text"):
            bericht += f"""

{d.get('wohnen_text')}
"""

        # =================================================
        # FAMILIE
        # =================================================

        bericht += """



3. Familiäre und soziale Situation
"""

        familienstand = d.get("familienstand")

        if familienstand == "ledig":
            bericht += """
Die Betroffene sei ledig.
"""

        elif familienstand == "verheiratet":
            bericht += """
Die Betroffene sei verheiratet.
"""

        elif familienstand == "geschieden":
            bericht += """
Die Betroffene sei geschieden.
"""

        elif familienstand == "verwitwet":
            bericht += """
Die Betroffene sei verwitwet.
"""

        elif familienstand == "getrennt lebend":
            bericht += """
Die Betroffene lebe getrennt.
"""

        if d.get("kinder"):
            bericht += """
Kinder seien vorhanden.
"""

        if d.get("angehoerige"):
            bericht += """
Angehörige seien vorhanden.
"""

        if d.get("unterstuetzung"):
            bericht += """
Angehörige unterstützten die Betroffene teilweise im Alltag.
"""

        if d.get("kein_kontakt"):
            bericht += """
Ein regelmäßiger Kontakt zu Angehörigen bestehe derzeit nicht.
"""

        if d.get("isolation"):
            bericht += """
Die Betroffene wirke insgesamt sozial isoliert.
"""

        if d.get("familie_text"):
            bericht += f"""

{d.get('familie_text')}
"""

        # =================================================
        # FINANZEN
        # =================================================

        bericht += """



4. Zur finanziellen Situation
"""

        einkommen = d.get("einkommen", "")
        hoehe = d.get("einkommen_hoehe", "")

        if einkommen:

            if einkommen == "Rente":

                if hoehe:
                    bericht += f"""
Die Betroffene beziehe eine Rente in Höhe von ca. {hoehe} Euro monatlich.
"""
                else:
                    bericht += """
Die Betroffene beziehe eine Rente.
"""

            elif einkommen == "EU-Rente":

                if hoehe:
                    bericht += f"""
Die Betroffene beziehe eine EU-Rente in Höhe von ca. {hoehe} Euro monatlich.
"""
                else:
                    bericht += """
Die Betroffene beziehe eine EU-Rente.
"""

            elif einkommen == "Bürgergeld":

                if hoehe:
                    bericht += f"""
Die Betroffene erhalte Leistungen nach dem SGB II in Höhe von ca. {hoehe} Euro monatlich.
"""

            elif einkommen == "Grundsicherung":

                if hoehe:
                    bericht += f"""
Die Betroffene erhalte Grundsicherungsleistungen in Höhe von ca. {hoehe} Euro monatlich.
"""

            elif einkommen == "ergänzende Grundsicherung":

                if hoehe:
                    bericht += f"""
Die Betroffene erhalte ergänzende Grundsicherungsleistungen in Höhe von ca. {hoehe} Euro monatlich.
"""

        if d.get("vermoegen") == "kein Vermögen":
            bericht += """
Vermögen sei nach eigenen Angaben nicht vorhanden.
"""

        elif d.get("vermoegen"):
            bericht += f"""
Das vorhandene Vermögen liege {d.get('vermoegen')}.
"""

        if d.get("schulden"):
            bericht += f"""
Es bestünden Schulden bzw. offene Forderungen in Höhe von ca. {d.get('schulden')}.
"""

        if d.get("miete"):
            bericht += f"""
Die monatlichen Mietkosten beliefen sich auf ca. {d.get('miete')} Euro.
"""

        # =================================================
        # GESUNDHEIT
        # =================================================

        bericht += """



5. Zur gesundheitlichen Situation
"""

        if d.get("psychisch"):
            bericht += """
Hinweise auf psychische Einschränkungen lägen vor.
"""

        if d.get("demenz"):
            bericht += """
Hinweise auf dementielle Veränderungen lägen vor.
"""

        if d.get("koerperlich"):
            bericht += """
Zudem lägen körperliche Einschränkungen vor.
"""

        if d.get("sucht"):
            bericht += """
Weiterhin bestünden Hinweise auf eine Suchterkrankung bzw. Alkoholproblematik.
"""

        if d.get("krankheitseinsicht"):
            bericht += """
Eine ausreichende Krankheitseinsicht bestehe offenbar nicht.
"""

        if d.get("diagnosen"):
            bericht += f"""

Die Betroffene berichte über folgende Beschwerden bzw. Diagnosen:

{d.get('diagnosen')}
"""

        if d.get("pflegegrad"):

            if d.get("pflegegrad") == "kein Pflegegrad":
                bericht += """
Ein Pflegegrad liege derzeit nicht vor.
"""

            else:
                bericht += f"""
Es liege {d.get('pflegegrad')} vor.
"""

        # =================================================
        # HAUSBESUCH
        # =================================================

        bericht += """



6. Beobachtungen beim Hausbesuch
"""

        if d.get("wohnung_unordentlich"):
            bericht += """
Im Rahmen des Hausbesuchs hat sich die Wohnsituation insgesamt als unordentlich dargestellt.
"""

        if d.get("verwahrlosung"):
            bericht += """
Es haben sich Hinweise auf Verwahrlosungstendenzen gezeigt.
"""

        if d.get("post"):
            bericht += """
Es haben sich ungeöffnete Schreiben sowie Postrückstände gezeigt.
"""

        if d.get("hausbesuch_text"):
            bericht += f"""

{d.get('hausbesuch_text')}
"""

        # =================================================
        # BETREUUNGSBEDARF
        # =================================================

        bericht += """



7. Defizite / Betreuungsbedarf
"""

        if d.get("finanzen_problem"):
            bericht += """
Im Umgang mit finanziellen Angelegenheiten wirkte die Betroffene teilweise überfordert.
"""

        if d.get("post_problem"):
            bericht += """
Es bestünden Einschränkungen bei der Bearbeitung behördlicher Angelegenheiten.
"""

        if d.get("gesundheit_problem"):
            bericht += """
Eine ausreichende gesundheitliche Selbstfürsorge erscheine derzeit nicht gewährleistet.
"""

        if d.get("bedarf_text"):
            bericht += f"""

{d.get('bedarf_text')}
"""

        if d.get("betreuung"):
            bericht += """
Die Einrichtung einer rechtlichen Betreuung erscheine aus fachlicher Sicht weiterhin erforderlich.
"""

        # =================================================
        # HILFEN
        # =================================================

        bericht += """



8. Bereits vorhandene Hilfen
"""

        if d.get("hilfen"):
            bericht += f"""
Derzeit bestünden folgende Hilfen bzw. Unterstützungsangebote:

{d.get('hilfen')}
"""

        if d.get("hilfen_reichen_nicht"):
            bericht += f"""

{d.get('hilfen_reichen_nicht')}
"""

        st.text_area(
            "Fertiger Bericht",
            bericht,
            height=1400
        ) 
