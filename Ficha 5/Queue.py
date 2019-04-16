from LinkedLists import LinkedList

class Queue:
    def __init__(self):
        self.items = LinkedList()
    def enqueue(self, item):
        return self.items.add(item)
    def dequeue(self, item):
        return self.items.pop()
    def isEmpty(self):
        return self.items.isEmpty()
    def size(self):
        return self.items.size()    