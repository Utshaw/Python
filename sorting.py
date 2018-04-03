
li = [9,1,8,2,7,3,6,4,5]

s_li = sorted(li) # returns a new sorted list

print('Sorted List: ', s_li )
print('Original List: ', li )

li.sort() # sort() sorts the list in place and returns None
print('Original List: ', li )

r_list = sorted(li, reverse=True)
print('Reverse Sorted List ', r_list)

dict = {'roll': 1505105, 'name': 'Utshaw'}

print(sorted(dict)) # returns a list of sorted key's


# using key parameter for sorting in desired order
li = [-6, -5, -4, 3, 2, 1]
s_li = sorted(li, key=abs)
print(s_li) # [1, 2, 3, -4, -5, -6]

class Employee:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return self.name

    def __repr__(self):
        return '{} aged {} is paid {} Tk.'.format(self.name, self.age, self.salary)


# using this key in sorted() results in sorting according to age
def e_sort(emp):
    return emp.age



emp1 = Employee('Utshaw', 16, 60000)
emp2 = Employee('Tanvir', 17, 50000)
emp3 = Employee('Farhan', 18, 80000)

employees = [emp1, emp2, emp3]

print(sorted(employees, key=e_sort))


from operator import attrgetter

print(sorted(employees, key=attrgetter('age')))



