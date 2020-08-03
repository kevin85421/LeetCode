class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Row
        for row in board:
            if self.isValidRow(row) == False:
                return False
        # Column
        for i in range(9):
            column = []
            for row in board:
                if row[i] != ".":
                    if row[i] not in column:
                        column.append(row[i])
                    else:
                        return False
        # Sub-Box
        for subbox_x in range(3):
            for subbox_y in range(3):
                subbox = []
                for j in range(3):
                    for k in range(3):
                        if board[j+3*subbox_x][k+3*subbox_y] != ".":
                            if board[j+3*subbox_x][k+3*subbox_y] not in subbox:
                                subbox.append(board[j+3*subbox_x][k+3*subbox_y])
                            else:
                                return False
        return True

    def isValidRow(self, row: List[str]) -> bool:
        row_elements = []
        for element in row:
            if element != ".":
                if element not in row_elements:
                    row_elements.append(element)
                else:
                    return False