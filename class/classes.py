class Human:
    def __init__(self, n, s, a):
        self.name = n
        self.surname = s
        self.age = a

class Employee(Human):
    def __init__(self, n, s, a, sal):
        super().__init__(n, s, a)
        self.salary = sal

    def __repr__(self):
        return self.name + " " + self.surname


class Manager(Human):
    def __init__(self, n, s, a):
        super().__init__(n, s, a)
        self.employees = []

    def hire_employee(self, *emp):
        for em in emp:
            self.employees.append(em)

    def fire_employee(self, emp):
        self.employees.remove(emp)

    def print_employees(self):
        for emp in self.employees:
            print(emp)

    def __repr__(self):
        return self.name + " " + self.surname

def main():
    emp1 = Employee("John", "Smith", 35, 3500)
    emp2 = Employee("James", "Scott", 45, 4500)
    emp3 = Employee("Bella", "Cruz", 25, 5500)
    emp4 = Employee("Ann", "Alba", 18, 18000)
    man1 = Manager("James", "Bond", 39)
    print("Before hiring")
    man1.print_employees()
    print("We are hiring")
    man1.hire_employee(emp1, emp2, emp3, emp4)
    man1.print_employees()
    print("Bella is fired")
    man1.fire_employee(emp3)
    man1.print_employees()
    man1 = None
    print(man1)


if __name__ == '__main__':
    main()
