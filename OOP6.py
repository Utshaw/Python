
# getter, setter, deleter

# to use a method as an attribute use @property attribute


class Employee:

    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_of_emps += 1

    # access email like property
    @property
    def email(self):
        return self.first.lower() + '.' + self.last.lower() + '@email.com'



    def emailAddress(self):
        return self.email

    @property
    def fullName(self):
        return '{} {}'.format(self.first, self.last)

    @fullName.setter
    def fullName(self, name):
        first, last = name.split()
        self.first = first
        self.last = last

    @fullName.deleter
    def fullName(self):
        print('Delete FullName!')
        self.first = None
        self.last = None


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



emp1 = Employee('Farhan', 'Utshaw', 50000)

emp1.first = 'Tanvir'

emp1.fullName = 'FARHAN TANVIR'

print(emp1.email) # farhan.tanvir@email.com

del emp1.fullName # Delete FullName!

















