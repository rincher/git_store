N, M = map(int, input().split())
num = list(map(int, input().split()))
queue = []
answer = 0

for i in range(1, N + 1):
    queue.append(i)


for i in range(M):
    queue_index = queue.index(num[i])
    queue_len = len(queue)

    if queue_index < queue_len - queue_index:
        while True:
            if queue[0] == num[i]:
                del queue[0]
                break
            else:
                queue.append(queue[0])
                del queue[0]
                answer += 1
    else:
        while True:
            if queue[0] == num[i]:
                del queue[0]
                break
            else:
                queue.insert(0, queue[-1])
                del queue[-1]
                answer += 1
print(answer)
