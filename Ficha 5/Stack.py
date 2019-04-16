from LinkedLists import LinkedList

class Stack:
    def __init__(self):
        self.items = LinkedList()
    def isEmpty(self):
        return self.items.isEmpty()
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        temp = self.items.pop()
        self.items.append(temp)
        return temp
    def size(self):
        return self.items.size()