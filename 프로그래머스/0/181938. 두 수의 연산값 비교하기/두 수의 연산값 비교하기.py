def solution(a, b):
    ab = str(a)+str(b)
    ba = str(b)+str(a)
    if int(ab) > 2*a*b:
        answer = int(ab)
    else:
        answer = 2*a*b
    return answer