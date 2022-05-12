from collections import defaultdict
#[[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]
mat = [[11, 25, 66, 1, 69, 7], [23, 55, 17, 45, 15, 52], [75, 31, 36, 44, 58, 8], [22, 27, 33, 25, 68, 4], [84, 28, 14, 11, 5, 50]]
diagonal = defaultdict(list)
for row in range(len(mat)):
    for col in range(len(mat[0])):
        diagonal[row-col].append(mat[row][col])
for i in diagonal:
    diagonal[i].sort()
for row in range(len(mat)):
    for col in range(len(mat[0])):
        mat[row][col] = diagonal[row-col].pop(0)
print(mat)
