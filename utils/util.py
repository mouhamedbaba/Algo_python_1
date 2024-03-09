# FONCTION permettant de recuperer le nombre de saisi
import os


def get_n(saisi = "saisi") -> int:
    n_sentence = input(f"\nEnterer le nombre de {saisi} que vous voulez saisir (max 10) : ")
    if not n_sentence.isdigit():
        print("\nle nombre de saisi doit etre un entier")
        n_sentence = get_n()
    else :
        if int(n_sentence) > 10 :
            print("\nle nombre de saisi ne doit pas depasser 10 : ")
            n_sentence = get_n()  
    return int(n_sentence)


# FONCTION permettant de supprimer les espaces unitiles
def remove_unnecessary_space(sentence) -> str:
    new_sentence = ""
    prev_char = ''
    for char in sentence:
        if not (prev_char == ' ' and char == ' '):
            if prev_char in ["'", ".", "."]:
                new_sentence = new_sentence + " " + char
            else :
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
        
def get_int(prompt: str = "\nVeuillez entre un entier : ", ispositif: bool = False, limit:int | None = None) -> int:
    number = input(prompt)
    if number == "":
        input("\nLa chaine ne peut pas etres vide, reessayer : ")
        number = get_int(prompt, ispositif, limit)
    if str(number).isdigit() == False:
        print("\nVeuillez entre un entier : ")
        number = get_int(prompt, ispositif, limit)
    if limit != None and str(number).isdigit():
        if int(number) > limit :
            print(f"\nL'entier ne doit pas deppaser {limit} : ")
            number = get_int(prompt, ispositif, limit)
    if ispositif == True :
        if int(number) < 0 and str(number).isdigit():
            print("\nVeuillez entre un entier positif: ")
            number = get_int(prompt, ispositif, limit)
    return int(number)



def get_str(prompt: str = "\nVeuillez entre un entier : ", limit : int | None = None) :
    chaine = input(prompt)
    message  = "\nVeuillez entre un chaine valide : "
    alphab = [chr(i) for i in range(65, 91)]
    have_car = False
    for car in chaine :
        if car.upper() in alphab:
            have_car =True
            break
    if str(chaine).isdigit() or (limit != None and len(chaine) > limit) or have_car == False :
        print(message)
        chaine = get_str(prompt, limit)
    return chaine
            
        

    

# FONCTION permettant de verifier la validite des numeros
def check_number_validity(number: str) -> bool:
    operateurs = {
        "orange": "77",
        "kirene": "78",
        "free": "76",
        "expresso": "70",
        "promobile": "75",
        "fix": "33"
    }
    if len(number) != 9:
        return False
    prefix = number[:2]
    if prefix not in operateurs.values():
        return False
    if not number.isdigit():
        return False
    return True

# FONCTION pour nettoyer les numeros
def clean_number(number: str) -> str:
    number = remove_unnecessary_space(number)
    number = number.strip()
    carracter_autorise = [" ", "-", "_", ".", ","]
    for i in number :
        if i in carracter_autorise:
            number = number.replace(i, "")
    return number

def clean_os():
    os.system("clear")