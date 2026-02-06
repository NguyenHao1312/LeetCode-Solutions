from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        groups = defaultdict(list)
        
        for s in strs:
            # sorted(s) trả về list, cần ép kiểu về tuple để làm key cho dict
            key = tuple(sorted(s))
            groups[key].append(s)
            
        return list(groups.values())
        