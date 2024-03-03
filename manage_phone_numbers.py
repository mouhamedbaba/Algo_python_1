# importation des FONCTION nessaisaires
from utils import get_n, remove_unnecessary_space


# FONCTION pour recuperer les numeros
def get_number() -> str:
    number = input("\nEntrez un numero : ")
    return number

# FONCTION permettant de verifier la validite des numeros
def check_number_validity(number: str | int) -> bool:
    # creations du dictinaire des operateurs
    operateurs = {
        "orange" : "77",
        "kirene": "78",
        "free" : "76",
        "expresso" : "70",
        "promobile" : "75",
        "fix" : "33"
    }
    prefix = number[0] + number[1]
    if (prefix not in operateurs.values()):
        return False
    if len(number) != 9:
        return False
    if not number.isdigit():
        return False
    return True

# FONCTION pour nettoyer les numeros
def clean_number(number: str) -> str:
    number = remove_unnecessary_space(number)
    number = number.strip()
    carracter_autorise = [" ", "-", "_", ".", ","]
    for i in number :
        if i in carracter_autorise:
            number = number.replace(i, "")
    return number

# FONCTION permettant de saisir le nombre de numeros et de retourner la liste de numero valide et invalide
def manage_number() -> list:
    numbers = [[],[]]
    n = get_n("numeros")
    for _ in range(n):
        number = get_number()
        number = clean_number(number)
        # verification de la validite
        isvalid = check_number_validity(number)
        # ajout dans la liste selon la validite
        if isvalid == True:
            numbers[0].append(number)
        else :
            numbers[1].append(number)
    return numbers

# PROCEDURE permettant d'afficher les numeros 
def display_numbers(numbers: list):
    empty = "---------"
    print()
    print("VALIDES \t | \t INVALIDES")
    print('-'*37)
    if len(numbers[0])>len(numbers[1]):
        len_n = len(numbers[0])
    else :
        len_n = len(numbers[1])
    for i in range(len_n):
        print(f"\n{numbers[0][i] if i < len(numbers[0]) else empty} \t | \t {numbers[1][i] if i < len(numbers[1]) else empty}")
# PROCEDURE permettant de lancer l'exercice 
def run_exo_4():
    numbers = manage_number()
    display_numbers(numbers)