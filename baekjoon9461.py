import sys

T = int(sys.stdin.readline())
P = {
    1: 1, 2: 1, 3: 1, 4: 2, 5: 2, 6: 3, 7: 4, 8: 5, 9: 7, 10: 9
}


def find(N):
    if N in P:
        return P[N]

    if N not in P:
        P[N] = find(N-3)+find(N-2)
        return P[N]


while T:
    N = int(sys.stdin.readline())
    print(find(N))
    T -= 1
