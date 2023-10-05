# Transfer knight class to another file
knight_moves = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
bishop_moves = [(1,1), (1, -1), (-1, 1), (-1, -1)]
is_no_threat = True


class Knight:
    def __init__(self):
        pass

    def take_input(self) -> int:
        nums = input('Please enter location: X Y: ')
        x, y = map(int, nums.split())
        return x, y 

    def is_valid_position(self, x : int, y : int) -> int:
        return 0 <= x <= 8 and 0 <= y <= 8

    def print_available_moves(self, x : int, y : int):
        ind = 0
        res = {}
        for dx, dy in knight_moves:
            new_x, new_y = x + dx, y + dy
            if self.is_valid_position(new_x, new_y):
                res[ind] = new_x, new_y
                ind += 1
        for i in res:
            print(res[i])


class Chess:
    def __init__(self):
        pass

    def take_input(self) -> dict:
        chessmen = {}
        loc_1 = input('Please enter location of the first chessmen : X Y: ')
        type_1 = input('Please enter the type of the first chessmen (b,k,r) : ')
        loc_2 = input('Please enter location of the second chessmen: X Y: ')
        type_2 = input('Please enter the type of the second chessmen (b,k,r) : ')
        if loc_1 == loc_2:
            print('Chessmen positions should not be identical')
            return False
        if type_1 == 'k':
            type_1 = 'knight'
        elif type_1 == 'b':
            type_1 = 'bishop'
        else:
            type_1 = 'rook'

        if type_2 == 'k':
            type_2 = 'knight'
        elif type_2 == 'b':
            type_2 = 'bishop'
        else:
            type_2 = 'rook'
        chessmen[type_1] = loc_1
        chessmen[type_2] = loc_2
        print(chessmen)
        return chessmen

    def check_chessman(self, chessmen : dict) -> bool:
        if len(chessmen) < 2:
            print('Chessmen should be different from each other')
            return False
        return True

    def is_valid_position(self, chessmen : dict) -> bool:
        for piece, position in chessmen.items():
            x, y = map(int, position.split())
            if not (0 <= x <= 8 and 0 <= y <= 8):
                return False
        return True

    def check_bishop(self, chessmen : dict):
        global is_no_threat
        for i in chessmen:
            if i == 'bishop':
                x_b, y_b = map(int, chessmen[i].split())
            else:
                type_o = i
                x_o, y_o = map(int, chessmen[i].split())
        for dx, dy in bishop_moves:
            new_x, new_y = x_b, y_b
            while 0 <= new_x <= 8 or 0 <= new_y <= 8:
                new_x += dx
                new_y += dy
                if new_x == x_o and new_y == y_o:
                    print(f'bishop threat {type_o}')
                    is_no_threat = False
                    break

    def check_rook(self, chessmen : dict):
        global is_no_threat
        for i in chessmen:
            if i == 'rook':
                x_r, y_r = map(int, chessmen[i].split())
            else:
                type_o = i
                x_o, y_o = map(int, chessmen[i].split())
        if x_r == x_o or y_r == y_o:
            print(f'rook threat {type_o}')
            is_no_threat = False

    def check_knight(self, chessmen : dict):
        global is_no_threat
        for i in chessmen:
            if i == 'knight':
                x_k, y_k = map(int, chessmen[i].split())
            else:
                type_o = i
                x_o, y_o = map(int, chessmen[i].split())
        for dx, dy in knight_moves:
            new_x, new_y = x_k + dx, y_k + dy
            if new_x == x_o and new_y == y_o:
                print(f'knight threat {type_o}')
                is_no_threat = False
                break
            else:
                break

# knightcommands =
a = Knight()
print("This program reads two intergers which \n represent the knight's location on the chess board")
x, y = a.take_input()
if a.is_valid_position(x, y):
    a.print_available_moves(x, y)
else:
    print('Input is illegal')

# chess commands =
# a = Chess()
# print("This program reads two intergers which \n represent the knight's location on the chess board")
# chessmen = a.take_input()
# if chessmen:
#     if a.is_valid_position(chessmen):
#         if a.check_chessman(chessmen):
#             for i in chessmen:
#                 if is_no_threat:
#                     if i == 'knight':
#                         a.check_knight(chessmen)
#                     elif i == 'rook':
#                         a.check_rook(chessmen)
#                     else:
#                         a.check_bishop(chessmen)
#             if is_no_threat:
#                 print('no threat')
#     else:
#         print('Position is not legal')