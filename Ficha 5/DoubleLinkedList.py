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
        while current is not None:
            if current.getData() == item:
                if current.getPrev() == None:
                    self.head = current.getNext()
                    current = self.head
                    current.setPrev(None)
                else:
                    if current.getNext() == None:
                        current = current.getPrev()
                        current.setNext(None)
                    else:
                        current.getNext().setPrev(current.getPrev())
                        current.getPrev().setNext(current.getNext())
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

def test_DLL():

    print("CREATING EMPTY DOUBLY LINKED LIST")
    my_dLL = DoubleLinkedList()
    print("my_DL_list =", my_dLL)
    print("The Doubly linked list is empty?", my_dLL.isEmpty())
    print("List size:", my_dLL.size())

    add_items = [31, 77, 17, 27]
    print("\nADDING ITEMS", add_items)
    for item in add_items:
        # print("Adding item", item, end="   ")
        my_dLL.add(item)
        # print("my_list =", my_list)

    remove_items = [17, 31, 27, 77]
    print("\nREMOVING ITEMS", remove_items)
    for item in remove_items:
        print("my_DL_list =", my_dLL)
        print("Removig item", item)
        my_dLL.remove(item)

    print("my_DL_list =", my_dLL)
    print("size = ", my_dLL.size())

    print("\nADDING, INSERTING and APPENDING ITEMS", add_items)
    item = 10
    print("\nAppending item", item)
    my_dLL.append(item)
    print("my_dLL = ", my_dLL)
    print("size = ", my_dLL.size())

    item = 11
    print("\nAppending item", item)
    my_dLL.append(item)
    print("my_dLL = ", my_dLL)
    print("size = ", my_dLL.size())

    item = 9
    print("\nAdding item", item)
    my_dLL.add(item)
    print("my_dLL = ", my_dLL)
    print("size = ", my_dLL.size())

    item = 12
    pos = 2
    print("\nInserting item", item, "at position", pos)
    my_dLL.insert(2, item)
    print("my_dLL = ", my_dLL)
    print("size = ", my_dLL.size())

    item = 13
    pos = 0
    print("\nInserting item", item, "at position", pos)
    my_dLL.add(item)
    print("my_dLL = ", my_dLL)
    print("size = ", my_dLL.size())

    item = 15
    pos = my_dLL.size()
    print("\nInserting item", item, "at position", pos)
    my_dLL.insert(pos, item)
    print("my_dLL = ", my_dLL)
    print("size = ", my_dLL.size())


    print("\nPOPPING ITEMS")

    print("\nPop() - Last Item")
    print("Item:", my_dLL.pop())
    print("my_DL_list =", my_dLL)

    print("\nPop(0) - First Item")
    print("Item:", my_dLL.pop(0))
    print("my_DL_list =", my_dLL)

    print("\nPop(1) - Second Item")
    print("Item:", my_dLL.pop(1))
    print("my_DL_list =", my_dLL)

if __name__ == "__main__":
    test_DLL()
