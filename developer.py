from employee import Employee

class Developer(Employee):
    raise_amt = 1.1
    def __init__(self, first, last, pay, progLang):
        super().__init__(first, last, pay)
        self.progLang = progLang
    pass

# dev1 = Developer('AD', 'Ng', 10000, 'Python')

# dev2 = Developer('DA', 'TT', 20000, 'Java')

# print(dev1.email)
# print(help(Developer))