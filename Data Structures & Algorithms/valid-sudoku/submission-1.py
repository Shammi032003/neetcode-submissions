class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        
        # Row check
        for i in range(n):
            seen = set()
            for j in range(n):
                val = board[i][j]
                if val == ".":
                    continue
                if val in seen:
                    return False
                seen.add(val)
        
        # Column check
        for j in range(n):
            seen = set()
            for i in range(n):
                val = board[i][j]
                if val == ".":
                    continue
                if val in seen:
                    return False
                seen.add(val)
        
        # 3x3 box check
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        val = board[box_row + i][box_col + j]
                        if val == ".":
                            continue
                        if val in seen:
                            return False
                        seen.add(val)
        
        return True
        

                
        