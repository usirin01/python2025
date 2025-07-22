# leere Liste erstellen

my_numbers = []

#Eingaben vom Benutzer abfragen und in die Liste einfügen

my_numbers.append(float(input(" Erste Zahl: ")))
my_numbers.append(float(input(" Zweite Zahl: ")))
my_numbers.append(float(input(" Dritte Zahl: ")))
my_numbers.append(float(input(" Vierte Zahl: ")))

# Berechnung

resultat = ((my_numbers[0] * my_numbers[1]) - my_numbers[1] ** 2 ) / (my_numbers[2] - my_numbers[3] )

# Ausgabe des Ergebnisses

print(resultat)