def lade_daten(dateiname):
    """CSV-Datei einlesen und Header + Daten zurückgeben."""
    with open(dateiname, "r", encoding="utf-8-sig") as file:
        lines = file.readlines()
    header = lines[0].strip().split(",")
    daten = []
    for line in lines[1:]:
        daten.append(line.strip().split(","))
    return header, daten

def menue_auswahl():
    print("\nWillkommen in der TIPperino Personendatenbank für frei erfundene Personen!")
    print("Wählen Sie mit der Zahl den Filter aus, den Sie anwenden möchten:")
    print("1: Geschlecht")
    print("2: Altersbereich")
    print("3: Beruf")
    print("4: E-Mail-Domain")
    print("5: Datensatznummernbereich")
    print("0: Beenden")
    return input("Ihre Wahl: ")

def filter_geschlecht(daten):
    geschlecht = input("Bitte Geschlecht eingeben (Male/Female): ").lower()
    gefiltert = []
    for person in daten:
        if person[4] == geschlecht:
            gefiltert.append(person)
    return gefiltert

def filter_geburtsjahr(daten):
    von = int(input("Geben Sie das Startjahr ein (z.B. 1950): "))
    bis = int(input("Geben Sie das Endjahr ein (z.B. 1980): "))
    gefiltert = []
    for person in daten:
        jahr = int(person[7].split("-")[0])
        if von <= jahr <= bis:
            gefiltert.append(person)
    return gefiltert

def filter_beruf(daten):
    suchbegriff = input("Nach welchem Beruf möchten Sie filtern: ").lower()
    gefiltert = []
    for person in daten:
        if suchbegriff in person[8].lower():
            gefiltert.append(person)
    return gefiltert

def filter_email_domain(daten):
    domain = input("Nach welcher E-Mail-Domain möchten Sie filtern (.net, .com, .org, etc.): ").lower()
    gefiltert = []
    for person in daten:
        if domain in person[5].lower():
            gefiltert.append(person)
    return gefiltert

def filter_indexbereich(daten):
    start = int(input("Startindex eingeben: "))
    ende = int(input("Endindex eingeben: "))
    gefiltert = []
    for i in range(start-1, ende):
        gefiltert.append(daten[i])
    return gefiltert

def ergebnis_ausgeben(header, daten):
    if not daten:
        print("\nKeine Datensätze gefunden!\n")
        return
    print("\n--- Gefilterte Datensätze ---")
    # Header
    print(", ".join(header))
    # Daten
    for person in daten:
        print(", ".join(person))
    print(f"\nInsgesamt {len(daten)} Datensätze gefunden.\n")

def ergebnis_speichern(header, daten):
    dateiname = input("Bitte Dateiname eingeben (Standard: persons.csv): ").strip()
    if dateiname == "":
        dateiname = "persons.csv"
    with open(dateiname, "w", encoding="utf-8") as file:
        file.write(",".join(header) + "\n")
        for person in daten:
            file.write(",".join(person) + "\n")
    print(f"Datei '{dateiname}' wurde erfolgreich erstellt!\n")

def main():
    header, daten = lade_daten("people-100.csv")
    while True:                                 #walh=""
        wahl = menue_auswahl()                  #while wahl != "0":
        if wahl == "0":
            print("Programm wird beendet. Auf Wiedersehen!")
            break
        elif wahl == "1":
            gefiltert = filter_geschlecht(daten)
        elif wahl == "2":
            gefiltert = filter_geburtsjahr(daten)
        elif wahl == "3":
            gefiltert = filter_beruf(daten)
        elif wahl == "4":
            gefiltert = filter_email_domain(daten)
        elif wahl == "5":
            gefiltert = filter_indexbereich(daten)
        else:
            print("Ungültige Eingabe, bitte erneut versuchen.\n")
            continue

        if not gefiltert:
            print("Keine Datensätze entsprechen dem Filter.\n")
        else:
            print("\nSoll das Ergebnis auf dem Bildschirm oder in eine Datei ausgegeben werden?")
            print("'B' gibt auf dem Bildschirm aus, 'D' speichert eine Datei.")
            print("Enter ohne Eingabe ist standardmäßig Bildschirmausgabe.")
            auswahl = input("Ihre Wahl: ").lower()
            if auswahl == "" or auswahl == "b":
                ergebnis_ausgeben(header, gefiltert)
            elif auswahl == "d":
                ergebnis_speichern(header, gefiltert)
            else:
                print("Ungültige Eingabe. Ergebnis wird nicht gespeichert.\n")

        nochmal = input("Möchten Sie eine weitere Abfrage tätigen? ('ja' für Wiederholung): ").lower()
        if nochmal != "ja":
            print("Programm beendet. Tschüss!")
            break

if __name__ == "__main__":
    main()