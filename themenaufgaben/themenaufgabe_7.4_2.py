koffer = []

anzahl_objekte = 4

fragen = [
    "Was soll ich zuerst einpacken? ",
    "Was soll ich als zweites einpacken? ",
    "Was soll ich als drittes einpacken? ",
    "Was soll ich als viertes einpacken? "
]

for i in range(anzahl_objekte):
    objekt = input(fragen[i]).lower()

    # Wenn das Objekt noch NICHT im Koffer ist, füge es hinzu
    if objekt not in koffer:
        koffer.append(objekt)
        print(koffer)
    else:
        print("Das hast du schon eingepackt.")

print("Wir haben den Koffer gefüllt. Lass mich nun kurz prüfen, ob...")

# Am Ende prüfen, ob der Reisepass dabei ist
if "reisepass" not in koffer:
    print("Du hast deinen Reisepass vergessen!")
else:
    print("Alles in Ordnung, du kannst losreisen!")