class Time1:
    def __init__(self, h : int, m : int):
        if 0 <= h <= 23:
            self.int_hour = h
        else:
            self.int_hour = 0
        if 0 <= m <= 59:
            self.int_minute = m
        else:
            self.int_minute = 0

    def __eq__(self, other) -> bool:
        if isinstance(other, Time1) == False:
            return False
        
        other = Time1(other)

        return (self.int_hour == other.int_hour and self.int_minute == other.int_minute)

# ///////////// Get Methods ///////////////

    def getHour(self):
        print(self.int_hour)

    def getMinute(self):
        print(self.int_minute)

# ///////////// Set Methods ///////////////
    
    def setHour(self, nums : int):
        if 0 <= nums <= 23:
            self.int_hour = nums

    def setMinute(self, nums : int):
        if 0 <= nums <= 59:
            self.int_minute = nums

    def toString(self):
        if self.int_hour >= 10:
            if self.int_minute >= 10:
                print(f'{self.int_hour}:{self.int_minute}')
            else:
                print(f'{self.int_hour}:0{self.int_minute}')
        else:
                if self.int_minute >= 10:
                    print(f'0{self.int_hour}:{self.int_minute}')
                else:
                    print(f'0{self.int_hour}:0{self.int_minute}')

    def minFromMidnight(self):
        print(self.int_hour * 60 + self.int_minute)

    def equals(self, x):
        pass


        
a = Time1(5,3)
a.getHour()
a.getMinute()
a.setHour(3)
a.getHour()
a.toString()
a.minFromMidnight()


