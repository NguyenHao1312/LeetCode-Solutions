class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort() # Sorting helps optimize, though it's optional
        result = []
        # Calling the helper method you are about to define below
        self.backtrack(candidates, target, 0, [], result)
        return result

    def backtrack(self, candidates, remain, start, current_comb, result):
        # Base case 1: We found a valid combination that hits the target
        if remain == 0:
            result.append(list(current_comb))
            return
        
        # Base case 2: We exceeded the target, no need to keep exploring this path
        if remain < 0:
            return
        
        # Explore further options
        for i in range(start, len(candidates)):
            # Choose a candidate
            current_comb.append(candidates[i])
            
            # Explore: Notice we pass 'i' (not i + 1) because we can reuse the same element
            self.backtrack(candidates, remain - candidates[i], i, current_comb, result)
            
            # Backtrack: Remove the candidate and try the next one in the loop
            current_comb.pop()