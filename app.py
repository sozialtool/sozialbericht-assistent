# =====================================================
# SOZIALBERICHT – STABILE VERSION
# OFFIZIELLE GLIEDERUNG
# =====================================================

import streamlit as st

st.set_page_config(
    page_title="Sozialbericht",
    layout="wide"
)

# =====================================================
# SESSION STATE
# =====================================================

if "daten" not in st.session_state:
    st.session_state.daten = {}

d = st.session_state.daten

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("Gliederung")

auswahl = st.sidebar.radio(
    "Bereiche",
    [
        "1. Zur sozialen Situation",
        "2. Zur finanziellen Situation",
        "3. Gesundheitliche Situation",
        "4. Zur praktischen Lebensbewältigung",
        "5. Vorsorge",
        "6. Mögliche Aufgabenkreise",
        "7. Einrichtung einer Betreuung",
        "8. Zur Person des Betreuers",
        "9. Hinweise für das gerichtliche Verfahren",
        "10. Grundlagen der Datenerhebung",
        "Bericht"
    ]
)

st.title("Sozialbericht")

# =====================================================
# 1 SOZIALE SITUATION
# =====================================================

if auswahl == "1. Zur sozialen Situation":

    st.header("1. Zur sozialen Situation")

    st.subheader(
        "Biografie, Ausbildung und beruflicher Werdegang"
    )

    d["beruf"] = st.text_input(
        "Ausbildung / Beruf",
        d.get("beruf", "")
    )

    d["berufssituation"] = st.selectbox(
        "Derzeitige Situation",
        [
            "",
            "EU-Rente",
            "Rente",
            "Bürgergeld",
            "ergänzende Grundsicherung",
            "arbeitslos",
            "nicht erwerbstätig",
            "erwerbstätig"
        ]
    )

    d["biografie"] = st.text_area(
        "Weitere biografische Angaben",
        d.get("biografie", "")
    )

    st.subheader(
        "Wohn- und Lebensverhältnisse"
    )

    d["wohnform"] = st.selectbox(
        "Wohnform",
        [
            "",
            "1-Raum-Wohnung",
            "2-Raum-Wohnung",
            "3-Raum-Wohnung",
            "Haus",
            "Pflegeheim",
            "betreutes Wohnen",
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
            "Notunterkunft"
        ]
    )

    d["alleinlebend"] = st.checkbox(
        "alleinlebend",
        d.get("alleinlebend", False)
    )

    d["wohnen_text"] = st.text_area(
        "Weitere Angaben zu den Wohnverhältnissen",
        d.get("wohnen_text", "")
    )

    st.subheader(
        "Familiäre Situation, Angehörige, Kontaktpersonen"
    )

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

    d["angehoerige"] = st.text_area(
        "Angehörige / Kontaktpersonen",
        d.get("angehoerige", "")
    )

    d["sozialkontakte"] = st.text_area(
        "Soziale Kontakte",
        d.get("sozialkontakte", "")
    )

    d["sozial_isoliert"] = st.checkbox(
        "wirkt sozial isoliert",
        d.get("sozial_isoliert", False)
    )

# =====================================================
# 2 FINANZEN
# =====================================================

elif auswahl == "2. Zur finanziellen Situation":

    st.header("2. Zur finanziellen Situation")

    d["einkommen"] = st.text_input(
        "Einkommen / Unterhalt / Rente",
        d.get("einkommen", "")
    )

    d["ergänzende_grundsicherung"] = st.checkbox(
        "ergänzende Grundsicherung",
        d.get("ergänzende_grundsicherung", False)
    )

    d["einkommen_hoehe"] = st.text_input(
        "Höhe der Einkünfte",
        d.get("einkommen_hoehe", "")
    )

    d["vermoegen"] = st.text_input(
        "Vermögen",
        d.get("vermoegen", "")
    )

    d["schulden"] = st.text_area(
        "Schulden / offene Forderungen",
        d.get("schulden", "")
    )

    d["verpflichtungen"] = st.text_input(
        "laufende finanzielle Verpflichtungen",
        d.get("verpflichtungen", "")
    )

# =====================================================
# 3 GESUNDHEIT
# =====================================================

