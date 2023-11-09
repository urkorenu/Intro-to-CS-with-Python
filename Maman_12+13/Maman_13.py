from Maman_12 import Flight

class Airport():
    def __init__(self,city : str) -> None:
        self.MAX_FLIGHTS = 200
        self.flightSchedule = []
        self.noOfFlights = 0
        self.city = city    

# ///////////// Set Methods ///////////////

    def addFlight(self, flight : Flight) -> bool :
        if flight.destination is 'Modiin' or flight.origin is 'Modiin':
            self.flightSchedule.append(flight)
            return True
        return False
    
    def removeFlight(self, flight : Flight) -> bool :
        if flight in self.flightSchedule:
            self.flightSchedule.remove(flight)
            return True
        return False
    
# ///////////// Get Methods ///////////////

    def firstFlightFromOrigin(self,place : str):
        first_flight_time = 10000
        first_flight = 0
        for cur_flight in self.flightSchedule:
            if cur_flight.origin is place:
                if cur_flight.departure.minFromMidnight() < first_flight_time:
                    first_flight = cur_flight
                    first_flight_time = cur_flight.departure.minFromMidnight()
        if first_flight is 0:
            return None
        return first_flight.toString()
    
    def howManyFullFlights(self) -> int:
        temp = 0
        for cur_flight in self.flightSchedule:
            if cur_flight.isfull:
                temp += 1
        return temp
    
    def howManyFlightsBetween(self, place : str) -> int:
        temp = 0
        for cur_flight in self.flightSchedule:
           if cur_flight.destination is place or cur_flight.origin is place: 
               temp += 1
        return temp
               
    def mostPopularDestination(self):
        destinations = {}
        for cur_flight in self.flightSchedule:
            if cur_flight.destination in destinations:
                destinations[cur_flight.destination] = destinations[cur_flight.destination] + 1
            else:
                destinations[cur_flight.destination] = 1
        max_key = [key for key, value in destinations.items() if value == max(destinations.values())]
        if max_key == []:
            return None
        return max_key[0]

    def mostExpensiveTicket(self):
        if self.flightSchedule == []:
            return None
        max_price = max(self.flightSchedule, key=lambda node: node.price)
        return max_price

    def longestFlight(self):
        if self.flightSchedule == []:
            return None
        max_duration = max(self.flightSchedule, key=lambda node: node.flight_duration)
        return max_duration
    
    def toString(self):
        if self.flightSchedule == []:
            return None
        string = ''
        for flight in self.flightSchedule:
            string += flight.toString()
            string += '\n'
        print(f'string: {string}')
        return f'The flights for airport {self.city} today are \n' + string[:-1]

a = Flight('Modiin', 'Amsterdam', 7, 2, 260, 260, 255)
b = Flight('Modiin', 'Tel Aviv', 23, 2, 240, 250, 260)
airport = Airport('Modiin')
print(f'Add flight: {airport.addFlight(a)}')
print(f'Add flight: {airport.addFlight(b)}')
print(f'Flight schedule: {airport.flightSchedule}')
# print(f'Remove flight {airport.removeFlight(b)}')
print(f'First flight: {airport.firstFlightFromOrigin("Modiin")}')
print(f'Full flights {airport.howManyFullFlights()}')
print(f'Flight between :{airport.howManyFlightsBetween("Modiin")}')
print(f'Most popular destination: {airport.mostPopularDestination()}')
print(f'Most Expensive ticket: {airport.mostExpensiveTicket()}')
print(f'Longest flight : {airport.longestFlight()}')
print(airport.toString())