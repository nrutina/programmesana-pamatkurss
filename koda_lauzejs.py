#definē sākuma un beigu vērtības, un minējumu skaitu.
apaksa = 1
augsa = 100
minejumi = 0

while True:
    #Pārbauda vai atbildes ir pretrunīgas, ja jā, tad izvada paziņojumu un pārtrauc ciklu.
    if apaksa > augsa:
        print("Sniegtās atbildes ir bijušas pretrunīgas. Spēle tiek pārtraukta.")
        break
    
    #Veido algoritmu minējumu veidošanai.
    minejums = (apaksa + augsa) // 2
    #Uzskaita minējumus pievienojot vienu cikla sākumā.
    minejumi += 1
    #Izvada minējumu.
    print(f"Mans minējums ir: {minejums}")
    #Dod lietotājam iespēju ievadīt atbildi par minējumu.
    atbilde = input("Ievadi atbildi (lielāks / mazāks / pareizi): ")
 
    #Pārbauda atbildi un pārbīda robežas
    if atbilde == "lielāks":
        apaksa = minejums + 1
    elif atbilde == "mazāks":
        augsa = minejums - 1
        
    #Ja atbilde ir pareiza, izvada paziņojumu un pārtrauc ciklu.
    elif atbilde == "pareizi":
        print(f"Skaitlis ir uzminēts! Bija nepieciešami {minejumi} minējumi.")
        break
        
    #Ja atbilde nav derīga, izvada paziņojumu un turpina ciklu.
    else:
        print("Lūdzu, ievadi 'lielāks', 'mazāks' vai 'pareizi'.")

    
    ##Lielākais minējumu skaits ko ieguvu:7. Sliktākajā gadījumā:100.
