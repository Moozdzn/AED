from Deque import Deque

def palChecker(string):
    d = Deque()
    for x in string:
        d.add_rear(x)
    while True:
        if d.size() == 1 or d.size() == 0:
            print('É palíndromo')
            break
        else:
            front = d.pop_front()
            rear = d.pop_rear()
            if front != rear:
                print('Não é palíndromo')
                break
b = 'I PREFER PI'
palChecker(b.replace(' ',''))
