import random

print("Welcome Word Salad Maschine!")
print("Bitte gib mir 3 Sätze im Format: Subjekt - Verb - Adverb - Objekt")

alle_saetze = []
satz_nummer = 1

#3 gültige Sätze sammeln
while satz_nummer <= 3:
    satz = input(f"{satz_nummer}. Satz:")
    satz = satz.replace("1. Satz:", "").replace("2. Satz:", "").replace("3. Satz:", "")
    teile = satz.split("-")
    if len(teile) == 4:
        alle_saetze.append(teile)
        #print(alle_saetze)
        satz_nummer = satz_nummer + 1
    else:
        print(" Fehler: Bitte genau 4 Teile ein geben ( Subjekt - Verb - Adverb - Objekt).")

#Transponieren mit zip()
subjekte, verben, adverben, objekte = zip(*alle_saetze) #Neues Form der Sätze

#Zufällige Auswahl

neuer_satz = " - ".join([
    random.choice(subjekte),
    random.choice(verben),
    random.choice(adverben),
    random.choice(objekte)
])

#Auzsgabe
print("Der Salat ist nun angerichtet!")
print(neuer_satz)
print("En Guete!:)")

