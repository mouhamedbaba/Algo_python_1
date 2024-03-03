from utils import get_n, remove_unnecessary_space

operateurs = {
        "orange" : "77",
        "kirene": "78",
        "free" : "76",
        "expresso" : "70",
        "promobile" : "70"
}

def get_number():
    number = input("\nEntrez un numero : ")
    return number

def check_number_validity(number):
    start_num = number[0] + number[1]
    if (start_num not in operateurs.values()):
        return False
    if len(number) != 9:
        return False
    if not number.isdigit():
        return False
    return True

def manage_number():
    numbers = [[],[]]
    n = get_n("numeros")
    for _ in range(int(n)):
        number = get_number()
        number = remove_unnecessary_space(number)
        number = number.replace(" ", "")
        number = number.strip()
        isvalid = check_number_validity(number)
        if isvalid == True:
            numbers[0].append(number)
        else :
            numbers[1].append(number)
    return numbers



def run_exo_4():
    empty = "---------"
    numbers = manage_number()
    print()
    print("VALIDES \t | \t INVALIDES")
    print('-'*37)
    if len(numbers[0])>len(numbers[1]):
        len_n = len(numbers[0])
    else :
        len_n = len(numbers[1])
    for i in range(len_n):
        print(f"\n{numbers[0][i] if i < len(numbers[0]) else empty} \t | \t {numbers[1][i] if i < len(numbers[1]) else empty}")