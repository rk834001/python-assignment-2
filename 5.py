class Employee:
    # Class variable to keep track of all employees' salaries
    total_salaries = []
    
    def init(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        Employee.total_salaries.append(salary)

    def get_salary(self):
        return self.salary

    def set_salary(self, new_salary):
        if new_salary >= 0:
            # Remove the current salary from the total_salaries list and update with the new salary
            Employee.total_salaries.remove(self.salary)
            self.salary = new_salary
            Employee.total_salaries.append(new_salary)
            return f"New salary for {self.name} (ID: {self.employee_id}) is ${new_salary}."
        else:
            return "Invalid salary value."

    @classmethod
    def calculate_average_salary(cls):
        if len(cls.total_salaries) > 0:
            average_salary = sum(cls.total_salaries) / len(cls.total_salaries)
            return f"Average salary of all employees is ${average_salary:.2f}"
        else:
            return "No employees with recorded salaries."

# Example usage:
employee1 = Employee("Alice", 101, 50000)
employee2 = Employee("Bob", 102, 60000)

print(employee1.get_salary())
print(employee1.set_salary(55000))
print(employee1.get_salary())

print(employee2.get_salary())
print(employee2.set_salary(65000))
print(employee2.get_salary())

print(Employee.calculate_average_salary())
