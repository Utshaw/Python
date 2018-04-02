# regular methods vs class methods vs static methods

# regular methods automatically takes the instance as first argument ('self' name)

# by convention instance variable is called 'self'

# by convention class variables are called 'cls'

# class methods automatically takes the class as first argument ('cls' name)

# class variables are shared among all instances of a class
# class methods are accessed like: class_name.var_name

# static methods don't pass anything automatically

# Staticmethods are used to group functions which have some logical connection with a class to the class.





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

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


    @classmethod
    def set_raise_amount(cls, amount): # alternative constructor
        cls.raise_amount = amount # this impaces all instance's raise_amount variable


    # Staticmethods are used to group functions which have some logical connection with a class to the class.
    @staticmethod
    def is_workday(day):
        if day.weekday() == 3 or day.weekday() == 4:
            return False
        return True


    def __repr__(self):
        return '{} {} is paid {} Tk.'.format(self.first, self.last, self.pay)


emp1 = Employee('Farhan', 'Utshaw', 5600)
Employee.set_raise_amount(1.05) # this affects all instances
Employee.raise_amount = 2.00 # this affects all instances too

print(emp1.raise_amount)

emp2_str = 'John-Doe-60000'
emp2 = Employee.from_string(emp2_str)
print(emp1)

print(emp2)

import datetime

print(emp2.is_workday(datetime.date(2018, 4, 5)))

print(emp2.is_workday(datetime.date.today()))



