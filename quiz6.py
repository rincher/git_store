n = int(input())


def hanoi(num, start, to, other):
    if num == 0:
        return
    hanoi(num - 1, start, other, to)
    print("num:", num, start, "에서", to, "로 옮긴다")
    hanoi(num - 1, other, to, start)


hanoi(n, 1, 3, 2)
