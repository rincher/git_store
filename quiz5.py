import sys
no_of_trees, target = map(int, input().split())
trees = list(map(int, input().split()))


def totalsum(height):
    total = 0
    for i in trees:
        if i > height:
            total += i-height
    return total


def binary(target):
    low = 0
    highest = max(trees)
    while low <= highest:
        mid = (low + highest)//2
        total = totalsum(mid)

        if total < target:
            highest = mid - 1

        if total >= target:
            ans = mid
            low = mid + 1

    return ans


print(binary(target))
