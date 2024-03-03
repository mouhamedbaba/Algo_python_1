# FONCTION permettant de recuperer le nombre de saisi
def get_n(saisi = "saisi") -> int:
    n_sentence = input(f"\nEnterer le nombre de {saisi} que vous voulez saisir (max 10) : ")
    if not n_sentence.isdigit():
        print("\nle nombre de saisi doit etre un entier")
        n_sentence = get_n()
    while int(n_sentence) > 10 :
        n_sentence = input("\nle nombre de saisi ne doit pas depasser 10 : ")
    return int(n_sentence)


# FONCTION permettant de supprimer les espaces unitiles
def remove_unnecessary_space(sentence) -> str:
    new_sentence = ""
    prev_char = ''
    for char in sentence:
        if not (prev_char == ' ' and char == ' '):
            new_sentence = new_sentence + char
        prev_char = char
    return new_sentence


# PROCEDURE permettant d'afficher une matrice
def display_matrice(matrice: list):
    print("\n[")  
    for line in matrice :
        for i in line:
            print("  ",i, end="\t")
        print()
    print("]")

# FONCTION permettant de recupurer l'odre d'une matrice
def get_ordre() -> int:
    ordre = input("\nOrdre de votre de matrice : ")
    while not ordre.isdigit() :
        ordre = input("\nOrdre de votre de matrice doit etre un int : ")
    
    while int(ordre) < 4 : 
        ordre = input("\nOrdre de votre de matrice doit etre superieur a 4 : ")
    return int(ordre)

# FONCTION permettant de recuperer une phrase
def get_sentence() -> str:
    sentence = input("\nEnterer une phrase: ")
    return sentence

# FONCTION pour creer une matrice d'odre de racine carre
def create_matrice(ordre : int) -> list:
    matrice=[]
    for i in range(ordre):
        matrice.append([])
        for _ in range(ordre) :
            matrice[i].append(0)
    return matrice


def get_colors() -> dict:
    colors = {
    "rouge" : "\033[91m0\033[0m",
    "bleu" : "\033[94m0\033[0m",
    "cyan" : "\033[96m0\033[0m",
    "vert" : "\033[92m0\033[0m",
    "jaune" : "\033[93m0\033[0m",
    "rose" : "\033[95m0\033[0m",
    }
    return colors

# PRCEDURE pour afficher un menu 
def display_menu(menu: dict, choix = "CHOIX", ul_dec ="bullet") -> str:

    bull = "○ "
    b_s = "bullet"
    empty = ""
    print(f"""
        ========================>  {choix.upper()} DISPONIBLES   <=========================
    """.upper())
    for i in menu.keys():
        print(f"{bull if ul_dec == b_s else empty}{i:6} : {menu[i]} ")