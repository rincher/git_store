import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
stack = [0 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if array[i] > array[j] and stack[i] < stack[j]:
            stack[i] = stack[j]
    stack[i] += 1
print(max(stack))
