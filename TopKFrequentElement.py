from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        # most_common(k) trả về [(phần_tử, số_lần), ...], ta chỉ lấy phần_tử
        return [item[0] for item in count.most_common(k)]