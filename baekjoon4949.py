while True:
    # 문자열 입력받기
    string1 = input()
    # 만약에 . 만 들어 온 경우 입력 중단
    if string1 == '.':
        break
    # string에 "(" , ")" , "[", "]" 가 있는지를 확인해야함.
    stack = []
    # 기본 조건은 참
    answer = True
    for i in string1:
        # 처음으로 들어온 ( or [ 은 스택에 추가
        if i == "[" or i == "(":
            stack.append(i)
        # 만약에 )가 들어 왔을때
        elif i == ")":
            # 스택이 없거나 스택 가장 마지막에 있는것이 [ 면 균형이 맞지 않아 거짓, break
            if not stack or stack[-1] == "[":
                answer = False
                break
            # 스택 가장 마지막에 있는 것이 ( 면 ()가 완성 됨으로 ( 반환
            elif stack[-1] == "(":
                stack.pop()
        # 만약에 ]가 들어 왔을때
        elif i == "]":
            # 스택이 없거나 스택 가장 마지막에 있는것이 ( 면 균형이 맞지 않아 거짓, break
            if not stack or stack[-1] == "(":
                answer = False
                break
            # 스택 가장 마지막에 있는 것이 [ 면 [] 가 완성 됨으로 [ 반환
            elif stack[-1] == "[":
                stack.pop()
    # 끝까지 참 즉 전부 균형이 맞았고 스택이 비었으면 yes 아니면 no
    if answer == True and not stack:
        print("yes")
    else:
        print("no")
