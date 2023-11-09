# //////////// Part 1  ///////////////

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
        self.int_hour = other.int_hour
        self.int_minute = other.int_minute

# ///////////// Get Methods ///////////////

    def getHour(self) -> int :
        return self.int_hour

    def getMinute(self) -> int:
        return self.int_minute

# ///////////// Set Methods ///////////////
    
    def setHour(self, nums : int):
        if 0 <= nums <= 23:
            self.int_hour = nums

    def setMinute(self, nums : int):
        if 0 <= nums <= 59:
            self.int_minute = nums

    def toString(self) -> str:
        if self.int_hour >= 10:
            if self.int_minute >= 10:
                return f'{self.int_hour}:{self.int_minute}'
            else:
                return f'{self.int_hour}:0{self.int_minute}'
        else:
                if self.int_minute >= 10:
                    return f'0{self.int_hour}:{self.int_minute}' 
                else:
                    return f'0{self.int_hour}:0{self.int_minute}'

    def minFromMidnight(self) -> int :
        return self.int_hour * 60 + self.int_minute
    
    def equals(self, hours : int, minutes : int) -> bool :
        if self.int_hour == hours and self.int_minute == minutes:
            return True
        return False
    
    def before(self, other) -> bool:
        if self.int_hour < other.int_hour:
            return True
        if self.int_hour == other.int_hour:
            if self.int_minute < other.int_minute:
                return True
        return False
    
    def after(self,other) -> bool:
        if self.before(other):
            return False
        if self.int_hour == other.int_hour and self.int_minute == other.int_minute:
            return False
        return True 
    
    def difference(self, other) -> int:
        if self.after(other):
            return (self.int_hour - other.int_hour) * 60 + (self.int_minute - other.int_minute)
        
    def addMinutes(self, num : int): 
        other_hour = self.int_hour
        other_minute = self.int_minute + num
        while other_minute >= 60:
            other_minute -= 60
            other_hour += 1
        while other_hour >= 24:
            other_hour -= 24
        other = Time1(other_hour, other_minute)
        return other 

# //////////// Part 1 commands ///////////////

# a = Time1(23,32)
# print(a.getHour())
# b = Time1(7,30)
# # a == b
# print(a.getHour())
# print(a.toString())
# print(a.minFromMidnight())
# print(a.equals(7,31))
# print(a.before(b))
# print(a.after(b))
# print(a.difference(b))
# print(a.addMinutes(70).toString())

# //////////// Part 2 ///////////////

class Time2():
    def __init__(self, h : int, m : int) -> None:
        if not 0 <= h <= 23:
            h = 0
        if not 0 <= m <= 59:
            m = 0
        self.int_min_fromMid = h * 60 + m

    def __eq__(self, other) -> bool:
        if isinstance(other, Time2) == False:
            return False
        self.int_min_fromMid = other.int_min_fromMid


# ///////////// Get Methods ///////////////

    def getHour(self) -> int :
        return self.int_min_fromMid // 60

    def getMinute(self) -> int:
        return self.int_min_fromMid % 60

# ///////////// Set Methods ///////////////

    def setHour(self, nums : int):
        if 0 <= nums <= 23:
            self.int_min_fromMid = self.int_min_fromMid - (self.getHour() * 60) + (nums * 60)

    def setMinute(self, nums : int):
        if 0 <= nums <= 59:
            self.int_min_fromMid = self.int_min_fromMid - self.getMinute() + nums

    def minFromMidnight(self) -> int :
        return self.int_min_fromMid
    
    def equals(self, other) -> bool :
        if self.int_min_fromMid == other.int_min_fromMid:
            return True
        return False
    
    def before(self, other) -> bool:
        if self.int_min_fromMid < other.int_min_fromMid:
            return True
        return False
    
    def after(self,other) -> bool:
        if self.before(other):
            return False
        if self.int_min_fromMid == other.int_min_fromMid:
            return False
        return True 
    
    def difference(self, other) -> int:
        if self.after(other):
            return self.int_min_fromMid - other.int_min_fromMid

    def toString(self) -> str:
        if self.getHour() >= 10:
            if self.getMinute() >= 10:
                return f'{self.getHour()}:{self.getMinute()}'
            else:
                return f'{self.getHour()}:0{self.getMinute()}'
        else:
                if self.getMinute() >= 10:
                    return f'0{self.getHour()}:{self.getMinute()}' 
                else:
                    return f'0{self.getHour()}:0{self.getMinute()}' 

    def addMinutes(self, num : int): 
        self.int_min_fromMid += num
        other_hour = self.getHour()
        other_minute = self.getMinute()
        while other_hour >= 24:
            other_hour -= 24
        other = Time2(other_hour, other_minute)
        return other 

