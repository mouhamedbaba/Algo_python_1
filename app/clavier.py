def code_phrase(phrase):
    code_clavier = {'A': '2', 'B': '22', 'C': '222','D': '3', 'E': '33', 'F': '333','G': '4', 'H': '44', 'I': '444','J': '5', 'K': '55', 'L': '555','M': '6', 'N': '66', 'O': '666','P': '7', 'Q': '77', 'R': '777', 'S': '7777','T': '8', 'U': '88', 'V': '888','W': '9', 'X': '99', 'Y': '999', 'Z': '9999','0': 'A', '1': 'B', '2': 'C','3': 'D', '4': 'E', '5': 'F','6': 'G', '7': 'H', '8': 'I', '9': 'J',' ': '00', "'": "'", ',': ',', '.': '.','!': '!', '?': '?', '-': '-', '': '', '#': '#'
    }
    nouvelle_phrase = ""
    for lettre in phrase :
        lettre_upper = lettre.upper()
        if lettre_upper in code_clavier:
            if len(nouvelle_phrase) > 0 and nouvelle_phrase[-1] == code_clavier[lettre_upper][0]:
                nouvelle_phrase += "0" + code_clavier[lettre_upper]
            else :
                nouvelle_phrase += code_clavier[lettre_upper]
    return nouvelle_phrase

def run_exo_7():
    phrase = input("Entrez une phrase :")
    nouvelle_phrase = code_phrase(phrase)
    print(phrase , " <=|>===<|=> " , nouvelle_phrase)