class Student:
    def init(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

# Example usage:
student1 = Student("John Doe", 18, "A")
student2 = Student("Jane Smith", 17, "B")

print(student1.display_info())
print(student2.display_info())
