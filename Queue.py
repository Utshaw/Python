
class Queue:

    def __init__(self):
        self.items = []

    def dequeue(self):
        return self.items.pop(0) if len(self.items) != 0 else '-1'

    def enqueue(self, item):
        self.items.append(item)

    def len(self):
        return len(self.items)


n_queue = int(input())
q = Queue()
i = 0
while i < n_queue:
    l = list(map(str, input().split()))
    if len(l) == 2:
        q.enqueue(l[1])
        print( q.len())
    else:
        print(q.dequeue(), q.len())
    i += 1
