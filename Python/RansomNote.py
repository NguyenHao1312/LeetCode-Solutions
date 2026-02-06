from collections import Counter

class Solution:
    def canConstruct(self, ransomNote, magazine) :
        note_counts = Counter(ransomNote)
        mag_counts = Counter(magazine)
        
        remaining = note_counts - mag_counts
        
        return not remaining