import sys

n = int(sys.stdin.readline())
for i in range(n):
    m = int(sys.stdin.readline())
    zero = 1
    one = 0
    temp = 0
    for _ in range(m):
        temp = one
        one += zero
        zero = temp
    print(zero, one)
