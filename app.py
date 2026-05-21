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
# GESPRÄCH / HAUSBESUCH
# =====================================================

if seite == "Gespräch / Hausbesuch":

    st.header("Gespräch / Hausbesuch")

    d["datum"] = st.date_input("Datum")

    d["ort"] = st.selectbox(
        "Ort",
        [
            "",
            "Hausbesuch",
            "Krankenhaus",
            "Einrichtung",
            "Behörde",
            "telefonisch"
        ]
    )

    d["teilnehmer"] = st.text_area(
        "Weitere teilnehmende Personen / Kontaktdaten",
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
            "arbeitslos",
            "Bürgergeld",
            "Grundsicherung",
            "erwerbstätig"
        ]
    )

    d["ausbildung"] = st.text_input(
        "Ausbildung / Beruf",
        d.get("ausbildung", "")
    )

    d["biografie"] = st.text_area(
        "Biografische Angaben",
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
            "Wohnung",
            "Haus",
            "Pflegeeinrichtung",
            "Wohnungslos",
            "Obdachlos"
        ]
    )

    d["wohnstatus"] = st.selectbox(
        "Wohnstatus",
        [
            "",
            "zur Miete",
            "Eigentum",
            "Unterkunft",
            "betreutes Wohnen"
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

    st.header("Familiäre Situation")

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
        "Angehörige unterstützen im Alltag"
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
            "Grundsicherung",
            "Lohn / Gehalt"
        ]
    )

    d["vermoegen"] = st.text_input(
        "Vermögen",
        d.get("vermoegen", "")
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

    d["krankheitseinsicht"] = st.checkbox(
        "fehlende Krankheitseinsicht"
    )

# =====================================================
# HAUSBESUCH
# =====================================================

elif seite == "Beobachtungen beim Hausbesuch":

    st.header("Beobachtungen beim Hausbesuch")

    d["wohnung_unordentlich"] = st.checkbox(
        "Wohnung unordentlich"
    )

    d["post"] = st.checkbox(
        "ungeöffnete Post vorhanden"
    )

    d["verwahrlosung"] = st.checkbox(
        "Verwahrlosungstendenzen"
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
        "Probleme mit Behörden / Post"
    )

    d["gesundheit_problem"] = st.checkbox(
        "fehlende Gesundheitsfürsorge"
    )

    d["betreuung"] = st.checkbox(
        "rechtliche Betreuung empfohlen"
    )

    d["bedarf_text"] = st.text_area(
        "Weitere Angaben",
        d.get("bedarf_text", "")
    )

# =====================================================
# HILFEN
# =====================================================

elif seite == "Hilfen":

    st.header("Hilfen")

    d["hilfen"] = st.text_area(
        "Bereits vorhandene Hilfen",
        d.get("hilfen", "")
    )

# =====================================================
# BERICHT
# =====================================================

elif seite == "Bericht":

    st.title("Sozialbericht")

    if st.button("Bericht generieren"):

        bericht = ""

        # =================================================
        # SOZIALE SITUATION
        # =================================================

        bericht += """
1. Zur sozialen Situation

"""

        if d.get("beruf"):
            bericht += f"""
Die Betroffene sei derzeit {d.get('beruf')}.
"""

        if d.get("ausbildung"):
            bericht += f"""
Die Betroffene habe eine Ausbildung bzw. berufliche Tätigkeit im Bereich {d.get('ausbildung')} ausgeübt.
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
            wohnsatz += "alleinlebend "

        if d.get("wohnstatus"):
            wohnsatz += f"in {d.get('wohnstatus')} "

        if d.get("wohnform"):
            wohnsatz += f"einer {d.get('wohnform')}."

        bericht += wohnsatz + "\n"

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

        familienstand = d.get("familienstand", "")

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
        schulden = d.get("schulden", "")
        miete = d.get("miete", "")
        vermoegen = d.get("vermoegen", "")

        if einkommen:

            if "rente" in einkommen.lower():
                bericht += """
Die Betroffene beziehe eine Rente.
"""

            elif "bürgergeld" in einkommen.lower():
                bericht += """
Die Betroffene erhalte Leistungen nach dem SGB II.
"""

            elif "grundsicherung" in einkommen.lower():
                bericht += """
Die Betroffene erhalte Grundsicherungsleistungen.
"""

            else:
                bericht += f"""
Die Betroffene verfüge über folgende Einkünfte bzw. Sozialleistungen: {einkommen}.
"""

        if vermoegen:

            if "kein" in vermoegen.lower():
                bericht += """
Vermögen sei nach eigenen Angaben nicht vorhanden.
"""

            else:
                bericht += f"""
Die Betroffene verfüge über folgendes Vermögen: {vermoegen}.
"""

        if schulden:

            if "miete" in schulden.lower():
                bericht += """
Mietrückstände bestünden derzeit.
"""

            else:
                bericht += f"""
Es bestünden Schulden bzw. offene Forderungen in Höhe von ca. {schulden}.
"""

        if miete:
            bericht += f"""
Die monatlichen Mietkosten beliefen sich auf ca. {miete} Euro.
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

        if d.get("diagnosen"):
            bericht += f"""
Die Betroffene berichte über folgende Beschwerden bzw. Diagnosen:

{d.get('diagnosen')}
"""

        if d.get("krankheitseinsicht"):
            bericht += """
Eine ausreichende Krankheitseinsicht bestehe offenbar nicht.
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

        if d.get("post"):
            bericht += """
Es haben sich ungeöffnete Schreiben bzw. Postrückstände gezeigt.
"""

        if d.get("verwahrlosung"):
            bericht += """
Es hätten sich Hinweise auf Verwahrlosungstendenzen ergeben.
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
Im Umgang mit finanziellen Angelegenheiten wirke die Betroffene teilweise überfordert.
"""

        if d.get("post_problem"):
            bericht += """
Es bestünden Einschränkungen bei der Bearbeitung behördlicher Angelegenheiten bzw. der Post.
"""

        if d.get("gesundheit_problem"):
            bericht += """
Eine ausreichende gesundheitliche Selbstfürsorge erscheine derzeit nicht gewährleistet.
"""

        if d.get("betreuung"):
            bericht += """
Die Einrichtung einer rechtlichen Betreuung erscheine aus fachlicher Sicht weiterhin prüfenswert.
"""

        if d.get("bedarf_text"):
            bericht += f"""

{d.get('bedarf_text')}
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

        st.success("Bericht erfolgreich erstellt")

        st.text_area(
            "Fertiger Bericht",
            bericht,
            height=900
        ) 
