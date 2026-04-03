from collections import defaultdict

class Solution(object):
    def specialTriplets(self, nums):
        MOD = 10**9 + 7
        n = len(nums)

        # Preload all elements into the "right" window
        right = defaultdict(int)
        for num in nums:
            right[num] += 1

        left = defaultdict(int)
        result = 0

        for j in range(n):
            val = nums[j]
            target = val * 2

            # nums[j] is now "at" j, so remove it from the right window
            right[val] -= 1

            # Count valid (i, k) pairs around this j
            left_count = left[target]
            right_count = right[target]
            result = (result + left_count * right_count) % MOD

            # Slide j into the left window
            left[val] += 1

        return result