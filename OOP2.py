
# class variables are shared among all instances of a class
# class methods are accessed like: class_name.var_name


class Employee:

    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_of_emps += 1


    def __repr__(self):
        return '{} {}'.format(self.first, self.last)

    def raise_amount(self):
        self.pay = self.pay * self.raise_amount

print(Employee.num_of_emps)

emp1 = Employee('Farhan', 'Utshaw', 1500) # emp1 is instance variable
emp2 = Employee('Test', 'User', 5566)



print(emp1)

print(emp2)

print(Employee.num_of_emps)