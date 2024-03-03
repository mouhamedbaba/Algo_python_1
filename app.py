from display_mounth import run_exo_1
from manage_phone_numbers import run_exo_4
from manage_sentence import run_exo_3
from matrice_color_carre import run_exo_5
from matrice_diagonal import run_exo_6
from remove_unness_espace import run_exo_2


def run():
    while True:
        print()
        print(" "*10 , "==============> EXERCICES ALOGOS PYTHON <===================")
        print()
        print("1 :  AFFICHAGE MOIS ENG/FR ")
        print("2 :  SUPPRIMER ESPACE UNITULES ")
        print("3 :  CORRECTION PHRASES ")
        print("4 :  SAISI NUMEROS ")
        print("5 :  MATRICE COULEURS ")
        print("6 :  MATRICE Diagonal ") 
        print("7 :  CLAVIER TOUCHE ")
        print("0 :  QUITTER ")
        
        option = input("\nVeuillez choisir un exercice : ")
        if option == "1":
            run_exo_1()
        elif option == "2":
            run_exo_2()
        elif option == "3":
            run_exo_3()
        elif option == "4":
            run_exo_4()
        elif option == "5":
            run_exo_5()
        elif option == "6":
            run_exo_6()
        elif option == "0":
            print(" "*10 , "==============> AU REVOIR <===================")
            break
        else:
            print("   OPTION NON VALIDE")
            
run()