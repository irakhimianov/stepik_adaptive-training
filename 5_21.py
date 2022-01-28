# row, col = [int(x) for x in input().split()]
# matrix = []
# new_matrix = [[0] * row for i in range(col)]
# for i in range(row):
#     matrix.append([int(x) for x in input().split()])
# # for i in range(row):
#     for j in range(col):
#         new_matrix[j][i] = matrix[i][j]
# for el in new_matrix:
#     print(*el)
#
row, col = map(int, input().split())
matrix = []
for i in range(row):
    matrix.append([int(x) for x in input().split()])
new_matrix = [list(row) for row in zip(*matrix)]
print(new_matrix)