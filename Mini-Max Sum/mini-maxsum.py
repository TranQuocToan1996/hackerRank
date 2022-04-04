
def miniMaxSum(arr):
    A=sorted(arr)
    print(sum(A[0:4]))
    print(sum(A[1:5]))


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
