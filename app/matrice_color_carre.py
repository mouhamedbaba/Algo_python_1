# imporation des fonction pour recuperer l'ordre d'une matrice et la creation d'une matrice
from utils.util import create_matrice, display_matrice, get_colors, get_ordre


# fonction pout choisir la couleur

def chose_color() -> str :
    colors = ["rouge", "bleu"]
    color = input("\nQUELLE COULEUR VOULEZ VOUS MODIFIER ? [BLEU/ROUGE] ".lower().capitalize())
    while color not in colors:
        color= input("\nVeuillez choisir une couleur entre rouge et bleu : ") 
    return color

def chose_position() -> str :
    positions = ["haut", "bas"]
    position = input("\nDans quelle position voulez vous placer la couleur ? ")
    while position not in positions:
        position = input("\nVeuillez choisir une position entre haut et bas : ")
    return position



def fill_h_matrice(matrice: list, color: str) ->list:
    colors = get_colors()
    for i in range(len(matrice) // 2):
        for j in range(len(matrice[0])):
            matrice[i][j] = colors["bleu"] if color == "bleu" else colors["rouge"]
    return matrice

def fill_b_mateice(matrice: list, color: str) -> list:
    colors = get_colors()
    for i in range(len(matrice) // 2, len(matrice)):
        for j in range(len(matrice)):
            matrice[i][j] = colors["bleu"] if color == "bleu" else colors["rouge"]
    return matrice

def run_exo_5():
    ordre = get_ordre()
    matrice = create_matrice(ordre)
    color= chose_color() 
    position = chose_position()
    if position == "haut":
        fill_h_matrice(matrice, color)
    else :
        fill_b_mateice(matrice, color)
    display_matrice(matrice)
    

