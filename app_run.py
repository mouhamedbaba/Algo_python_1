# importation des modules permettant de lancer un exercice
from app.display_mounth import run_exo_1
from app.remove_unness_espace import run_exo_2
from app.manage_sentence import run_exo_3
from app.manage_phone_numbers import run_exo_4
from app.matrice_color_carre import run_exo_5
from app.matrice_diagonal import run_exo_6
from app.clavier import run_exo_7
from students.app_student import App
from utils.util import display_menu


#  PROCEDURE permettant d'afficher le menu des exercice et de les lancer selon l'exercie choisie
def run():
    menu = {
        "1":" AFFICHAGE MOIS ENG/FR ",
        "2":" SUPPRIMER ESPACE UNITULES ",
        "3":" CORRECTION PHRASES ",
        "4":" SAISI NUMEROS ",
        "5":" MATRICE COULEURS ",
        "6":" MATRICE Diagonal ", 
        "7":" CLAVIER TOUCHE ",
        "8":" GESTION ETUDIANT ",
        "0":" QUITTER "
    }
    while True:
        display_menu(menu, ul_dec="number", choix="exercices")
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
        elif option == "7":
            run_exo_7()
        elif option == "8":
            app = App()
            app.run_exo_8()
        elif option == "0":
            print(" "*10 , "=================> AU REVOIR <===================")
            break
        else:
            print("\nOPTION NON VALIDE")

# appel a la fonction run pour executer le programe
run()