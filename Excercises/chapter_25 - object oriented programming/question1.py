class Room():
    def __init__(self, size : int, num_of_windows : int, air_directions : list) -> None:
        """
        Initiate Room class and validating the air directions.

        Args:
        - size(int) : Size of the room.
        - num_of_windows(int) : Number of windows in the room.
        - air_directions(list) : List of direction.    

        Returns:
        - None                           
        """
        self.dir_list       = ['west', 'east', 'south', 'north']
        self.size           = size
        self.num_of_windows = num_of_windows
        # Validate correct air directions
        for direction in air_directions:
            if direction.lower() not in self.dir_list:
                raise ValueError("not a valid direction")
        self.air_directions = air_directions

    def __repr__(self) -> str:
        return f'size : {self.size} m^2, num of windows : {self.num_of_windows}, directions : {self.air_directions}'

    def get_rent_price(self) -> int :
        return int((self.size + (self.num_of_windows / 2)) * 80)
    
class MeetingRoom(Room):
    def __init__(self, size : int, num_of_windows : int, directions : list, table_size : int) -> None:
        # Do the init of the the super class and then continues.
        super().__init__(size,num_of_windows,directions)
        self.table_size = table_size


    def __repr__(self) -> str:
        # Returns the repr of the super class and addons of this class.
        new_repr = super().__repr__() + f' table size : {self.table_size}'
        return new_repr
    
    def get_rent_price(self) -> int :
        return super().get_rent_price() + (self.table_size * 7)
    
class Building:
    def __init__(self, rooms : list, addres : str) -> None:
        self.rooms = rooms
        self.addres = addres

    def __repr__(self) -> str:
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
        return self.budget_rooms

    def get_meeting_room_by_occupancy(self, occupancy : int) -> list:
        self.occupancy_rooms = []
        for room in self.rooms:
            if isinstance(room ,MeetingRoom):
                if room.table_size >= occupancy:
                    self.occupancy_rooms.append(room)
        return self.occupancy_rooms
        

r1 = Room(122.3, 4,['West'])
r2 = Room(120, 4,['West'])
r3 = MeetingRoom(127, 4,['West'], 40)
b = Building([r1,r2,r3], "Hativat Harel 10")
print(b)
print(b.get_room_by_budget(10000))
print(b.get_meeting_room_by_occupancy(30))