bericht = f"""

SOZIALBERICHT


Betroffene Person: {name}
Geburtsdatum: {geburt}

Hausbesuch vom: {datum}


1. Zur sozialen Situation

"""

# =====================================================
# SOZIALE SITUATION
# =====================================================

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

if ausbildung:
    bericht += f"""

Die Betroffene habe eine Ausbildung bzw. berufliche Tätigkeit im Bereich {ausbildung} ausgeübt.
"""

if biografie:
    bericht += f"""

{biografie}
"""

if wohnung:
    bericht += f"""

Die Betroffene lebe derzeit in einer {wohnung}.
"""

if lebt == "alleinlebend":
    bericht += """
Die Betroffene sei alleinlebend.
"""

elif lebt == "mit Angehörigen lebend":
    bericht += """
Die Betroffene lebe gemeinsam mit Angehörigen.
"""

if familie:
    bericht += f"""

Zur familiären Situation sei bekannt, dass {familie}.
"""

# =====================================================
# FINANZEN
# =====================================================

bericht += """



2. Zur finanziellen Situation
"""

if einkommen:
    bericht += f"""

Die Betroffene erhalte derzeit folgende Leistungen bzw. Einkünfte:

{einkommen}.
"""

if schulden:
    bericht += f"""

Es bestünden Schulden bzw. offene Forderungen in Höhe von ca. {schulden}.
"""

if miete:
    bericht += f"""

Die monatlichen Mietkosten beliefen sich auf ca. {miete} Euro.
"""

# =====================================================
# GESUNDHEIT
# =====================================================

bericht += """



3. Zur gesundheitlichen Situation
"""

if psychisch:
    bericht += """
Es bestünden Hinweise auf psychische Einschränkungen.
"""

if koerperlich:
    bericht += """
Weiterhin lägen körperliche Einschränkungen vor.
"""

if sucht:
    bericht += """
Zudem bestünden Hinweise auf eine Suchterkrankung bzw. Alkoholproblematik.
"""

if diagnosen:
    bericht += f"""

Die Betroffene berichte über folgende Beschwerden bzw. gesundheitliche Einschränkungen:

{diagnosen}.
"""

if pflegegrad != "kein Pflegegrad":
    bericht += f"""

Es liege {pflegegrad} vor.
"""

else:
    bericht += """

Ein Pflegegrad liege derzeit nicht vor.
"""

if arzt:
    bericht += f"""

Zur ärztlichen Versorgung sei bekannt:

{arzt}.
"""

# =====================================================
# ALLTAG
# =====================================================

bericht += """



4. Zur praktischen Lebensbewältigung
"""

bericht += f"""

Im Rahmen des Hausbesuchs habe sich die Wohnsituation insgesamt als {wohnung_zustand} dargestellt.
"""

if post:
    bericht += """
Es hätten sich ungeöffnete Schreiben bzw. Postrückstände gezeigt.
"""

if geld:
    bericht += """
Im Umgang mit finanziellen Angelegenheiten wirke die Betroffene teilweise überfordert.
"""

if arztmeidung:
    bericht += """
Eine regelmäßige ärztliche Versorgung bestehe derzeit offenbar nicht.
"""

if alltag:
    bericht += f"""

{alltag}
"""

# =====================================================
# BETREUUNG
# =====================================================

bericht += """



5. Hilfen und Betreuungsbedarf
"""

if hilfen:
    bericht += f"""

Derzeit erfolge bereits folgende Unterstützung:

{hilfen}.
"""

if aufgaben:
    bericht += f"""

Aus fachlicher Sicht erscheine insbesondere Unterstützung in folgenden Bereichen erforderlich:

{aufgaben}.
"""

if schluss:
    bericht += f"""

{schluss}
"""

bericht += """

Aus den im Rahmen des Hausbesuchs gewonnenen Erkenntnissen ergebe sich, dass die Betroffene derzeit nur eingeschränkt in der Lage erscheine, ihre Angelegenheiten eigenständig und ausreichend zu regeln.

Die Einrichtung einer rechtlichen Betreuung erscheine aus fachlicher Sicht weiterhin prüfenswert.
""" 
