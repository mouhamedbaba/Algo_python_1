# IMPORTATION des fonction de nessaisaire pour la matrice le le dictionnaire des couleurs
from utils import create_matrice, display_matrice, display_menu, get_colors, get_ordre


# FONCTION pour recuperer la couleur a utiliser
def get_color() -> str:
    colors = get_colors()
    # affichage du menu de couleur
    display_menu(colors, "couleurs")
    color = input("\nChoisez une couleurs : ")
    while color.lower() not in colors.keys() :
        color = input("\nChoisisez une couleurs parmis la liste : ")
    # ici je retourne la valeur de la couleur qui est stocke dans la liste au lieu de la couleur saisi 
    # parceque la couleur saisi est une cle qui fait ref a la couleur stoke en dur dans le dictionair ;)
    # colors fait ref au dictionnair et color fait ref a la clee : colors[color] ==> dict[key] -> value
    return colors[color]

# FONCTION pour recuperer la position de la couleur
def get_position() -> str:
    positions  = {
    "ADDP": "au-dessus de la diagonale principale.",
    "EDDP": "en dessous de la diagonale principale",
    "SDP": "sur la diagonale principale",
    "ADDS": "au-dessus de la diagonale secondaire.",
    "EDDS": "en dessous de la diagonale secondaire",
    "SDS": "sur la diagonale secondaire"
}
    # affichage du menu de position
    display_menu(positions, "POSITION")
    position = input("\nVeuillez choisir une position : ")
    while position.upper() not in positions.keys():
        position = input("\nVeuillez choisir une position dans la liste :")
    return position

# FONCTION pour remplire diagonale principale.
def fill_sdp_matrice(matrice: list , color: str) -> list:
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if i == j:
                matrice[i][j] = color
    return matrice

# FONCTION pour remplire diagonale secondaire.
def fill_sds_matrice(matrice: list , color: str) -> list:
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if i == len(matrice) - j - 1:
                matrice[i][j] = color
    return matrice

# FONCTION pour remplire le dessus de la diagonal principal.
def fill_addp_matrice(matrice: list , color: str) -> list:
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if  i < j :
                matrice[i][j] = color
    return matrice

# FONCTION pour remplire le dessus de la diagonal secondaire.
def fill_adds_matrice(matrice: list , color: str) -> list:
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if  i < len(matrice) - j - 1 :
                matrice[i][j] = color
    return matrice

# FONCTION pour remplire le dessous de la diagonal principal.
def fill_eddp_matrice(matrice: list , color: str) -> list:
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if i > j:
                matrice[i][j] = color
    return matrice


# FONCTION pour remplire le dessous de la diagonal secondaire.
def fill_edds_matrice(matrice: list , color: str) -> list:
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if  i > len(matrice) - j - 1 :
                matrice[i][j] = color
    return matrice

# FONCTION pour remplire la matrice selon la posirion
def fill_matrice(matrice : list, position : str, color : str) -> list:
    position = position.upper()
    if position == "ADDP" :
        matrice = fill_addp_matrice(matrice, color)
    elif position == "ADDS":
        matrice = fill_adds_matrice(matrice, color)
    elif position == "EDDP":
        matrice = fill_eddp_matrice(matrice, color)
    elif position == "EDDS":
        matrice = fill_adds_matrice(matrice, color)
    elif position == "SDP":
        matrice = fill_sdp_matrice(matrice,color)
    elif position == "SDS" :
        matrice = fill_sds_matrice(matrice, color)   
    else :
        print("Une erreur S'est produite")
    return matrice

# PROCEDURE qui fait appel aux fonction pour lancer l'exercice
def run_exo_6():
    color = get_color()
    position = get_position()
    ordre = get_ordre()
    matrice = create_matrice(ordre)
    matrice = fill_matrice(matrice, position, color)
    display_matrice(matrice)