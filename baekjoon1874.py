n = int(input())
stack = []
op_stack = []
count = 1
answer = True
for i in range(n):
    num = int(input())
    while count <= num:
        stack.append(count)
        op_stack.append("+")
        count += 1
    if stack[-1] == num:
        stack.pop()
        op_stack.append("-")
    else:
        answer = False

if answer == False:
    print("NO")
else:
    for i in op_stack:
        print(i)
