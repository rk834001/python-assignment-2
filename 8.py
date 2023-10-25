class Person:
    def init(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def greet(self):
        return f"Hello, I'm {self.name}."

    def introduce(self):
        return f"My name is {self.name}, I am {self.age} years old, and I am {self.gender}."

class Student(Person):
    def init(self, name, age, gender, course):
        super().init(name, age, gender)
        self.course = course

    def introduce(self):
        person_info = super().introduce()
        return f"{person_info} I am a student in the {self.course} course."

class Teacher(Person):
    def init(self, name, age, gender, subject):
        super().init(name, age, gender)
        self.subject = subject

    def introduce(self):
        person_info = super().introduce()
        return f"{person_info} I am a teacher, and I teach {self.subject}."

# Example usage:
person1 = Person("Alice", 30, "Female")
student1 = Student("Bob", 20, "Male", "Computer Science")
teacher1 = Teacher("Carol", 40, "Female", "Mathematics")

print(person1.greet())
print(person1.introduce())

print(student1.greet())
print(student1.introduce())

print(teacher1.greet())
print(teacher1.introduce())
