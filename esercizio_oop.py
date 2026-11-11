
from abc import ABC, abstractmethod


# CLASSE ASTRATTA
class Person(ABC):

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    @abstractmethod
    def introduce(self):
        pass


# DIPENDENTE
class Dipendente(Person):

    def __init__(self, name, surname, age, salary, department):
        super().__init__(name, surname, age)
        self.salary = salary
        self.department = department

    def introduce(self):
        print(f"Sono {self.name} {self.surname}, lavoro nel reparto {self.department}")


# STUDENTE
class Studente(Person):

    def __init__(self, name, surname, age, school, course):
        super().__init__(name, surname, age)
        self.school = school
        self.course = course

    def introduce(self):
        print(f"Sono {self.name} {self.surname}, studio {self.course} presso {self.school}")


# DOCENTE
class Docente(Dipendente):

    def __init__(self, name, surname, age, salary, department, subject):
        super().__init__(name, surname, age, salary, department)
        self.subject = subject

    def introduce(self):
        print(f"Sono il docente {self.name} {self.surname}, insegno {self.subject}")


# FREELANCE
class Freelance(Dipendente):

    def __init__(self, name, surname, age, salary, department, hourly_rate):
        super().__init__(name, surname, age, salary, department)
        self.hourly_rate = hourly_rate

    def introduce(self):
        print(f"Sono {self.name} {self.surname}, lavoro come freelance e guadagno {self.hourly_rate} euro all'ora")



studente1 = Studente("Mario", "Rossi", 20, "Università", "Informatica")
docente1 = Docente("Luca", "Bianchi", 45, 2500, "Formazione", "Python")
freelance1 = Freelance("Anna", "Verdi", 30, 0, "IT", 35)

# STAMPA
studente1.introduce()
docente1.introduce()
freelance1.introduce()
