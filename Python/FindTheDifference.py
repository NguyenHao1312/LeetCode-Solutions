class Solution:
    def findTheDifference(self, s, t):
        char_count = {}

        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        for char in t:
            if char in char_count:
                char_count[char] -= 1
            else:
                return char

        for char, count in char_count.items():
            if count < 0:
                return char
s_input = input("Enter s: ")
t_input = input("Enter t: ")
solution = Solution()
print(solution.findTheDifference(s_input, t_input))