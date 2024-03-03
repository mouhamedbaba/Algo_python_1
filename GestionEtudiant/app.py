from student import Student
class App():
    def __init__(self) -> None:
        self.students = []
        
    def create_student(self):
        first_name = input("Your first name : ")
        last_name = input("Your last name : ")
        phone = input("your phone number : ")
        classe = input("Your class : ")
        dev = input("Your mark on dev : ")
        proj = input("Your mark on proj : ")
        exam = input("Your mark on exam : ")
        new_student = Student(first_name, last_name, int(phone), classe, int(dev), int(proj), int(exam))
        self.students.append(new_student)
        for student in self.students :
            print(student.last_name)

app = App()
app.create_student()