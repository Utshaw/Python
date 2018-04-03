
# Magic/Duncer methods


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

    # add methods
    def __add__(self, other):
        return self.pay + other.pay

    # len() methods
    def __len__(self):
        return len(self.first + self.last)


emp1 = Employee('Farhan', 'Utsahw', 50000)

emp2 = Employee('Test', 'Developer', 60000)

print(emp1 + emp2)

print(len(emp2))








