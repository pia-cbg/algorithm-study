def solution(nums):
    limit_ponket = len(nums)//2
    answer = len(list(set(nums)))
    if answer < limit_ponket:
        return answer
    else:
        return limit_ponket
        