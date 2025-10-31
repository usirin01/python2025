import random

symbols = ["🧲", "♦️", "♥️", "♠️", "🔔"]

def check_win(reel):
    a,b,c, = reel

    if a == b == c == "🔔":
        return 10
    elif a == b == c == "♥️":
        return 8 
    elif a == b == c == "♦️":
        return 6
    elif a == b == c == "♠️":
        return 4 
    elif a == b == "🧲" and c in ["♥️", "♦️"]:
        return 2
    elif a == b == "🧲":
        return 1
    else:
        return 0
    
#Drehen
def spin():
    return [random.choice(symbols) for _ in range(3)]

#Hauptprogramm
def main():
    player_nickels = int(input("Anzahl Nickels des Spielers: "))
    machine_nickels = 20

    print("Willkommen bei Liberty Bell!")
    print(f"Du startest mit {player_nickels} Nickels .\n")

    while player_nickels > 0 and machine_nickels > 0:
        #Will Spieler weiterspielen?
        antwort = input("Will Spieler aufhören? (j/n):").lower()
        if antwort == "j":
            print("Spiel beendet. Danke fürs Spielen!")
            break
        
        #Einsatz abfragen
        try: #gegen ungültige Eingabe schützen
            bet = int(input(f"Wie viel Nickels einsetzen? (Spieler hat {player_nickels}):"))
        except ValueError:
            print("Bitte eine gültige Zahl eingeben.")
            continue

        if bet > player_nickels:
            print("Du hast nicht genug Nickels.")
            continue

        #Spieler gibt Einsatz
        player_nickels -= bet
        machine_nickels += bet

        #Drehen
        reel = spin()
        print(f"Die Symbole: {reel[0]} | {reel[1]} | {reel[2]}")

        #Gewinn prüfen
        win = check_win(reel)
        if win > 0:
            print(f"Gewonnen! Auszahlung: {win} Nickels.")
            player_coins += win
            machine_coins -= win
        else:
            print("Leider verloren.")

        print (f"Spieler hat jetzt: {player_nickels} Nickels , Maschine: {machine_nickels} Nickels \n")


    #Spielende Kontrolle
    if player_nickels <= 0:
        print("Du hast keine Nickels mehr. Spiel vorbei!")
    elif machine_nickels <= 0:
        print("Die Maschine hat keine Nickels mehr. Du hast gewonnen!")


if __name__ == "__main__":
    main()