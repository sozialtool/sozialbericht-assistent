import streamlit as st

st.set_page_config(
    page_title="Sozialbericht-Assistent",
    layout="wide"
)

st.title("🧾 Sozialbericht-Assistent")

# =====================================================
# SESSION STATE
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

    d["gespraech"] = st.selectbox(
        "Art des Gesprächs",
        [
            "Hausbesuch",
            "Behördengespräch",
            "telefonisches Gespräch",
            "Klinikgespräch",
            "Pflegeheim"
        ]
    )

    d["datum"] = st.text_input(
        "Datum",
        d.get("datum", "")
    )

    st.subheader("Teilnehmende Personen")

    d["angehoerige"] = st.checkbox("Angehörige anwesend")
    d["pflege"] = st.checkbox("Pflegepersonal anwesend")
    d["einrichtung"] = st.checkbox("Einrichtung / Sozialdienst anwesend")
    d["sonstige"] = st.checkbox("sonstige Personen anwesend")

    d["teilnehmer_text"] = st.text_area(
        "Name / Funktion / Kontaktdaten",
        d.get("teilnehmer_text", "")
    )

# =====================================================
# SOZIALE SITUATION
# =====================================================

elif seite == "Soziale Situation":

    st.header("Zur sozialen Situation")

    d["beruf"] = st.selectbox(
        "Berufliche Situation",
        [
            "",
            "EU-Rente",
            "Altersrentner/in",
            "Bürgergeld",
            "Grundsicherung",
            "arbeitslos",
            "Werkstatt für behinderte Menschen",
            "erwerbstätig"
        ]
    )

    d["ausbildung"] = st.text_area(
        "Ausbildung / beruflicher Werdegang",
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

    d["wohnstatus"] = st.selectbox(
        "Wohnstatus",
        [
            "",
            "zur Miete",
            "Eigentum",
            "Wohnheim",
            "betreutes Wohnen",
            "Notunterkunft",
            "wohnungslos",
            "obdachlos"
        ]
    )

    d["wohnungsgroesse"] = st.selectbox(
        "Wohnungsgröße",
        [
            "",
            "1-Raum-Wohnung",
            "2-Raum-Wohnung",
            "3-Raum-Wohnung",
            "Einfamilienhaus",
            "Zimmer"
        ]
    )

    d["lebenssituation"] = st.selectbox(
        "Lebenssituation",
        [
            "",
            "alleinlebend",
            "mit Angehörigen lebend",
            "mit Partner/in lebend",
            "gemeinschaftlich wohnend"
        ]
    )

# =====================================================
# FAMILIE
# =====================================================

elif seite == "Familiäre Situation":

    st.header("Familiäre Situation")

    d["ledig"] = st.checkbox("ledig")
    d["geschieden"] = st.checkbox("geschieden")
    d["verwitwet"] = st.checkbox("verwitwet")

    d["kinder"] = st.checkbox("Kinder vorhanden")
    d["angehoerige_vorhanden"] = st.checkbox("Angehörige vorhanden")
    d["angehoerige_unterstuetzen"] = st.checkbox("Angehörige unterstützen")
    d["kein_kontakt"] = st.checkbox("kein Kontakt zu Angehörigen")
    d["isolation"] = st.checkbox("soziale Isolation")

    d["familie_text"] = st.text_area(
        "Weitere Angaben",
        d.get("familie_text", "")
    )

# =====================================================
# FINANZEN
# =====================================================

elif seite == "Finanzielle Situation":

    st.header("Finanzielle Situation")

    d["einkommen"] = st.multiselect(
        "Leistungen / Einkommen",
        [
            "Bürgergeld",
            "Grundsicherung",
            "Rente",
            "Erwerbseinkommen",
            "Sozialhilfe"
        ]
    )

    d["schulden"] = st.checkbox("Schulden vorhanden")
    d["mietrueckstaende"] = st.checkbox("Mietrückstände")
    d["stromschulden"] = st.checkbox("Stromschulden")
    d["konto"] = st.checkbox("Kontopfändung")

    d["finanzen_text"] = st.text_area(
        "Weitere Angaben",
        d.get("finanzen_text", "")
    )

# =====================================================
# GESUNDHEIT
# =====================================================

elif seite == "Gesundheitliche Situation":

    st.header("Gesundheitliche Situation")

    d["psychisch"] = st.checkbox("psychische Erkrankung")
    d["demenz"] = st.checkbox("Demenz")
    d["sucht"] = st.checkbox("Suchterkrankung")
    d["koerperlich"] = st.checkbox("körperliche Einschränkungen")
    d["krankheitseinsicht"] = st.checkbox("fehlende Krankheitseinsicht")
    d["arztmeidung"] = st.checkbox("Arztmeidung")

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

    d["gesundheit_text"] = st.text_area(
        "Diagnosen / gesundheitliche Angaben",
        d.get("gesundheit_text", "")
    )

# =====================================================
# BEOBACHTUNGEN
# =====================================================

elif seite == "Beobachtungen beim Hausbesuch":

    st.header("Beobachtungen beim Hausbesuch")

    d["wohnung"] = st.selectbox(
        "Wohnsituation",
        [
            "geordnet",
            "unordentlich",
            "verwahrlost",
            "vermüllt",
            "hygienisch auffällig"
        ]
    )

    d["orientiert"] = st.checkbox("orientiert")
    d["desorientiert"] = st.checkbox("desorientiert")
    d["aggressiv"] = st.checkbox("aggressiv")
    d["kooperativ"] = st.checkbox("kooperativ")
    d["misstrauisch"] = st.checkbox("misstrauisch")

    d["post"] = st.checkbox("ungeöffnete Post vorhanden")
    d["lebensmittel"] = st.checkbox("fehlende Lebensmittel")
    d["struktur"] = st.checkbox("fehlende Tagesstruktur")

    d["hausbesuch_text"] = st.text_area(
        "Weitere Beobachtungen",
        d.get("hausbesuch_text", "")
    )

# =====================================================
# DEFIZITE
# =====================================================

elif seite == "Defizite / Betreuungsbedarf":

    st.header("Defizite / Betreuungsbedarf")

    d["defizite"] = st.multiselect(
        "Betroffene Lebensbereiche",
        [
            "Vermögenssorge",
            "Behördenangelegenheiten",
            "Gesundheitsfürsorge",
            "Wohnungsangelegenheiten",
            "Postangelegenheiten",
            "Aufenthaltsangelegenheiten"
        ]
    )

    d["defizite_text"] = st.text_area(
        "Beschreibung der Defizite",
        d.get("defizite_text", "")
    )

# =====================================================
# HILFEN
# =====================================================

elif seite == "Hilfen":

    st.header("Hilfen")

    d["hilfen"] = st.multiselect(
        "Bestehende Hilfen",
        [
            "Pflegedienst",
            "Eingliederungshilfe",
            "BEW",
            "Angehörige",
            "Sozialdienst",
            "Vorsorgevollmacht"
        ]
    )

    d["hilfen_text"] = st.text_area(
        "Warum reichen die Hilfen nicht aus?",
        d.get("hilfen_text", "")
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
Das Gespräch fand im Rahmen eines {d.get('gespraech', '')}s am {d.get('datum', '')} statt.
"""

        if d.get("teilnehmer_text"):
            bericht += f"""

An dem Gespräch nahmen zusätzlich folgende Personen teil:

{d.get('teilnehmer_text')}
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
Die Betroffene sei derzeit arbeitslos.
"""

        elif beruf == "Werkstatt für behinderte Menschen":
            bericht += """
Die Betroffene arbeite derzeit in einer Werkstatt für behinderte Menschen.
"""

        elif beruf == "Altersrentner/in":
            bericht += """
Die Betroffene befinde sich im Altersrentenbezug.
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

        wohnstatus = d.get("wohnstatus", "")
        groesse = d.get("wohnungsgroesse", "")
        leben = d.get("lebenssituation", "")

        if wohnstatus == "zur Miete":
            bericht += f"""
Die Betroffene lebe {leben} in einer angemieteten {groesse}.
"""

        elif wohnstatus == "Eigentum":
            bericht += f"""
Die Betroffene lebe {leben} in eigenem Wohnraum.
"""

        elif wohnstatus == "wohnungslos":
            bericht += """
Die Betroffene sei derzeit wohnungslos.
"""

        elif wohnstatus == "obdachlos":
            bericht += """
Die Betroffene sei derzeit obdachlos.
"""

        elif wohnstatus == "Notunterkunft":
            bericht += """
Die Betroffene sei derzeit in einer Notunterkunft untergebracht.
"""

        # =================================================
        # FAMILIE
        # =================================================

        bericht += """



3. Familiäre Situation
"""

        if d.get("angehoerige_vorhanden"):
            bericht += """
Angehörige seien vorhanden.
"""

        if d.get("angehoerige_unterstuetzen"):
            bericht += """
Angehörige unterstützten die Betroffene teilweise im Alltag.
"""

        if d.get("kein_kontakt"):
            bericht += """
Belastbare familiäre Kontakte bestünden derzeit nicht.
"""

        if d.get("isolation"):
            bericht += """
Insgesamt wirke die Betroffene sozial isoliert.
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

        einkommen = ", ".join(d.get("einkommen", []))

        if einkommen:
            bericht += f"""
Die Betroffene verfüge über folgende Einkünfte bzw. Sozialleistungen: {einkommen}.
"""

        if d.get("schulden"):
            bericht += """
Es bestünden Schulden bzw. offene Forderungen.
"""

        if d.get("mietrueckstaende"):
            bericht += """
Zudem bestünden Mietrückstände.
"""

        if d.get("stromschulden"):
            bericht += """
Weiterhin bestünden Stromschulden.
"""

        if d.get("konto"):
            bericht += """
Es sei eine Kontopfändung bekannt.
"""

        if d.get("finanzen_text"):
            bericht += f"""

{d.get('finanzen_text')}
"""

        # =================================================
        # GESUNDHEIT
        # =================================================

        bericht += """



5. Zur gesundheitlichen Situation
"""

        if d.get("psychisch"):
            bericht += """
Es bestünden Hinweise auf psychische Einschränkungen.
"""

        if d.get("demenz"):
            bericht += """
Hinweise auf dementielle Veränderungen lägen vor.
"""

        if d.get("sucht"):
            bericht += """
Weiterhin bestünden Hinweise auf eine Suchterkrankung.
"""

        if d.get("koerperlich"):
            bericht += """
Zudem lägen körperliche Einschränkungen vor.
"""

        if d.get("krankheitseinsicht"):
            bericht += """
Eine ausreichende Krankheitseinsicht bestehe offenbar nicht.
"""

        if d.get("arztmeidung"):
            bericht += """
Eine regelmäßige ärztliche Behandlung erfolge derzeit offenbar nicht.
"""

        bericht += f"""

{d.get('gesundheit_text')}
"""

        if d.get("pflegegrad") != "kein Pflegegrad":
            bericht += f"""

Es liege {d.get('pflegegrad')} vor.
"""

        # =================================================
        # HAUSBESUCH
        # =================================================

        bericht += """



6. Beobachtungen beim Hausbesuch
"""

        bericht += f"""

Die Wohnsituation hat sich im Rahmen des Hausbesuchs als {d.get('wohnung')} dargestellt.
"""

        if d.get("post"):
            bericht += """
Es haben sich ungeöffnete Schreiben sowie Postrückstände gezeigt.
"""

        if d.get("lebensmittel"):
            bericht += """
Teilweise hätten nur unzureichende Lebensmittelvorräte vorgelegen.
"""

        if d.get("struktur"):
            bericht += """
Eine ausreichende Tagesstruktur habe sich nicht gezeigt.
"""

        if d.get("kooperativ"):
            bericht += """
Die Betroffene wirkte im Gespräch kooperativ.
"""

        if d.get("misstrauisch"):
            bericht += """
Die Betroffene wirkte teilweise misstrauisch.
"""

        if d.get("aggressiv"):
            bericht += """
Die Betroffene wirkte zeitweise verbal aggressiv.
"""

        if d.get("hausbesuch_text"):
            bericht += f"""

{d.get('hausbesuch_text')}
"""

        # =================================================
        # DEFIZITE
        # =================================================

        bericht += """



7. Defizite / Betreuungsbedarf
"""

        defizite = ", ".join(d.get("defizite", []))

        if defizite:
            bericht += f"""
Defizite zeigten sich insbesondere in folgenden Bereichen: {defizite}.
"""

        if d.get("defizite_text"):
            bericht += f"""

{d.get('defizite_text')}
"""

        # =================================================
        # HILFEN
        # =================================================

        bericht += """



8. Hilfen
"""

        hilfen = ", ".join(d.get("hilfen", []))

        if hilfen:
            bericht += f"""
Derzeit erfolgten bereits Hilfen in Form von: {hilfen}.
"""

        if d.get("hilfen_text"):
            bericht += f"""

{d.get('hilfen_text')}
"""

        bericht += """

Aus den im Rahmen der Sachverhaltsermittlung gewonnenen Erkenntnissen ergibt sich, dass die Betroffene derzeit nur eingeschränkt in der Lage erscheint, ihre Angelegenheiten eigenständig und ausreichend zu regeln.

Die Einrichtung einer rechtlichen Betreuung erscheint aus fachlicher Sicht weiterhin erforderlich.
"""

        st.text_area(
            "Fertiger Bericht",
            bericht,
            height=1500
        ) 
