class Tracker:
    instanceCount = 0

    def __init__(self):
        Tracker.instanceCount += 1
        self.serialNo = Tracker.instanceCount
    
    def printSerialNo(self):
        print("Serial no:", self.serialNo)

t1 = Tracker()
t2 = Tracker()
t1.printSerialNo()
t2.printSerialNo()