# //////////// Part 2 commands ///////////////

# a = Time2(7,60)
# print(a.int_min_fromMid)
# b = Time2(3,20)
# a == b
# print(a.int_min_fromMid)
# print(a.getHour())
# print(a.getMinute())
# a.setHour(23)
# a.setMinute(30)
# print(a.int_min_fromMid)
# print(a.equals(b))
# print(a.before(b))
# print(a.after(b))
# print(a.difference(b))
# print(a.addMinutes(32).toString())

# //////////// Part 3 ///////////////
class Flight():
    def __init__(self, origin : str , destination : str, h : int, m : int, flight_duration : int, nof_passengers : int , price : int) -> None:
        self.MAX_CAPACITY = 250
        self.origin = origin 
        self.destination = destination
        self.departure = Time1(h,m)
        if flight_duration < 0:
            flight_duration = 0
        else:
            self.flight_duration  = flight_duration
        self.nof_passengers = nof_passengers 
        self.isfull = self.define_isfull()
        if price < 0:
            price = 0
        else:    
            self.price = price

    def define_isfull(self):
        if self.MAX_CAPACITY < self.nof_passengers:
            return True
        elif self.nof_passengers < 0:
            return 0
        elif self.MAX_CAPACITY - self.nof_passengers: 
            return False
        return True

    def __eq__(self, other) -> bool:
        self.origin = other.origin 
        self.destination = other.destination
        self.departure = other.departure
        self.flight_duration  = other.flight_duration
        self.nof_passengers = other.nof_passengers 
        self.isfull = other.isfull
        self.price = other.price

    def equals(self,other):
        return vars(self) == vars(other)
    
    def getArrivalTime(self) -> str:
        return self.departure.addMinutes(self.flight_duration).toString()
    
    def addPassengers(self, num : int) -> bool:
        if (self.nof_passengers + num) > self.MAX_CAPACITY:
            return False
        if (self.nof_passengers + num) <= self.MAX_CAPACITY:
            self.nof_passengers += num
            self.isfull = self.define_isfull()
            return True
    def isCheaper(self, other) -> bool:
        if self.price < other.price:
            return True
        return False
    
    def totalPrice(self) -> int:
        return self.price * self.nof_passengers
    
    def landsEarlier(self, other) -> bool:
        if self.departure.minFromMidnight() < other.departure.minFromMidnight():
            return True
        return False
    
    def toString(self):
        if self.isfull:
            is_itfull = 'full'
        else: 
            is_itfull = 'not full'
        return f'Flight from: {self.origin} to: {self.destination} departs at {self.departure.toString()}, Flight is {is_itfull}'

# //////////// Part 2 commands ///////////////

# a = Flight('Modiin', 'Amsterdam', 7, 2, 260, 260, 300)
# print(a.isfull)
# b = Flight('Modiin', 'Tel Aviv', 23, 2, 240, -1, 301)
# a == b
# print(f' A destination: {a.destination}')
# print(f' A equal B: {a.equals(b)}')
# print(f'Arrival time: {a.getArrivalTime()}')
# print(f'Add passengers : {a.addPassengers(10)}')
# print(f'A is cheaper : {a.isCheaper(b)}')
# print(f'Total price: {a.totalPrice()}')
# print(f'Landing earlier: {a.landsEarlier(b)}')
# a.toString()
