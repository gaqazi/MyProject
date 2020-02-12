class Employee:
    def __init__(self, name):
        self.name = name


    def displayEmpDetails(self):
        print(self.name)

employee = Employee("Wajiha")
employee.displayEmpDetails()

employee2 = Employee("Azmat")
employee2.displayEmpDetails()