from .student import Student
from utils.util import display_menu, get_int, check_number_validity, clean_number, get_str, clean_os
import json
import os
class App():
    def __init__(self) -> None:
        self.students = []


# Methodes intermediares

    def _get_student(self):
        # Chargement des données existantes
        data = []
        try:
            with open("data/students.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("\nUne erreur s'est produite : Le fichier es introuvable")
        except json.JSONDecodeError:
            print("\nUne erreur s'est produite : Le fichier n'est pas au format JSON ou est Vide !")
        self.students  = data
        return True



    def _dumb_data(self, student):
        existing_data = []
        try:
            with open("data/students.json", "r") as file:
                existing_data = json.load(file)
        except Exception as e:
            print("Error ", e)
        
        data = {
            "first_name": student.first_name[0],
            "last_name": student.last_name,
            "phone": student.phone,
            "classe": student.classe,
            "dev": student.dev,
            "proj": student.proj,
            "exam": student.exam,
            "avg": student.avg
        }

        existing_data.append(data)
        
        with open("data/students.json", "w") as file:
            json.dump(existing_data, file, indent=4)



    def _get_info(self):
        first_name = get_str("\nPrenom de l'etudiant : ", limit=10)
        last_name = get_str("\nNom de l'etudiant : ", limit=10)
        phone = self._get_phone()
        classe = get_str("\nClasse de l'etudiant : ", limit=10)
        dev = get_int("\nNote de l'etudiant en Dev : ", ispositif=True, limit=20)
        proj = get_int("\nNote de l'etudiant en projet : ", ispositif=True, limit=20)
        exam = get_int("\nNote de l'etudiant en exam : ", ispositif=True, limit=20)
        return first_name, last_name, phone, classe,  dev , proj , exam



    def _get_phone(self):
        while True:
            phone = input("\nNuméro de l'étudiant : ")
            if not self._check_number(phone):
                print("\nNuméro invalide ou existe deja ! reesayer : ")
            else:
                return int(phone)



    def _is_number_valid(self, phone):
        phone_in_data = [str(student['phone']) for student in self.students]
        if len(phone) < 9:
            return False
        if phone in phone_in_data:
            return False
        return check_number_validity(phone)



    def _check_number(self, phone):
        return self._is_number_valid(phone)



    def _search_by_key(self, key ):
        data = []
        key = key.lower() 
        for student in self.students :
            if key == student["first_name"].lower() or key == student["last_name"].lower() or key == str(student["phone"]) or key == student["classe"].lower():
                data.append(student)
        return data



# debut de la creation de methodes concretes

    def display_student(self, students : list ):
        tabs = ["Prenom","Nom", "Telephone", "Classe","dev", "Projet", "Exam", "Moyenne"]
        if len(students) == 0 :
            print()
            print("-"*124)
            for tab in tabs :
                print(f"{tab:10}" ,end=" | \t") 
            print('')
            print("-"*124)
            print("\t\t\t\t \t\t  PAS DE DONNES TROUVE  ",  end="\t\t\t \t\t\t   |")
            print()
            print("-"*124)
            return
        print()
        print("-"*124)
        for tab in tabs :
            print(f"{tab:10}" ,end=" | \t") 
        print('')
        print("-"*124)
        for student in students:
            first_name = student["first_name"]
            last_name = student["last_name"]
            phone = student["phone"]
            classe = student["classe"] 
            dev = student["dev"] 
            proj = student["proj"] 
            exam = student["exam"] 
            avg = student["avg"] 
            
            print(f"{first_name:10}" ,end=" | \t")
            print(f"{last_name:10}" ,end=" | \t")
            print(f"{phone:10}" ,end=" | \t")
            print(f"{classe:10}" ,end=" | \t")
            print(f"{dev:10}" ,end=" | \t")
            print(f"{proj:10}" ,end=" | \t")
            print(f"{exam:10}" ,end=" | \t")
            print(f"{avg:10.2f}" ,end=" | \t")
            print('')
            print("-"*124)
        print()


    def create_student(self):
        first_name, last_name, phone, classe,  dev , proj , exam = self._get_info()
        new_student = Student(first_name, last_name, int(phone), classe, int(dev), int(proj), int(exam))
        self._dumb_data(new_student)
        self._get_student()


    def update_student_note(self):
        data = []
        phone = get_int("Veuillez entrer le numero de l'etudiant que vous voulez modifier", ispositif=True)
        is_number_in_data = self._is_number_in_data(phone)
        if is_number_in_data  == False:
            print(f"Pas d'etudiant avec le numero {phone}")
        else : 
            dev = get_int("Note de l'etudiant en Dev : ", ispositif=True, limit=20)
            proj = get_int("Note de l'etudiant en projet : ", ispositif=True, limit=20)
            exam = get_int("Note de l'etudiant en exam : ", ispositif=True, limit=20)
            for student in self.students :
                if student["phone"]== phone :
                    data.append(student)
                    student["dev"]= dev
                    student["proj"] = proj
                    student["exam"] = exam
        return data


    def sort_avg(self):
        data = self.students[:]
        sorted_data = []
        len_data = len(self.students)
        for i in range(len_data):
            for j in range(i + 1, len_data):
                if data[i]["avg"] < data[j]["avg"]:
                    data[i]["avg"], data[j]["avg"] = data[j]["avg"], data[i]["avg"]
            sorted_data.append(data[i])
        return sorted_data


    def search(self):
        keyword = input("\nVeuillez entrez le mot cle que vous voulez rechercher : ")
        data = self._search_by_key(keyword)
        return data


    def run_exo_8(self):
        while True :
            menu = {
                "1": "Afficher tout",
                "2": "Ajouter un etudiant",
                "3": "Trier et afficher par décroissant de la moyenne",
                "4": "Rechercher",
                "5": "Modification de notes",
                "0": "Sortir"
            }
            display_menu(menu, ul_dec="")
            print()
            option = get_int("Veuillez choisir une option  : ", ispositif=True, limit=5)
            if option == 1 :
                clean_os()
                self._get_student()
                self.display_student(self.students)
            elif option == 2 :
                clean_os()
                self.create_student()
                self._get_student()
            elif option == 4:
                clean_os()
                result = self.search()
                self.display_student(result)
            elif option == 3 :
                clean_os()
                result = self.sort_avg()
                self.display_student(result)
            elif option == 5 :
                clean_os()
                result = self.update_student_note()
                self.display_student(result)
            elif option == 0:
                clean_os()
                print()
                break
            else :
                print("Choix non disponible")

