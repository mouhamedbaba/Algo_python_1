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