import math, sys

print("Willkomen beim TIP-Löser für quadrische Gleichungen!")

#Eingabe des Benutzers
a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

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
print("Diskriminante D = " + str(D))
print("Lösung x_1 = " + str(x1))
print("Lösung x_1 = " + str(x2))

print("\n==========================")
print("Das wars und bis bald!")