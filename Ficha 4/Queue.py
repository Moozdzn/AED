
class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self,item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def reverse(self):
        self.items.reverse()
    def __str__(self):
        string = ""
        for item in self.items:
                string = string + item + " "
        return string
    def list2Queue(self,items):
        q = Queue()
        for x in items:
            q.enqueue(x)
        return print(q)
