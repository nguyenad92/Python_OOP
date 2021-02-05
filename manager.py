from employee import Employee
from developer import Developer

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def addEmpl(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def removeEmpl(self, emp):
        self.employees.remove(emp)

    def listEmployee(self):
        for emp in self.employees:
            print('-->', emp.fullname())

dev1 = Developer('AD', 'Ng', 10000, 'Python')

dev2 = Developer('DA', 'TT', 20000, 'Java')

manager1 = Manager('haha', 'hoho', 90000, [dev1, dev2])
# print(manager1.email)
print(manager1.listEmployee())

print(issubclass(Manager, Employee))