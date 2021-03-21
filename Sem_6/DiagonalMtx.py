# 00 01 02 03 04
# 10 11 12 13 14
# 20 21 22 23 24
# 30 31 32 33 34

# 00
# 10 01
# 20 11 02
# 30 21 12 03
# 31 22 13 04
# 32 23 14
# 33 24
# 34

# 04
# 03 14
# 02 13 24
# 01 12 23 34
# 00 11 22 33
# 10 21 32
# 20 31
# 30
# https://stackoverflow.com/questions/6313308/get-all-the-diagonals-in-a-matrix-list-of-lists-in-python

test = [[ 1, 2, 3],
        [ 4, 5, 6],
        [ 7, 8, 9],
        [10,11,12]]

max_col = len(test[0])
max_row = len(test)
cols = [[] for _ in range(max_col)]
rows = [[] for _ in range(max_row)]
fdiag = [[] for _ in range(max_row + max_col - 1)]
bdiag = [[] for _ in range(len(fdiag))]
min_bdiag = -max_row + 1

print(bdiag)
for x in range(max_col):
    for y in range(max_row):
        cols[x].append(test[y][x])
        rows[y].append(test[y][x])
        fdiag[x+y].append(test[y][x])
        bdiag[x-y-min_bdiag].append(test[y][x])

print(cols)
print(rows)
print(fdiag)
print(bdiag)

