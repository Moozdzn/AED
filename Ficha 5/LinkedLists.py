class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self, newdata):
        self.data = newdata
    def setNext(self,newnext):
        self.next = newnext

class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0
    def isEmpty(self):
        return self.head == None
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        print(count)
        return count
    def sizeCount(self):
        print(self.count)
        return self.count
    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        self.count += 1
    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                if previous == None:
                    self.head = current.getNext()
                elif current != None:
                    previous.setNext(current.getNext())
                self.count -= 1
            previous = current
            current = current.getNext()
            if current == None:
                print('Item not currently in list, non-existant or removed')
                found = True
    def append(self,item):
        current = self.head
        previous = None
        while current.getNext() != None:
            previous = current
            current = current.getNext()
        n = Node(item)
        current.setNext(n)
        self.count += 1
    def index(self,item):
        current = self.head
        found = False
        count = -1
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
            count += 1
        if found:
            return count
        else:
            return 'Item not in list'

    def insert(self,pos,item):
        current = self.head
        previous = None
        for i in range(pos):
            previous = current
            current = current.getNext()
        n = Node(item)
        if previous == None:
            n.setNext(current)
            self.head = n
        else:
            n.setNext(previous.getNext())
            previous.setNext(n)
        self.count +=1

    def pop(self, pos = None):
        current = self.head
        previous = None
        if pos is None:
            while current.getNext() != None:
                previous = current
                current = current.getNext()

            if previous == None:
                self.head = None
                self.count -= 1
                return current.getData()
            else:
                previous.setNext(current.getNext())
                self.count -= 1
                return current.getData()
        else:
            for i in range(pos):
                previous = current
                current = current.getNext()
            if previous == None:
                self.head = current.getNext()
                self.count -= 1
                return current.getData()
            else:
                previous.setNext(current.getNext())
                self.count -= 1
                return current.getData()
            if current == None:
                print('Item not currently in list, non-existant or removed')
            return current.getData()


    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found
    def copy(self):
        l = LinkedList()
        current = self.head
        while current.getNext() is not None:
            l.append(current.getData())
            current = current.getNext()
        return l
    def concatenate(self, b):
        current = self.head
        currentB = b.head
        count = b.count
        while current.getNext() is not None:
            current = current.getNext()
        current.setNext(currentB)
        self.count += count

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
my_list = LinkedList()
my_list.add(5)
my_list.add(3)
my_list.add(5)
my_list.add(4)
my_list.add(5)
my_list.add(6)
my_list.add(5)

my_list.add(5)
my_list.add(2)
print(my_list)
my_list.remove(5)
print(my_list)
