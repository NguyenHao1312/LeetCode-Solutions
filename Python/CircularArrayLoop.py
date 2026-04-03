class Solution:
    def circularArrayLoop(self, nums):
        n = len(nums)

        def next_index(i):
            return (i + nums[i]) % n

        for i in range(n):
            if nums[i] == 0:
                continue

            slow, fast = i, i

            while nums[slow] * nums[fast] > 0 and nums[slow] * nums[next_index(fast)] > 0:
                slow = next_index(slow)
                fast = next_index(next_index(fast))

                if slow == fast:
                    if slow == next_index(slow):
                        break
                    return True

            # Mark all nodes in this path as visited
            slow = i
            direction = nums[i]
            while nums[slow] * direction > 0:
                nxt = next_index(slow)
                nums[slow] = 0
                slow = nxt

        return False