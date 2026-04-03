class Solution:
    def canIWin(self, maxChoosableInteger, desiredTotal):
        # If the desired total is 0, the first player wins by default
        if desiredTotal <= 0:
            return True

        # If the sum of all available integers is less than the desired total, it's impossible to win
        if (maxChoosableInteger * (maxChoosableInteger + 1)) // 2 < desiredTotal:
            return False

        # Use memoization to store results of subproblems
        memo = {}

        def canWin(used, currentTotal):
            if currentTotal >= desiredTotal:
                return False

            if used in memo:
                return memo[used]

            for i in range(1, maxChoosableInteger + 1):
                if not (used & (1 << i)):  # If the number is not used
                    newUsed = used | (1 << i)
                    if not canWin(newUsed, currentTotal + i):
                        memo[used] = True
                        return True

            memo[used] = False
            return False

        return canWin(0, 0)