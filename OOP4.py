

# inheritance

class Employee:

    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first.lower() +  '.' + self.last.lower() + '@email.com'
        Employee.num_of_emps += 1

    def emailAddress(self):
        return self.email


    def __repr__(self):
        return '{} {} is paid {} Tk.'.format(self.first, self.last, self.pay)

    def raise_amount(self):
        self.pay = self.pay * self.raise_amount

class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang = 'Java'):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

    def __repr__(self):
        return '{} {}'.format(self.first, self.last)


class Manager(Employee):

    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)


    def delete_amp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        print('Employees of ' + '{} {}:'.format(self.first, self.last))
        for emp in self.employees:
            print('-->', end='')
            print(emp, end='')
            print()




dev1 = Developer('Test', 'Devs001', 60000)

mgr1 = Manager('Farhan', 'Utshaw', 100000, [dev1])


mgr1.print_emp()

# isinstance() --> if an object is an instance of a class
# issubclass() --> if a class is a subclass of another



