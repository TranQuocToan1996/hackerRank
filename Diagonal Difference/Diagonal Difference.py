# https://www.hackerrank.com/challenges/diagonal-difference/problem
N = int(input())
total = 0
for i in range(N):
    row = input().split()
    total += int(row[i])-int(row[-(i+1)])
print(abs(total))


d1 = sum([a[x][x] for x in range(n)]) 
d2 = sum([a[x][n-1-x] for x in range (n)])
print(abs(d1-d2))

def diagonalDifference(arr):
    # Write your code here
    d1 = sum([arr[x][x] for x in range(len(arr))])
    d2 = sum([arr[x][n - 1 - x] for x in range(len(arr))])
    return(abs(d1 - d2))