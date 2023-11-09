class Room():
    def __init__(self, size : int, num_of_windows : float, directions : list) -> None:
        self.dir_list = ['west', 'east', 'south', 'north']
        self.size = size
        self.num_of_windows = num_of_windows
        for direct in directions:
            if direct.lower() not in self.dir_list:
                raise ValueError("not a valid direction")
        self.directions = directions

    def __repr__(self) -> str:
        return f'size : {self.size} m^2, num of windows : {self.num_of_windows}, directions : {self.directions}'

    def get_rent_price(self) -> int :
        return int((self.size + (self.num_of_windows / 2)) * 80)
    
class MeetingRoom(Room):
    def __init__(self, size, num_of_windows, directions, table_size : int):
        super().__init__(size,num_of_windows,directions)
        self.table_size = table_size


    def __repr__(self) -> str:
        new_repr = super().__repr__() + f' table size : {self.table_size}'
        return new_repr
    
    def get_rent_price(self) -> int :
        return int(Room.get_rent_price(self) + (self.table_size * 7))
    
class Building:
    def __init__(self, rooms, addres):
        self.rooms = rooms
        self.addres = addres

    def __repr__(self):
        s = f'Addres: {self.addres} \n'
        rooms_sorted = sorted(self.rooms, key=lambda r:r.size, reverse=True)
        for room in rooms_sorted:
            s += room.__repr__() + "\n"
        return s[:-1]
    
    def get_room_by_budget(self, budget):
        self.budget_rooms = []
        for room in self.rooms:
            if room.get_rent_price() <= budget:
                self.budget_rooms.append(room.get_rent_price())
        print(self.budget_rooms)

    def get_meeting_room_by_occupancy(self, occupancy):
        self.occupancy_rooms = []
        for room in self.rooms:
            if isinstance(room ,MeetingRoom):
                if room.table_size <= occupancy:
                    self.occupancy_rooms.append(room)
        print(self.occupancy_rooms)
        

r1 = Room(122.3, 4,['West'])
r2 = Room(120, 4,['West'])
r3 = MeetingRoom(127, 4,['West'], 40)
b = Building([r1,r2,r3], "Hativat Harel 10")
print(b)
b.get_room_by_budget(10000)
b.get_meeting_room_by_occupancy(30)