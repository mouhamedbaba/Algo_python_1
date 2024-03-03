from matrice_color_carre import create_matrice
from utils import display_matrice, get_ordre
def display_menu(menu: dict, choix = "CHOIX") -> str:
    print(f"""
        ========================>  {choix.upper()} DISPONIBLES   <=========================
    """.upper())
    for i in menu.keys():
        print(f"○ {i:6} : {menu[i]} ")
        
def get_color() -> str:
    colors = {
    "rouge" : "\033[91m0\033[0m",
    "bleu" : "\033[94m0\033[0m",
    "cyan" : "\033[96m0\033[0m",
    "vert" : "\033[92m0\033[0m",
    "jaune" : "\033[93m0\033[0m",
    "rose" : "\033[95m0\033[0m",
    }
    display_menu(colors, "couleurs")
    color = input("\nChoisez une couleurs : ")
    while color.lower() not in colors.keys() :
        color = input("\nChoisisez une couleurs parmis la liste : ")   
    return colors[color]

def get_position() -> str:
    positions  = {
    "ADDP": "au-dessus de la diagonale principale.",
    "EDDP": "en dessous de la diagonale principale",
    "SDP": "sur la diagonale principale",
    "ADDS": "au-dessus de la diagonale secondaire.",
    "EDDS": "en dessous de la diagonale secondaire",
    "SDS": "sur la diagonale secondaire"
}
    display_menu(positions, "POSITION")
    position = input("\nVeuillez choisir une position : ")
    
    while position.upper() not in positions.keys():
        position = input("\nVeuillez choisir une position dans la liste :")
    return position

def fill_sdp_matrice(matrice: list , color: str) -> list:
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if i == j:
                matrice[i][j] = color
    return matrice
def fill_sds_matrice(matrice: list , color: str) -> list:
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if i == len(matrice) - j - 1:
                matrice[i][j] = color
    return matrice

def fill_addp_matrice(matrice: list , color: str) -> list:
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if  i < j :
                matrice[i][j] = color
    return matrice
def fill_adds_matrice(matrice: list , color: str) -> list:
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if  i < len(matrice) - j - 1 :
                matrice[i][j] = color
    return matrice
def fill_eddp_matrice(matrice: list , color: str) -> list:
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if i > j:
                matrice[i][j] = color
    return matrice

def fill_edds_matrice(matrice: list , color: str) -> list:
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if  i > len(matrice) - j - 1 :
                matrice[i][j] = color
    return matrice

def run_exo_6():
    color = get_color()
    position = get_position()
    ordre = get_ordre()
    matrice = create_matrice(ordre)
    if position.upper() == "ADDP" :
        matrice = fill_addp_matrice(matrice, color)
    elif position.upper() == "ADDS":
        matrice = fill_adds_matrice(matrice, color)
    elif position.upper() == "EDDP":
        matrice = fill_eddp_matrice(matrice, color)
    elif position.upper() == "EDDS":
        matrice = fill_adds_matrice(matrice, color)
    elif position.upper() == "SDP":
        matrice = fill_sdp_matrice(matrice,color)
    elif position.upper() == "SDS" :
        matrice = fill_sds_matrice(matrice, color)   
    else :
        print("Une erreur S'est produite")
    display_matrice(matrice)