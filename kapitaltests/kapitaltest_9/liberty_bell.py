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

#Eine Runde spielen
def play_round(bet, player_coins, machine_coins):
    if bet > player_coins:
        print("Du hast nicht genug Nickels!")
        return player_coins, machine_coins

    
    #Spieler gibt Einsatz
    player_coins -= bet
    machine_coins += bet

    reel = spin()
    print(f"Die Symbole: {reel[0]} | {reel[1]} | {reel[2]}")

    win = check_win(reel)
    if win > 0:
        print(f"Gewonnen! Auszahlung: {win} Nickels.")
        player_coins += win
        machine_coins -= win
    else:
        print("Leider verloren.")

    print (f"Spieler hat jetzt: {player_coins} Nickels , Maschine: {machine_coins} Nickels \n")
    return player_coins, machine_coins
    
#Hauptprogramm
def main():
    player = 10
    machine = 20

    print("Willkommen bei Liberty Bell!")
    print(f"Du startest mit {player} Nickels .\n")

    while player > 0 and machine > 0:
        eingabe = input("Wie viel Nickes einsetzen? (oder 'q' zum Beenden): ")

        if eingabe.lower( ) == "q":
            print("Spiel beendet. Danke fürs Spielen!")
            break
        try: #gegen ungültige Eingabe schützen
            bet = int(eingabe)
        except ValueError:
            print("Bitte eine gültige Zahl eingeben.")
            continue

        player, machine = play_round(bet, player, machine)

    if player <= 0:
        print("Du hast keine Nickels mehr. Spiel vorbei!")
    elif machine <= 0:
        print("Die Maschine hat keine Nickels mehr. Du hast gewonnen!")

if __name__ == "__main__":
    main()