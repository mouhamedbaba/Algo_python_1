from utils import remove_unnecessary_space

def get_sentence():
    sentence = input("\nEnterer une phrase: ")
    return sentence

def run_exo_2():
    sentence = get_sentence()
    sentence = remove_unnecessary_space(sentence)
    print()
    print("\nPhrase corrigee : ", sentence)
    