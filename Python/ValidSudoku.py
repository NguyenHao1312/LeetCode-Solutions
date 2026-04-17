class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if (board[i][j] in rows[i] or
                    board[i][j] in cols[j] or
                    board[i][j] in boxes[(i // 3) * 3 + j // 3]):
                    return False
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                boxes[(i // 3) * 3 + j // 3].add(board[i][j])
        return True