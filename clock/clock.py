

class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minutes = minute
        self.calc()
            
    def __repr__(self):
        return self.calc()

    def __eq__(self, other):
        return repr(self) == repr(other)

    def __add__(self, minutes):
        self.minutes = int(self.minutes) + minutes
        return self.calc()

    def __sub__(self, minutes):
        self.minutes = int(self.minutes) - minutes
        return self.calc()

    def calc(self):
        self.hour = int(self.hour)
        self.minutes = int(self.minutes)
        while self.minutes<0:
            self.minutes += 60
            self.hour -= 1 
        
        while self.hour<0:
            self.hour += 24
        
        if self.minutes>60:
            self.minutes /= 60             
            self.hour += int(self.minutes)
            self.minutes = round(self.minutes % 1 * 60)
            
        while self.hour>=24:
            self.hour -= 24
            
        if self.minutes == 60:
            self.hour += 1
            self.minutes = 0
        #Adding the extra '0' on the left is the input is missing it
            
        self.minutes = "0" + str(self.minutes) if len(str(self.minutes))<2 else str(self.minutes)
        self.hour = "0" + str(self.hour) if len(str(self.hour))<2 else str(self.hour)
        
        return self.hour + ":" + self.minutes