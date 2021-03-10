A = int(input())
for _ in range(A):
    H, W, N = map(int, input().split())
    if N % H != 0:
        a = N % H
    else:
        a = H
    b = (N//H) + 1
    print(str(a)+"0"+str(b))
