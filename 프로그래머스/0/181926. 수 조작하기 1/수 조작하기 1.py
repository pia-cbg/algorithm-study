def solution(n, control):
    num = n
    for ch in control:
        if ch == 'w':
            num += 1
        elif ch == 's':
            num -= 1
        elif ch == 'd':
            num += 10
        elif ch == 'a':
            num -= 10
    return num
    