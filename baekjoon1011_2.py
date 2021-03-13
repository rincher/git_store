import sys

T = int(sys.stdin.readline())

while T:
    x, y = map(int, sys.stdin.readline().split())
    T -= 1
    # 거리
    original_dist = y - x
    dis = y - x
    if original_dist <= 3:
        print(original_dist)
        continue

    if original_dist % 2 != 0:
        dis -= 1

    # 총 이동 거리
    cnt = 0
    # 몇번 돌렸는지를 확인
    answer = 0

    flag = False

    # 총 이동 거리가 거리와 같아 질때까지
    while cnt < dis:
        answer += 1

        if cnt + answer >= dis:
            flag = True

        cnt += answer * 2
        # 몇번 이동 했는지를 보여주기 위함

    output = answer * 2

    if flag == True:
        output -= 1

    if original_dist % 2 != 0 and original_dist ** 0.5 % 1 != 0:
        output += 1

    print(output)
