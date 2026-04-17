class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # Sorting is absolutely MANDATORY here to handle duplicates
        candidates.sort() 
        result = []
        self.backtrack(candidates, target, 0, [], result)
        return result

    def backtrack(self, candidates, remain, start, current_comb, result):
        # Base case 1: Target reached
        if remain == 0:
            result.append(list(current_comb))
            return
        
        # Base case 2: Exceeded target
        if remain < 0:
            return
        
        for i in range(start, len(candidates)):
            # SKIP DUPLICATES: Prevent using the same number at the same depth
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            
            # Choose a candidate
            current_comb.append(candidates[i])
            
            # Explore: Notice we pass 'i + 1' because each number can only be used ONCE
            self.backtrack(candidates, remain - candidates[i], i + 1, current_comb, result)
            
            # Backtrack
            current_comb.pop()