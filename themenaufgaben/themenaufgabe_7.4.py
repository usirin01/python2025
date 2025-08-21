# hier Lösungsvorschlag zu 3. schreiben: 

def ist_schaltjahr(jahr):
    return jahr % 400 == 0 or (jahr % 4 == 0 and jahr % 100 != 0)

monat = input("Welchen Monat soll ich betrachten?").lower()
jahr = int(input("In welchem Jahr?"))

if jahr < 1990 or jahr >2030:
    print("Das haben wir aber als Jahreszahl nicht abgemacht...")

else:
    # normale Monate
    tage_im_monat = {
        "januar": 31, "märz": 31, "april": 30,
        "mai": 31, "juni": 30, "juli": 31,
        "august": 31, "september": 30, "oktober": 31,
        "november": 30, "dezember": 31
    }

    if monat == "februar":
        if ist_schaltjahr(jahr):
            print("Dieser Februar ist in einem Schaltjahr und hat 29 Tage.")
        else:
            print("Dieser Februar hat 28 Tage.")
    elif monat in tage_im_monat:
        print("Der Monat", monat, "hat", tage_im_monat[monat], "Tage.")