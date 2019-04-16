from Queue import Queue
from random import randint

def playA(nameList, count):
    q = Queue()
    for x in nameList:
        q.enqueue(x)
    while q.size() > 1:
        for i in range(count):
            q.enqueue(q.dequeue())
        q.dequeue()
    return q.dequeue()

def playB():
    nrPlayers = int(input('Quantos jogadores? '))
    q = Queue()
    for x in range(nrPlayers):
        name = input('Nome do jogador: \n')
        q.enqueue(name)
    count = int(input('Nr até a batata rebentar: \n'))
    while q.size() > 1:
        for i in range(count):
            q.enqueue(q.dequeue())
        q.dequeue()
    return q.dequeue()

def playC():
    nrPlayers = int(input('Quantos jogadores? '))
    q = Queue()
    for x in range(nrPlayers):
        name = input('Nome do jogador: \n')
        q.enqueue(name)
    while q.size() > 1:
        count = randint(0,9)
        for i in range(count):
            q.enqueue(q.dequeue())
        q.dequeue()
    return q.dequeue()

my_list = ['Diogo','Andre','Hugo', 'Francisco','joao']
print(playA(my_list,2))
print(playB())
print(playC())
