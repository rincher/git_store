import sys
# 동적 계획법을 사용하기 위해서 메모이제이션
# 입력 받는 수가 1개 일 경우는 1차원 이라서 딕셔너리, 입력받는 수가 3개이기 때문에 3차원으로 구현
memo = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]


def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    # 값이 이미 존재한다면 그 값을 바로 리턴.
    if memo[a][b][c]:
        return memo[a][b][c]
    if a < b < c:
        memo[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return memo[a][b][c]

    memo[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + \
        w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return memo[a][b][c]


# 숫자들을 입력 받아서 수열을 재귀함수로 돌리기 위한곳
while True:

    a, b, c = map(int, sys.stdin.readline().split())
    # -1, -1, -1 일 경우에는 멈춰야 해서
    if a == -1 and b == -1 and c == -1:
        break

    print("w(%d, %d, %d) = %d" % (a, b, c, w(a, b, c)))
