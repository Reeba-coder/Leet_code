def diagonalSum(mat):
    n = len(mat)
    total = 0
    for i in range(n):
        total += mat[i][i]  # primary diagonal
        total += mat[i][n - 1 - i]  # secondary diagonal

    if n % 2 == 1:
        # center element is counted twice, subtract once
        total -= mat[n // 2][n // 2]

    return total
mat = [[1,2,3],[4,5,6],[7,8,9]]
print(diagonalSum(mat))