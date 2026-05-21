# =====================================================
# SOZIALBERICHT – OFFIZIELLE GLIEDERUNG
# =====================================================

import streamlit as st
from datetime import date

st.set_page_config(
    page_title="Sozialbericht",
    layout="wide"
)

# =====================================================
# DATENSPEICHER
# =====================================================

if "bericht" not in st.session_state:
    st.session_state.bericht = ""

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
# 1. SOZIALE SITUATION
# =====================================================

if auswahl == "1. Zur sozialen Situation":

    st.header("1. Zur sozialen Situation")

    st.subheader(
        "Biografie, Ausbildung und beruflicher Werdegang"
    )

    beruf = st.text_input(
        "Ausbildung / Beruf"
    )

    berufssituation = st.selectbox(
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

    biografie = st.text_area(
        "Weitere biografische Angaben"
    )

    st.subheader(
        "Wohn- und Lebensverhältnisse"
    )

    wohnform = st.selectbox(
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

    wohnstatus = st.selectbox(
        "Wohnstatus",
        [
            "",
            "zur Miete",
            "Eigentum",
            "Notunterkunft"
        ]
    )

    alleinlebend = st.checkbox(
        "alleinlebend"
    )

    wohnen_text = st.text_area(
        "Weitere Angaben zu den Wohnverhältnissen"
    )

    st.subheader(
        "Familiäre Situation, Angehörige, Kontaktpersonen"
    )

    familienstand = st.selectbox(
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

    angehörige = st.text_area(
        "Angehörige / Kontaktpersonen"
    )

    sozialkontakte = st.text_area(
        "Soziale Kontakte"
    )

    sozial_isoliert = st.checkbox(
        "wirkt sozial isoliert"
    )

# =====================================================
# 2. FINANZEN
# =====================================================

elif auswahl == "2. Zur finanziellen Situation":

    st.header("2. Zur finanziellen Situation")

    einkommen = st.text_input(
        "Einkommen / Unterhalt / Rente"
    )

    ergänzende_grundsicherung = st.checkbox(
        "ergänzende Grundsicherung"
    )

    einkommen_höhe = st.text_input(
        "Höhe der Einkünfte"
    )

    vermögen = st.text_input(
        "Vermögen"
    )

    schulden = st.text_area(
        "Schulden / offene Forderungen"
    )

    verpflichtungen = st.text_input(
        "laufende finanzielle Verpflichtungen"
    )

# =====================================================
# 3. GESUNDHEIT
# =====================================================

elif auswahl == "3. Gesundheitliche Situation":

    st.header("3. Gesundheitliche Situation")

    psychisch = st.checkbox(
        "psychische Erkrankung"
    )

    geistig = st.checkbox(
        "geistige oder seelische Beeinträchtigung"
    )

    körperlich = st.checkbox(
        "körperliche Beeinträchtigung"
    )

    eigene_angaben = st.text_area(
        "Nach eigenen Angaben"
    )

    diagnosen = st.text_area(
        "Diagnosen"
    )

    pflegegrad = st.selectbox(
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

    schwerbehinderung = st.checkbox(
        "Schwerbehinderung"
    )

    krankenkasse = st.text_input(
        "Krankenkasse"
    )

    hausarzt = st.text_input(
        "behandelnder Hausarzt"
    )

    fachärzte = st.text_input(
        "behandelnde Fachärzte"
    )

# =====================================================
# 4. PRAKTISCHE LEBENSBEWÄLTIGUNG
# =====================================================

elif auswahl == "4. Zur praktischen Lebensbewältigung":

    st.header(
        "4. Zur praktischen Lebensbewältigung"
    )

    st.subheader(
        "Folgende Defizite bei der Wahrnehmung eigener Angelegenheiten bestehen"
    )

    wohnung_unordentlich = st.checkbox(
        "Wohnung unordentlich"
    )

    post_ungeöffnet = st.checkbox(
        "ungeöffnete Post"
    )

    finanzen_problem = st.checkbox(
        "Überforderung mit finanziellen Angelegenheiten"
    )

    krankheitseinsicht = st.checkbox(
        "fehlende Krankheitseinsicht"
    )

    orientierung = st.checkbox(
        "Orientierungsprobleme"
    )

    mobilität = st.checkbox(
        "Mobilität eingeschränkt"
    )

    beobachtungen = st.text_area(
        "Weitere Beobachtungen beim Hausbesuch"
    )

# =====================================================
# 5. VORSORGE
# =====================================================

elif auswahl == "5. Vorsorge":

    st.header("5. Vorsorge")

    vorsorgevollmacht = st.checkbox(
        "Vorsorgevollmacht"
    )

    betreuungsverfügung = st.checkbox(
        "Betreuungsverfügung"
    )

    patientenverfügung = st.checkbox(
        "Patientenverfügung"
    )

# =====================================================
# 6. AUFGABENKREISE
# =====================================================

elif auswahl == "6. Mögliche Aufgabenkreise":

    st.header(
        "6. Mögliche Aufgabenkreise"
    )

    vermögenssorge = st.checkbox(
        "Vermögenssorge"
    )

    wohnungsangelegenheiten = st.checkbox(
        "Wohnungsangelegenheiten"
    )

    gesundheitssorge = st.checkbox(
        "Gesundheitssorge / Heilbehandlung"
    )

    aufenthalt = st.checkbox(
        "Aufenthaltsbestimmung"
    )

    postangelegenheiten = st.checkbox(
        "Postangelegenheiten"
    )

    behörden = st.checkbox(
        "Vertretung gegenüber Behörden"
    )

# =====================================================
# 7. EINRICHTUNG BETREUUNG
# =====================================================

elif auswahl == "7. Einrichtung einer Betreuung":

    st.header(
        "7. Einrichtung einer Betreuung"
    )

    einverstanden = st.selectbox(
        "Die betroffene Person ist",
        [
            "",
            "mit der Betreuung einverstanden",
            "mit der Betreuung nicht einverstanden",
            "nicht in der Lage sich zu äußern"
        ]
    )

# =====================================================
# 8. BETREUER
# =====================================================

elif auswahl == "8. Zur Person des Betreuers":

    st.header(
        "8. Zur Person des Betreuers"
    )

    betreuer = st.text_input(
        "Vorschlag / Wunschbetreuer"
    )

# =====================================================
# 9. GERICHT
# =====================================================

elif auswahl == "9. Hinweise für das gerichtliche Verfahren":

    st.header(
        "9. Hinweise für das gerichtliche Verfahren"
    )

    anhörung = st.checkbox(
        "Anhörung möglich"
    )

    verfahrenspfleger = st.checkbox(
        "Verfahrenspfleger erforderlich"
    )

    schlussbemerkung = st.text_area(
        "Weitere Hinweise"
    )

# =====================================================
# 10. DATENGRUNDLAGE
# =====================================================

elif auswahl == "10. Grundlagen der Datenerhebung":

    st.header(
        "10. Grundlagen der Datenerhebung"
    )

    daten_betroffene = st.checkbox(
        "Betroffene selbst"
    )

    daten_angehörige = st.checkbox(
        "Angehörige"
    )

    daten_betreuung = st.checkbox(
        "Bezugsbetreuung / Einrichtung"
    )

    daten_aktenlage = st.checkbox(
        "Aktenlage"
    )

# =====================================================
# BERICHT
# =====================================================

elif auswahl == "Bericht":

    st.header("Fertiger Bericht")

    if st.button("Bericht generieren"):

        bericht = ""

        # =================================================
        # 1 SOZIALE SITUATION
        # =================================================

        bericht += (
            "1. Zur sozialen Situation\n\n"
        )

        if berufssituation:
            bericht += (
                f"Die Betroffene sei derzeit "
                f"{berufssituation}.\n\n"
            )

        if beruf:
            bericht += (
                f"Die Betroffene habe im Bereich "
                f"{beruf} gearbeitet bzw. eine "
                f"entsprechende Ausbildung "
                f"absolviert.\n\n"
            )

        if biografie:
            bericht += f"{biografie}\n\n"

        wohnsatz = "Die Betroffene lebe "

        if alleinlebend:
            wohnsatz += "allein "

        if wohnstatus:
            wohnsatz += f"{wohnstatus} "

        if wohnform:
            wohnsatz += f"in einer {wohnform}"

        wohnsatz += "."

        bericht += wohnsatz + "\n\n"

        if wohnen_text:
            bericht += (
                f"{wohnen_text}\n\n"
            )

        if familienstand:
            bericht += (
                f"Die Betroffene sei "
                f"{familienstand}.\n\n"
            )

        if angehörige:
            bericht += (
                f"{angehörige}\n\n"
            )

        if sozialkontakte:
            bericht += (
                f"{sozialkontakte}\n\n"
            )

        if sozial_isoliert:
            bericht += (
                "Die Betroffene wirkte "
                "insgesamt sozial isoliert.\n\n"
            )

        # =================================================
        # 2 FINANZEN
        # =================================================

        bericht += (
            "2. Zur finanziellen Situation\n\n"
        )

        if einkommen:

            if einkommen_höhe:
                bericht += (
                    f"Die Betroffene beziehe "
                    f"{einkommen} in Höhe von "
                    f"ca. {einkommen_höhe} "
                    f"monatlich.\n\n"
                )

            else:
                bericht += (
                    f"Die Betroffene beziehe "
                    f"{einkommen}.\n\n"
                )

        if ergänzende_grundsicherung:
            bericht += (
                "Zudem werde ergänzende "
                "Grundsicherung bezogen.\n\n"
            )

        if vermögen:
            bericht += (
                f"Vermögen sei in Form von "
                f"{vermögen} vorhanden.\n\n"
            )

        if schulden:
            bericht += (
                f"Es bestünden folgende "
                f"Schulden bzw. offene "
                f"Forderungen: "
                f"{schulden}\n\n"
            )

        if verpflichtungen:
            bericht += (
                f"Laufende finanzielle "
                f"Verpflichtungen bestünden "
                f"für "
                f"{verpflichtungen}.\n\n"
            )

        # =================================================
        # 3 GESUNDHEIT
        # =================================================

        bericht += (
            "3. Gesundheitliche Situation\n\n"
        )

        if psychisch:
            bericht += (
                "Hinweise auf psychische "
                "Erkrankungen lagen vor.\n\n"
            )

        if geistig:
            bericht += (
                "Es zeigten sich geistige "
                "bzw. seelische "
                "Beeinträchtigungen.\n\n"
            )

        if körperlich:
            bericht += (
                "Zudem lagen körperliche "
                "Beeinträchtigungen vor.\n\n"
            )

        if eigene_angaben:
            bericht += (
                f"Nach eigenen Angaben "
                f"bestünden folgende "
                f"gesundheitliche "
                f"Beschwerden: "
                f"{eigene_angaben}\n\n"
            )

        if diagnosen:
            bericht += (
                f"Folgende Diagnosen seien "
                f"bekannt: "
                f"{diagnosen}\n\n"
            )

        if pflegegrad:
            if pflegegrad != "kein Pflegegrad":
                bericht += (
                    f"Es liege "
                    f"{pflegegrad} vor.\n\n"
                )

        if schwerbehinderung:
            bericht += (
                "Eine Schwerbehinderung "
                "liege vor.\n\n"
            )

        if krankenkasse:
            bericht += (
                f"Die Betroffene sei bei der "
                f"{krankenkasse} "
                f"krankenversichert.\n\n"
            )

        if hausarzt:
            bericht += (
                f"Hausärztlich werde die "
                f"Betroffene durch "
                f"{hausarzt} betreut.\n\n"
            )

        if fachärzte:
            bericht += (
                f"Zusätzlich erfolge eine "
                f"fachärztliche Behandlung "
                f"durch "
                f"{fachärzte}.\n\n"
            )

        # =================================================
        # 4 LEBENSBEWÄLTIGUNG
        # =================================================

        bericht += (
            "4. Zur praktischen "
            "Lebensbewältigung\n\n"
        )

        if wohnung_unordentlich:
            bericht += (
                "Im Rahmen des Hausbesuchs "
                "stellte sich die Wohnung "
                "insgesamt als "
                "unordentlich dar.\n\n"
            )

        if post_ungeöffnet:
            bericht += (
                "Es zeigten sich "
                "ungeöffnete Schreiben "
                "sowie Postrückstände.\n\n"
            )

        if finanzen_problem:
            bericht += (
                "Im Umgang mit finanziellen "
                "Angelegenheiten wirkte die "
                "Betroffene teilweise "
                "überfordert.\n\n"
            )

        if krankheitseinsicht:
            bericht += (
                "Eine ausreichende "
                "Krankheitseinsicht "
                "bestand offenbar nicht.\n\n"
            )

        if orientierung:
            bericht += (
                "Es zeigten sich "
                "Orientierungsprobleme.\n\n"
            )

        if mobilität:
            bericht += (
                "Die Mobilität erschien "
                "eingeschränkt.\n\n"
            )

        if beobachtungen:
            bericht += (
                f"{beobachtungen}\n\n"
            )

        # =================================================
        # 5 VORSORGE
        # =================================================

        bericht += (
            "5. Vorsorge\n\n"
        )

        if vorsorgevollmacht:
            bericht += (
                "Eine Vorsorgevollmacht "
                "liege vor.\n\n"
            )

        if betreuungsverfügung:
            bericht += (
                "Eine Betreuungsverfügung "
                "liege vor.\n\n"
            )

        if patientenverfügung:
            bericht += (
                "Eine Patientenverfügung "
                "liege vor.\n\n"
            )

        # =================================================
        # 6 AUFGABENKREISE
        # =================================================

        bericht += (
            "6. Mögliche Aufgabenkreise\n\n"
        )

        aufgaben = []

        if vermögenssorge:
            aufgaben.append(
                "Vermögenssorge"
            )

        if wohnungsangelegenheiten:
            aufgaben.append(
                "Wohnungsangelegenheiten"
            )

        if gesundheitssorge:
            aufgaben.append(
                "Gesundheitssorge"
            )

        if aufenthalt:
            aufgaben.append(
                "Aufenthaltsbestimmung"
            )

        if postangelegenheiten:
            aufgaben.append(
                "Postangelegenheiten"
            )

        if behörden:
            aufgaben.append(
                "Vertretung gegenüber Behörden"
            )

        if aufgaben:
            bericht += (
                ", ".join(aufgaben)
                + ".\n\n"
            )

        # =================================================
        # 7 BETREUUNG
        # =================================================

        bericht += (
            "7. Einrichtung einer Betreuung\n\n"
        )

        if einverstanden:
            bericht += (
                f"Die Betroffene sei "
                f"{einverstanden}.\n\n"
            )

        # =================================================
        # 8 BETREUER
        # =================================================

        bericht += (
            "8. Zur Person des Betreuers\n\n"
        )

        if betreuer:
            bericht += (
                f"Als Betreuungsperson "
                f"werde vorgeschlagen: "
                f"{betreuer}\n\n"
            )

        # =================================================
        # 9 GERICHT
        # =================================================

        bericht += (
            "9. Hinweise für das "
            "gerichtliche Verfahren\n\n"
        )

        if anhörung:
            bericht += (
                "Eine Anhörung erscheine "
                "möglich.\n\n"
            )

        if verfahrenspfleger:
            bericht += (
                "Die Bestellung eines "
                "Verfahrenspflegers "
                "erscheine erforderlich.\n\n"
            )

        if schlussbemerkung:
            bericht += (
                f"{schlussbemerkung}\n\n"
            )

        # =================================================
        # 10 DATEN
        # =================================================

        bericht += (
            "10. Grundlagen der "
            "Datenerhebung\n\n"
        )

        daten = []

        if daten_betroffene:
            daten.append(
                "Betroffene selbst"
            )

        if daten_angehörige:
            daten.append(
                "Angehörige"
            )

        if daten_betreuung:
            daten.append(
                "Bezugsbetreuung / Einrichtung"
            )

        if daten_aktenlage:
            daten.append(
                "Aktenlage"
            )

        if daten:
            bericht += (
                ", ".join(daten)
                + ".\n\n"
            )

        st.text_area(
            "Fertiger Bericht",
            bericht,
            height=1200
        ) 
