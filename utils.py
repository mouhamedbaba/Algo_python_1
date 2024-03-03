def get_n(saisi = "saisi"):
    n_sentence = input(f"\nEnterer le nombre de {saisi} que vous voulez saisir (max 10) : ")
    if not n_sentence.isdigit():
        print("\nle nombre de saisi doit etre un entier")
        n_sentence = get_n()
    while int(n_sentence) > 10 :
        n_sentence = input("\nle nombre de saisi ne doit pas depasser 10 : ")
    return int(n_sentence)

def remove_unnecessary_space(sentence):
    new_sentence = ""
    prev_char = ''
    for char in sentence:
        if not (prev_char == ' ' and char == ' '):
            new_sentence = new_sentence + char
        prev_char = char
    return new_sentence

def display_matrice(matrice: list):
    print("\n[")  
    for line in matrice :
        for i in line:
            print("  ",i, end="\t")
        print()
    print("]")
    
def get_ordre() -> int:
    ordre = input("\nOrdre de votre de matrice : ")
    while not ordre.isdigit() :
        ordre = input("\nOrdre de votre de matrice doit etre un int : ")
    
    while int(ordre) < 4 : 
        ordre = input("\nOrdre de votre de matrice doit etre superieur a 4 : ")
    return int(ordre)
                