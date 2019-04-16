#CHANGE the folowing line to import your QUEUE implementation
from Queue import Queue

def merge(a, b):
    q = Queue()
    while not a.isEmpty() or not b.isEmpty():
        strA = a.dequeue()
        strB = b.dequeue()
        if strA < strB:
            q.enqueue(strA)
        elif strA > strB:
            q.enqueue(strB)
        elif a.isEmpty() and not b.isEmpty():
            q.enqueue(b.dequeue())
        elif b.isEmpty() and not a.isEmpty():
            q.enqueue(a.dequeue())
        else:
            q.enqueue(strB)
    return q

def main():

    a = Queue()
    b = Queue()

    items = input("Elementos da primeira fila (ordenados e separados por espaço) --> ")
    listA = items.split(' ')

    # INSIRA AQUI CÓDIGO PARA CRIAR A QUEUE a
    for x in listA:
        a.enqueue(x)
    a.reverse()

    items = input("Elementos da segunda fila (ordenados e separados por espaço) --> ")
    listB = items.split(' ')

    # INSIRA AQUI CÓDIGO PARA CRIAR A QUEUE a
    for x in listB:
        b.enqueue(x)
    b.reverse()

    print("a: ", a)
    print("b: ", b)
    print("merge =", merge(a, b))


if __name__ == "__main__":
    main()
