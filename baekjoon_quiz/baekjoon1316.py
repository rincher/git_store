import sys
N = int(sys.stdin.readline())
result = 0
for _ in range(N):
    words = sys.stdin.readline().strip()
    print(list(words))
    print(sorted(words, key=words.find))
    result += list(words) == sorted(words, key=words.find)

print(result)
