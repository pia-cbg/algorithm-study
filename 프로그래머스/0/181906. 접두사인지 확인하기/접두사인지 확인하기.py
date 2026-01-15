def solution(my_string, is_prefix):
    if len(is_prefix) > len(my_string):
        return 0
    if is_prefix[0] == my_string[0]:
        return 1
    else:
        return 0