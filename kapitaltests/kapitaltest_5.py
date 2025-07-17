import math

print("Willkomen beim TIP-Löser für quadrische Gleichungen!")

#Eingabe des Benutzers
a = float(input("Gib einen Wert für a ein: "))
b = float(input("Gib einen Wert für b ein: "))
c = float(input("Gib einen Wert für c ein: "))

#Eingaben anzeigen
print("\n==========================")
print("Deine Eingaben: ")
print("a = " + str(a) + ", b = " + str(b) + ", c = " + str(c))

#Berechnung der Diskriminante
D = b ** 2 - 4 * a * c
D = round(D, 4)  # Runden auf vier Dezimalstellen

#Lösung
x1 = (-b + math.sqrt(D)) / (2 * a)
x2 = (-b - math.sqrt(D)) / (2 * a)

#Ergebnis anzeigen
print("\n==========================")
print("Daraus ergeben sich folgende Lösungen: ")
print("Diskriminante D = ")
print("Lösung x_1 = " + str(x1))
print("Lösung x_1 = " + str(x2))

print("\n==========================")
print("Das wars und bis bald!")