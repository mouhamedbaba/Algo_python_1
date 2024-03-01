from remove_unness_espace import get_sentence
from utils import remove_unnecessary_space, get_n



def sentence():
    sentences = []
    n_sentence = get_n("phrases")
    spcial_char = ["#", "$", "%", "&", "'", "(", ")", "*", "+", "-", "/", "<", "=", ">", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~"]
    for _ in range(int(n_sentence)):
        while True:
            sentence = get_sentence()
            if  any(char in spcial_char for char in sentence):
               print("\nla phrase ne doit pas contenir de caractere speciaux reesayer")
            elif sentence[0].islower() or sentence[-1] != ".":
                print("\nune phrase commence par une lettre majuscule et se termine par un point reesayer")
            elif len(sentence) < 25:
                print("\nla phrase doir contenir au moins 25 carracteres")
            else:
                sentence = remove_unnecessary_space(sentence)
                sentences.append(sentence)
                break
    return sentences

def run_exo_3():
    sentences = sentence()
    print()
    print("\nles phrase que vous avez saisi :")
    print()
    for sent in sentences:
        print("-"*len(sent))
        print(sent)
        print("-"*len(sent))
    print()

# run()