class Solution:
    def combinationSum3(self, k, n):
        results = []
        
        # Helper function for recursion
        def backtrack(start_num, current_path, remaining_target):
            # Base Case 1: We have selected k numbers
            if len(current_path) == k:
                # If the numbers add up to the target, save this path
                if remaining_target == 0:
                    results.append(list(current_path))
                return

            # Base Case 2: Optimization (Pruning)
            # If remaining_target < 0, we exceeded the sum. Stop.
            if remaining_target < 0:
                return

            # Loop through numbers from start_num to 9
            for i in range(start_num, 10):
                # Optimization: If the number 'i' is already greater 
                # than the remaining target, no need to check further.
                if i > remaining_target:
                    break
                
                # 1. CHOOSE: Add number to the current path
                current_path.append(i)
                
                # 2. EXPLORE: Recurse with the next number (i + 1)
                # We subtract 'i' from the target
                backtrack(i + 1, current_path, remaining_target - i)
                
                # 3. UN-CHOOSE: Backtrack (remove the number) to try the next option
                current_path.pop()

        # Start the recursion with number 1, an empty path, and target n
        backtrack(1, [], n)
        return results