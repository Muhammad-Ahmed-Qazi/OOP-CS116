class Time:
    def __init__(self, h=0, m=0, s=0):
        self.hours = h
        self.minutes = m
        self.seconds = s
        self.formatTime()
        
    def formatTime(self):
        if self.seconds >= 60:
            spareMin = self.seconds // 60
            self.minutes += spareMin
            self.seconds -= spareMin * 60
        if self.minutes >= 60:
            spareHr = self.minutes // 60
            self.hours += spareHr
            self.minutes -= spareHr * 60
    
    def printTime(self):
        print(f"{f'0{self.hours}' if len(str(self.hours)) == 1 else self.hours}:{f'0{self.minutes}' if len(str(self.minutes)) == 1 else self.minutes}:{f'0{self.seconds}' if len(str(self.seconds)) == 1 else self.seconds}")

    def addTime(self, t):
        self.hours += t.hours
        self.minutes += t.minutes
        self.seconds += t.seconds
        self.formatTime()

t1 = Time(5, 59, 1)
t1.printTime()
t2 = Time(0, 1, 0)
t1.addTime(t2)
t1.printTime()