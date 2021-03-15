import sys


def test(distance):
    distance_travelled = 0
    turns = 0
    speed = 0

    while distance_travelled < distance:
        speed += 1

        # add left
        turns += 1
        distance_travelled += speed
        if distance_travelled >= distance:
            break

        # add right
        turns += 1
        distance_travelled += speed
        if distance_travelled >= distance:
            break

    print(turns)


T = int(sys.stdin.readline())

while T:
    x, y = map(int, sys.stdin.readline().split())
    T -= 1
    test(y-x)
