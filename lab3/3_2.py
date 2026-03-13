class Student:
    def __init__(self, name, age, group):
        self.name = name
        self.age = age
        self.group = group

    def info(self):
        return f"Студент: {self.name}, Возраст: {self.age}, Группа: {self.group}"

student1 = Student("Иван", 20, "221331")
print(student1.info())