elif auswahl == "3. Gesundheitliche Situation":

    st.header("3. Gesundheitliche Situation")

    d["psychisch"] = st.checkbox(
        "psychische Erkrankung",
        d.get("psychisch", False)
    )

    d["geistig"] = st.checkbox(
        "geistige oder seelische Beeinträchtigung",
        d.get("geistig", False)
    )

    d["koerperlich"] = st.checkbox(
        "körperliche Beeinträchtigung",
        d.get("koerperlich", False)
    )

    d["eigene_angaben"] = st.text_area(
        "Nach eigenen Angaben",
        d.get("eigene_angaben", "")
    )

    d["diagnosen"] = st.text_area(
        "Diagnosen",
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

    d["schwerbehinderung"] = st.checkbox(
        "Schwerbehinderung",
        d.get("schwerbehinderung", False)
    )

    d["krankenkasse"] = st.text_input(
        "Krankenkasse",
        d.get("krankenkasse", "")
    )

    d["hausarzt"] = st.text_input(
        "behandelnder Hausarzt",
        d.get("hausarzt", "")
    )

    d["fachaerzte"] = st.text_input(
        "behandelnde Fachärzte",
        d.get("fachaerzte", "")
    )

# =====================================================
# 4 LEBENSBEWÄLTIGUNG
# =====================================================

elif auswahl == "4. Zur praktischen Lebensbewältigung":

    st.header(
        "4. Zur praktischen Lebensbewältigung"
    )

    st.subheader(
        "Folgende Defizite bei der Wahrnehmung eigener Angelegenheiten bestehen"
    )

    d["wohnung_unordentlich"] = st.checkbox(
        "Wohnung unordentlich",
        d.get("wohnung_unordentlich", False)
    )

    d["post_ungeoeffnet"] = st.checkbox(
        "ungeöffnete Post",
        d.get("post_ungeoeffnet", False)
    )

    d["finanzen_problem"] = st.checkbox(
        "Überforderung mit finanziellen Angelegenheiten",
        d.get("finanzen_problem", False)
    )

    d["krankheitseinsicht"] = st.checkbox(
        "fehlende Krankheitseinsicht",
        d.get("krankheitseinsicht", False)
    )

    d["orientierung"] = st.checkbox(
        "Orientierungsprobleme",
        d.get("orientierung", False)
    )

    d["mobilitaet"] = st.checkbox(
        "Mobilität eingeschränkt",
        d.get("mobilitaet", False)
    )

    d["beobachtungen"] = st.text_area(
        "Weitere Beobachtungen beim Hausbesuch",
        d.get("beobachtungen", "")
    )

# =====================================================
# 5 VORSORGE
# =====================================================

elif auswahl == "5. Vorsorge":

    st.header("5. Vorsorge")

    d["vorsorgevollmacht"] = st.checkbox(
        "Vorsorgevollmacht",
        d.get("vorsorgevollmacht", False)
    )

    d["betreuungsverfuegung"] = st.checkbox(
        "Betreuungsverfügung",
        d.get("betreuungsverfuegung", False)
    )

    d["patientenverfuegung"] = st.checkbox(
        "Patientenverfügung",
        d.get("patientenverfuegung", False)
    )

# =====================================================
# 6 AUFGABENKREISE
# =====================================================

elif auswahl == "6. Mögliche Aufgabenkreise":

    st.header(
        "6. Mögliche Aufgabenkreise"
    )

    d["vermoegenssorge"] = st.checkbox(
        "Vermögenssorge",
        d.get("vermoegenssorge", False)
    )

    d["wohnungsangelegenheiten"] = st.checkbox(
        "Wohnungsangelegenheiten",
        d.get("wohnungsangelegenheiten", False)
    )

    d["gesundheitssorge"] = st.checkbox(
        "Gesundheitssorge / Heilbehandlung",
        d.get("gesundheitssorge", False)
    )

    d["aufenthalt"] = st.checkbox(
        "Aufenthaltsbestimmung",
        d.get("aufenthalt", False)
    )

    d["postangelegenheiten"] = st.checkbox(
        "Postangelegenheiten",
        d.get("postangelegenheiten", False)
    )

    d["behoerden"] = st.checkbox(
        "Vertretung gegenüber Behörden",
        d.get("behoerden", False)
    )

# =====================================================
# 7 BETREUUNG
# =====================================================

elif auswahl == "7. Einrichtung einer Betreuung":

    st.header(
        "7. Einrichtung einer Betreuung"
    )

    d["einverstanden"] = st.selectbox(
        "Die betroffene Person ist",
        [
            "",
            "mit der Betreuung einverstanden",
            "mit der Betreuung nicht einverstanden",
            "nicht in der Lage sich zu äußern"
        ]
    )

# =====================================================
# 8 BETREUER
# =====================================================

elif auswahl == "8. Zur Person des Betreuers":

    st.header(
        "8. Zur Person des Betreuers"
    )

    d["betreuer"] = st.text_input(
        "Vorschlag / Wunschbetreuer",
        d.get("betreuer", "")
    )

# =====================================================
# 9 GERICHT
# =====================================================

elif auswahl == "9. Hinweise für das gerichtliche Verfahren":

    st.header(
        "9. Hinweise für das gerichtliche Verfahren"
    )

    d["anhoerung"] = st.checkbox(
        "Anhörung möglich",
        d.get("anhoerung", False)
    )

    d["verfahrenspfleger"] = st.checkbox(
        "Verfahrenspfleger erforderlich",
        d.get("verfahrenspfleger", False)
    )

    d["schlussbemerkung"] = st.text_area(
        "Weitere Hinweise",
        d.get("schlussbemerkung", "")
    )

# =====================================================
# 10 DATEN
# =====================================================

elif auswahl == "10. Grundlagen der Datenerhebung":

    st.header(
        "10. Grundlagen der Datenerhebung"
    )

    d["daten_betroffene"] = st.checkbox(
        "Betroffene selbst",
        d.get("daten_betroffene", False)
    )

    d["daten_angehoerige"] = st.checkbox(
        "Angehörige",
        d.get("daten_angehoerige", False)
    )

    d["daten_betreuung"] = st.checkbox(
        "Bezugsbetreuung / Einrichtung",
        d.get("daten_betreuung", False)
    )

    d["daten_aktenlage"] = st.checkbox(
        "Aktenlage",
        d.get("daten_aktenlage", False)
    )

# =====================================================
# BERICHT
# =====================================================

elif auswahl == "Bericht":

    st.header("Fertiger Bericht")

    if st.button("Bericht generieren"):

        bericht = ""

        # 1
        bericht += "1. Zur sozialen Situation\n\n"

        if d.get("berufssituation"):
            bericht += (
                f"Die Betroffene sei derzeit "
                f"{d.get('berufssituation')}.\n\n"
            )

        if d.get("beruf"):
            bericht += (
                f"Die Betroffene habe im Bereich "
                f"{d.get('beruf')} gearbeitet bzw. "
                f"eine entsprechende Ausbildung "
                f"absolviert.\n\n"
            )

        if d.get("biografie"):
            bericht += f"{d.get('biografie')}\n\n"

        wohnsatz = "Die Betroffene lebe "

        if d.get("alleinlebend"):
            wohnsatz += "allein "

        if d.get("wohnstatus"):
            wohnsatz += f"{d.get('wohnstatus')} "

        if d.get("wohnform"):
            wohnsatz += f"in einer {d.get('wohnform')}"

        wohnsatz += "."

        bericht += wohnsatz + "\n\n"

        if d.get("wohnen_text"):
            bericht += f"{d.get('wohnen_text')}\n\n"

        if d.get("familienstand"):
            bericht += (
                f"Die Betroffene sei "
                f"{d.get('familienstand')}.\n\n"
            )

        if d.get("angehoerige"):
            bericht += f"{d.get('angehoerige')}\n\n"

        if d.get("sozialkontakte"):
            bericht += f"{d.get('sozialkontakte')}\n\n"

        if d.get("sozial_isoliert"):
            bericht += (
                "Die Betroffene wirkte "
                "insgesamt sozial isoliert.\n\n"
            )

        # 2
        bericht += "2. Zur finanziellen Situation\n\n"

        if d.get("einkommen"):

            if d.get("einkommen_hoehe"):
                bericht += (
                    f"Die Betroffene beziehe "
                    f"{d.get('einkommen')} "
                    f"in Höhe von ca. "
                    f"{d.get('einkommen_hoehe')} "
                    f"monatlich.\n\n"
                )

            else:
                bericht += (
                    f"Die Betroffene beziehe "
                    f"{d.get('einkommen')}.\n\n"
                )

        if d.get("ergänzende_grundsicherung"):
            bericht += (
                "Zudem werde ergänzende "
                "Grundsicherung bezogen.\n\n"
            )

        if d.get("vermoegen"):
            bericht += (
                f"Vermögen sei in Form von "
                f"{d.get('vermoegen')} "
                f"vorhanden.\n\n"
            )

        if d.get("schulden"):
            bericht += (
                f"Es bestünden folgende "
                f"Schulden bzw. offene "
                f"Forderungen: "
                f"{d.get('schulden')}\n\n"
            )

        if d.get("verpflichtungen"):
            bericht += (
                f"Laufende finanzielle "
                f"Verpflichtungen bestünden "
                f"für "
                f"{d.get('verpflichtungen')}.\n\n"
            )

        st.text_area(
            "Fertiger Bericht",
            bericht,
            height=1200
        ) 
