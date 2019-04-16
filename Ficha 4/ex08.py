#CHANGE the folowing line to import your QUEUE implementation
from Queue import Queue

def process(q, a, b):
    # REMOVE the following line
    # INSERT you code HERE
    while q.isEmpty() == False:
        char = q.dequeue()
        name = q.dequeue()

        if char == 'A' or char == 'a':
            a.enqueue(name)
        elif char == 'B' or char == 'b':
            b.enqueue(name)
        elif char == 'X' or char == 'x':
            if a.size() > b.size():
                print('teste1')
                b.enqueue(name)
            elif a.size() < b.size():
                print('teste2')
                a.enqueue(name)
            else:
                a.enqueue(name)
        else:
            print('Este input está errado: %s' % char)


def read_int():
    while True:
        try:
            n = int(input("Número de nomes --> "))
            if n >= 1:
                return n
            else:
                print("Ops! O número tem de ser um inteiro positivo")
        except ValueError:
            print("Ops! O número tem de ser um inteiro positivo")

def main ():

    q = Queue()
    a = Queue()
    b = Queue()

    n = read_int()

    for i in range(0, n):

        nome_operacao = input("Nome e Operação (separados por espaço) --> ")
        nome_operacao = nome_operacao.split()

        q.enqueue(nome_operacao[1])
        q.enqueue(nome_operacao[0])

    print("Início:")
    print("q: ", q)
    print("a: ", a)
    print("b: ", b)

    process(q, a, b)

    print("-------------------------------")
    print("q: ", q)
    print("a: ", a)
    print("b: ", b)

if __name__ == "__main__":
    main()
