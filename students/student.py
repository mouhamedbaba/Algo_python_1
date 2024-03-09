class Student():
    def __init__(self, first_name :str, last_name: str, phone: int, classe: str, dev: int, proj: int, exam: int) -> None:
        self.first_name = first_name,
        self.last_name = last_name
        self.phone = phone
        self.classe = classe
        self.dev = dev
        self.proj = proj
        self.exam = exam
        self.avg = (self.dev + self.proj + self.exam) / 3