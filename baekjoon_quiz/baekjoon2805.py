import sys

N, M = map(int, sys.stdin.readline().split())
tree_list = list(map(int, sys.stdin.readline().split()))


def total_sum(height):
    total = 0
    for i in tree_list:
        if i > height:
            total += i - height

    return total


def binary_search(M):
    low = 0
    end = max(tree_list)
    while low <= end:
        height = (low + end) // 2
        total = total_sum(height)

        if M > total:
            end = height - 1

        if M <= total:
            ans = height
            low = height + 1

    return ans


print(binary_search(M))
