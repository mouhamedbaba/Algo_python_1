def create_matrice(ordre):
    matrice=[]
    for i in range(ordre):
        matrice.append([])
        for _ in range(ordre) :
            matrice[i].append(0)
    return matrice

def choose_color_poition():
    colors = ["rouge", "bleu"]
    positions = ["haut", "bas"]
    color = input("\nQUELLE COULEUR VOULEZ VOUS MODIFIER ? [BLEU/ROUGE] ".lower().capitalize())
    while color not in colors:
        color= input("\nVeuillez choisir une couleur entre rouge et bleu : ")
    position = input("\nDans quelle position voulez vous placer la couleur ? ")
    while position not in positions:
        position = input("\nVeuillez choisir une position entre haut et bas : ")
    return color, position

def fill_matrice(matrice, color, position):
    bleu = "\033[91m0\033[0m"
    rouge = "\033[94m0\033[0m"
    if position == "haut":
        for i in range(len(matrice) // 2):
            for j in range(len(matrice[0])):
                matrice[i][j] = bleu if color == "bleu" else rouge
    else:
        for i in range(len(matrice) // 2, len(matrice)):
            for j in range(len(matrice)):
                matrice[i][j] = bleu if color == "bleu" else rouge
    return matrice

def run_exo_5():
    ordre = input("\nDonner L'odre de votre Matrice : ")
    matrice = create_matrice(int(ordre))
    color, position = choose_color_poition()
    matrice = fill_matrice(matrice, color, position)
    print("\n[")  
    for line in matrice :
        for i in line:
            print("  ",i, end="\t")
        print()
    print("]")

