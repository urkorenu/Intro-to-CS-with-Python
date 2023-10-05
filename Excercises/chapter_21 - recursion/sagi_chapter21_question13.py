# ----------------------------------------------------------------------------------------------------
# solution approach:
# given N stacks and a starting point (initial stack) 
# with M weights sorted in some order, we need to move all of the
# weights from the initial stack to a different stack so that we get
# a stack that is identical to the initial stack, but isnt the initial stack
#
# Lets split solution to cases:
#
# Case 1: we only have 2 stacks, and a single weight, psuedo code would be:
#   if initial stack is empty
#       if a non-initial stack is sorted with all weights in it:
#           done
#       else
#           try sorting one of the sta    
#
#   else if we can move a 
# ----------------------------------------------------------------------------------------------------

from enum import IntEnum
from typing import Union
from dataclasses import dataclass, field

# Enum: sort_order_enum
#
# An enum to represent the sort order of a list
class sort_order_enum(IntEnum):
    ASCENDING_ORDER = 0
    DECENDING_ORDER = 1

@dataclass(init=False)
# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
# -----------------------------------------------

class WeightedStack:
    count       : int
    nof_weights : int
    sort_order  : sort_order_enum
    stack       : list[int]
                                            
    def __init__(cls, nof_weights: int = 0, sort_order: sort_order_enum = sort_order_enum.DECENDING_ORDER.value, stack: list[int] = []):
        cls.nof_weights = nof_weights
        cls.sort_order  = sort_order
        cls.stack       = []

        if cls.nof_weights == 0:
            return
        
        for i in range(1, cls.nof_weights + 1):
            if (sort_order == sort_order_enum.ASCENDING_ORDER):
                cls.push_back(i)
            else:
                cls.push_front(i)
            
    def is_empty(cls) -> bool:
        return len(cls.stack) == 0

    def is_sorted(cls) -> bool:
        if (cls.size() <= 1):
            return True

        tmp = cls.stack
        tmp.sort(reverse=bool(cls.sort_order == sort_order_enum.DECENDING_ORDER.value))
        return tmp == cls.stack

    def is_fully_sorted(cls, total_nof_weights) -> bool:
        return cls.size() == total_nof_weights and cls.is_sorted

    def size(cls):
        return len(cls.stack)

    def peek_front(cls) -> int:
        if (cls.is_empty()):
            return 0
        
        return int(cls.stack[0])
    
    def peek_back(cls) -> int:
        if cls.is_empty():
            return 0
        
        return int(cls.stack[-1])

    def can_push_front(cls, item: int) -> bool:
        tmp = cls.peek_front()
        return (
            cls.is_empty() or
            (cls.sort_order == sort_order_enum.ASCENDING_ORDER.value and item <= tmp) or
            (cls.sort_order == sort_order_enum.DECENDING_ORDER.value and item >= tmp)
        )
    
    def can_push_back(cls, item: int) -> bool:
        tmp = cls.peek_back()
        return (
            cls.is_empty() or
            (cls.sort_order == sort_order_enum.ASCENDING_ORDER.value and item >= tmp) or
            (cls.sort_order == sort_order_enum.DECENDING_ORDER.value and item <= tmp)
        )

    def push_front(cls, item: int) -> bool:
        if (not cls.can_push_front(item)):
            return False
        
        cls.stack.insert(0, item)
        return True

    def push_back(cls, item: int) -> bool:
        if (not cls.can_push_back(item)):
            return False
        
        cls.stack.append(item)
        return True

    def pop_front(cls) -> Union[int, None]:
        if cls.is_empty():
            return None
        return cls.stack.pop(0)

    def pop_back(cls) -> Union[int, None]:
        if cls.is_empty():
            return None
        return cls.stack.pop(-1)

@dataclass(init=False)
class WeightedStacks:
    _nof_stacks     : int
    _nof_weights    : int
    _sort_order     : sort_order_enum
    _stacks          : list[WeightedStack]

    def __init__(cls, _nof_stacks: int = 3, _nof_weights: int = 5, _sort_order: sort_order_enum = sort_order_enum.DECENDING_ORDER.value, _stacks: list[WeightedStack] = []):
        if _nof_stacks < 3 or _nof_weights == 0:
            raise Exception
        
        cls._nof_stacks     = _nof_stacks
        cls._nof_weights    = _nof_weights
        cls._sort_order     = _sort_order
        cls._stacks          = []
        
        if (len(_stacks) != 0):
            cls._stacks = _stacks
            return
        
        cls._stacks.append(WeightedStack(nof_weights=_nof_weights, sort_order=_sort_order))

        for i in range(_nof_stacks - 1):
            cls._stacks.append(WeightedStack(nof_weights=0, sort_order=_sort_order))

    
    def size(cls) -> int:
        return len(cls._stacks)

    def are_sorted(cls) -> bool:
        if (cls.size() == 0 or not cls._stacks[0].is_empty()):
            return False
        
        for stack in cls._stacks:
            if stack.is_fully_sorted(cls._nof_weights):
                return True
            
        return False
    
    def move(cls, from_idx: int, to_idx: int) -> bool:
        if (cls._stacks[from_idx].size() == 0):
            return
        
        return cls._stacks[to_idx].push_back(cls._stacks[from_idx].pop_back())

    def weighted_sort(cls) -> bool:
        result = False

        if cls.are_sorted():
            return True
        
        for i in range(cls.size()):
            for j in range(cls.size()):
                if i == j:
                    continue

                tmp = cls
                if (not tmp.move(i, j)):
                    continue

                result = result or tmp.weighted_sort()

                if result:
                    return True

        return result




def weighted_sort_new(start, via, target, n, max_n):
    start.count += 1
    if (n == 0):
        if (start.is_fully_sorted(max_n) or via.is_fully_sorted(max_n) or target.is_fully_sorted(max_n)):
            print("Fully sorted")
            print(f"{start.name}:{start.stack}, {target.name}:{target.stack}, {via.name}:{via.stack}, n:{n}")
        return True

    # go in
    weighted_sort_new(start, target, via, n-1, max_n)

    # action
    print(f"{start.peek_back()} from {start.name} to {target.name}")
    target.push_back(start.pop_back())
    print(f"{start.name}:{start.stack}, {target.name}:{target.stack}, {via.name}:{via.stack}, n:{n}")

    # go in
    weighted_sort_new(via, start, target, n-1, max_n)
    



def main():
    nof_weights = int(input("enter nof weights: "))
    start = WeightedStack(nof_weights,sort_order=sort_order_enum.DECENDING_ORDER)
    via = WeightedStack(sort_order=sort_order_enum.DECENDING_ORDER)
    end = WeightedStack(sort_order=sort_order_enum.DECENDING_ORDER)
    start.name = "A"
    via.name = "B"
    end.name = "C"
    print("start")
    print("---------------------------------")
    print(f"{start.stack}")
    print("---------------------------------")
    weighted_sort_new(start, via, end, nof_weights, nof_weights)

if __name__ == '__main__':
    main()

# A | B | C |
#
# 3, 2, 1 | 0 | 0 |
#
# 3, 2 | 0 | 1 |
#
# 3 | 2 | 1 |
# 
# 3 | 2, 1 | 0 |
#
# 0 | 2, 1 | 3 |
#
# 1 | 2 | 3 |
# 1 | 0 | 3, 2 |
# 0 | 0 | 3, 2, 1 |