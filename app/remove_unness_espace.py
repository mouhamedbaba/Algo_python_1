# importation de la FONCTION permettant de suprimer les espaces inutules
from utils.util import remove_unnecessary_space, get_sentence


# PROCEDURE permettant de d'afficher le phrase corrige
def run_exo_2():
    sentence = get_sentence()
    # utilisation de la FONCTION  permettant de suprimer les espaces inutules
    sentence = remove_unnecessary_space(sentence)
    print()
    print("\nPhrase corrigee : ", sentence)

