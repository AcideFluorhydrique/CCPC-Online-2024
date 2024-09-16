n, m = map(int, input().split())

matrix = []

for i in range(n):
    row = list(input())
    matrix.append(row)
    
count = 0
for j in range(1, n):
    for k in range(0, m - 1):
        if matrix[j][k] == "p" and matrix[j][k + 1] == "c" and matrix[j - 1][k + 1] == "c" and matrix[j - 1][k] == "c":
            count += 1
print(count)