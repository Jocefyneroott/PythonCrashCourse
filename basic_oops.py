class Employee:
    name = "jocef"
    salary = 1

# jocef = Employee()
# jocef.name = "Jocefyneroot"
# jocef.salary = 12
# print(jocef.name)
# print(jocef.salary)

class Employee2:
    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary

    def getName(self):
        return self.name
    
    def getSalary(self):
        return self.salary

# emp1 = Employee2("Jocefyneroot", 12)
# print(emp1.name)
# print(emp1.salary)

# print(emp1.getName())
# print(emp1.getSalary())