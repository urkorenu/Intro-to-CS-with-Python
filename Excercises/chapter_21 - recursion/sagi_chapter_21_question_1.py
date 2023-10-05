# ------------------------------------------------------------------------------------------------------- #
#
# ---------
# Question: 
# ---------
#   Given a number of stairs, and a maximum number of
#   steps that can be taken each time - Count the total
#   number of possible combinations to reach the top of 
#   the staircase.
#
# ------------------
# Solution Approach:
# ------------------
#   In the begining, there are N stairs.
#   In order to reach the top of the staircase, we can take 
#   between [1 to M] number of steps each time.
#   
#   Suppose we have a total of 1 stairs, and can take a maximum
#   number of 2 steps.
#  
#   we start at stair number 0, with 1 stairs remaining.
#
#   if we take 1 step ->    we now have 0 stairs remaining, therefore,
#                           we can say that 1 combination was found.
#
#   if we take 2 steps ->   it is not possible, we will have -1 
#                           remaining stairs, impossible.
#                           therefore the result for 2 steps
#                           would be 0 combinations.
#
#   Considering that example - we can already see that we need at least 2 checks 
#   for solving the problem:
#       1. A check which tells us if we reach the top after taking M steps.
#       2. A check which tells us if we will fall over the edge after taking M steps.
#
#   using these two checks, we can start counting the combinations,
#   if we reach the top, it means a combination was found.
#   if we fall over - the combination is not possible and we need to revert.
#   if we still have more steps to climb, we should try to continue climbing
#   by trying out every number of possible next steps [1 to M].
#
# 
# ------------------------
# Solution in Psuedo-Code:  
# ------------------------
#   start climbing():
#       max_steps = M.
#       n_stairs = N.
#       m_steps = 1.
#       combination count = 0.
#
#       while (m_steps is smaller than the maximum possible steps we can try, that is, M):
#         * try climbing m_steps.
#
#         * if top was reached, there is nothing more we can do - we reached our goal, 
#           therefore we can add 1 to the combination count and return back.
#           return (combination count + 1)
#
#         * if we fell over - we have reached a dead end, we can no longer reach
#           the top (cause we fell over and broke our leg) - therefore we dont add
#           anything to the count, and return, no matter how much we increase the 
#           number of steps from the previous point, we will always fall of.
#           return (combination count + 0)
#
#         * if there are still more stairs to climb, start climbing again,
#           this time, we again have M options of steps to take - [1 to M],
#           but the number of stairs have decreased by the number of steps we already
#           took now.
#           start_climbing_again(
#               try [1 to m] steps, 
#               until reaching (N - steps we took) stairs
#           )
# ------------------------------------------------------------------------------------------------------- #


# can_climb
# ---------
def can_climb(n_steps: int, n_stairs: int) -> bool:
    return (n_stairs - n_steps >= 0)

# reached_top
# -----------
def reached_top(n_steps: int, n_stairs: int) -> bool:
    return (n_stairs - n_steps == 0)

# climb
# -----
def climb(n_steps: int, n_stairs: int, max_nof_next_steps: int) -> int:
    combinations_cnt = 0

    if (reached_top(n_steps, n_stairs)):
        return 1

    if (not can_climb(n_steps, n_stairs)):
        return 0

    for next_n_steps in range(1, max_nof_next_steps + 1):
        combinations_cnt += climb(next_n_steps, (n_stairs - n_steps), max_nof_next_steps)

    return combinations_cnt

# count_nof_climbing_combinations
# -------------------------------
def count_nof_climbing_combinations(n_stairs: int, max_nof_steps: int) -> int:
    return climb(0, n_stairs, max_nof_steps)

# main
# ----
def main():
    n_stairs                    = int(input("Enter number of stairs to climb: "))
    max_n_steps                 = int(input("Enter maximum number of steps to climb each time: "))
    possible_combinations_cnt   = count_nof_climbing_combinations(n_stairs, max_n_steps)
    print(f"Total number of possible combinations found is: {possible_combinations_cnt}")

# ------------------------ #
if __name__ == "__main__":
    main()