def setZeroes(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    hash_table = defaultdict(int)
    m = len(matrix) # number of rows
    n = len(matrix[0]) # number of columns
    for row_idx in range(m):
        for col_idx in range(n):
            if matrix[row_idx][col_idx] == 0:
                hash_table[row_idx] = 1
                hash_table[m + col_idx] = 1
    # Update row
    for row_idx in range(m):
        if hash_table[row_idx] == 1:
            col_idx = 0
            while col_idx < n:
                matrix[row_idx][col_idx] = 0
                col_idx += 1
    # Update column
    row_start = 0
    while row_start < m:
        if hash_table[row_start] == 1:
            row_start += 1
        else:
            break
    for col_idx in range(n):
        if hash_table[m + col_idx] == 1:
            row_idx = row_start
            while row_idx < m:
                matrix[row_idx][col_idx] = 0
                row_idx += 1