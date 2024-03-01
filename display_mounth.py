month_french = ["janvier","fevrier","mars","avril","mai","juin","juillet","aout","septembre","octobre","novembre","decembre",]
month_english = ["january","february","march","april","may","june","july","august","september","october","november","december",]

# creer la fonction pour diviser la liste en matrice
def mouth_matrice_3_4(mouth):
    matrice = []
    for i in range(4):
        matrice.append([])
        for j in range(3):
            matrice[i].append(mouth[i*3+j])
    return matrice

#  creer les matrices pour chaque liste
french_mounth_matrice = mouth_matrice_3_4(month_french)
english_mounth_matrice = mouth_matrice_3_4(month_english)

#  procedure affichage mounth
def display_mount(mouth):
    for i in range(3):
        print("-"*59)
        for j in range(4):
            print(f"{mouth[j][i]:10}", end="|\t")
        print("")
    print("-"*59)
        


def run_exo_1():
    print()
    print(" "*30, "======> FRANCAIS <======")
    print()
    display_mount(french_mounth_matrice)
    is_lang_french=True
    while True:
        print()
        print("======> OPTIONS <======")
        print("1 : Changer de langue ")
        print("0 : Menu precedent ")
        print()
        option = input("veuillez choisir une option : ")
        if option == "1" :
            if is_lang_french == True:
                is_lang_french = False
                print(" "*30, "======> ANGLAIS <======")
                print()
                display_mount(english_mounth_matrice)
            elif is_lang_french == False:
                is_lang_french = True
                print(" "*30, "======> FRANCAIS <======")
                print()
                display_mount(french_mounth_matrice)
        elif option == "0":
            break
        else :
            print()
            print("OPTION NON VALIDE ")
            print()