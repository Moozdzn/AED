class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
        self.prev = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def getPrev(self):
        return self.prev
    def setData(self, newdata):
        self.data = newdata
    def setNext(self, newnext):
        self.next = newnext
    def setPrev(self, newprev):
        self.prev = newprev
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def isEmpty(self):
        return self.head == None
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count
    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        if self.isEmpty():
            self.head = temp
            self.tail = temp
        else:
            self.head.setPrev(temp)  
            self.head = temp            
    def remove(self,item):
        current = self.head
        found = False
        while not found:
            if current.getData() == item:
                current.getNext().setPrev(current.getPrev())
                current.getPrev().setNext(current.getNext())
                return
            current = current.getNext()   
    def append(self, item):
        n = Node(item)
        current = self.tail
        current.setNext(n)
        n.setPrev(current)
        n = self.tail
    def pop(self):
        current = self.tail
        self.tail = current.getPrev()
        self.tail.setNext(None)
    def insert(self,pos,item):
        #a = int(self.size()/2)
        current = self.head
        for i in range(pos):
            current = current.getNext()
        n = Node(item)
        n.setNext(current)
        n.setPrev(current.getPrev())
        current.getPrev().setNext(n)
        current.setPrev(n)
    def __str__(self):
        string = "["
        current = self.head
        while current != None:
            string += str(current.getData())    
            if current.getNext() != None:
                string += ', '
            current = current.getNext()
        if current == None:
                string += ']'        
        return string

my_list = DoubleLinkedList()
my_list.add(10)
my_list.add(20)
my_list.add(30)
my_list.remove(20)
print(my_list)
