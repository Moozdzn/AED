from Queue import Queue
import random

class Printer:
    def __init__(self,ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0
    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self,newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60/self.pagerate

class Task:
    def __init__(self,time):
        self.timestamp = time
        self.pages = random.randrange(1,21)   

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self,currenttime):
        return currenttime - self.timestamp

def simulation(numSeconds, pagesPerMinute, stud = None , implem = None):
    
    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):
        
        if newPrintTask(stud, implem):
            task = Task(currentSecond)
            printQueue.enqueue(task)
        
        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)
        labprinter.tick()

    averageWait = sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining." % (averageWait,printQueue.size()))

def newPrintTask(stud, implem):
    num = random.randrange(1,181)
    numA = random.randrange(1,91)
    numB = random.randrange(1,361)
    if stud is None:
        if implem != None:
            if implem == 'A':
                if numA == 90:
                    return True
                else:
                    return False
            if implem == 'B':
                if numB == 360:
                    return True
                else:
                    return False
        else:
            if num == 180:
                return True
            else:
                return False
    else:
        tasksPerSec = int(3600/stud)
        numC = random.randrange(1,tasksPerSec + 1)
        if numC == tasksPerSec:
            return True
        else:
            return False

for i in range(10):
    simulation(3600,10,20)