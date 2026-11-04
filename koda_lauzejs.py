apaksa = 1
augsa = 100
minejumi = 0
#definē sākuma un beigu vērtības, un minējumu skaitu.

while True:
    minejums = (apaksa + augsa) // 2
    #Veido algoritmu minējumu veidošanai.
    minejumi += 1
    #Uzskaita minējumus pievienojot vienu cikla sākumā.
    print(f"Mans minējums ir: {minejums}")
    #Izvada minējumu.
    
    atbilde = input("Ievadi atbildi (lielāks / mazāks / pareizi): ")
    #Dod lietotājam iespēju ievadīt atbildi par minējumu.
    
    if atbilde == "lielāks":
        apaksa = minejums + 1
    elif atbilde == "mazāks":
        augsa = minejums - 1
    # Pārbauda atbildi un pārbīda robežas
    elif atbilde == "pareizi":
        print(f"Skaitlis ir uzminēts! Bija nepieciešami {minejumi} minējumi.")
        break
    # Ja atbilde ir pareiza, izvada paziņojumu un pārtrauc ciklu.
    else:
        print("Lūdzu, ievadi 'lielāks', 'mazāks' vai 'pareizi'.")
    # Ja atbilde nav derīga, izvada paziņojumu un turpina ciklu.
    
    ##Lielākais minējumu skaits ko ieguvu:7. Sliktākajā gadījumā:100.