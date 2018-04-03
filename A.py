
#immutable objects are fundamentally expensive to “change”, because doing so involves creating a copy. Changing mutable objects is cheap.

#Immutable are quicker to access than mutable objects.

#Mutable objects are great to use when you need to change the size of the object, example list, dict etc.. Immutables are used when you need to ensure that the object you made will always stay the same.



class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return 'No Food'
        return self.items.pop()

    def peek(self):
        return self.items[0]

    def size(self):
        return  len(self.items)


num_q = int(input())
i = 0
s = Stack()
while i < num_q:
    l = list(map(int, input().split()))
    if len(l) < 2:
        type = l[0]
        popped_item = s.pop()
        if popped_item == None:
            print('No Food')
        else:
            print()
    else:
        type, cost = l[0], l[1]
        s.push(cost)
    print(l)
    i+=1


















