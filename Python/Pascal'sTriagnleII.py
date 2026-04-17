class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        res = [[1], [1, 1]]
        for i in range(2, rowIndex + 1):
            row = [1]
            for j in range(1, i):
                row.append(res[i - 1][j - 1] + res[i - 1][j])
            row.append(1)
            res.append(row)
        return res[rowIndex]