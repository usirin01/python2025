import sys

def schaltjahr(jahr):
    return jahr % 400 == 0 or (jahr % 4 == 0 and jahr % 100 != 0)

def max_tage_im_monat(monat, jahr):
  if monat in [1, 3, 5, 7, 8, 10, 12]:
      return 31
  elif monat in [4, 6, 9, 11]:
      return 30
  elif monat == 2:
      if schaltjahr(jahr):
          return 29 if schaltjahr(jahr) else 28
  else:
      return 0  # Ungültiger Monat
  
def main():
      #Kontrolle(Anzahl der Argumente)
    if len(sys.argv) != 4:
        print("Bitte geben Sie das Skript mit drei Argumenten aus: <tag><monat> <jahr>")
        return

    tag_str, monat_str, jahr_str = sys.argv[1], sys.argv[2], sys.argv[3]

    #Prüfen(numerisch)

    if not (tag_str.isnumeric() and monat_str.isnumeric() and jahr_str.isnumeric()):
        print("Alle drei Argumente müssen ganze Zahlen sein.")
        return    

    tag, monat, jahr = int(tag_str), int(monat_str), int(jahr_str)

    #Prüfen(gültiger Bereich)

    if not (1 <= tag <=31 and 1 <= monat <=12 and 1 <=jahr <= 9999):
        print("Eingabe liegt nicht im zulässigen Bereich.")
        return

    #Einen Tag hizufügen
    max_tage = max_tage_im_monat(monat, jahr)
    tag += 1
    if tag > max_tage:
          tag = 1
          monat += 1
          if monat > 12:
              monat = 1
              jahr += 1
              if jahr > 9999:
                  print("Jahr liegt außerhalb des gültigen Bereichs.")
                  return
              
    #Ausgabe

    print("Willkommen beim TIP-Datumsasistenten!")
    print(f"Dein Datum ist: {tag_str}.{monat_str}.{jahr_str}")
    print (f"Der nächste Tag wir entsprehend {tag}.{monat}.{jahr} sein.")

if __name__ == "__main__":
    main()



