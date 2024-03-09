# importation des FONCTION nessaisaires
from utils.util import check_number_validity, clean_number, get_n, remove_unnecessary_space


# FONCTION pour recuperer les numeros
def get_number() -> str:
    number = input("\nEntrez un numero : ")
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