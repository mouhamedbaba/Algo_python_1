# importation des FONCTION nessaisaires
from utils.util import remove_unnecessary_space, get_n, get_sentence


# FONCTION permettant de saisir le nombre de phrase voulueet retourner la liste de phrases
def sentence() -> list:
    sentences = []
    n_sentence = get_n("phrases")
    spcial_char = ["#", "$", "%", "&", "'", "(", ")", "*", "+", "-", "/", "<", "=", ">", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~"]
    for _ in range(int(n_sentence)):
        while True:
            sentence = get_sentence()
            # verification des carracters speciaux
            if  any(char in spcial_char for char in sentence):
                print("\nla phrase ne doit pas contenir de caractere speciaux reesayer")
            # verifier la phrase commence par un majuscule et se ternime par un point 
            elif sentence[0].islower() or sentence[-1] != ".":
                print("\nune phrase commence par une lettre majuscule et se termine par un point reesayer")
            # verifiaction de la longeur de la phrase
            elif len(sentence) < 25:
                print("\nla phrase doir contenir au moins 25 carracteres")
            else:
                # utiliser la FONCTION pour suprimer les esapaces unitiles
                sentence = remove_unnecessary_space(sentence)
                # ajout de la phrase a la liste des phrases
                sentences.append(sentence)
                break
    return sentences

# PROCEDURE permettant d'afficher les phrases
def display_sentences(sentences: list):
    for sent in sentences:
        print("-"*len(sent))
        print(sent)
        print("-"*len(sent))
    print()

# PROCEDURE permettant de lancer l'exercice
def run_exo_3():
    sentences = sentence()
    print()
    print("\nles phrase que vous avez saisi :")
    print()
    display_sentences(sentences)