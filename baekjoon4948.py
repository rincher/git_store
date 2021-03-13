import math
import sys


# 소수인지를 비교하는 부분
def isPrime(num):
    if num == 1:
        return False

    for j in range(2, int(math.sqrt(num))+1):
        if num % j == 0:
            return False

    return True


# 2 부터 주어진 수의 크기 만큼 리스트를 만들어서
li = list(range(2, 123456*2))
prime_li = []
for i in li:
    # 소수인지 확인하는 함수를 호출해서
    if isPrime(i):
        # 소수가 맞으면 리스트에 추가
        prime_li.append(i)
# 이 부분이 끝나면 에라토스테네스 의 체가 완성

# 여기서 부터 입력 받기
while True:
    answer = 0
    n = int(sys.stdin.readline())
    if n == 0:
        break
    # 처음에 코드를 만들었을때는 받은 수를 소수인지를 체크했지만,
    # 새로 고친 코드는 에라토스테네스의 체와 비교함
    for i in prime_li:
        if n < i <= n*2:
            answer += 1

    print(answer)
