class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        result = []
        for h in range(12):
            for m in range(60):
                if (bin(h) + bin(m)).count('1') == turnedOn:
                    result.append(f"{h}:{m:02d}")
        return result